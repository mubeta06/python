:mod:`libqrencode._qrencode`
============================

Python ctypes bindings to libqrencode. Note these bindings have been automatically generated by ctypeslib using h2xml and xml2py as follows ::

    $ python -m ctypeslib.h2xml -c -o qrencode.xml /usr/local/include/qrencode.h
    
    $ python -m ctypeslib.xml2py qrencode.xml -k defst -l /usr/local/lib/libqrencode.so -o _qrencode.py

This shows how to build the binding automatically under linux. The process is similar under windows with the expception that the .dll path needs to be specified.

Pre-requisites
--------------

Python (http://www.python.org)

libqrencode (http://fukuchi.org/works/qrencode/index.html.en)

ctypeslib (http://pypi.python.org/pypi/ctypeslib/)

gccxml (http://www.gccxml.org)
