"""This file is part of libqrencode python ctypes bindings.

Copyright (C) 2013 Matthew Baker <mu.beta.06@gmail.com>

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

from _bcm2835 import *

def main():
    """Example program for bcm2835 library. Shows how to interface with SPI to 
    transfer a byte to and from an SPI device.
    Original Author: Mike McCauley
    
    Usage: sudo python spi.py
    
    """
    if !bcm2835_init():
        return

    bcm2835_spi_begin()
    bcm2835_spi_setBitOrder(BCM2835_SPI_BIT_ORDER_MSBFIRST)      # The default
    bcm2835_spi_setDataMode(BCM2835_SPI_MODE0)                   # The default
    bcm2835_spi_setClockDivider(BCM2835_SPI_CLOCK_DIVIDER_65536) # The default
    bcm2835_spi_chipSelect(BCM2835_SPI_CS0)                      # The default
    bcm2835_spi_setChipSelectPolarity(BCM2835_SPI_CS0, LOW)      # the default

    # Send a byte to the slave and simultaneously read a byte back from the slave
    # If you tie MISO to MOSI, you should read back what was sent
    data = bcm2835_spi_transfer(0x23);
    print "Read from SPI: %02X\n" % data

    bcm2835_spi_end()
    bcm2835_close()

if __name__ == '__main__':
    main()
