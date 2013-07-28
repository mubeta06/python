.. libqrencode ctypes bindings documentation master file, created by
   sphinx-quickstart on Wed Jan 18 20:23:06 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

:mod:`libqrencode` -- Python Bindings to libqrencode
====================================================

.. |p1| replace:: libqrencode is a C library for encoding data in a QR Code symbol, a kind of 2D symbology that can be scanned by handy terminals such as a mobile phone with CCD (http://fukuchi.org/works/qrencode/index.html.en). libqrencode is a stand-alone library not requiring any additional files at run time and demonstrates fast symbol encoding with automatic optimization of input data. libqrencode supports QR Code model 2, described in JIS (Japanese Industrial Standards) X0510:2004 or ISO/IEC 18004.

.. |p2| replace:: This documentation describes python bindings written to interface with the libqrencode API. The bindings have been constructed using ctypes (http://docs.python.org/library/ctypes.html) which provides functionality to dynamically load shared libraries / DLLs, and hence, allows construction of bindings in pure python. This binding only uses built-in python modules with the exception of PIL for image IO but only when the bindings are run in scripted fashion, thereby, making the binding highly portable. Given the binding is pure python it is also somewhat python version agnostic. Futhermore, since the binding loads up the shared library dynamically the binding more comprehensively exposes the API for future enhancements in contrast to other interpretter extension binding approaches.

.. |p3| replace:: Any questions or comments regarding the bindings please feel free to get in touch with me, mu.beta.06@gmail.com

.. |qrimage| image:: /_static/qrimage.png
    :scale: 200 %

+-----------------+-----------+
| |p1|            |           |
|                 |           |
| |p2|            | |qrimage| |
|                 |           |
| |p3|            |           |
+-----------------+-----------+

Contents:

.. toctree::
   :maxdepth: 2

   qrencode
   _qrencode

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

