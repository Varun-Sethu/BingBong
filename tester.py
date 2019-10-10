# Set of tests for individual functions within the library
from bing import util
import matplotlib.pyplot as plt
import pyaudio
import time
import numpy as np

RATE     = 44100
CHUNK    = 1024
CHANNELS = 1

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
            channels=CHANNELS,
            rate=RATE,
            output=True,
            input=True,
            frames_per_buffer=CHUNK)

def envelope_test():
    stream.start_stream()

    data = np.array([])
    for i in range(0, RATE // CHUNK * 2):
        raw_data = stream.read(CHUNK)
        audio_data = np.frombuffer(raw_data, dtype=np.float32)
        data = np.append(data, audio_data)    

    stream.close()
    start = time.time()
    envelope = util.envelope(data)
    end = time.time()
    print(f"Executed envelope in: {end - start}")

    fig = plt.figure()
    s = fig.add_subplot(111)
    s.plot(data)
    s.plot(envelope, linewidth=1)
    plt.show()


envelope_test()