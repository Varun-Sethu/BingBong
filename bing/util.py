import numpy as np


# This really aint necessary, it just a semi emulation of static variables within a function scope in C++
def static_var(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate







# DSP Algorithms

# implementation of ta discrete fourier transform
def dft(x):
    N = len(x)
    freq_bin = [0]*N

    for n in range(N):
        for k in range(N):
            freq_bin[n] += x[k] * np.exp((-2j * np.pi)/N * k * n)

    return freq_bin


# implementation of the cooley-tukey algorithm
def cooley_tukey(x):
    N = len(x)
    if N <= 1:
        return x
    
    # Compute the even and odd cooley tukeys
    even_indicies = cooley_tukey(x[0::2])
    odd_indicies  = cooley_tukey(x[1::2])

    freq_bin = [0]*N
    for k in range(N//2):
        freq_bin[k]        = even_indicies[k] + odd_indicies[k] * np.exp((-2j * np.pi)*k/N) 
        freq_bin[k + N//2] = even_indicies[k] - odd_indicies[k] * np.exp((-2j * np.pi)*k/N) 

    return freq_bin


# Pads an audio signal until its length is a power of 2 
def pad(x):
    power = np.log(len(x), 2)
    if np.floor(power) == power:
        return x

    return x.append([0]*(2*np.ceil(power) - len(x)))



# Function to compute the envelope of a signal
def envelope(x):
    # basically this is an implementation of the exponential moving average
    # https://www.investopedia.com/terms/e/ema.asp for more info
    # smooth out data
    data = np.abs(x)
    N = len(data)
    envelope = np.full((N), 0.0, dtype=np.float64)
    SMA_LIM = 30
    SMOOTHING_FACTOR = 0.002

    # Compute a SMA for the first 30 samples
    for i in range(1, SMA_LIM+1):
        envelope[i-1] = np.sum(data[:1]) / (i+1)

    # Compute the rest of the samples using an exponential average
    for i in range(SMA_LIM, N):
        ema_val = data[i]*SMOOTHING_FACTOR + envelope[i-1]*(1-SMOOTHING_FACTOR)
        envelope[i] = ema_val

    # note that this envelope wont be the best enevelope and will only vaugely correspond to the function but this correspondence is enough for us
    return envelope


