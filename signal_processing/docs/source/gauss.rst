sp.gauss
========

.. automodule:: sp.gauss

Example Usage
^^^^^^^^^^^^^

fspecial_gauss / gaussian2
__________________________
::

    from mpl_toolkits.mplot3d.axes3d import Axes3D
    import pylab
    import numpy
    from sp import gauss
    size = 11
    sigma = 1.5
    x, y = numpy.mgrid[-size//2 + 1:size//2 + 1, -size//2 + 1:size//2 + 1]

    fig = pylab.figure()
    fig.suptitle('Some 2-D Gauss Functions')
    ax = fig.add_subplot(2, 1, 1, projection='3d')
    ax.plot_surface(x, y, gauss.fspecial_gauss(size, sigma), rstride=1, 
                    cstride=1, linewidth=0, antialiased=False, cmap=pylab.jet())
    ax = fig.add_subplot(2, 1, 2, projection='3d')
    ax.plot_surface(x, y, gauss.gaussian2(size, sigma), rstride=1, cstride=1, 
                    linewidth=0, antialiased=False, cmap=pylab.jet())
    pylab.show()

.. plot::

    from mpl_toolkits.mplot3d.axes3d import Axes3D
    import pylab
    import numpy
    from sp import gauss
    size = 11
    sigma = 1.5
    x, y = numpy.mgrid[-size//2 + 1:size//2 + 1, -size//2 + 1:size//2 + 1]

    fig = pylab.figure()
    fig.suptitle('Some 2-D Gauss Functions')
    ax = fig.add_subplot(2, 1, 1, projection='3d')
    ax.plot_surface(x, y, gauss.fspecial_gauss(size, sigma), rstride=1, 
                    cstride=1, linewidth=0, antialiased=False, cmap=pylab.jet())
    ax = fig.add_subplot(2, 1, 2, projection='3d')
    ax.plot_surface(x, y, gauss.gaussian2(size, sigma), rstride=1, cstride=1, 
                    linewidth=0, antialiased=False, cmap=pylab.jet())
    pylab.show()

See the individual methods below for further details.

Functions
^^^^^^^^^

.. autofunction:: sp.gauss.gaussian2

.. autofunction:: sp.gauss.fspecial_gauss
