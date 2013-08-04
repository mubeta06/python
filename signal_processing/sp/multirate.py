#!/usr/bin/env python
"""Module providing Multirate signal processing functionality.
Largely based on MATLAB's Multirate signal processing toolbox with consultation 
of Octave m-file source code.
"""

import sys
import fractions
import numpy
from scipy import signal


def downsample(s, n, phase=0):
    """Decrease sampling rate by integer factor n with included offset phase.
    """
    return s[phase::n]


def upsample(s, n, phase=0):
    """Increase sampling rate by integer factor n  with included offset phase.
    """
    return numpy.roll(numpy.kron(s, numpy.r_[1, numpy.zeros(n-1)]), phase)


def decimate(s, r, n=None, fir=False):
    """Decimation - decrease sampling rate by r. The decimation process filters 
    the input data s with an order n lowpass filter and then resamples the 
    resulting smoothed signal at a lower rate. By default, decimate employs an 
    eighth-order lowpass Chebyshev Type I filter with a cutoff frequency of 
    0.8/r. It filters the input sequence in both the forward and reverse 
    directions to remove all phase distortion, effectively doubling the filter 
    order. If 'fir' is set to True decimate uses an order 30 FIR filter (by 
    default otherwise n), instead of the Chebyshev IIR filter. Here decimate 
    filters the input sequence in only one direction. This technique conserves 
    memory and is useful for working with long sequences.
    """
    if fir:
        if n is None:
            n = 30
        b = signal.firwin(n, 1.0/r)
        a = 1
        f = signal.lfilter(b, a, s)
    else: #iir
        if n is None:
            n = 8
        b, a = signal.cheby1(n, 0.05, 0.8/r)
        f = signal.filtfilt(b, a, s)
    return downsample(f, r)


def interp(s, r, l=4, alpha=0.5):
    """Interpolation - increase sampling rate by integer factor r. Interpolation 
    increases the original sampling rate for a sequence to a higher rate. interp
    performs lowpass interpolation by inserting zeros into the original sequence
    and then applying a special lowpass filter. l specifies the filter length 
    and alpha the cut-off frequency. The length of the FIR lowpass interpolating
    filter is 2*l*r+1. The number of original sample values used for 
    interpolation is 2*l. Ordinarily, l should be less than or equal to 10. The 
    original signal is assumed to be band limited with normalized cutoff 
    frequency 0=alpha=1, where 1 is half the original sampling frequency (the 
    Nyquist frequency). The default value for l is 4 and the default value for 
    alpha is 0.5.
    """
    b = signal.firwin(2*l*r+1, alpha/r);
    a = 1
    return r*signal.lfilter(b, a, upsample(s, r))[r*l+1:-1]


def resample(s, p, q, h=None):
    """Change sampling rate by rational factor. This implementation is based on
    the Octave implementation of the resample function. It designs the 
    anti-aliasing filter using the window approach applying a Kaiser window with
    the beta term calculated as specified by [2].
    
    Ref [1] J. G. Proakis and D. G. Manolakis,
    Digital Signal Processing: Principles, Algorithms, and Applications,
    4th ed., Prentice Hall, 2007. Chap. 6

    Ref [2] A. V. Oppenheim, R. W. Schafer and J. R. Buck, 
    Discrete-time signal processing, Signal processing series,
    Prentice-Hall, 1999
    """
    gcd = fractions.gcd(p,q)
    if gcd>1:
        p=p/gcd
        q=q/gcd
    
    if h is None: #design filter
        #properties of the antialiasing filter
        log10_rejection = -3.0
        stopband_cutoff_f = 1.0/(2.0 * max(p,q))
        roll_off_width = stopband_cutoff_f / 10.0
    
        #determine filter length
        #use empirical formula from [2] Chap 7, Eq. (7.63) p 476
        rejection_db = -20.0*log10_rejection;
        l = numpy.ceil((rejection_db-8.0) / (28.714 * roll_off_width))
  
        #ideal sinc filter
        t = numpy.arange(-l, l + 1)
        ideal_filter=2*p*stopband_cutoff_f*numpy.sinc(2*stopband_cutoff_f*t)  
  
        #determine parameter of Kaiser window
        #use empirical formula from [2] Chap 7, Eq. (7.62) p 474
        beta = signal.kaiser_beta(rejection_db)
          
        #apodize ideal filter response
        h = numpy.kaiser(2*l+1, beta)*ideal_filter

    ls = len(s)
    lh = len(h)

    l = (lh - 1)/2.0
    ly = numpy.ceil(ls*p/float(q))

    #pre and postpad filter response
    nz_pre = numpy.floor(q - numpy.mod(l,q))
    hpad = h[-lh+nz_pre:]

    offset = numpy.floor((l+nz_pre)/q)
    nz_post = 0;
    while numpy.ceil(((ls-1)*p + nz_pre + lh + nz_post )/q ) - offset < ly:
        nz_post += 1
    hpad = hpad[:lh + nz_pre + nz_post]

    #filtering
    xfilt = upfirdn(s, hpad, p, q)

    return xfilt[offset-1:offset-1+ly]


def upfirdn(s, h, p, q):
    """Upsample signal s by p, apply FIR filter as specified by h, and 
    downsample by q. Using fftconvolve as opposed to lfilter as it does not seem
    to do a full convolution operation (and its much faster than convolve).
    """
    return downsample(signal.fftconvolve(h, upsample(s, p)), q)

def main():
    """Show simple use cases for functionality provided by this module. Each 
    example below attempts to mimic the examples provided by mathworks MATLAB
    documentation, http://www.mathworks.com/help/toolbox/signal/
    """
    import pylab
    argv = sys.argv
    if len(argv) != 1:
        print >>sys.stderr, 'usage: python -m pim.sp.multirate'
        sys.exit(2)

    #Downsample
    x = numpy.arange(1, 11)
    print 'Down Sampling %s by 3' % x
    print  downsample(x, 3)
    print 'Down Sampling %s by 3 with phase offset 2' % x
    print  downsample(x, 3, phase=2)

    #Upsample
    x = numpy.arange(1, 5)
    print 'Up Sampling %s by 3' % x
    print upsample(x, 3)
    print 'Up Sampling %s by 3 with phase offset 2' % x
    print upsample(x, 3, 2)

    #Decimate
    t = numpy.arange(0, 1, 0.00025)
    x = numpy.sin(2*numpy.pi*30*t) + numpy.sin(2*numpy.pi*60*t)
    y = decimate(x,4)
    pylab.figure()
    pylab.subplot(2, 1, 1)
    pylab.title('Original Signal')
    pylab.stem(numpy.arange(len(x[0:120])), x[0:120])
    pylab.subplot(2, 1, 2)
    pylab.title('Decimated Signal')
    pylab.stem(numpy.arange(len(y[0:30])), y[0:30])

    #Interp
    t = numpy.arange(0, 1, 0.001)
    x = numpy.sin(2*numpy.pi*30*t) + numpy.sin(2*numpy.pi*60*t)
    y = interp(x,4)
    pylab.figure()
    pylab.subplot(2, 1, 1)
    pylab.title('Original Signal')
    pylab.stem(numpy.arange(len(x[0:30])), x[0:30])
    pylab.subplot(2, 1, 2)
    pylab.title('Interpolated Signal')
    pylab.stem(numpy.arange(len(y[0:120])), y[0:120])

    #upfirdn
    L = 147.0 
    M = 160.0
    N = 24.0*L
    h = signal.firwin(N-1, 1/M, window=('kaiser', 7.8562))
    h = L*h
    Fs = 48000.0
    n = numpy.arange(0, 10239)
    x  = numpy.sin(2*numpy.pi*1000/Fs*n)
    y = upfirdn(x, h, L, M)
    pylab.figure()
    pylab.stem(n[1:49]/Fs, x[1:49])
    pylab.stem(n[1:45]/(Fs*L/M), y[13:57], 'r', markerfmt='ro',)
    pylab.xlabel('Time (sec)')
    pylab.ylabel('Signal value')

    #resample
    fs1 = 10.0
    t1 = numpy.arange(0, 1 + 1.0/fs1, 1.0/fs1)
    x = t1
    y = resample(x, 3, 2)
    t2 = numpy.arange(0,(len(y)))*2.0/(3.0*fs1)
    pylab.figure()
    pylab.plot(t1, x, '*')
    pylab.plot(t2, y, 'o')
    pylab.plot(numpy.arange(-0.5,1.5, 0.01), numpy.arange(-0.5,1.5, 0.01), ':')
    pylab.legend(('original','resampled'))
    pylab.xlabel('Time')
    
    x = numpy.hstack([numpy.arange(1,11), numpy.arange(9,0,-1)])
    y = resample(x,3,2)
    pylab.figure()
    pylab.subplot(2, 1, 1)
    pylab.title('Edge Effects Not Noticeable')
    pylab.plot(numpy.arange(19)+1, x, '*')
    pylab.plot(numpy.arange(29)*2/3.0 + 1, y, 'o')
    pylab.legend(('original', 'resampled'))
    x = numpy.hstack([numpy.arange(10, 0, -1), numpy.arange(2,11)])
    y = resample(x,3,2)
    pylab.subplot(2, 1, 2)
    pylab.plot(numpy.arange(19)+1, x, '*')
    pylab.plot(numpy.arange(29)*2/3.0 + 1, y, 'o')
    pylab.title('Edge Effects Very Noticeable')
    pylab.legend(('original', 'resampled'))

    pylab.show()
    return 0

if __name__ == '__main__':
    sys.exit(main())
