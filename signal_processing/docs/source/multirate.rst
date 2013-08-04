sp.multirate
============

.. automodule:: sp.multirate

Example Usage
^^^^^^^^^^^^^

downsample
__________

    >>> import numpy
    >>> from sp import multirate
    >>> x = numpy.arange(1, 11)
    >>> multirate.downsample(x, 3)
    array([ 1,  4,  7, 10])
    >>> multirate.downsample(x, 3, phase=2)
    array([3, 6, 9])

upsample
________

    >>> import numpy
    >>> from sp import multirate
    >>> x = numpy.arange(1, 5)
    >>> multirate.upsample(x, 3)
    array([ 1.,  0.,  0.,  2.,  0.,  0.,  3.,  0.,  0.,  4.,  0.,  0.])
    >>> multirate.upsample(x, 3, 2)
    array([ 0.,  0.,  1.,  0.,  0.,  2.,  0.,  0.,  3.,  0.,  0.,  4.])

decimate
________
::

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

.. plot::

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

interp
________
::

    import numpy
    import pylab
    from sp import multirate
    t = numpy.arange(0, 1, 0.001)
    x = numpy.sin(2*numpy.pi*30*t) + numpy.sin(2*numpy.pi*60*t)
    y = interp(x,4)
    pylab.figure()
    pylab.subplot(2, 1, 1)
    pylab.title('Original Signal')
    pylab.stem(numpy.arange(len(x[0:30])), x[0:30])
    pylab.subplot(2, 1, 2)
    pylab.title('Interpolated Signal')
    pylab.stem(numpy.arange(len(y[0:120])), y[0:120])
    pylab.show()

.. plot::

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

upfirdn
________
::

    import numpy
    import pylab
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

.. plot::

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

resample
________
::

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

.. plot::

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

::

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

.. plot::

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

See the individual methods below for further details.

Functions
^^^^^^^^^

.. autofunction:: sp.multirate.downsample

.. autofunction:: sp.multirate.upsample

.. autofunction:: sp.multirate.decimate

.. autofunction:: sp.multirate.interp

.. autofunction:: sp.multirate.upfirdn

.. autofunction:: sp.multirate.resample
