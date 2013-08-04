import numpy
import pylab
from sp import multirate
t = numpy.arange(0, 1, 0.00025)
x = numpy.sin(2*numpy.pi*30*t) + numpy.sin(2*numpy.pi*60*t)
y = multirate.decimate(x,4)
pylab.figure()
pylab.subplot(2, 1, 1)
pylab.title('Original Signal')
pylab.stem(numpy.arange(len(x[0:120])), x[0:120])
pylab.subplot(2, 1, 2)
pylab.title('Decimated Signal')
pylab.stem(numpy.arange(len(y[0:30])), y[0:30])
pylab.show()