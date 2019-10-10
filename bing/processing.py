import pyaudio
import numpy as np

from .__init__ import RATE, CHUNK, CHANNELS, SILENCE_THRESHOLD
from .util import static_var, envelope






# Compute the "mask" of an audio signal, the mask refers to the identificaiton of periods of silence and loudness
def __compute_mask(audio_data):
    mask = []
    audio_envelope = envelope(audio_data)

    # w can be adjusted according to your preferences
    w = 0.05
    for i, env_val in enumerate(audio_envelope):
        if env_val - SILENCE_THRESHOLD * (1.0 + w) <= 0:
            # determine the state of this slice, this is a joke btw :)
            state = {
                True: "start",
                False: "end"
            }[mask[-1] == None or mask[-1][0] == "end"]
            mask.append((state, i))

    return np.array(mask)






# function that processes a chunk of audio data
@static_var(incomplete_signal=None, prev_state="")
def breakup(audio_data): 
    mask = compute_mask(audio_data)

    # Chop the last entry if the mask is incmplete
    temp_mask = mask[:-1] if mask[-1][0] == "start" else mask   
    data_chunks = np.array([]) 


    # This section just deals with an incomplete signal from the previous chunk, the masking algorithm by design wont pick up on this
    if breakup.prev_state == "start":
        # our first chunk of audio equals the previous incomplete signal + the untracked section of the new signal
        init_start = mask[0][1]
        data_chunks.append(breakup.incomplete_signal + audio_data[:init_start])
        breakup.incomplete_signal = None
        breakup.prev_state = ""


    # This chunk just appends the rest of the real audio signal to the final output
    for i in range(len(temp_mask), step=2):
        data_chunks.append([audio_data[temp_mask[i]: temp_mask[i+1]]])


    # Now we just have to deal with incomplete signals, basically these get passed onto the next function call to deal with
    if mask - temp_mask != None:
        region = mask[-1][1]
        breakup.incomplete_signal = audio_data[region:]
        breakup.prev_state = "start"
    
    return data_chunks
