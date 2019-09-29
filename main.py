import pyaudio
import time
import numpy as np
from bing import Note_Detector


RATE          = 44100
CHUNK         = 1024 
CHANNELS      = 1
NOTE_DETECTOR = Note_Detector()





# Callback function for pyaudio
def callback(in_data, frame_count, time_info, flag):
    dry_data = []
    fulldata = []

    audio_data = np.frombuffer(in_data, dtype=np.float32)
    NOTE_DETECTOR.process(audio_data)

    return (audio_data, pyaudio.paContinue)



if __name__ == '__main__':
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                input=True,
                frames_per_buffer=CHUNK,
                stream_callback=callback)

    # Begin recording
    stream.start_stream()
    while stream.is_active():
        time.sleep(0.1)
    stream.close()
    p.terminate()