# 2)
# 2. Assume x(t) is applied to a low-pass filter with bandwidth W1.
# • Plot the output (the filtered signal) and compare it with x(t) and comment on it.
# • Show the effect of changes in bandwidth of the filter on the filtered signal. Plot the
# filtered signal for the different bandwidth values which affects the output results.


import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import signal

#("**** signal parameters ****")
SamplingFrequency = 400                                # Sampling Frequency
TimePattern = np.linspace(0, 1 - 1 / SamplingFrequency, SamplingFrequency)          # time sequence
DataPoints = 2048					                      # FFT points
FrequencyScale = np.linspace(-SamplingFrequency / 2, SamplingFrequency / 2 - SamplingFrequency / DataPoints, DataPoints)		# Frequency scale in Hz

#("**** Create arbitrary x(t) wave ****")
Amplitude = 8					                        # Signal Amplitude (Volt)
Frequency = 12				                        # Signal Frequency (Hz)

x = Amplitude * np.sin(2 * np.pi * Frequency * TimePattern);            # Arbitrary x(t) signal

#("********** Create a low-pass filter **********")
FrequencyLowPass = 13                                 # Frequency
taps = 3                                # Low-pass Filter Taps. Generates taps for a low-pass filter and stores it in variable called whatever the ID is set to.
bands = np.array([0, 0.9 * FrequencyLowPass / SamplingFrequency, 1.1 * FrequencyLowPass / SamplingFrequency, 1])  # Monotonic nondecreasing sequence containing band edges
desired = np.array([1, 1, 0, 0])        # Sequence same as band to represent start and end gain points of bands
B = signal.firls(taps, bands, desired)

#("********** Filter a pulse **********")
y = signal.lfilter(B, 1, x)             # Filter the x(t) signal with low-pass-filter

#("********** Fourier Transforms **********")
fx = scipy.fft.fftshift(abs(scipy.fft.fft(y, DataPoints)))   #Fourier transform of filtered signal

#("********** Plot Filtered Signal **********")
fig, ax1 = plt.subplots(nrows=2, ncols=1, figsize=(12,10), sharex=True)
ax1[0].set(title='Plot of filtered signal', xlabel='Time (s)',
          ylabel='Amplitude')
ax1[0].plot(TimePattern, y, 'green', label='Filtered Signal')
ax1[0].legend()


#("********** Plot Original vs Filtered Signal **********")
ax1[1].set(title='Plot of Original vs Filtered signal', xlabel='Time (s)',
          ylabel='Amplitude')
ax1[1].plot(TimePattern, x, 'red', label='Original Signal')
ax1[1].plot(TimePattern, y, 'green', label='Filtered Signal')
ax1[1].legend()
plt.show()

#("********** Spectrum of Filtered Signal **********")
fig, ax2 = plt.subplots(nrows=1, ncols=1, figsize=(12,8))
ax2.set(title='Spectrum of filtered signal',xlabel='Frequency (Hz)',
          ylabel='Magnitude', xlim=(-50, 50))
ax2.plot(FrequencyScale, fx, label='Filtered Signal')
ax2.legend()
plt.show()