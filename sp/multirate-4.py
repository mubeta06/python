import numpy
import pylab
from sp import multirate
fs1 = 10.0
t1 = numpy.arange(0, 1 + 1.0/fs1, 1.0/fs1)
x = t1
y = multirate.resample(x, 3, 2)
t2 = numpy.arange(0,(len(y)))*2.0/(3.0*fs1)
pylab.figure()
pylab.plot(t1, x, '*')
pylab.plot(t2, y, 'o')
pylab.plot(numpy.arange(-0.5,1.5, 0.01), numpy.arange(-0.5,1.5, 0.01), ':')
pylab.legend(('original','resampled'), numpoints=1)
pylab.xlabel('Time')
pylab.show()