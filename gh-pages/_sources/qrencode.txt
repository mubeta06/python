:mod:`libqrencode.qrencode` -- QR Encoding
==========================================

.. automodule:: libqrencode.qrencode


Installation
------------

1. Install libqrencode.

2. Unpack archive onto local machine.

3. Run ::

    $ python setup.py install

4. Test ::

    $ python -m libqrencode.qrencode 'Hello World'
    XXXXXXXXXXXXXX    XX  XXXX  XXXXXXXXXXXXXX
    XX          XX    XXXXXX    XX          XX
    XX  XXXXXX  XX  XXXX  XXXX  XX  XXXXXX  XX
    XX  XXXXXX  XX    XX  XX    XX  XXXXXX  XX
    XX  XXXXXX  XX      XX  XX  XX  XXXXXX  XX
    XX          XX          XX  XX          XX
    XXXXXXXXXXXXXX  XX  XX  XX  XXXXXXXXXXXXXX
                    XXXX  XXXX                
    XXXXXX  XXXXXXXXXXXXXXXX  XXXX      XX    
      XXXX  XXXX    XXXXXX      XXXXXX    XXXX
    XX  XX  XX  XX  XX  XX  XXXX  XXXXXXXXXXXX
        XX          XXXXXX          XX    XX  
    XXXX    XX  XXXX  XX    XXXX  XXXX        
                    XX  XXXX  XX        XXXX  
    XXXXXXXXXXXXXX  XX  XXXX      XXXX  XXXXXX
    XX          XX  XXXX  XXXX    XX        XX
    XX  XXXXXX  XX  XX    XX        XX        
    XX  XXXXXX  XX    XXXXXX    XXXXXX  XXXX  
    XX  XXXXXX  XX  XX  XX  XX  XX  XX  XX  XX
    XX          XX  XX    XX        XX    XX  
    XXXXXXXXXXXXXX  XX  XXXXXX    XX      XXXX

Usage
-----

Scripted Usage
^^^^^^^^^^^^^^

1. Run the following for usage  ::

    $ python -m libqrencode.qrencode -h
    Usage: qrencode [OPTION]... [STRING]

    libqrencode ctypes python binding version 1.0, libqrencode version 3.2.1

    Options:
      -h, --help            show this help message and exit
      -o FILENAME, --filename=FILENAME
                            Encoded image filename (.png, .pdf, .jpg, .tif...)
      -s SIZE, --size=SIZE  Specify module size in dots (pixels). (default=3)
      -l LEVEL, --level=LEVEL
                            specify error correction level from L (lowest) to H
                            (highest). (default=L)
      -v SYMVERSION, --symversion=SYMVERSION
                            specify the version of the symbol. (default=auto)
      -m MARGIN, --margin=MARGIN
                            specify the width of the margins. (default=4)
                            (2 for Micro)))
      -d DPI, --dpi=DPI     specify the DPI of the generated PNG. (default=72)
      -S, --structured      make structured symbols. Version must be
                            specified.
      -k, --kanji           assume that the input text contains kanji
                            (shift-jis).
      -c, --casesensitive   encode lower-case alphabet characters in 8-bit mode.
                            (default)
      -8, --eightbit        encode entire data in 8-bit mode. -k and -c will be
                            ignored.
      -M, --micro           encode in a Micro QR Code. (experimental).


Module Usage
^^^^^^^^^^^^

1. Import libqrencode bindings::

      >>> from libqrencode import qrencode

2. Create a :class:`qrencode.QREncoder` instantiation::

      >>> encoder = qrencode.QREncoder()
    
3. Encode a string using the aforementioned instantiation::

      >>> encoder.encode('Hello World')
                        
4. Select encoded output format from one of the following output formats:
      
      1. ASCII::
      
          >>> encoder.asciipreview()
          XXXXXXXXXXXXXX    XX  XXXX  XXXXXXXXXXXXXX
          XX          XX    XXXXXX    XX          XX
          XX  XXXXXX  XX  XXXX  XXXX  XX  XXXXXX  XX
          XX  XXXXXX  XX    XX  XX    XX  XXXXXX  XX
          XX  XXXXXX  XX      XX  XX  XX  XXXXXX  XX
          XX          XX          XX  XX          XX
          XXXXXXXXXXXXXX  XX  XX  XX  XXXXXXXXXXXXXX
                          XXXX  XXXX                
          XXXXXX  XXXXXXXXXXXXXXXX  XXXX      XX    
            XXXX  XXXX    XXXXXX      XXXXXX    XXXX
          XX  XX  XX  XX  XX  XX  XXXX  XXXXXXXXXXXX
              XX          XXXXXX          XX    XX  
          XXXX    XX  XXXX  XX    XXXX  XXXX        
                          XX  XXXX  XX        XXXX  
          XXXXXXXXXXXXXX  XX  XXXX      XXXX  XXXXXX
          XX          XX  XXXX  XXXX    XX        XX
          XX  XXXXXX  XX  XX    XX        XX        
          XX  XXXXXX  XX    XXXXXX    XXXXXX  XXXX  
          XX  XXXXXX  XX  XX  XX  XX  XX  XX  XX  XX
          XX          XX  XX    XX        XX    XX  
          XXXXXXXXXXXXXX  XX  XXXXXX    XX      XXXX
          
      2. Boolean list of lists::
      
          >>> qr_list = encoder.as2dlist()

      3. Postscript string::
      
          >>> qr_ps = encoder.asps()

See the individual classes, methods, attributes and functions below for further details.

Classes
-------

.. autoclass:: QREncode
   :members:
   
.. autoclass:: QRcode
   :members:
   
.. autoclass:: QRcode_List
   :members:

.. autoclass:: QREncoder
   :members:

.. autoclass:: StructuredQREncoder
   :members:

Functions
---------

.. autofunction:: call

.. autofunction:: main

Exceptions
----------

.. autoexception:: Error

Pre-requisites
--------------

Python (http://www.python.org)

libqrencode (http://fukuchi.org/works/qrencode/index.html.en)

Python Imaging Library (PIL, http://www.pythonware.com/products/pil/) (optional)

Known Issues
----------------------

1. For the moment the bindings have only be constructed for use under linux. I could be tempted to support windows if required.

