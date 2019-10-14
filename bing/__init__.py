import numpy as np
import pyaudio
import matplotlib.pyplot as plt


RATE     = 44100
CHUNK    = 1024
CHANNELS = 1


# Open a pyAudio stream and instance
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
            channels=CHANNELS,
            rate=RATE,
            output=True,
            input=True,
            frames_per_buffer=CHUNK)
stream.start_stream()



# Determine the envelope of silence
print("Determining silence threshold....")
# Record data for 10 seconds
data = np.array([])
for i in range(0, RATE // CHUNK * 1):
    raw_data = stream.read(CHUNK)
    audio_data = np.frombuffer(raw_data, dtype=np.float32)
    data = np.append(data, audio_data)    
data = np.absolute(data)


stream.close()
p.terminate()


# Average out the amplitude in this sample to determine the silence threshold
SILENCE_THRESHOLD = sum(data) / len(data)

# fig = plt.figure()
# s = fig.add_subplot(111)
# s.plot(data)
# plt.axhline(y=SILENCE_THRESHOLD, color='r', linestyle='-')
# plt.show()


