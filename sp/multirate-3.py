import numpy
import pylab
from scipy import signal
from sp import multirate
L = 147.0
M = 160.0
N = 24.0*L
h = signal.firwin(N-1, 1/M, window=('kaiser', 7.8562))
h = L*h
Fs = 48000.0
n = numpy.arange(0, 10239)
x  = numpy.sin(2*numpy.pi*1000/Fs*n)
y = multirate.upfirdn(x, h, L, M)
pylab.figure()
pylab.stem(n[1:49]/Fs, x[1:49])
pylab.stem(n[1:45]/(Fs*L/M), y[13:57], 'r', markerfmt='ro',)
pylab.xlabel('Time (sec)')
pylab.ylabel('Signal value')
pylab.show()