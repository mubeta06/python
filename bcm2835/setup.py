from distutils.core import setup
import libbcm2835
setup(
    name='libbcm2835',
    description='Python ctypes bindings libbcm2835',
    provides=['spi', '_bcm2835'],
    requires=[],
    long_description=
    """
    This package is a python ctypes wrapper for the libbcm2835 api 
    http://www.airspayce.com/mikem/bcm2835/
    """,
    version=libbcm2835.version,
    packages=['libbcm2835'],
    package_dir={'libbcm2835': './libbcm2835'},
    url='http://matbaker.net',
    author='Matthew Baker',
    author_email='mu.beta.06@gmail.com',
    platforms='Linux (RaspberryPi)',
    license='GNU Library or Lesser General Public License (LGPL)'
)
