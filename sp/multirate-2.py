import numpy
import pylab
from sp import multirate
t = numpy.arange(0, 1, 0.001)
x = numpy.sin(2*numpy.pi*30*t) + numpy.sin(2*numpy.pi*60*t)
y = multirate.interp(x,4)
pylab.figure()
pylab.subplot(2, 1, 1)
pylab.title('Original Signal')
pylab.stem(numpy.arange(len(x[0:30])), x[0:30])
pylab.subplot(2, 1, 2)
pylab.title('Interpolated Signal')
pylab.stem(numpy.arange(len(y[0:120])), y[0:120])
pylab.show()