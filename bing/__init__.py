import numpy as np
from musical_detection import Note_Detector


RATE     = 44100
CHUNK    = 1024
CHANNELS = 1

# Determine the envelope of silence
print("Determining silence threshold....")
# Record data for 10 seconds
data = []
for i in range(0, RATE / CHUNK * 10):
    raw_data = stream.read(CHUNK)
    audio_data = np.frombuffer(raw_data)
    data.append(*audio_data)    
data = np.abs(data)

# Average out the amplitude in this sample to determine the silence threshold
SILENCE_THRESHOLD = sum(data) / len(data)