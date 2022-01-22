import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import signal

#Signal inputs are given below. Variables are mentioned with orginal names for better uderstanding
SamplingFrequency = 300                                # Sampling Frequency
TimePattern = np.linspace(0, 1 - 1 / SamplingFrequency, SamplingFrequency)          # time sequence
DataPoints = 2048					                      # FFT points
FrequencyScale = np.linspace(-SamplingFrequency / 2, SamplingFrequency / 2 - SamplingFrequency / DataPoints, DataPoints)		# Frequency scale in Hz

# Creating arbitrary x(t) signal
Amplitude = 8					                        # Signal Amplitude in  (Volt)
Frequency = 16					                        # Signal Frequency in (Hz)


#Defining Pulse for filter
x = Amplitude * np.sin(2 * np.pi * Frequency * TimePattern);


# Defining Band-pass filter variables
#A band-pass filter or bandpass filter is a device that passes frequencies
# within a certain range and rejects frequencies outside that range

FrequencyBandPass = 180                                 # Frequency
taps = 36                                # W2
bands = np.array([0, 0.9 * FrequencyBandPass / SamplingFrequency, 1.1 * FrequencyBandPass / SamplingFrequency, 1])  # Monotonic nondecreasing sequence containing band edges
desired = np.array([1, 1, 0, 0])        # Sequence same as band to represent start and end gain points of bands
B = signal.firwin2(taps, bands, desired)

#Defining Pulse for filter
y = signal.lfilter(B, 1, x)             # Filter the x(t) signal with low-pass-filter

#Fourier Transform
# In mathematics, a Fourier transform is a mathematical transform that decomposes functions depending on space
# or time into functions depending on spatial or temporal frequency,
# such as the expression of a musical chord in terms of the volumes and frequencies of its constituent notes

fx = scipy.fft.fftshift(abs(scipy.fft.fft(y, DataPoints)))   #This function swaps half-spaces for all axes listed (defaults to all). Note that y[0] is the Nyquist component only if len(x) is even.


#Ploting the Filtered Signal
fig, ax1 = plt.subplots(nrows=2, ncols=1, figsize=(12,10), sharex=True) # By using Sharex You can share the x or y axis limits for one axis with another by passing an axes instance as a sharex or sharey keyword argument.
ax1[0].set(title='Plot of filtered signal', xlabel='Time (s)',
          ylabel='Amplitude')
ax1[0].plot(TimePattern, y, 'green', label='Filtered Signal')
ax1[0].legend()


# Plotting the difference between Filtered and Original Signal
ax1[1].set(title='Plotting the difference between Filtered and Original Signal', xlabel='Time (s)',
          ylabel='Amplitude')
ax1[1].plot(TimePattern, x, 'red', label='Original Signal')
ax1[1].plot(TimePattern, y, 'green', label='Filtered Signal')
ax1[1].legend()
plt.show()

# Filtered Signal output spectrum
fig, ax2 = plt.subplots(nrows=1, ncols=1, figsize=(12,8))
ax2.set(title='Spectrum of filtered signal',xlabel='Frequency (Hz)',
          ylabel='Magnitude', xlim=(-50, 50))
ax2.plot(FrequencyScale, fx, label='Filtered Signal')
ax2.legend()
plt.show()