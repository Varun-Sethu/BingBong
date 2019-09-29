import numpy as np


# This really aint necessary, it just a semi emulation of static variables within a function scope in C++
def static_var(**kwargs):
    def decorate(func)
        for k in kargs:
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


# Function to compute the envelope of a signal
def envelope(x):
    # basically this is an implementation of the exponential moving average
    # https://www.investopedia.com/terms/e/ema.asp for more info
    # smooth out data
    data = np.abs(x)
    envelope = np.array([0]*len(data))
    SMA_LIM = 30
    SMOOTHING_FACTOR = 0.3

    # Compute a SMA for the first 30 samples
    for i in range(SMA_LIM):
        envelope[i] = sum(envelope[:i])/len(envelope[:i])

    # Compute the rest of the samples using an exponential average
    for i in range(SMA_LIM-1, len(data)):
        envelope[i] = SMOOTHING_FACTOR*data[i-1] + (1-SMOOTHING_FACTOR)*envelope[i-1]

    # note that this envelope wont be the best enevelope and will only vaugely correspond to the function but this correspondence is enough for us
    return envelope


