
sp.ssim
=======

.. automodule:: sp.ssim

Example Usage
^^^^^^^^^^^^^

ssim
____

::

    import pylab
    import numpy
    from sp import ssim
    from PIL import Image
    einstein = numpy.asarray(Image.open('./imgs/einstein.tif'))
    meanshift = numpy.asarray(Image.open('./imgs/meanshift.tif'))
    contrast = numpy.asarray(Image.open('./imgs/contrast.tif'))
    impulse = numpy.asarray(Image.open('./imgs/impulse.tif'))
    blur = numpy.asarray(Image.open('./imgs/blur.tif'))
    jpg = numpy.asarray(Image.open('./imgs/jpg.tif'))
    einstein_ssim = ssim.ssim(einstein, einstein)
    meanshift_ssim = ssim.ssim(einstein, meanshift)
    contrast_ssim = ssim.ssim(einstein, contrast)
    impulse_ssim = ssim.ssim(einstein, impulse)
    blur_ssim = ssim.ssim(einstein, blur)
    jpg_ssim = ssim.ssim(einstein, jpg)
    pylab.figure()
    pylab.subplot(2, 3, 1)
    pylab.title('Original\n SSIM %.3f' % einstein_ssim.mean())
    pylab.imshow(einstein, cmap=pylab.gray())
    pylab.subplot(2, 3, 2)
    pylab.title('Mean-Shifted\n SSIM %.3f' % meanshift_ssim.mean())
    pylab.imshow(meanshift, cmap=pylab.gray())
    pylab.subplot(2, 3, 3)
    pylab.title('Contrast-Adjusted\n SSIM %.3f' % contrast_ssim.mean())
    pylab.imshow(contrast, cmap=pylab.gray())
    pylab.subplot(2, 3, 4)
    pylab.title('Impulse-Noise\n SSIM %.3f' % impulse_ssim.mean())
    pylab.imshow(impulse, cmap=pylab.gray())
    pylab.subplot(2, 3, 5)
    pylab.title('Blur\n SSIM %.3f' % blur_ssim.mean())
    pylab.imshow(blur, cmap=pylab.gray())
    pylab.subplot(2, 3, 6)
    pylab.title('JPG\n SSIM %.3f' % jpg_ssim.mean())
    pylab.imshow(jpg, cmap=pylab.gray())
    pylab.show()

.. plot::

    import pylab
    import numpy
    from sp import ssim
    from PIL import Image
    einstein = numpy.asarray(Image.open('./imgs/einstein.tif'))
    meanshift = numpy.asarray(Image.open('./imgs/meanshift.tif'))
    contrast = numpy.asarray(Image.open('./imgs/contrast.tif'))
    impulse = numpy.asarray(Image.open('./imgs/impulse.tif'))
    blur = numpy.asarray(Image.open('./imgs/blur.tif'))
    jpg = numpy.asarray(Image.open('./imgs/jpg.tif'))
    einstein_ssim = ssim.ssim(einstein, einstein)
    meanshift_ssim = ssim.ssim(einstein, meanshift)
    contrast_ssim = ssim.ssim(einstein, contrast)
    impulse_ssim = ssim.ssim(einstein, impulse)
    blur_ssim = ssim.ssim(einstein, blur)
    jpg_ssim = ssim.ssim(einstein, jpg)
    pylab.figure()
    pylab.subplot(2, 3, 1)
    pylab.title('Original\n SSIM %.3f' % einstein_ssim.mean())
    pylab.imshow(einstein, cmap=pylab.gray())
    pylab.subplot(2, 3, 2)
    pylab.title('Mean-Shifted\n SSIM %.3f' % meanshift_ssim.mean())
    pylab.imshow(meanshift, cmap=pylab.gray())
    pylab.subplot(2, 3, 3)
    pylab.title('Contrast-Adjusted\n SSIM %.3f' % contrast_ssim.mean())
    pylab.imshow(contrast, cmap=pylab.gray())
    pylab.subplot(2, 3, 4)
    pylab.title('Impulse-Noise\n SSIM %.3f' % impulse_ssim.mean())
    pylab.imshow(impulse, cmap=pylab.gray())
    pylab.subplot(2, 3, 5)
    pylab.title('Blur\n SSIM %.3f' % blur_ssim.mean())
    pylab.imshow(blur, cmap=pylab.gray())
    pylab.subplot(2, 3, 6)
    pylab.title('JPG\n SSIM %.3f' % jpg_ssim.mean())
    pylab.imshow(jpg, cmap=pylab.gray())
    pylab.show()

::

    import numpy
    import pylab
    from sp import ssim
    from PIL import Image
    original = numpy.asarray(Image.open('./imgs/building.tif'))
    jpg = numpy.asarray(Image.open('./imgs/building_jpg.tif'))
    ssim_map = ssim.ssim(original, jpg)
    abs_map = numpy.abs(original.astype('float64')-jpg.astype('float64'))
    pylab.figure()
    pylab.subplot(2, 2, 1)
    pylab.title('Original')
    pylab.imshow(original, cmap=pylab.gray())
    pylab.subplot(2, 2, 2)
    pylab.title('JPEG compressed')
    pylab.imshow(jpg, cmap=pylab.gray())
    pylab.subplot(2, 2, 3)
    pylab.title('Absolute error map')
    pylab.imshow(abs_map.astype('uint8'), cmap=pylab.gray())
    pylab.subplot(2, 2, 4)
    pylab.title('SSIM index map')
    pylab.imshow(ssim_map, cmap=pylab.gray())
    pylab.show()

.. plot::

    import numpy
    import pylab
    from sp import ssim
    from PIL import Image
    original = numpy.asarray(Image.open('./imgs/building.tif'))
    jpg = numpy.asarray(Image.open('./imgs/building_jpg.tif'))
    ssim_map = ssim.ssim(original, jpg)
    abs_map = numpy.abs(original.astype('float64')-jpg.astype('float64'))
    pylab.figure()
    pylab.subplot(2, 2, 1)
    pylab.title('Original')
    pylab.imshow(original, cmap=pylab.gray())
    pylab.subplot(2, 2, 2)
    pylab.title('JPEG compressed')
    pylab.imshow(jpg, cmap=pylab.gray())
    pylab.subplot(2, 2, 3)
    pylab.title('Absolute error map')
    pylab.imshow(abs_map.astype('uint8'), cmap=pylab.gray())
    pylab.subplot(2, 2, 4)
    pylab.title('SSIM index map')
    pylab.imshow(ssim_map, cmap=pylab.gray())
    pylab.show()

msssim
______

::

    import numpy
    import pylab
    from sp import ssim
    from PIL import Image
    einstein = numpy.asarray(Image.open('./imgs/einstein.tif'))
    impulse = numpy.asarray(Image.open('./imgs/impulse.tif'))
    ms_ssim = ssim.msssim(original, impulse)
    pylab.figure()
    pylab.subplot(1, 2, 1)
    pylab.title('Original')
    pylab.imshow(original, cmap=pylab.gray())
    pylab.subplot(1, 2, 2)
    pylab.title('Impulse-Noise\n %.3f' % ms_ssim)
    pylab.imshow(impulse, cmap=pylab.gray())
    pylab.show()

.. plot::

    import numpy
    import pylab
    from sp import ssim
    from PIL import Image
    einstein = numpy.asarray(Image.open('./imgs/einstein.tif'))
    impulse = numpy.asarray(Image.open('./imgs/impulse.tif'))
    ms_ssim = ssim.msssim(einstein, impulse)
    pylab.figure()
    pylab.subplot(1, 2, 1)
    pylab.title('Original')
    pylab.imshow(einstein, cmap=pylab.gray())
    pylab.subplot(1, 2, 2)
    pylab.title('Impulse-Noise\n MSSSIM %.3f' % ms_ssim)
    pylab.imshow(impulse, cmap=pylab.gray())
    pylab.show()

See the individual methods below for further details.

Functions
^^^^^^^^^

.. autofunction:: sp.ssim.ssim

.. autofunction:: sp.ssim.msssim
