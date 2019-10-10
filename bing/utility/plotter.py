# https://gist.github.com/denisb411/cbe1dce9bc01e770fa8718e4f0dc7367
# Not entirely my code


import pyaudio
import numpy as np
import time
import wave
import matplotlib.pyplot as plt

CHUNK    = 1024
RATE     = 44100
CHANNELS = 1


window = np.blackman(CHUNK//2)
plt.ion()
fig = plt.figure(figsize=(10,8))
ax1 = fig.add_subplot(211)


def plot_audio(data):
    t1=time.time()
    indata = data*window
    #Plot time domain
    ax1.cla()
    ax1.plot(indata)
    ax1.grid()
    ax1.axis([0,CHUNK,-5000,5000])