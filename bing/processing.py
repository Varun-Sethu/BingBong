import pyaudio
import numpy as np

from .__init__ import RATE, CHUNK, CHANNELS, SILENCE_THRESHOLD
from .util import static_var, envelope






# Compute the "mask" of an audio signal, the mask refers to the identificaiton of periods of silence and loudness
def __compute_mask(audio_data):
    mask = []
    audio_envelope = envelope(audio_data)
    # w can be adjusted according to your preferences
    w = 0.3
    upper_silence_threshold = SILENCE_THRESHOLD * (1.0 + w)

    for i in range(0, len(audio_envelope)):
        env_val = audio_envelope[i]

        # Get the current state of mask
        curr_state = mask[-1][0] if len(mask) != 0 else "end"
        if curr_state is "start" and env_val < upper_silence_threshold:
            mask.append(["end", i])
        elif curr_state is "end" and env_val > upper_silence_threshold:
            mask.append(["start", i])

    return np.array(mask)






# function that processes a chunk of audio data
@static_var(incomplete_signal=None, prev_state="")
def breakup(audio_data): 
    mask = __compute_mask(audio_data)
    if len(mask) == 0:
        return np.array([]) 

    # Chop the last entry if the mask is incmplete
    temp_mask = mask[:-1] if mask[-1][0] == "start" else mask   
    data_chunks = [] 


    # This section just deals with an incomplete signal from the previous chunk, the masking algorithm by design wont pick up on this
    if breakup.prev_state == "start":
        # our first chunk of audio equals the previous incomplete signal + the untracked section of the new signal
        init_start = int(mask[0][1]) # init_start will always be 0 but for the sake of readability yeh
        init_end   = int(mask[1][1])

        data_chunks.append(breakup.incomplete_signal + audio_data[init_start:init_end])
        breakup.incomplete_signal = None
        breakup.prev_state = ""


    # This chunk just appends the rest of the real audio signal to the final output
    for i in range(0, len(temp_mask), 2):
        block_start = int(temp_mask[i][1])
        block_end   = int(temp_mask[i+1][1])
        data_chunks.append([audio_data[block_start:block_end]])


    # Now we just have to deal with incomplete signals, basically these get passed onto the next function call to deal with
    if len(mask) != len(temp_mask):
        region = int(mask[-1][1])
        breakup.incomplete_signal = audio_data[region:]
        breakup.prev_state = "start"


    return np.array(data_chunks)
