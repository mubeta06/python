import numpy
import pylab
from sp import multirate
x = numpy.hstack([numpy.arange(1,11), numpy.arange(9,0,-1)])
y = multirate.resample(x,3,2)
pylab.figure()
pylab.subplot(2, 1, 1)
pylab.title('Edge Effects Not Noticeable')
pylab.plot(numpy.arange(19)+1, x, '*')
pylab.plot(numpy.arange(29)*2/3.0 + 1, y, 'o')
pylab.legend(('original', 'resampled'), numpoints=1)
x = numpy.hstack([numpy.arange(10, 0, -1), numpy.arange(2,11)])
y = multirate.resample(x,3,2)
pylab.subplot(2, 1, 2)
pylab.plot(numpy.arange(19)+1, x, '*')
pylab.plot(numpy.arange(29)*2/3.0 + 1, y, 'o')
pylab.title('Edge Effects Very Noticeable')
pylab.legend(('original', 'resampled'), numpoints=1)
pylab.show()