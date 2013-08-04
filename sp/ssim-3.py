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