#!/usr/bin/env python
"""Module to design window based fir filter and analyse the frequency response 
of fir filters.

This implementation is largely based on Chapter 16 of The Scientist and 
Engineer's Guide to Digital Signal Processing Second Edition.

"""

import pylab
import numpy

def hamming(M):
    """Return an M + 1 point symmetric hamming window."""
    if M%2:
        raise Exception('M must be even')
    return 0.54 - 0.46*numpy.cos(2*numpy.pi*numpy.arange(M + 1)/M)

def blackman(M):
    """Return an M + 1 point symmetric point hamming window."""
    if M%2:
        raise Exception('M must be even')
    return (0.42 - 0.5*numpy.cos(2*numpy.pi*numpy.arange(M + 1)/M) + 
            0.08*numpy.cos(4*numpy.pi*numpy.arange(M + 1)/M))

def sinc_filter(M, fc):
    """Return an M + 1 point symmetric point sinc kernel with normalised cut-off 
    frequency fc 0->0.5."""
    if M%2:
        raise Exception('M must be even')
    return numpy.sinc(2*fc*(numpy.arange(M + 1) - M/2))

def plot_fft(x, style='b'):
    """Convenience routine for plotting fft's of signal with normalised 
    frequency axis."""
    pylab.plot(numpy.arange(len(x))/float(len(x)), numpy.abs(numpy.fft.fft(x))
                , style)

def build_filter(M, fc, window=None):
    """Construct filter using the windowing method for filter parameters M
    number of taps, cut-off frequency fc and window. Window defaults to None 
    i.e. a rectangular window."""
    if window is None:
        h = sinc_filter(M, fc)
    else:
        h = sinc_filter(M, fc)*window(M)
    return h/h.sum()

def main():
    f0 = 20 #20Hz
    ts = 0.01 # i.e. sampling frequency is 1/ts = 100Hz
    x = numpy.arange(-10, 10, ts)
    signal = (numpy.cos(2*numpy.pi*f0*x) + numpy.sin(2*numpy.pi*2*f0*x) + 
                numpy.cos(2*numpy.pi*0.5*f0*x) + numpy.cos(2*numpy.pi*1.5*f0*x))

    #build up some filters
    #Low pass
    M = 100 #number of taps in filter
    fc = 0.25 #i.e. normalised cutoff frequency 1/4 of sampling rate i.e. 25Hz
    ham_lp = build_filter(M, fc, window=hamming)
    black_lp = build_filter(M, fc, window=blackman)
    rect_lp = build_filter(M, fc)

    #filter the signals
    f_ham = numpy.convolve(signal, ham_lp)
    f_black = numpy.convolve(signal, black_lp)
    f_rect = numpy.convolve(signal, rect_lp)

    #plotting
    pylab.figure()
    pylab.subplot(3,1,1)
    pylab.title('Original Spectrum')
    pylab.xlabel('Normalised Frequency')
    plot_fft(signal)
    pylab.subplot(3,1,2)
    pylab.title('Lowpass Filter Frequency Response')
    pylab.xlabel('Normalised Frequency')
    plot_fft(ham_lp)
    plot_fft(black_lp, style='k')
    plot_fft(rect_lp, style='r')
    pylab.legend(('Hamming', 'Blackman', 'Rectangular'))
    #window and fft
    pylab.subplot(3,1,3)
    pylab.title('Filtered Spectrum')
    pylab.xlabel('Normalised Frequency')
    plot_fft(hamming(len(f_ham))[:-1]*(f_ham))
    plot_fft(hamming(len(f_black))[:-1]*(f_black), 'k')
    plot_fft(hamming(len(f_rect))[:-1]*(f_rect), 'r')
    pylab.subplots_adjust(hspace = 0.6)

    #High Pass
    shift = numpy.cos(2*numpy.pi*0.5*numpy.arange(M + 1))
    ham_hp = ham_lp*shift
    black_hp = black_lp*shift
    rect_hp = rect_lp*shift

    #filter the signals
    f_ham = numpy.convolve(signal, ham_hp)
    f_black = numpy.convolve(signal, black_hp)
    f_rect = numpy.convolve(signal, rect_hp)

    #plotting
    pylab.figure()
    pylab.subplot(3,1,1)
    pylab.title('Original Spectrum')
    pylab.xlabel('Normalised Frequency')
    plot_fft(signal)
    pylab.subplot(3,1,2)
    pylab.title('Highpass Filter Frequency Response')
    pylab.xlabel('Normalised Frequency')
    plot_fft(ham_hp)
    plot_fft(black_hp, style='k')
    plot_fft(rect_hp, style='r')
    pylab.legend(('Hamming', 'Blackman', 'Rectangular'))
    #window and fft
    pylab.subplot(3,1,3)
    pylab.title('Filtered Spectrum')
    pylab.xlabel('Normalised Frequency')
    plot_fft(hamming(len(f_ham))[:-1]*(f_ham))
    plot_fft(hamming(len(f_black))[:-1]*(f_black), 'k')
    plot_fft(hamming(len(f_rect))[:-1]*(f_rect), 'r')
    pylab.subplots_adjust(hspace = 0.6)

    #Bandpass
    #first need a low-pass with fc 0.35
    fc = 0.35
    ham_lp = build_filter(M, fc, window=hamming)
    black_lp = build_filter(M, fc, window=blackman)
    rect_lp = build_filter(M, fc)
    ham_hp = ham_lp*shift
    black_hp = black_lp*shift
    rect_hp = rect_lp*shift
    #now we can create the bandpass filter
    ham_bp = numpy.convolve(ham_lp, ham_hp)
    black_bp = numpy.convolve(black_lp, black_hp)
    rect_bp = numpy.convolve(rect_lp, rect_hp)

    #filter the signals
    f_ham = numpy.convolve(signal, ham_bp)
    f_black = numpy.convolve(signal, black_bp)
    f_rect = numpy.convolve(signal, rect_bp)

    #plotting
    pylab.figure()
    pylab.subplot(3,1,1)
    pylab.title('Original Spectrum')
    pylab.xlabel('Normalised Frequency')
    plot_fft(signal)
    pylab.subplot(3,1,2)
    pylab.title('Bandpass Filter Frequency Response')
    pylab.xlabel('Normalised Frequency')
    plot_fft(ham_bp)
    plot_fft(black_bp, style='k')
    plot_fft(rect_bp, style='r')
    pylab.legend(('Hamming', 'Blackman', 'Rectangular'))
    #window and fft
    pylab.subplot(3,1,3)
    pylab.title('Filtered Spectrum')
    pylab.xlabel('Normalised Frequency')
    plot_fft(hamming(len(f_ham))[:-1]*(f_ham))
    plot_fft(hamming(len(f_black))[:-1]*(f_black), 'k')
    plot_fft(hamming(len(f_rect))[:-1]*(f_rect), 'r')
    pylab.subplots_adjust(hspace = 0.6)

    #Bandstop
    #first need a low-pass with fc 0.15
    fc = 0.15
    ham_lp = build_filter(M, fc, window=hamming)
    black_lp = build_filter(M, fc, window=blackman)
    rect_lp = build_filter(M, fc)
    #next need a high-pass
    ham_hp = ham_lp*shift
    black_hp = black_lp*shift
    rect_hp = rect_lp*shift
    #now we can create the bandstop filter
    ham_bs = ham_lp + ham_hp
    black_bs = black_lp + black_hp
    rect_bs = rect_lp + rect_hp

    #filter the signals
    f_ham = numpy.convolve(signal, ham_bs)
    f_black = numpy.convolve(signal, black_bs)
    f_rect = numpy.convolve(signal, rect_bs)

    #plotting
    pylab.figure()
    pylab.subplot(3,1,1)
    pylab.title('Original Spectrum')
    pylab.xlabel('Normalised Frequency')
    plot_fft(signal)
    pylab.subplot(3,1,2)
    pylab.title('Bandstop Filter Frequency Response')
    pylab.xlabel('Normalised Frequency')
    plot_fft(ham_bs)
    plot_fft(black_bs, style='k')
    plot_fft(rect_bs, style='r')
    pylab.legend(('Hamming', 'Blackman', 'Rectangular'))
    #window and fft
    pylab.subplot(3,1,3)
    pylab.title('Filtered Spectrum')
    pylab.xlabel('Normalised Frequency')
    plot_fft(hamming(len(f_ham))[:-1]*(f_ham))
    plot_fft(hamming(len(f_black))[:-1]*(f_black), 'k')
    plot_fft(hamming(len(f_rect))[:-1]*(f_rect), 'r')
    pylab.subplots_adjust(hspace = 0.6)

    pylab.show()

if __name__ == '__main__':
    main()