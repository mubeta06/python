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