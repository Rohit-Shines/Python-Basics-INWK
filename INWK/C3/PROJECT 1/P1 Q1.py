import numpy as N
import matplotlib.pyplot as plt
import scipy

#Signal inputs are given below. Variables are mentione with orginal names for better uderstanding
SamplingFrequency = 400                                # Sampling Frequency
TimePattern = N.linspace(0, 1 - 1 / SamplingFrequency, SamplingFrequency)          # time sequence
DataPoints = 2048

#The frequency resolution is defined as ((SamplingFrequency/DataPoints))  in FFT. Where Fs is sample frequency,
# N is number of data points used in the FFT. For example,
# if the sample frequency is 1000 Hz and the number of data points used by you in FFT is 1000.
# Then the frequency resolution is equal to 1000 Hz/1000 = 1 Hz

FrequencyScale = N.linspace(-SamplingFrequency / 4, SamplingFrequency / 4 - SamplingFrequency / DataPoints, DataPoints) # Frequency scale in Hz

# Creating arbitrary x(t) signal
Amplitude = 8					                        # Signal Amplitude (Volt)
Frequency = 12					                        # Signal Frequency (Hz)

x = Amplitude * N.sin(2 * N.pi * Frequency * TimePattern)             # Arbitrary x(t)

#Plot Signal
fig, ax = plt.subplots(figsize=(12,8))
ax.plot(TimePattern, x, label='Arbitray Signal x(t)')
ax.set(title ='x(t) signal',
       xlabel='Time(s)',
       ylabel='Amplitude')
ax.legend()
plt.show()

#Fourier Transform
fx = scipy.fft.fft(x, DataPoints)
fx = scipy.fft.fftshift(abs(fx))

#Plot Frequency Spectrum

fig, ax = plt.subplots(figsize=(12,8))
ax.plot(FrequencyScale, fx, label='Arbitray Signal x(t)')
ax.set(title ='Frequency Spectrum',
        xlabel='Frequency (Hz)',
        ylabel='Magnitude')
ax.legend()
plt.show()