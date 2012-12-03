from distutils.core import setup
import libqrencode
setup(
    name='libqrencode',
    description='Python ctypes libqrencode wrapper',
    provides=['qrencode'],
    requires=[],
    long_description=
    """
    This package is a python ctypes wrapper for the libqrencode api 
    http://fukuchi.org/works/qrencode/index.html.en
    """,
    version=libqrencode.version,
    packages=['libqrencode'],
    package_dir={'libqrencode': './libqrencode'},
    url='http://matbaker.net',
    author='Matthew Baker',
    author_email='mu.beta.06@gmail.com',
    platforms='Linux',
    license='GNU Library or Lesser General Public License (LGPL)'
)
