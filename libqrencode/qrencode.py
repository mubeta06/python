#!/usr/bin/env python
"""Python ctypes binding to libqrencode.

This module when ran as a script attempts to mimic the c sample program 
qrenc.c otherwise known as qrencode


This file is part of libqrencode python ctypes bindings.

Copyright (C) 2012 Matthew Baker <mu.beta.06@gmail.com>

This is free software: you can redistribute it and/or modify
it under the terms of the LGNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This software is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the LGNU Lesser General Public License
along with this software.  If not, see <http://www.gnu.org/licenses/>."""

import ctypes
import errno
import optparse
import os
import sys

from _qrencode import *


class Error(Exception):

    """This is a user-defined exception for errors raised by this module."""

    pass


def call(func, *args):
    """Convenience routine to call function func, check for NULL pointer and
    subsequently check errno to report useful error message."""
    p = func(*args)
    if p:
        return p
    else:
        raise Error('NULL pointer returned when calling %s, errno %s' % 
                    (str(func), errno.errorcode[ctypes.get_errno()]))


class QREncode(object):

    """Base class for representing QREncode c structures. Allows for struct 
    member read access as class attributes."""

    def __init__(self, p):
        """Initialise an DmtxStructure object with pointer p."""
        self._p = p

    def __getattribute__(self, name):
       """Overloaded method so each field of c structure can be assessed as 
       read only attributes."""
       try:
           return object.__getattribute__(self, name)
       except AttributeError:
           p = object.__getattribute__(self, '_p')
           return getattr(p.contents, name)


class QRcode(QREncode):

    """Python representation of QRcode c structure"""

    def __init__(self, p, cleanup=True):
        if p:
            super(QRcode, self).__init__(p)
            self.cleanup = cleanup #boolean to perform QRcode cleanup or not
        else:
            raise ValueError('Invalid pointer to QRcode c structure required')

    def __del__(self):
        """Clean up QRcode c structure."""
        if self._p and self.cleanup:
            QRcode_free(self._p)


class QRcode_List(QREncode, list):

    """Python representation of QRcode_List c structure."""

    def __init__(self, p):
        if p:
            super(QRcode_List, self).__init__(p)
            while p:
                self.append(QRcode(p.contents.code, cleanup=False))
                p = p.contents.next
        else:
            raise ValueError('Invalid pointer to QRcode_List c structure')

    def __del__(self):
        """Clean up QRcode_List c structure."""
        if self._p:
            QRcode_List_free(self._p)


class QREncoder(object):

    """Base class for representing QREncoder.
    
    Largely used to maintain the state that the globals in qrenc.c represent.
    """

    def __init__(self):
        """Initialise object."""
        self._casesensitive = True
        self._code = None #Represents encoded result i.e. a QRcode c structure
        self._eightbit = False
        self._hint = QR_MODE_8
        self._level = QR_ECLEVEL_L
        self._micro = False
        self._version = 0

    def encode(self, data):
        """Encode input string represented by data"""
        cdata = ctypes.cast(data, ctypes.POINTER(ctypes.c_ubyte 
                                if self.eightbit else ctypes.c_char))
        length = len(data)
        if self.micro:
            if self.version == 0:
                e = 'Version must be specified to encode a Micro QR Code symbol' 
                raise Error(e)
            elif self.version > MQRSPEC_VERSION_MAX:
                e = 'Version should be less or equal to %d.'
                raise Error(e % MQRSPEC_VERSION_MAX)
            elif self.eightbit:
                self.code = call(QRcode_encodeDataMQR, length, cdata, 
                                    self.version, self.level)
            else:
	        self.code = call(QRcode_encodeStringMQR, cdata, self.version, 
                                    self.level, self.hint, self.casesensitive)
        else:
            if self.eightbit:
                self.code = call(QRcode_encodeData, length, cdata, self.version,
                                    self.level)
            else:
                self.code = call(QRcode_encodeString, cdata, self.version, 
                                    self.level, self.hint, self.casesensitive)

    def as2dlist(self):
        """Return a list of lists describing the encoded data."""
        l = list()
        offset = 0
        for y in range(self.code.width):
            row = list()
            for x in range(self.code.width):
                row.append(bool(self.code.data[offset] & 1))
                offset += 1
            l.append(row)
        return l

    def asciipreview(self):
        """Print an ascii representation of the Encoder output to stdout"""
        for row in self.as2dlist():
            for col in row:
                sys.stdout.write('XX' if col else '  ')
            sys.stdout.write('\n')

    def asps(self):
        """Return a PostScript representation of the encoded QRCode.

        Paints the "black" symbol in the current colour on the assumption
        that the background has already been painted and appropriate colour.
        Symbols are assumed to be 1 user coordinate square.

        """
        ps = """
        %QR Code postscript output
        %Generated by qrencodes.py

        """
        # Get the datamatrix symbols in bottom-to-top & left-to-right order.
        rows = self.as2dlist()
        nrow = len(rows)
        ps += '%d array\n' % nrow
        for i in range(nrow):
            ps += 'dup %d [' % (nrow - 1 - i)
            for sym in rows[i]:
                ps += '1 ' if sym else '0 '
            ps += '] put\n'
        ps += """
        gsave 2 dict begin
        /x 0 def
        /y 0 def
        {
            {
                1 eq {x y 1 1 rectfill} if
                /x x 1 add store
            } forall
            /y y 1 add store
            /x 0 store
        } forall
        end grestore
        """
        return ps

    def _get_casesensitive(self):
        """Return the QREncoder's casesensitive property."""
        return int(self._casesensitive)

    def _set_casesensitive(self, casesensitive):
        if isinstance(casesensitive, (bool)):
            self._casesensitive = casesensitive
        else:
            raise ValueError('boolean required')

    def _get_code(self):
        """Return the QREncode object"""
        return self._code

    def _set_code(self, code):
        self._code = QRcode(code)

    def _get_eightbit(self):
        """Return the QREncoder's eightbit property."""
        return self._eightbit

    def _set_eightbit(self, eightbit):
        if isinstance(eightbit, (bool)):
            self._eightbit = eightbit
        else:
            raise ValueError('boolean required')

    def _get_hint(self):
        """Return the QREncoder's hint."""
        return self._hint

    def _set_hint(self, hint):
        if hint in [QR_MODE_8, QR_MODE_KANJI]:
            self._hint = hint
        else:
            raise ValueError('invalid hint %s' % str(hint))

    def _get_level(self):
        """Return the QREncoder's level."""
        return self._level

    def _set_level(self, level):
        if level in [QR_ECLEVEL_L, QR_ECLEVEL_M, QR_ECLEVEL_Q, QR_ECLEVEL_H]:
            self._level = level
        else:
            raise ValueError('invalid level %s' % str(level))

    def _get_micro(self):
        """Return the QREncoder's micro property."""
        return self._micro

    def _set_micro(self, micro):
        if isinstance(micro, (bool)):
            self._micro = micro
        else:
            raise ValueError('boolean required')

    def _get_version(self):
        """Return the QREncoder's symbol version property."""
        return self._version

    def _set_version(self, version):
        if isinstance(version, (int)) and 0<= version <= QRSPEC_VERSION_MAX:
            self._version = version
        else:
            raise ValueError('version must be 0<=int<=%d' % QRSPEC_VERSION_MAX)

    #properties
    casesensitive = property(_get_casesensitive, _set_casesensitive, None)
    code = property(_get_code, _set_code, None)
    eightbit = property(_get_eightbit, _set_eightbit, None)
    hint = property(_get_hint, _set_hint, None)
    level = property(_get_level, _set_level, None)
    micro = property(_get_micro, _set_micro, None)
    version = property(_get_version, _set_version, None)


class StructuredQREncoder(QREncoder):

    """Subclassing of QREncoder for structured QR encoding."""

    def __init__(self):
        """Initialise object."""
        super(StructuredQREncoder, self).__init__()
        self._code_list = [] # encoded result i.e. a QRcode_List c structure

    def encode(self, data):
        """Encode input string represented by data"""
        if self.version == 0:
            e = 'Version must be specified to encode structured symbols.'
            raise Error(e)
        elif self.micro:
            e = 'Micro QR Code does not support structured symbols.'
            raise Error(e)
        else:
            cdata = ctypes.cast(data, ctypes.POINTER(ctypes.c_ubyte 
                                    if self.eightbit else ctypes.c_char))
            length = len(data)
            if self.eightbit:
                self.code_list = call(QRcode_encodeDataStructured, length, 
                                        cdata, self.version, self.level)
            else:
	        self.code_list = call(QRcode_encodeStringStructured, cdata, 
                                        self.version, self.level, self.hint,
                                        self.casesensitive)
    def as2dlists(self):
        """Return a list of list of lists describing the encoded data."""
        l = list()
        for code in self.code_list:
            self._code = code
            l.append(super(StructuredQREncoder, self).as2dlist())
        return l

    def asciipreview(self):
        """Print an ascii representation of the Encoder output to stdout"""
        for code in self.code_list:
            self._code = code
            super(StructuredQREncoder, self).asciipreview()
            sys.stdout.write('\n')

    def asps(self):
        """Return a list of PostScript strings representing the encoded 
        QRCode's of the StructuredQREncoder."""
        l = list()
        for code in self.code_list:
            self._code = code
            l.append(super(StructuredQREncoder, self).asps())
        return l

    def _get_code_list(self):
        """Return StructuredQREncoder's code_list."""
        return self._code_list

    def _set_code_list(self, code_list):
        self._code_list = QRcode_List(code_list)        

    code_list = property(_get_code_list, _set_code_list, None)


def main(argv):
    import libqrencode
    version = libqrencode.version
    desc = """libqrencode ctypes python binding version %s, """ % version
    desc += """libqrencode version %s""" % QRcode_APIVersionString()
    usage = 'Usage: qrencode [OPTION]... [STRING]'
    p = optparse.OptionParser(description=desc, usage=usage)
    p.add_option('-o', '--filename', default=None, type='string', 
                    action='store', 
                    help='Encoded image filename (.png, .pdf, .jpg, .tif...)')
    p.add_option('-s', '--size', default=3, type='int', action='store', 
                    help='Specify module size in dots (pixels). (default=3)')
    p.add_option('-l', '--level', default='L', type='choice', action='store', 
                    choices=['L', 'M', 'Q', 'H'], 
                    help="""specify error correction level from L (lowest) to H 
                            (highest). (default=L)""")
    p.add_option('-v', '--symversion', default=0, type='int', action='store', 
                    help='specify the version of the symbol. (default=auto)')
    p.add_option('-m', '--margin', default=None, type='int', action='store', 
                    help="""specify the width of the margins. (default=4) 
                            (2 for Micro)))""")
    p.add_option('-d', '--dpi', default=72, type='int', action='store', 
                    help='specify the DPI of the generated PNG. (default=72)')
    p.add_option('-S', '--structured', default=False, action='store_true',
                    help="""make structured symbols. Version must be 
                            specified.""")
    p.add_option('-k', '--kanji', default=False, action='store_true',
                    help="""assume that the input text contains kanji 
                            (shift-jis).""")
    p.add_option('-c', '--casesensitive', default=True, action='store_false',
                    help="""encode lower-case alphabet characters in 8-bit mode.
                            (default)""")
    p.add_option('-8', '--eightbit', default=False, action='store_true',
                    help="""encode entire data in 8-bit mode. -k and -c will be
                            ignored.""")
    p.add_option('-M', '--micro', default=False, action='store_true',
                    help="""encode in a Micro QR Code. (experimental).""")
    options, args = p.parse_args(argv[1:])

    #set defaults and do error checking
    if options.margin is None:
        if options.micro:
            options.margin = 2
        else:
            options.margin = 4
    elif options.margin < 0:
        raise Error('Invalid margin: %d' % options.margin)
    if options.size <= 0:
        raise Error('Invalid size: %d' % options.size)
    if options.symversion < 0:
        raise Error('Invalid version: %d' % options.symversion)
    if options.level == 'L':
        options.level = QR_ECLEVEL_L
    elif options.level == 'M':
        options.level = QR_ECLEVEL_M
    elif options.level == 'Q':
        options.level = QR_ECLEVEL_Q
    elif options.level == 'H':
        options.level = QR_ECLEVEL_H
    if options.dpi < 0:
        raise Error('Invalid dpi: %d' % options.dpi)
    if options.kanji:
        options.kanji = QR_MODE_KANJI
    else:
        options.kanji = QR_MODE_8

    if args == []:
        string = sys.stdin.read() #read from stdin into string
    else:
        string = args[0]

    if not options.structured:
        encoder = QREncoder()
    else:
        encoder = StructuredQREncoder()

    #set properties of encoder
    encoder.casesensitive = options.casesensitive
    encoder.eightbit = options.eightbit
    encoder.hint = options.kanji
    encoder.level = options.level
    encoder.micro = options.micro
    encoder.version = options.symversion

    #encode
    encoder.encode(string)

    #next write output if required.
    if options.filename is None:
        encoder.asciipreview() #output to stdout
    else:
        try:
            from PIL import Image
        except Exception, e:
            e = 'Cannot write image %s, %s' % (options.filename, str(e))
            print >> sys.stderr, e
        def saveimage(filename, qr):
            qrim = Image.new('1', (len(qr),)*2)
            qrim.putdata([0 if symbol else 1 for row in qr for symbol in row])
            qrim = qrim.resize((len(qr)*options.size,)*2, Image.NEAREST)
            im = Image.new('1', tuple(s + 2*options.margin for s in qrim.size),
                            color=1)
            im.paste(qrim, (options.margin,)*2)
            im = im.convert('RGB')
            im.save(filename, dpi=(options.dpi,)*2)
        if isinstance(encoder, (StructuredQREncoder)):
            i = 1            
            for qr in encoder.as2dlists():
                basename, ext = os.path.splitext(options.filename)
                saveimage(basename + str(i) + ext, qr)
                i += 1
        else:
            qr = encoder.as2dlist()
            saveimage(options.filename, qr)


if __name__ == '__main__':
    main(sys.argv)
