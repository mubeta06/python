import numpy
import pylab

from sp import firwin

f0 = 20 #20Hz
ts = 0.01 # i.e. sampling frequency is 1/ts = 100Hz
x = numpy.arange(-10, 10, ts)
signal = (numpy.cos(2*numpy.pi*f0*x) + numpy.sin(2*numpy.pi*2*f0*x) +
            numpy.cos(2*numpy.pi*0.5*f0*x) + numpy.cos(2*numpy.pi*1.5*f0*x))

#build filter
#First build a Lowpass filter
M = 100 #number of taps in filter
fc = 0.25 #i.e. normalised cutoff frequency 1/4 of sampling rate i.e. 25Hz
lp = firwin.build_filter(M, fc, window=firwin.blackman)
#next build Highpass filter by shifting frequency domain
shift = numpy.cos(2*numpy.pi*0.5*numpy.arange(M + 1))
hp = lp*shift

#filter the signal
filtered = numpy.convolve(signal, hp)

#plotting
pylab.figure()
pylab.subplot(3,1,1)
pylab.title('Original Spectrum')
pylab.xlabel('Normalised Frequency')
firwin.plot_fft(signal)
pylab.subplot(3,1,2)
pylab.title('Filter Frequency Response')
pylab.xlabel('Normalised Frequency')
firwin.plot_fft(hp)
#window and fft
pylab.subplot(3,1,3)
pylab.title('Filtered Spectrum')
pylab.xlabel('Normalised Frequency')
firwin.plot_fft(firwin.hamming(len(filtered))[:-1]*(filtered))
pylab.subplots_adjust(hspace = 0.6)
pylab.show()