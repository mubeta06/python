#!/usr/bin/env python
"""Module to provide filter functions for data, etc.

"""

from numpy import fft

def cconv(x, y):
    """Calculate the circular convolution of 1-D input numpy arrays using DFT
    """
    return fft.ifft(fft.fft(x)*fft.fft(y))

def ccorr(x, y):
    """Calculate the circular correlation of 1-D input numpy arrays using DFT
    """
    return fft.ifft(fft.fft(x)*fft.fft(y).conj())

