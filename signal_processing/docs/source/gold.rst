
sp.gold
=======

.. automodule:: sp.gold

Example Usage
^^^^^^^^^^^^^

gold
____

::

    import numpy
    import pylab
    from sp import mls
    from sp import filter
    nbits = 9
    m = mls.mls(nbits)
    pylab.figure()
    pylab.title('%d bit M-Sequence Periodic Autocorrelation' % nbits)
    m = numpy.where(m, 1.0, -1.0)
    pylab.plot((numpy.roll(filter.ccorr(m, m).real, 2**nbits/2 - 1)))
    pylab.xlim(0, len(m))
    pylab.show()

.. plot::

    import numpy
    import pylab
    from sp import mls
    from sp import filter
    nbits = 9
    m = mls.mls(nbits)
    pylab.figure()
    pylab.title('%d bit M-Sequence Periodic Autocorrelation' % nbits)
    m = numpy.where(m, 1.0, -1.0)
    pylab.plot((numpy.roll(filter.ccorr(m, m).real, 2**nbits/2 - 1)))
    pylab.xlim(0, len(m))
    pylab.show()

See the individual methods below for further details.

Functions
^^^^^^^^^

.. autofunction:: sp.gold.gold

.. autofunction:: sp.gold.gen_gold
   
