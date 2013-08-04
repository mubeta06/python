#!/usr/bin/env python
"""
Module providing the functionality to generate Gold Codes / Sequences
"""

import numpy
import pylab

import filter
import mls


preferred_pairs = {5:[[2],[1,2,3]], 6:[[5],[1,4,5]], 7:[[4],[4,5,6]],
                        8:[[1,2,3,6,7],[1,2,7]], 9:[[5],[3,5,6]], 
                        10:[[2,5,9],[3,4,6,8,9]], 11:[[9],[3,6,9]]}


def gen_gold(seq1, seq2):
    """Function to produce a gold sequence based on two input preferred pair 
    Maximal Length Sequences
    """
    gold = [seq1, seq2]
    for shift in range(len(seq1)):
        gold.append(numpy.logical_xor(seq1, numpy.roll(seq2, -shift)))
    return gold


def gold(n):
    """Generate a set of 2^n +1 Gold Codes
    """
    n = int(n)
    if not n in preferred_pairs:
        raise ss.Error('preferred pairs for %s bits unknown' % str(n))
    seed = list(numpy.ones(n))
    seq1 = mls.lfsr(preferred_pairs[n][0], seed)
    seq2 = mls.lfsr(preferred_pairs[n][1], seed)
    return gen_gold(seq1, seq2)
 

def paper_eg():
    """Gold code set example base on paper by E. H. Dinan and B. Jabbari 
    Spreading Codes for Direct Sequence CDMA and Wideband CDMA Cellular 
    Networks"""
    seq1 = mls.lfsr([2],[1, 1, 1, 1, 1])
    print 'Sequence 1:', numpy.where(seq1, 1, 0)
    seq2 = mls.lfsr([1, 2, 3], [1, 1, 1, 1, 1])
    print 'Sequence 2:', numpy.where(seq2, 1, 0)
    gold = gen_gold(seq1, seq2)
    print 'Gold 0 shift combination:', numpy.where(gold[0], 1, 0)
    print 'Gold 1 shift combination:', numpy.where(gold[1], 1, 0)
    print 'Gold 30 shift combination:', numpy.where(gold[-1], 1, 0)
    
    pylab.figure()
    pylab.subplot(2,2,1)
    pylab.title('Autocorrelation gold[0]')
    g0 = numpy.where(gold[0], 1.0, -1.0)
    pylab.plot((numpy.roll(filter.ccorr(g0, g0).real, len(g0)/2-1)))
    pylab.subplot(2,2,2)
    pylab.title('Autocorrelation gold[30]')
    g30 = numpy.where(gold[30], 1.0, -1.0)
    pylab.plot((numpy.roll(filter.ccorr(g30, g30).real, len(g30)/2-1)))
    pylab.subplot(2,2,3)
    pylab.title('Crosscorrelation gold[0] gold[1]')
    g1 = numpy.where(gold[1], 1.0, -1.0)
    pylab.plot((numpy.roll(filter.ccorr(g0, g1).real, len(g0)/2-1)))
    pylab.subplot(2,2,4)
    pylab.title('Crosscorrelation gold[0] gold[30]')
    pylab.plot((numpy.roll(filter.ccorr(g0, g30).real, len(g0)/2-1)))
    pylab.show()
 

def web_eg():
    """Example of producing Gold Codes from the net 
    (http://paginas.fe.up.pt/~hmiranda/cm/Pseudo_Noise_Sequences.pdf)"""
    seq1 = mls.lfsr([1],[1,0,0])
    print 'Sequence 1:', numpy.where(seq1, 1, 0)
    seq2 = mls.lfsr([2], [1,0,0])
    print 'Sequence 2:', numpy.where(seq2, 1, 0)
    for gold in gen_gold(seq1, seq2):
        print 'Gold Code:', numpy.where(gold, 1, 0)


def main(nbits):
    """Main Program"""
    print nbits
    if nbits != None:
        g = gold(nbits)
        #plotting
        pylab.figure()
        pylab.subplot(2,2,1)
        pylab.title('Autocorrelation g[0]')
        g0 = numpy.where(g[0], 1.0, -1.0)
        pylab.plot((numpy.roll(filter.ccorr(g0, g0).real, len(g0)/2-1)))
        pylab.xlim(0, len(g0))
        pylab.subplot(2,2,2)
        pylab.title('Autocorrelation g[-1]')
        gm1 = numpy.where(g[-1], 1.0, -1.0)
        pylab.plot((numpy.roll(filter.ccorr(gm1, gm1).real, len(gm1)/2-1)))
        pylab.xlim(0, len(gm1))
        pylab.subplot(2,2,3)
        pylab.title('Crosscorrelation g[0] g[1]')
        g1 = numpy.where(g[1], 1.0, -1.0)
        pylab.plot((numpy.roll(filter.ccorr(g0, g1).real, len(g0)/2-1)))
        pylab.xlim(0, len(g0))
        pylab.subplot(2,2,4)
        pylab.title('Crosscorrelation g[0] g[-1]')
        pylab.plot((numpy.roll(filter.ccorr(g0, gm1).real, len(g0)/2-1)))
        pylab.xlim(0, len(g0))
        pylab.show()
    else:
        print 'Paper Example:'
        paper_eg()
        print 'Web Example:'
        web_eg()


if __name__ == '__main__':
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else None)
