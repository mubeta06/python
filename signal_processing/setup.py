from distutils.core import setup
import sp
setup(
    name='sp',
    description='Python Signal Processing Library',
    provides=[],
    requires=[],
    long_description=
    """
    This package contains various Signal Processing modules.
    """,
    version=sp.version,
    packages=['sp'],
    package_dir={'sp': './sp'},
    url='http://matbaker.net',
    author='Matthew Baker',
    author_email='mu.beta.06@gmail.com',
    platforms='Linux',
    license='GNU Library or Lesser General Public License (LGPL)'
)
