# Set of tests for individual functions within the library
from bing import util
from bing import processing
from bing import musical_detection
from bing.__init__ import SILENCE_THRESHOLD
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


def __sample_audio():
    print("Recoridng....")
    stream.start_stream()
    data = np.array([])
    for i in range(0, RATE // CHUNK * 2):
        raw_data = stream.read(CHUNK)
        audio_data = np.frombuffer(raw_data, dtype=np.float32)
        data = np.append(data, audio_data)  
    return data
    stream.close()


# Function to test envelope function
def envelope_test():
    data = __sample_audio()      

    start = time.time()
    envelope = util.envelope(data)
    end = time.time()
    print(f"Executed envelope in: {end - start}")

    fig = plt.figure()
    s = fig.add_subplot(111)
    s.plot(data)
    s.plot(envelope, linewidth=1)
    s.axhline(y=SILENCE_THRESHOLD, color='r')
    s.axhline(y=SILENCE_THRESHOLD*1.3, color='b')
    s.axhline(y=SILENCE_THRESHOLD*0.7, color='b')
    plt.show()




# Function that tests the breakup function which is designed to deconstruct an audio signal
def breakup_test():
    # Testing mask
    data = __sample_audio()
    start = time.time()
    processing.breakup(data)
    end = time.time()
    print(f"Executed Beakup in: {end - start}")


def note_detection_test():
    data = __sample_audio()
    detector = musical_detection.Note_Detector()
    detector.process(data)



note_detection_test()
