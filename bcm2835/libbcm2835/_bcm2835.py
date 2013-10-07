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

from ctypes import *

_libraries = {}
_libraries['/usr/local/lib/libbcm2835.so'] = CDLL('/usr/local/lib/libbcm2835.so')
STRING = c_char_p


BCM2835_I2C_CLOCK_DIVIDER_150 = 150
BCM2835_PWM_CLOCK_DIVIDER_1 = 1
BCM2835_PWM_CLOCK_DIVIDER_2 = 2
BCM2835_PWM_CLOCK_DIVIDER_4 = 4
BCM2835_PWM_CLOCK_DIVIDER_8 = 8
BCM2835_PWM_CLOCK_DIVIDER_16 = 16
BCM2835_PWM_CLOCK_DIVIDER_32 = 32
BCM2835_PWM_CLOCK_DIVIDER_64 = 64
BCM2835_PWM_CLOCK_DIVIDER_128 = 128
BCM2835_PWM_CLOCK_DIVIDER_256 = 256
BCM2835_PWM_CLOCK_DIVIDER_512 = 512
BCM2835_PWM_CLOCK_DIVIDER_1024 = 1024
BCM2835_PWM_CLOCK_DIVIDER_2048 = 2048
BCM2835_PWM_CLOCK_DIVIDER_4096 = 4096
BCM2835_PWM_CLOCK_DIVIDER_8192 = 8192
BCM2835_PWM_CLOCK_DIVIDER_16384 = 16384
BCM2835_PWM_CLOCK_DIVIDER_32768 = 32768
BCM2835_GPIO_FSEL_ALT2 = 6
BCM2835_SPI_CS_NONE = 3
BCM2835_SPI_CS2 = 2
BCM2835_SPI_CS1 = 1
BCM2835_SPI_BIT_ORDER_MSBFIRST = 1
BCM2835_SPI_BIT_ORDER_LSBFIRST = 0
BCM2835_GPIO_PUD_UP = 2
BCM2835_GPIO_PUD_DOWN = 1
BCM2835_GPIO_PUD_OFF = 0
BCM2835_SPI_CS0 = 0
BCM2835_GPIO_FSEL_MASK = 7
BCM2835_GPIO_FSEL_ALT5 = 2
RPI_V2_GPIO_P5_04 = 29
BCM2835_SPI_CLOCK_DIVIDER_32768 = 32768
BCM2835_SPI_CLOCK_DIVIDER_65536 = 0
BCM2835_GPIO_FSEL_ALT3 = 7
RPI_V2_GPIO_P1_24 = 8
BCM2835_I2C_CLOCK_DIVIDER_148 = 148
RPI_V2_GPIO_P1_23 = 11
BCM2835_I2C_CLOCK_DIVIDER_626 = 626
BCM2835_I2C_CLOCK_DIVIDER_2500 = 2500
BCM2835_GPIO_FSEL_OUTP = 1
RPI_V2_GPIO_P1_21 = 9
BCM2835_PAD_GROUP_GPIO_28_45 = 1
BCM2835_PAD_GROUP_GPIO_0_27 = 0
RPI_V2_GPIO_P1_19 = 10
RPI_V2_GPIO_P1_18 = 24
RPI_V2_GPIO_P1_15 = 22
RPI_V2_GPIO_P5_06 = 31
RPI_V2_GPIO_P5_05 = 30
BCM2835_GPIO_FSEL_ALT4 = 3
RPI_V2_GPIO_P5_03 = 28
RPI_V2_GPIO_P1_26 = 7
BCM2835_GPIO_FSEL_ALT1 = 5
BCM2835_GPIO_FSEL_ALT0 = 4
RPI_V2_GPIO_P1_05 = 3
RPI_V2_GPIO_P1_22 = 25
BCM2835_GPIO_FSEL_INPT = 0
RPI_V2_GPIO_P1_16 = 23
RPI_V2_GPIO_P1_03 = 2
RPI_V2_GPIO_P1_13 = 27
RPI_V2_GPIO_P1_12 = 18
RPI_V2_GPIO_P1_11 = 17
RPI_V2_GPIO_P1_10 = 15
RPI_V2_GPIO_P1_08 = 14
RPI_V2_GPIO_P1_07 = 4
BCM2835_SPI_CLOCK_DIVIDER_4 = 4
BCM2835_SPI_CLOCK_DIVIDER_1 = 1
BCM2835_SPI_CLOCK_DIVIDER_2 = 2
RPI_GPIO_P1_26 = 7
RPI_GPIO_P1_24 = 8
RPI_GPIO_P1_23 = 11
RPI_GPIO_P1_22 = 25
BCM2835_SPI_CLOCK_DIVIDER_8 = 8
RPI_GPIO_P1_21 = 9
BCM2835_SPI_CLOCK_DIVIDER_128 = 128
RPI_GPIO_P1_18 = 24
BCM2835_SPI_CLOCK_DIVIDER_512 = 512
BCM2835_SPI_CLOCK_DIVIDER_1024 = 1024
BCM2835_SPI_CLOCK_DIVIDER_2048 = 2048
BCM2835_SPI_CLOCK_DIVIDER_16 = 16
RPI_GPIO_P1_12 = 18
BCM2835_SPI_CLOCK_DIVIDER_8192 = 8192
BCM2835_SPI_CLOCK_DIVIDER_16384 = 16384
RPI_GPIO_P1_08 = 14
RPI_GPIO_P1_07 = 4
BCM2835_SPI_CLOCK_DIVIDER_32 = 32
RPI_GPIO_P1_05 = 1
RPI_GPIO_P1_03 = 0
BCM2835_SPI_CLOCK_DIVIDER_64 = 64
RPI_GPIO_P1_19 = 10
BCM2835_PAD_GROUP_GPIO_46_53 = 2
BCM2835_SPI_CLOCK_DIVIDER_256 = 256
RPI_GPIO_P1_16 = 23
RPI_GPIO_P1_15 = 22
RPI_GPIO_P1_13 = 21
BCM2835_SPI_CLOCK_DIVIDER_4096 = 4096
RPI_GPIO_P1_11 = 17
RPI_GPIO_P1_10 = 15
BCM2835_SPI_MODE3 = 3
BCM2835_SPI_MODE2 = 2
BCM2835_SPI_MODE1 = 1
BCM2835_SPI_MODE0 = 0
BCM2835_I2C_REASON_ERROR_DATA = 4
BCM2835_I2C_REASON_ERROR_CLKT = 2
BCM2835_I2C_REASON_ERROR_NACK = 1
BCM2835_I2C_REASON_OK = 0
uint32_t = c_uint32
bcm2835_st = (POINTER(uint32_t)).in_dll(_libraries['/usr/local/lib/libbcm2835.so'], 'bcm2835_st')
bcm2835_gpio = (POINTER(uint32_t)).in_dll(_libraries['/usr/local/lib/libbcm2835.so'], 'bcm2835_gpio')
bcm2835_pwm = (POINTER(uint32_t)).in_dll(_libraries['/usr/local/lib/libbcm2835.so'], 'bcm2835_pwm')
bcm2835_clk = (POINTER(uint32_t)).in_dll(_libraries['/usr/local/lib/libbcm2835.so'], 'bcm2835_clk')
bcm2835_pads = (POINTER(uint32_t)).in_dll(_libraries['/usr/local/lib/libbcm2835.so'], 'bcm2835_pads')
bcm2835_spi0 = (POINTER(uint32_t)).in_dll(_libraries['/usr/local/lib/libbcm2835.so'], 'bcm2835_spi0')
bcm2835_bsc0 = (POINTER(uint32_t)).in_dll(_libraries['/usr/local/lib/libbcm2835.so'], 'bcm2835_bsc0')
bcm2835_bsc1 = (POINTER(uint32_t)).in_dll(_libraries['/usr/local/lib/libbcm2835.so'], 'bcm2835_bsc1')

# values for enumeration 'bcm2835FunctionSelect'
bcm2835FunctionSelect = c_int # enum

# values for enumeration 'bcm2835PUDControl'
bcm2835PUDControl = c_int # enum

# values for enumeration 'bcm2835PadGroup'
bcm2835PadGroup = c_int # enum

# values for enumeration 'RPiGPIOPin'
RPiGPIOPin = c_int # enum

# values for enumeration 'bcm2835SPIBitOrder'
bcm2835SPIBitOrder = c_int # enum

# values for enumeration 'bcm2835SPIMode'
bcm2835SPIMode = c_int # enum

# values for enumeration 'bcm2835SPIChipSelect'
bcm2835SPIChipSelect = c_int # enum

# values for enumeration 'bcm2835SPIClockDivider'
bcm2835SPIClockDivider = c_int # enum

# values for enumeration 'bcm2835I2CClockDivider'
bcm2835I2CClockDivider = c_int # enum

# values for enumeration 'bcm2835I2CReasonCodes'
bcm2835I2CReasonCodes = c_int # enum

# values for enumeration 'bcm2835PWMClockDivider'
bcm2835PWMClockDivider = c_int # enum
bcm2835_init = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_init
bcm2835_init.restype = c_int
bcm2835_init.argtypes = []
bcm2835_close = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_close
bcm2835_close.restype = c_int
bcm2835_close.argtypes = []
uint8_t = c_uint8
bcm2835_set_debug = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_set_debug
bcm2835_set_debug.restype = None
bcm2835_set_debug.argtypes = [uint8_t]
bcm2835_peri_read = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_peri_read
bcm2835_peri_read.restype = uint32_t
bcm2835_peri_read.argtypes = [POINTER(uint32_t)]
bcm2835_peri_read_nb = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_peri_read_nb
bcm2835_peri_read_nb.restype = uint32_t
bcm2835_peri_read_nb.argtypes = [POINTER(uint32_t)]
bcm2835_peri_write = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_peri_write
bcm2835_peri_write.restype = None
bcm2835_peri_write.argtypes = [POINTER(uint32_t), uint32_t]
bcm2835_peri_write_nb = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_peri_write_nb
bcm2835_peri_write_nb.restype = None
bcm2835_peri_write_nb.argtypes = [POINTER(uint32_t), uint32_t]
bcm2835_peri_set_bits = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_peri_set_bits
bcm2835_peri_set_bits.restype = None
bcm2835_peri_set_bits.argtypes = [POINTER(uint32_t), uint32_t, uint32_t]
bcm2835_gpio_fsel = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_fsel
bcm2835_gpio_fsel.restype = None
bcm2835_gpio_fsel.argtypes = [uint8_t, uint8_t]
bcm2835_gpio_set = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_set
bcm2835_gpio_set.restype = None
bcm2835_gpio_set.argtypes = [uint8_t]
bcm2835_gpio_clr = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_clr
bcm2835_gpio_clr.restype = None
bcm2835_gpio_clr.argtypes = [uint8_t]
bcm2835_gpio_set_multi = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_set_multi
bcm2835_gpio_set_multi.restype = None
bcm2835_gpio_set_multi.argtypes = [uint32_t]
bcm2835_gpio_clr_multi = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_clr_multi
bcm2835_gpio_clr_multi.restype = None
bcm2835_gpio_clr_multi.argtypes = [uint32_t]
bcm2835_gpio_lev = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_lev
bcm2835_gpio_lev.restype = uint8_t
bcm2835_gpio_lev.argtypes = [uint8_t]
bcm2835_gpio_eds = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_eds
bcm2835_gpio_eds.restype = uint8_t
bcm2835_gpio_eds.argtypes = [uint8_t]
bcm2835_gpio_set_eds = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_set_eds
bcm2835_gpio_set_eds.restype = None
bcm2835_gpio_set_eds.argtypes = [uint8_t]
bcm2835_gpio_ren = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_ren
bcm2835_gpio_ren.restype = None
bcm2835_gpio_ren.argtypes = [uint8_t]
bcm2835_gpio_clr_ren = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_clr_ren
bcm2835_gpio_clr_ren.restype = None
bcm2835_gpio_clr_ren.argtypes = [uint8_t]
bcm2835_gpio_fen = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_fen
bcm2835_gpio_fen.restype = None
bcm2835_gpio_fen.argtypes = [uint8_t]
bcm2835_gpio_clr_fen = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_clr_fen
bcm2835_gpio_clr_fen.restype = None
bcm2835_gpio_clr_fen.argtypes = [uint8_t]
bcm2835_gpio_hen = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_hen
bcm2835_gpio_hen.restype = None
bcm2835_gpio_hen.argtypes = [uint8_t]
bcm2835_gpio_clr_hen = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_clr_hen
bcm2835_gpio_clr_hen.restype = None
bcm2835_gpio_clr_hen.argtypes = [uint8_t]
bcm2835_gpio_len = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_len
bcm2835_gpio_len.restype = None
bcm2835_gpio_len.argtypes = [uint8_t]
bcm2835_gpio_clr_len = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_clr_len
bcm2835_gpio_clr_len.restype = None
bcm2835_gpio_clr_len.argtypes = [uint8_t]
bcm2835_gpio_aren = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_aren
bcm2835_gpio_aren.restype = None
bcm2835_gpio_aren.argtypes = [uint8_t]
bcm2835_gpio_clr_aren = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_clr_aren
bcm2835_gpio_clr_aren.restype = None
bcm2835_gpio_clr_aren.argtypes = [uint8_t]
bcm2835_gpio_afen = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_afen
bcm2835_gpio_afen.restype = None
bcm2835_gpio_afen.argtypes = [uint8_t]
bcm2835_gpio_clr_afen = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_clr_afen
bcm2835_gpio_clr_afen.restype = None
bcm2835_gpio_clr_afen.argtypes = [uint8_t]
bcm2835_gpio_pud = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_pud
bcm2835_gpio_pud.restype = None
bcm2835_gpio_pud.argtypes = [uint8_t]
bcm2835_gpio_pudclk = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_pudclk
bcm2835_gpio_pudclk.restype = None
bcm2835_gpio_pudclk.argtypes = [uint8_t, uint8_t]
bcm2835_gpio_pad = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_pad
bcm2835_gpio_pad.restype = uint32_t
bcm2835_gpio_pad.argtypes = [uint8_t]
bcm2835_gpio_set_pad = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_set_pad
bcm2835_gpio_set_pad.restype = None
bcm2835_gpio_set_pad.argtypes = [uint8_t, uint32_t]
bcm2835_delay = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_delay
bcm2835_delay.restype = None
bcm2835_delay.argtypes = [c_uint]
uint64_t = c_uint64
bcm2835_delayMicroseconds = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_delayMicroseconds
bcm2835_delayMicroseconds.restype = None
bcm2835_delayMicroseconds.argtypes = [uint64_t]
bcm2835_gpio_write = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_write
bcm2835_gpio_write.restype = None
bcm2835_gpio_write.argtypes = [uint8_t, uint8_t]
bcm2835_gpio_write_multi = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_write_multi
bcm2835_gpio_write_multi.restype = None
bcm2835_gpio_write_multi.argtypes = [uint32_t, uint8_t]
bcm2835_gpio_write_mask = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_write_mask
bcm2835_gpio_write_mask.restype = None
bcm2835_gpio_write_mask.argtypes = [uint32_t, uint32_t]
bcm2835_gpio_set_pud = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_gpio_set_pud
bcm2835_gpio_set_pud.restype = None
bcm2835_gpio_set_pud.argtypes = [uint8_t, uint8_t]
bcm2835_spi_begin = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_spi_begin
bcm2835_spi_begin.restype = None
bcm2835_spi_begin.argtypes = []
bcm2835_spi_end = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_spi_end
bcm2835_spi_end.restype = None
bcm2835_spi_end.argtypes = []
bcm2835_spi_setBitOrder = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_spi_setBitOrder
bcm2835_spi_setBitOrder.restype = None
bcm2835_spi_setBitOrder.argtypes = [uint8_t]
uint16_t = c_uint16
bcm2835_spi_setClockDivider = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_spi_setClockDivider
bcm2835_spi_setClockDivider.restype = None
bcm2835_spi_setClockDivider.argtypes = [uint16_t]
bcm2835_spi_setDataMode = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_spi_setDataMode
bcm2835_spi_setDataMode.restype = None
bcm2835_spi_setDataMode.argtypes = [uint8_t]
bcm2835_spi_chipSelect = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_spi_chipSelect
bcm2835_spi_chipSelect.restype = None
bcm2835_spi_chipSelect.argtypes = [uint8_t]
bcm2835_spi_setChipSelectPolarity = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_spi_setChipSelectPolarity
bcm2835_spi_setChipSelectPolarity.restype = None
bcm2835_spi_setChipSelectPolarity.argtypes = [uint8_t, uint8_t]
bcm2835_spi_transfer = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_spi_transfer
bcm2835_spi_transfer.restype = uint8_t
bcm2835_spi_transfer.argtypes = [uint8_t]
bcm2835_spi_transfernb = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_spi_transfernb
bcm2835_spi_transfernb.restype = None
bcm2835_spi_transfernb.argtypes = [STRING, STRING, uint32_t]
bcm2835_spi_transfern = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_spi_transfern
bcm2835_spi_transfern.restype = None
bcm2835_spi_transfern.argtypes = [STRING, uint32_t]
bcm2835_spi_writenb = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_spi_writenb
bcm2835_spi_writenb.restype = None
bcm2835_spi_writenb.argtypes = [STRING, uint32_t]
bcm2835_i2c_begin = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_i2c_begin
bcm2835_i2c_begin.restype = None
bcm2835_i2c_begin.argtypes = []
bcm2835_i2c_end = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_i2c_end
bcm2835_i2c_end.restype = None
bcm2835_i2c_end.argtypes = []
bcm2835_i2c_setSlaveAddress = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_i2c_setSlaveAddress
bcm2835_i2c_setSlaveAddress.restype = None
bcm2835_i2c_setSlaveAddress.argtypes = [uint8_t]
bcm2835_i2c_setClockDivider = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_i2c_setClockDivider
bcm2835_i2c_setClockDivider.restype = None
bcm2835_i2c_setClockDivider.argtypes = [uint16_t]
bcm2835_i2c_set_baudrate = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_i2c_set_baudrate
bcm2835_i2c_set_baudrate.restype = None
bcm2835_i2c_set_baudrate.argtypes = [uint32_t]
bcm2835_i2c_write = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_i2c_write
bcm2835_i2c_write.restype = uint8_t
bcm2835_i2c_write.argtypes = [STRING, uint32_t]
bcm2835_i2c_read = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_i2c_read
bcm2835_i2c_read.restype = uint8_t
bcm2835_i2c_read.argtypes = [STRING, uint32_t]
bcm2835_i2c_read_register_rs = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_i2c_read_register_rs
bcm2835_i2c_read_register_rs.restype = uint8_t
bcm2835_i2c_read_register_rs.argtypes = [STRING, STRING, uint32_t]
bcm2835_st_read = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_st_read
bcm2835_st_read.restype = uint64_t
bcm2835_st_read.argtypes = []
bcm2835_st_delay = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_st_delay
bcm2835_st_delay.restype = None
bcm2835_st_delay.argtypes = [uint64_t, uint64_t]
bcm2835_pwm_set_clock = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_pwm_set_clock
bcm2835_pwm_set_clock.restype = None
bcm2835_pwm_set_clock.argtypes = [uint32_t]
bcm2835_pwm_set_mode = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_pwm_set_mode
bcm2835_pwm_set_mode.restype = None
bcm2835_pwm_set_mode.argtypes = [uint8_t, uint8_t, uint8_t]
bcm2835_pwm_set_range = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_pwm_set_range
bcm2835_pwm_set_range.restype = None
bcm2835_pwm_set_range.argtypes = [uint8_t, uint32_t]
bcm2835_pwm_set_data = _libraries['/usr/local/lib/libbcm2835.so'].bcm2835_pwm_set_data
bcm2835_pwm_set_data.restype = None
bcm2835_pwm_set_data.argtypes = [uint8_t, uint32_t]
int8_t = c_int8
int16_t = c_int16
int32_t = c_int32
int64_t = c_int64
int_least8_t = c_byte
int_least16_t = c_short
int_least32_t = c_int
int_least64_t = c_long
uint_least8_t = c_ubyte
uint_least16_t = c_ushort
uint_least32_t = c_uint
uint_least64_t = c_ulong
int_fast8_t = c_byte
int_fast16_t = c_long
int_fast32_t = c_long
int_fast64_t = c_long
uint_fast8_t = c_ubyte
uint_fast16_t = c_ulong
uint_fast32_t = c_ulong
uint_fast64_t = c_ulong
intptr_t = c_long
uintptr_t = c_ulong
intmax_t = c_long
uintmax_t = c_ulong
__all__ = ['RPI_V2_GPIO_P1_11', 'bcm2835PUDControl',
           'bcm2835_i2c_read', 'bcm2835_gpio_eds',
           'BCM2835_GPIO_PUD_DOWN', 'RPI_V2_GPIO_P1_22',
           'RPI_V2_GPIO_P1_23', 'int_fast32_t', 'RPI_V2_GPIO_P1_21',
           'RPI_V2_GPIO_P1_26', 'RPiGPIOPin', 'RPI_V2_GPIO_P1_24',
           'BCM2835_I2C_CLOCK_DIVIDER_148', 'BCM2835_SPI_MODE0',
           'BCM2835_SPI_MODE1', 'BCM2835_SPI_MODE2',
           'BCM2835_SPI_MODE3', 'uint8_t',
           'BCM2835_SPI_CLOCK_DIVIDER_2048',
           'BCM2835_SPI_BIT_ORDER_MSBFIRST', 'BCM2835_GPIO_FSEL_INPT',
           'BCM2835_SPI_CLOCK_DIVIDER_512', 'uint_least16_t',
           'bcm2835_gpio_set_eds', 'bcm2835_gpio_clr_afen',
           'bcm2835_spi_chipSelect', 'bcm2835_peri_write',
           'bcm2835_clk', 'BCM2835_I2C_CLOCK_DIVIDER_626',
           'BCM2835_SPI_CLOCK_DIVIDER_64', 'intptr_t',
           'uint_least64_t', 'bcm2835_gpio_clr_fen', 'uint_fast64_t',
           'int_least32_t', 'bcm2835_gpio_set', 'bcm2835_gpio_pud',
           'bcm2835_st_delay', 'RPI_GPIO_P1_22', 'RPI_V2_GPIO_P1_16',
           'BCM2835_I2C_CLOCK_DIVIDER_150', 'RPI_GPIO_P1_21',
           'RPI_V2_GPIO_P1_13', 'RPI_V2_GPIO_P1_12', 'RPI_GPIO_P1_24',
           'RPI_V2_GPIO_P1_10', 'bcm2835_gpio_clr',
           'RPI_V2_GPIO_P1_19', 'RPI_V2_GPIO_P1_18',
           'bcm2835_gpio_lev', 'bcm2835_gpio_pudclk',
           'BCM2835_PWM_CLOCK_DIVIDER_32768', 'int_least16_t',
           'bcm2835_gpio_set_pud', 'bcm2835_gpio_hen',
           'BCM2835_GPIO_FSEL_MASK', 'BCM2835_I2C_REASON_ERROR_DATA',
           'BCM2835_GPIO_FSEL_ALT1', 'BCM2835_GPIO_PUD_OFF',
           'bcm2835_gpio_clr_ren', 'bcm2835_gpio_len',
           'bcm2835_spi_writenb', 'bcm2835_spi_setDataMode',
           'bcm2835_pwm_set_range', 'RPI_V2_GPIO_P5_04',
           'RPI_V2_GPIO_P5_05', 'RPI_V2_GPIO_P5_06', 'bcm2835_st',
           'bcm2835_i2c_setClockDivider', 'RPI_V2_GPIO_P5_03',
           'BCM2835_SPI_CLOCK_DIVIDER_32768', 'bcm2835_gpio_set_pad',
           'intmax_t', 'bcm2835_gpio_write',
           'BCM2835_PAD_GROUP_GPIO_28_45', 'bcm2835_bsc0',
           'RPI_V2_GPIO_P1_03', 'RPI_V2_GPIO_P1_05',
           'BCM2835_GPIO_PUD_UP', 'BCM2835_PWM_CLOCK_DIVIDER_4096',
           'uint_fast16_t', 'bcm2835_gpio_clr_len', 'uint_fast32_t',
           'bcm2835_gpio_write_multi', 'bcm2835SPIMode',
           'bcm2835_pwm_set_mode', 'bcm2835_i2c_end',
           'BCM2835_PWM_CLOCK_DIVIDER_16384',
           'bcm2835PWMClockDivider', 'BCM2835_PWM_CLOCK_DIVIDER_4',
           'BCM2835_PWM_CLOCK_DIVIDER_2', 'bcm2835_bsc1',
           'bcm2835_gpio_clr_hen', 'BCM2835_PWM_CLOCK_DIVIDER_1',
           'BCM2835_GPIO_FSEL_ALT5', 'BCM2835_GPIO_FSEL_ALT4',
           'BCM2835_GPIO_FSEL_ALT3', 'BCM2835_GPIO_FSEL_ALT2',
           'BCM2835_PWM_CLOCK_DIVIDER_8', 'BCM2835_GPIO_FSEL_ALT0',
           'BCM2835_I2C_CLOCK_DIVIDER_2500', 'RPI_GPIO_P1_08',
           'bcm2835I2CClockDivider', 'RPI_GPIO_P1_05',
           'RPI_GPIO_P1_07', 'RPI_GPIO_P1_03',
           'bcm2835_gpio_clr_aren', 'bcm2835_gpio_aren',
           'bcm2835_spi_setChipSelectPolarity', 'BCM2835_SPI_CS_NONE',
           'bcm2835_peri_write_nb', 'BCM2835_SPI_CLOCK_DIVIDER_32',
           'BCM2835_PWM_CLOCK_DIVIDER_64', 'bcm2835_gpio_fsel',
           'bcm2835_pwm', 'bcm2835_gpio_ren', 'uint16_t',
           'bcm2835SPIClockDivider', 'uint_fast8_t',
           'bcm2835_gpio_pad', 'RPI_GPIO_P1_19', 'RPI_GPIO_P1_18',
           'BCM2835_PWM_CLOCK_DIVIDER_128', 'RPI_GPIO_P1_13',
           'RPI_GPIO_P1_12', 'RPI_GPIO_P1_11', 'RPI_GPIO_P1_10',
           'RPI_GPIO_P1_16', 'RPI_GPIO_P1_15',
           'bcm2835_spi_transfernb', 'BCM2835_SPI_CLOCK_DIVIDER_256',
           'BCM2835_I2C_REASON_ERROR_CLKT', 'bcm2835_delay',
           'bcm2835_i2c_set_baudrate', 'bcm2835FunctionSelect',
           'bcm2835_i2c_read_register_rs', 'bcm2835_spi_transfern',
           'BCM2835_GPIO_FSEL_OUTP', 'BCM2835_PWM_CLOCK_DIVIDER_16',
           'bcm2835_i2c_write', 'bcm2835_spi0', 'bcm2835_gpio',
           'uint_least32_t', 'int_least64_t', 'bcm2835_gpio_afen',
           'bcm2835_set_debug', 'uintptr_t', 'bcm2835PadGroup',
           'bcm2835_gpio_fen', 'BCM2835_PWM_CLOCK_DIVIDER_8192',
           'int8_t', 'BCM2835_SPI_CLOCK_DIVIDER_128',
           'BCM2835_PAD_GROUP_GPIO_46_53', 'int32_t', 'int_fast64_t',
           'RPI_V2_GPIO_P1_08', 'BCM2835_PAD_GROUP_GPIO_0_27',
           'bcm2835_gpio_set_multi', 'BCM2835_SPI_CLOCK_DIVIDER_16',
           'bcm2835_st_read', 'BCM2835_SPI_BIT_ORDER_LSBFIRST',
           'bcm2835SPIBitOrder', 'bcm2835SPIChipSelect',
           'BCM2835_SPI_CLOCK_DIVIDER_1024', 'bcm2835_spi_begin',
           'int16_t', 'uint64_t', 'bcm2835I2CReasonCodes',
           'bcm2835_spi_setClockDivider',
           'BCM2835_SPI_CLOCK_DIVIDER_1',
           'BCM2835_SPI_CLOCK_DIVIDER_2',
           'BCM2835_SPI_CLOCK_DIVIDER_4', 'bcm2835_spi_setBitOrder',
           'BCM2835_SPI_CLOCK_DIVIDER_8', 'bcm2835_gpio_clr_multi',
           'bcm2835_init', 'uintmax_t', 'int64_t', 'int_fast16_t',
           'bcm2835_i2c_setSlaveAddress', 'bcm2835_delayMicroseconds',
           'uint_least8_t', 'BCM2835_PWM_CLOCK_DIVIDER_1024',
           'bcm2835_pwm_set_data', 'BCM2835_PWM_CLOCK_DIVIDER_32',
           'bcm2835_i2c_begin', 'BCM2835_PWM_CLOCK_DIVIDER_512',
           'BCM2835_SPI_CLOCK_DIVIDER_65536', 'RPI_V2_GPIO_P1_07',
           'int_fast8_t', 'BCM2835_PWM_CLOCK_DIVIDER_256',
           'BCM2835_I2C_REASON_ERROR_NACK', 'bcm2835_spi_transfer',
           'bcm2835_peri_set_bits', 'BCM2835_SPI_CLOCK_DIVIDER_8192',
           'BCM2835_SPI_CLOCK_DIVIDER_16384',
           'BCM2835_SPI_CLOCK_DIVIDER_4096', 'bcm2835_peri_read_nb',
           'bcm2835_pwm_set_clock', 'bcm2835_gpio_write_mask',
           'BCM2835_SPI_CS2', 'BCM2835_SPI_CS1', 'BCM2835_SPI_CS0',
           'bcm2835_close', 'BCM2835_I2C_REASON_OK', 'RPI_GPIO_P1_23',
           'RPI_V2_GPIO_P1_15', 'bcm2835_spi_end',
           'BCM2835_PWM_CLOCK_DIVIDER_2048', 'bcm2835_peri_read',
           'uint32_t', 'RPI_GPIO_P1_26', 'int_least8_t',
           'bcm2835_pads']
