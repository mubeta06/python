from ctypes import *

_libraries = {}
_libraries['/usr/local/lib/libbcm2835.so'] = CDLL('/usr/local/lib/libbcm2835.so')
STRING = c_char_p


BCM2835_PWM_CLOCK_DIVIDER_2048 = 2048
BCM2835_I2C_REASON_ERROR_DATA = 4
BCM2835_I2C_REASON_ERROR_CLKT = 2
BCM2835_I2C_REASON_ERROR_NACK = 1
BCM2835_I2C_REASON_OK = 0
RPI_GPIO_P1_26 = 7
RPI_V2_GPIO_P1_05 = 3
BCM2835_PWM_CLOCK_DIVIDER_8192 = 8192
RPI_GPIO_P1_11 = 17
BCM2835_PWM_CLOCK_DIVIDER_1 = 1
BCM2835_PWM_CLOCK_DIVIDER_2 = 2
BCM2835_PWM_CLOCK_DIVIDER_32 = 32
BCM2835_PWM_CLOCK_DIVIDER_64 = 64
BCM2835_PWM_CLOCK_DIVIDER_1024 = 1024
BCM2835_PWM_CLOCK_DIVIDER_32768 = 32768
BCM2835_GPIO_PUD_UP = 2
BCM2835_GPIO_PUD_DOWN = 1
BCM2835_GPIO_PUD_OFF = 0
BCM2835_SPI_CS_NONE = 3
BCM2835_SPI_CS2 = 2
BCM2835_SPI_CS1 = 1
BCM2835_SPI_CS0 = 0
BCM2835_I2C_CLOCK_DIVIDER_148 = 148
BCM2835_I2C_CLOCK_DIVIDER_626 = 626
BCM2835_I2C_CLOCK_DIVIDER_2500 = 2500
BCM2835_SPI_MODE3 = 3
BCM2835_SPI_MODE2 = 2
BCM2835_SPI_MODE0 = 0
BCM2835_PWM_CLOCK_DIVIDER_4 = 4
BCM2835_PWM_CLOCK_DIVIDER_8 = 8
BCM2835_PWM_CLOCK_DIVIDER_16 = 16
RPI_GPIO_P1_16 = 23
BCM2835_PWM_CLOCK_DIVIDER_128 = 128
BCM2835_PWM_CLOCK_DIVIDER_256 = 256
BCM2835_GPIO_FSEL_ALT5 = 2
BCM2835_GPIO_FSEL_ALT4 = 3
BCM2835_GPIO_FSEL_ALT2 = 6
BCM2835_PWM_CLOCK_DIVIDER_512 = 512
BCM2835_GPIO_FSEL_ALT0 = 4
BCM2835_GPIO_FSEL_OUTP = 1
BCM2835_GPIO_FSEL_INPT = 0
BCM2835_SPI_BIT_ORDER_MSBFIRST = 1
RPI_GPIO_P1_15 = 22
BCM2835_SPI_CLOCK_DIVIDER_1 = 1
BCM2835_SPI_CLOCK_DIVIDER_2 = 2
BCM2835_GPIO_FSEL_MASK = 7
BCM2835_SPI_CLOCK_DIVIDER_4 = 4
BCM2835_SPI_CLOCK_DIVIDER_8 = 8
BCM2835_SPI_CLOCK_DIVIDER_16 = 16
BCM2835_SPI_CLOCK_DIVIDER_32 = 32
BCM2835_SPI_CLOCK_DIVIDER_64 = 64
BCM2835_SPI_CLOCK_DIVIDER_128 = 128
RPI_V2_GPIO_P1_15 = 22
BCM2835_SPI_CLOCK_DIVIDER_256 = 256
BCM2835_SPI_CLOCK_DIVIDER_512 = 512
BCM2835_SPI_CLOCK_DIVIDER_1024 = 1024
BCM2835_SPI_CLOCK_DIVIDER_2048 = 2048
BCM2835_PWM_CLOCK_DIVIDER_4096 = 4096
BCM2835_SPI_CLOCK_DIVIDER_4096 = 4096
BCM2835_SPI_CLOCK_DIVIDER_8192 = 8192
BCM2835_SPI_CLOCK_DIVIDER_16384 = 16384
BCM2835_SPI_CLOCK_DIVIDER_32768 = 32768
BCM2835_SPI_CLOCK_DIVIDER_65536 = 0
BCM2835_GPIO_FSEL_ALT3 = 7
BCM2835_PWM_CLOCK_DIVIDER_16384 = 16384
BCM2835_SPI_BIT_ORDER_LSBFIRST = 0
BCM2835_GPIO_FSEL_ALT1 = 5
BCM2835_I2C_CLOCK_DIVIDER_150 = 150
RPI_V2_GPIO_P1_13 = 27
BCM2835_PAD_GROUP_GPIO_46_53 = 2
BCM2835_PAD_GROUP_GPIO_28_45 = 1
BCM2835_PAD_GROUP_GPIO_0_27 = 0
RPI_V2_GPIO_P5_05 = 30
RPI_V2_GPIO_P1_24 = 8
RPI_V2_GPIO_P1_23 = 11
RPI_V2_GPIO_P1_22 = 25
RPI_V2_GPIO_P1_21 = 9
RPI_V2_GPIO_P1_11 = 17
RPI_V2_GPIO_P1_19 = 10
RPI_V2_GPIO_P1_18 = 24
RPI_V2_GPIO_P5_04 = 29
RPI_V2_GPIO_P1_12 = 18
RPI_V2_GPIO_P1_10 = 15
RPI_V2_GPIO_P1_07 = 4
RPI_V2_GPIO_P5_03 = 28
RPI_V2_GPIO_P1_03 = 2
RPI_GPIO_P1_24 = 8
RPI_GPIO_P1_23 = 11
RPI_GPIO_P1_22 = 25
RPI_V2_GPIO_P1_26 = 7
RPI_GPIO_P1_21 = 9
RPI_GPIO_P1_19 = 10
RPI_GPIO_P1_18 = 24
RPI_GPIO_P1_13 = 21
RPI_GPIO_P1_12 = 18
RPI_GPIO_P1_07 = 4
RPI_GPIO_P1_05 = 1
RPI_GPIO_P1_03 = 0
RPI_GPIO_P1_10 = 15
RPI_V2_GPIO_P1_16 = 23
RPI_GPIO_P1_08 = 14
RPI_V2_GPIO_P1_08 = 14
RPI_V2_GPIO_P5_06 = 31
BCM2835_SPI_MODE1 = 1
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
BCM2835_SPI0_CS_ADCS = 2048 # Variable c_int '2048'
BCM2835_ST_CLO = 4 # Variable c_int '4'
BCM2835_PAD_DRIVE_16mA = 7 # Variable c_int '7'
_ATFILE_SOURCE = 1 # Variable c_int '1'
__USE_XOPEN2KXSI = 1 # Variable c_int '1'
BCM2835_BSC_S_RXR = 8 # Variable c_int '8'
BCM2835_BSC_DLEN = 8 # Variable c_int '8'
BCM2835_BSC_S_DONE = 2 # Variable c_int '2'
__GNU_LIBRARY__ = 6 # Variable c_int '6'
BCM2835_GPFEN1 = 92 # Variable c_int '92'
BCM2835_PWMCLK_CNTL = 40 # Variable c_int '40'
__USE_XOPEN = 1 # Variable c_int '1'
BCM2835_SPI0_CS_DONE = 65536 # Variable c_int '65536'
BCM2835_SPI0_LTOH = 16 # Variable c_int '16'
BCM2835_PWM1_MS_MODE = 32768 # Variable c_int '32768'
__USE_XOPEN2K8 = 1 # Variable c_int '1'
__USE_POSIX2 = 1 # Variable c_int '1'
BCM2835_SPI0_CS_TA = 128 # Variable c_int '128'
BCM2835_PWM1_ENABLE = 256 # Variable c_int '256'
BCM2835_PWM0_REVPOLAR = 16 # Variable c_int '16'
BCM2835_SPI0_CS_CLEAR_TX = 16 # Variable c_int '16'
BCM2835_BSC_C_ST = 128 # Variable c_int '128'
BCM2835_BSC0_BASE = 538988544 # Variable c_int '538988544'
BCM2835_GPIO_BASE = 538968064 # Variable c_int '538968064'
BCM2835_BSC_C_INTD = 256 # Variable c_int '256'
BCM2835_BSC_S_RXD = 32 # Variable c_int '32'
BCM2835_CORE_CLK_HZ = 250000000 # Variable c_int '250000000'
__STDC_IEC_559__ = 1 # Variable c_int '1'
BCM2835_SPI0_CS_RXD = 131072 # Variable c_int '131072'
HIGH = 1 # Variable c_int '1'
BCM2835_PWM0_MS_MODE = 128 # Variable c_int '128'
BCM2835_PWM1_OFFSTATE = 2048 # Variable c_int '2048'
__USE_ATFILE = 1 # Variable c_int '1'
BCM2835_SPI0_CS_RXR = 524288 # Variable c_int '524288'
__GLIBC_HAVE_LONG_LONG = 1 # Variable c_int '1'
BCM2835_BSC_C_INTT = 512 # Variable c_int '512'
BCM2835_PAD_DRIVE_12mA = 5 # Variable c_int '5'
BCM2835_BLOCK_SIZE = 4096 # Variable c_int '4096'
BCM2835_PAD_DRIVE_6mA = 2 # Variable c_int '2'
_POSIX_SOURCE = 1 # Variable c_int '1'
_ISOC95_SOURCE = 1 # Variable c_int '1'
BCM2835_BSC_S_CLKT = 512 # Variable c_int '512'
BCM2835_GPCLR1 = 44 # Variable c_int '44'
BCM2835_GPHEN0 = 100 # Variable c_int '100'
BCM2835_PWM_FIF1 = 6 # Variable c_int '6'
__USE_POSIX = 1 # Variable c_int '1'
__USE_SVID = 1 # Variable c_int '1'
BCM2835_PWM0_REPEATFF = 4 # Variable c_int '4'
BCM2835_GPFSEL3 = 12 # Variable c_int '12'
BCM2835_GPFSEL2 = 8 # Variable c_int '8'
BCM2835_GPFSEL1 = 4 # Variable c_int '4'
BCM2835_GPFSEL0 = 0 # Variable c_int '0'
BCM2835_PWMCLK_DIV = 41 # Variable c_int '41'
BCM2835_GPFSEL5 = 20 # Variable c_int '20'
BCM2835_GPFSEL4 = 16 # Variable c_int '16'
BCM2835_SPI0_BASE = 538984448 # Variable c_int '538984448'
BCM2835_GPPUDCLK0 = 152 # Variable c_int '152'
BCM2835_GPPUDCLK1 = 156 # Variable c_int '156'
BCM2835_SPI0_CS_CLEAR = 48 # Variable c_int '48'
BCM2835_PWM1_REPEATFF = 1024 # Variable c_int '1024'
__USE_POSIX199309 = 1 # Variable c_int '1'
BCM2835_PERI_BASE = 536870912 # Variable c_int '536870912'
BCM2835_PWM_DMAC = 2 # Variable c_int '2'
BCM2835_BSC_S_TXE = 64 # Variable c_int '64'
BCM2835_BSC_S_TXD = 16 # Variable c_int '16'
BCM2835_GPHEN1 = 104 # Variable c_int '104'
BCM2835_GPCLR0 = 40 # Variable c_int '40'
BCM2835_BSC_S_TXW = 4 # Variable c_int '4'
BCM2835_SPI0_CS_DMAEN = 256 # Variable c_int '256'
BCM2835_SPI0_CS_TXD = 262144 # Variable c_int '262144'
BCM2835_GPIO_PWM = 539017216 # Variable c_int '539017216'
BCM2835_BSC_C_CLEAR_1 = 32 # Variable c_int '32'
BCM2835_BSC_C_CLEAR_2 = 16 # Variable c_int '16'
_SVID_SOURCE = 1 # Variable c_int '1'
__USE_XOPEN2K = 1 # Variable c_int '1'
BCM2835_PADS_GPIO_0_27 = 44 # Variable c_int '44'
BCM2835_ST_CS = 0 # Variable c_int '0'
BCM2835_PWM0_OFFSTATE = 8 # Variable c_int '8'
BCM2835_PAD_SLEW_RATE_UNLIMITED = 16 # Variable c_int '16'
BCM2835_ST_BASE = 536883200 # Variable c_int '536883200'
BCM2835_PWM1_SERIAL = 512 # Variable c_int '512'
BCM2835_SPI0_CS_REN = 4096 # Variable c_int '4096'
__USE_GNU = 1 # Variable c_int '1'
__USE_BSD = 1 # Variable c_int '1'
BCM2835_GPSET1 = 32 # Variable c_int '32'
__USE_LARGEFILE64 = 1 # Variable c_int '1'
BCM2835_BSC_FIFO_SIZE = 16 # Variable c_int '16'
BCM2835_GPAREN1 = 128 # Variable c_int '128'
BCM2835_GPAREN0 = 124 # Variable c_int '124'
BCM2835_PWM0_SERIAL = 2 # Variable c_int '2'
_LARGEFILE_SOURCE = 1 # Variable c_int '1'
_POSIX_C_SOURCE = 200809 # Variable c_long '200809l'
BCM2835_SPI0_CS_INTR = 1024 # Variable c_int '1024'
BCM2835_SPI0_CS_LMONO = 16384 # Variable c_int '16384'
BCM2835_GPLEN1 = 116 # Variable c_int '116'
BCM2835_GPLEN0 = 112 # Variable c_int '112'
BCM2835_PAD_DRIVE_8mA = 3 # Variable c_int '3'
BCM2835_BSC_C_INTR = 1024 # Variable c_int '1024'
BCM2835_ST_CHI = 8 # Variable c_int '8'
BCM2835_SPI0_CS_CSPOL2 = 8388608 # Variable c_int '8388608'
BCM2835_SPI0_CS_CSPOL0 = 2097152 # Variable c_int '2097152'
BCM2835_SPI0_CS_CSPOL1 = 4194304 # Variable c_int '4194304'
BCM2835_SPI0_CS_INTD = 512 # Variable c_int '512'
__USE_UNIX98 = 1 # Variable c_int '1'
__USE_ANSI = 1 # Variable c_int '1'
BCM2835_PWM_PASSWRD = 1509949440 # Variable c_int '1509949440'
__USE_MISC = 1 # Variable c_int '1'
BCM2835_GPLEV1 = 56 # Variable c_int '56'
BCM2835_GPLEV0 = 52 # Variable c_int '52'
BCM2835_BSC_C_READ = 1 # Variable c_int '1'
__USE_EXTERN_INLINES_IN_LIBC = 1 # Variable c_int '1'
BCM2835_PWM_CONTROL = 0 # Variable c_int '0'
BCM2835_PAD_DRIVE_10mA = 4 # Variable c_int '4'
BCM2835_BSC_S_TA = 1 # Variable c_int '1'
BCM2835_PWM1_USEFIFO = 8192 # Variable c_int '8192'
BCM2835_GPREN0 = 76 # Variable c_int '76'
BCM2835_SPI0_CS_DMA_LEN = 16777216 # Variable c_int '16777216'
BCM2835_PAGE_SIZE = 4096 # Variable c_int '4096'
BCM2835_SPI0_FIFO = 4 # Variable c_int '4'
_STDINT_H = 1 # Variable c_int '1'
__USE_FORTIFY_LEVEL = 2 # Variable c_int '2'
_ISOC99_SOURCE = 1 # Variable c_int '1'
BCM2835_BSC_DIV = 20 # Variable c_int '20'
BCM2835_PWM0_DATA = 5 # Variable c_int '5'
BCM2835_BSC_CLKT = 28 # Variable c_int '28'
BCM2835_BSC_FIFO = 16 # Variable c_int '16'
__STDC_ISO_10646__ = 200009 # Variable c_long '200009l'
BCM2835_CLOCK_BASE = 537923584 # Variable c_int '537923584'
__STDC_IEC_559_COMPLEX__ = 1 # Variable c_int '1'
__USE_XOPEN_EXTENDED = 1 # Variable c_int '1'
BCM2835_PAD_HYSTERESIS_ENABLED = 8 # Variable c_int '8'
BCM2835_GPREN1 = 80 # Variable c_int '80'
__USE_POSIX199506 = 1 # Variable c_int '1'
BCM2835_SPI0_CLK = 8 # Variable c_int '8'
BCM2835_PAD_DRIVE_4mA = 1 # Variable c_int '1'
__USE_LARGEFILE = 1 # Variable c_int '1'
__USE_EXTERN_INLINES = 1 # Variable c_int '1'
BCM2835_GPPUD = 148 # Variable c_int '148'
BCM2835_GPIO_PADS = 537919488 # Variable c_int '537919488'
_FEATURES_H = 1 # Variable c_int '1'
BCM2835_BSC_S_ERR = 256 # Variable c_int '256'
BCM2835_PWM1_RANGE = 8 # Variable c_int '8'
BCM2835_PWM_STATUS = 1 # Variable c_int '1'
BCM2835_SPI0_CS_CPHA = 4 # Variable c_int '4'
BCM2835_BSC_C_I2CEN = 32768 # Variable c_int '32768'
BCM2835_GPSET0 = 28 # Variable c_int '28'
BCM2835_SPI0_CS_LEN_LONG = 33554432 # Variable c_int '33554432'
BCM2835_GPAFEN1 = 140 # Variable c_int '140'
BCM2835_GPAFEN0 = 136 # Variable c_int '136'
__WORDSIZE_COMPAT32 = 1 # Variable c_int '1'
BCM2835_BSC_S_RXF = 128 # Variable c_int '128'
LOW = 0 # Variable c_int '0'
BCM2835_PWM0_RANGE = 4 # Variable c_int '4'
__WCHAR_MIN = -2147483648 # Variable c_int '-0x00000000080000000'
BCM2835_PAD_DRIVE_14mA = 6 # Variable c_int '6'
BCM2835_SPI0_CS_CLEAR_RX = 32 # Variable c_int '32'
_XOPEN_SOURCE_EXTENDED = 1 # Variable c_int '1'
BCM2835_SPI0_CS_CSPOL = 64 # Variable c_int '64'
BCM2835_PWM0_USEFIFO = 32 # Variable c_int '32'
__USE_XOPEN2K8XSI = 1 # Variable c_int '1'
__WORDSIZE = 64 # Variable c_int '64'
BCM2835_PADS_GPIO_28_45 = 48 # Variable c_int '48'
BCM2835_SPI0_DC = 20 # Variable c_int '20'
BCM2835_SPI0_CS_TE_EN = 32768 # Variable c_int '32768'
BCM2835_BSC_DEL = 24 # Variable c_int '24'
_SYS_CDEFS_H = 1 # Variable c_int '1'
_LARGEFILE64_SOURCE = 1 # Variable c_int '1'
_XOPEN_SOURCE = 700 # Variable c_int '700'
BCM2835_SPI0_CS_RXF = 1048576 # Variable c_int '1048576'
BCM2835_PWM1_DATA = 9 # Variable c_int '9'
BCM2835_SPI0_CS_LEN = 8192 # Variable c_int '8192'
BCM2835_GPEDS0 = 64 # Variable c_int '64'
BCM2835_GPEDS1 = 68 # Variable c_int '68'
BCM2835_PAD_PASSWRD = 1509949440 # Variable c_int '1509949440'
BCM2835_GPFEN0 = 88 # Variable c_int '88'
__USE_ISOC95 = 1 # Variable c_int '1'
BCM2835_SPI0_DLEN = 12 # Variable c_int '12'
__GLIBC__ = 2 # Variable c_int '2'
__USE_ISOC99 = 1 # Variable c_int '1'
_BITS_WCHAR_H = 1 # Variable c_int '1'
__GLIBC_MINOR__ = 15 # Variable c_int '15'
BCM2835_PWM1_REVPOLAR = 4096 # Variable c_int '4096'
BCM2835_BSC_S = 4 # Variable c_int '4'
BCM2835_SPI0_CS = 0 # Variable c_int '0'
BCM2835_PWM_CLEAR_FIFO = 64 # Variable c_int '64'
BCM2835_PAD_DRIVE_2mA = 0 # Variable c_int '0'
BCM2835_PADS_GPIO_46_53 = 52 # Variable c_int '52'
BCM2835_BSC1_BASE = 545275904 # Variable c_int '545275904'
BCM2835_PWM0_ENABLE = 1 # Variable c_int '1'
_BSD_SOURCE = 1 # Variable c_int '1'
BCM2835_BSC_A = 12 # Variable c_int '12'
BCM2835_SPI0_CS_CS = 3 # Variable c_int '3'
BCM2835_BSC_C = 0 # Variable c_int '0'
BCM2835_SPI0_CS_CPOL = 8 # Variable c_int '8'
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
__all__ = ['BCM2835_SPI0_CS_ADCS', '_ATFILE_SOURCE',
           'BCM2835_PWM1_MS_MODE', 'bcm2835_i2c_read', 'int_fast32_t',
           'BCM2835_SPI_MODE0', 'BCM2835_SPI_MODE1',
           'BCM2835_SPI_MODE2', 'BCM2835_SPI_MODE3', 'uint8_t',
           'BCM2835_SPI_CLOCK_DIVIDER_2048', 'BCM2835_GPIO_FSEL_INPT',
           'BCM2835_SPI0_CS_CLEAR_TX', 'BCM2835_BSC0_BASE',
           'BCM2835_I2C_CLOCK_DIVIDER_626', 'BCM2835_BSC_S_RXD',
           'BCM2835_BSC_S_RXF', 'BCM2835_I2C_REASON_OK',
           'BCM2835_I2C_CLOCK_DIVIDER_150', 'BCM2835_BSC_S_RXR',
           'bcm2835_st_delay', 'BCM2835_BLOCK_SIZE',
           'BCM2835_PAD_DRIVE_6mA', '_POSIX_SOURCE',
           'bcm2835_gpio_hen', 'BCM2835_GPIO_FSEL_MASK',
           'BCM2835_SPI_BIT_ORDER_LSBFIRST', '__GNU_LIBRARY__',
           'BCM2835_PWMCLK_CNTL', 'bcm2835_st',
           'BCM2835_SPI_CLOCK_DIVIDER_32768', 'RPI_V2_GPIO_P1_03',
           'RPI_V2_GPIO_P1_05', 'RPI_V2_GPIO_P1_07',
           'bcm2835_gpio_clr_len', 'BCM2835_PWM_DMAC',
           'bcm2835I2CClockDivider', 'bcm2835_spi_setBitOrder',
           'bcm2835_gpio_set', 'bcm2835_gpio_clr',
           'BCM2835_GPIO_FSEL_ALT4', 'BCM2835_GPIO_FSEL_ALT3',
           'BCM2835_GPIO_FSEL_ALT2', 'BCM2835_GPIO_PUD_DOWN',
           'BCM2835_GPIO_FSEL_ALT0', 'BCM2835_SPI0_CS_DONE',
           'BCM2835_PWM0_OFFSTATE', 'BCM2835_GPSET0',
           'BCM2835_GPSET1', 'uint_fast8_t', '_LARGEFILE_SOURCE',
           'BCM2835_SPI_BIT_ORDER_MSBFIRST', 'BCM2835_PAD_DRIVE_8mA',
           '__USE_POSIX199506', 'BCM2835_GPIO_FSEL_OUTP',
           'BCM2835_PWM_CLOCK_DIVIDER_16', 'bcm2835_i2c_write',
           'uint_least32_t', 'int_least64_t', '__USE_FORTIFY_LEVEL',
           'BCM2835_BSC_DIV', 'BCM2835_PWM0_DATA',
           '__USE_XOPEN_EXTENDED', 'bcm2835SPIBitOrder',
           'BCM2835_SPI0_CLK', 'BCM2835_PAD_DRIVE_4mA',
           'BCM2835_GPPUD', 'bcm2835_spi_begin',
           'bcm2835_spi_setClockDivider',
           'BCM2835_SPI_CLOCK_DIVIDER_1',
           'BCM2835_SPI_CLOCK_DIVIDER_2',
           'BCM2835_SPI_CLOCK_DIVIDER_4',
           'BCM2835_SPI_CLOCK_DIVIDER_8', 'bcm2835_init',
           'BCM2835_BSC_FIFO', 'bcm2835_delayMicroseconds',
           'BCM2835_PWM_CLOCK_DIVIDER_1024', 'BCM2835_PWM0_REVPOLAR',
           '__WORDSIZE', 'BCM2835_SPI0_DC', '_XOPEN_SOURCE',
           'bcm2835_spi_transfer', 'BCM2835_GPEDS0',
           'BCM2835_SPI_CLOCK_DIVIDER_8192',
           'BCM2835_SPI_CLOCK_DIVIDER_16384', '__USE_ISOC95',
           '__GLIBC__', '__USE_ISOC99',
           'BCM2835_PWM_CLOCK_DIVIDER_2048', 'BCM2835_PWM0_ENABLE',
           'bcm2835PUDControl', '_SVID_SOURCE', 'BCM2835_BSC_S_DONE',
           'BCM2835_PWM0_RANGE', '__USE_XOPEN', '__USE_POSIX2',
           'BCM2835_BSC_C_INTT', 'BCM2835_PWM1_ENABLE',
           'bcm2835_i2c_begin', 'BCM2835_SPI_CLOCK_DIVIDER_512',
           'BCM2835_BSC_C_INTR', 'uint_least16_t',
           'BCM2835_BSC_C_INTD', 'bcm2835_gpio_clr_fen',
           'uint_fast64_t', 'bcm2835_gpio_pud', 'BCM2835_SPI0_CS_RXD',
           'HIGH', 'BCM2835_SPI0_CS_CSPOL0', '__USE_ATFILE',
           'BCM2835_SPI0_CS_RXR', 'bcm2835_pwm_set_clock',
           'bcm2835_gpio_pudclk', 'BCM2835_PWM_CLOCK_DIVIDER_32768',
           'bcm2835_gpio_set_pud', 'BCM2835_BSC_S_CLKT',
           'BCM2835_GPCLR1', 'BCM2835_GPCLR0', 'BCM2835_GPIO_PUD_OFF',
           '__USE_POSIX', 'BCM2835_PWM_FIF1',
           'bcm2835_i2c_setClockDivider', 'BCM2835_PWM1_REPEATFF',
           'bcm2835_pwm_set_data', 'BCM2835_PERI_BASE',
           'BCM2835_GPIO_PUD_UP', 'BCM2835_PWM_CLOCK_DIVIDER_4096',
           'uint_fast16_t', '_BITS_WCHAR_H', '__GLIBC_MINOR__',
           'bcm2835_gpio_write_multi', 'bcm2835_i2c_end',
           'BCM2835_PWM_CLOCK_DIVIDER_16384', 'BCM2835_SPI0_CS_TXD',
           'uint_least8_t', 'RPI_GPIO_P1_08', 'RPI_V2_GPIO_P1_16',
           'RPI_GPIO_P1_05', 'RPI_GPIO_P1_07', 'RPI_GPIO_P1_03',
           'bcm2835_gpio_clr_aren', 'BCM2835_GPEDS1',
           'BCM2835_SPI_CS_NONE', 'BCM2835_PAD_PASSWRD',
           'BCM2835_SPI_CLOCK_DIVIDER_32', '__USE_GNU',
           'bcm2835_gpio_fsel', 'bcm2835_pwm',
           'BCM2835_BSC_FIFO_SIZE', 'BCM2835_ST_CHI',
           'BCM2835_PWM0_SERIAL', '_POSIX_C_SOURCE',
           'BCM2835_SPI0_CS_INTR', 'BCM2835_SPI_CLOCK_DIVIDER_256',
           '__USE_SVID', 'bcm2835_delay', '__USE_ANSI',
           'BCM2835_GPLEV1', 'BCM2835_GPLEV0',
           'bcm2835_i2c_read_register_rs', 'BCM2835_PWM_CONTROL',
           'bcm2835_spi_transfern', 'bcm2835_gpio_ren',
           'BCM2835_BSC_S_TA', 'BCM2835_PWM1_USEFIFO',
           'BCM2835_PWM_CLOCK_DIVIDER_8192', 'BCM2835_PWM1_REVPOLAR',
           'BCM2835_BSC1_BASE', '__STDC_ISO_10646__',
           'BCM2835_PAD_GROUP_GPIO_46_53', 'BCM2835_PWM1_DATA',
           'RPI_V2_GPIO_P1_08', 'BCM2835_GPPUDCLK1', 'BCM2835_GPREN1',
           'bcm2835_pwm_set_range', '__USE_LARGEFILE',
           '__USE_EXTERN_INLINES', 'BCM2835_GPIO_PADS', '_FEATURES_H',
           'uint64_t', 'BCM2835_PWM1_RANGE', 'BCM2835_BSC_C_I2CEN',
           'BCM2835_SPI0_CS_LEN_LONG', 'BCM2835_GPAFEN1',
           'BCM2835_GPAFEN0', '__WORDSIZE_COMPAT32',
           'BCM2835_SPI0_CS_CLEAR_RX', '_XOPEN_SOURCE_EXTENDED',
           '__USE_POSIX199309', 'bcm2835_gpio_clr_afen',
           'BCM2835_SPI_CLOCK_DIVIDER_65536',
           'BCM2835_SPI_CLOCK_DIVIDER_4096',
           'bcm2835_gpio_write_mask', 'BCM2835_SPI_CS2',
           'BCM2835_SPI_CS1', 'BCM2835_SPI_CS0', 'BCM2835_BSC_S_ERR',
           'bcm2835_spi_end', 'BCM2835_PADS_GPIO_46_53',
           '_BSD_SOURCE', 'BCM2835_SPI0_CS_CS', 'BCM2835_ST_CLO',
           'bcm2835_gpio_eds', 'RPI_V2_GPIO_P1_22',
           'RPI_V2_GPIO_P1_23', 'RPI_V2_GPIO_P1_21',
           'RPI_V2_GPIO_P1_26', 'RPI_V2_GPIO_P1_24',
           '__USE_LARGEFILE64', '__USE_XOPEN2KXSI',
           'BCM2835_SPI0_CS_LMONO', 'bcm2835_spi_transfernb',
           'BCM2835_GPIO_BASE', 'bcm2835_gpio_set_eds',
           'bcm2835_gpio_set_multi', 'intptr_t', 'int_fast8_t',
           '__GLIBC_HAVE_LONG_LONG', 'BCM2835_GPIO_FSEL_ALT5',
           'bcm2835_peri_write', 'bcm2835_gpio_lev',
           'BCM2835_GPIO_FSEL_ALT1', 'bcm2835_gpio_len',
           'BCM2835_PWM0_REPEATFF', 'BCM2835_PWMCLK_DIV',
           'RPI_V2_GPIO_P5_04', 'RPI_V2_GPIO_P5_05',
           'RPI_V2_GPIO_P5_06', 'RPI_V2_GPIO_P5_03',
           'BCM2835_GPPUDCLK0', 'bcm2835_gpio_set_pad', 'int16_t',
           'BCM2835_PWM0_USEFIFO', 'bcm2835SPIMode',
           'bcm2835_pwm_set_mode', 'BCM2835_BSC_DLEN',
           'BCM2835_PWM_CLOCK_DIVIDER_4',
           'BCM2835_PWM_CLOCK_DIVIDER_2', 'bcm2835_gpio_clr_hen',
           'BCM2835_PWM_CLOCK_DIVIDER_1',
           'BCM2835_PWM_CLOCK_DIVIDER_8', 'BCM2835_GPIO_PWM',
           '__USE_XOPEN2K', 'BCM2835_PADS_GPIO_0_27',
           'bcm2835_spi_setChipSelectPolarity',
           'BCM2835_PAD_SLEW_RATE_UNLIMITED', 'BCM2835_ST_BASE',
           'BCM2835_PWM1_SERIAL', 'bcm2835_peri_write_nb',
           'BCM2835_GPAREN1', 'BCM2835_GPAREN0', 'uint16_t',
           'bcm2835SPIClockDivider', 'RPI_GPIO_P1_19',
           'RPI_GPIO_P1_18', 'BCM2835_GPLEN1',
           'BCM2835_PWM_CLOCK_DIVIDER_128', 'RPI_GPIO_P1_13',
           'RPI_GPIO_P1_12', 'RPI_GPIO_P1_11', 'RPI_GPIO_P1_10',
           'RPI_GPIO_P1_16', 'RPI_GPIO_P1_15',
           'BCM2835_I2C_REASON_ERROR_CLKT', 'BCM2835_SPI0_CS_CLEAR',
           '__USE_MISC', '__USE_EXTERN_INLINES_IN_LIBC',
           'bcm2835_spi0', 'bcm2835_gpio', 'BCM2835_SPI0_FIFO',
           'bcm2835_gpio_fen', '_STDINT_H',
           'BCM2835_SPI_CLOCK_DIVIDER_128', 'BCM2835_BSC_CLKT',
           'BCM2835_PAD_GROUP_GPIO_0_27',
           'BCM2835_PAD_HYSTERESIS_ENABLED', 'BCM2835_PWM_STATUS',
           'BCM2835_SPI0_CS_CPHA', 'uintmax_t', 'LOW', 'int_fast16_t',
           'BCM2835_PWM_CLOCK_DIVIDER_32', 'BCM2835_SPI0_CS_CSPOL',
           '__USE_XOPEN2K8XSI', 'BCM2835_BSC_C_ST',
           'BCM2835_PADS_GPIO_28_45', 'BCM2835_PWM0_MS_MODE',
           'BCM2835_SPI0_CS_TE_EN', '_SYS_CDEFS_H',
           'BCM2835_PWM_CLOCK_DIVIDER_256', 'BCM2835_SPI0_CS_RXF',
           'BCM2835_I2C_REASON_ERROR_NACK', 'bcm2835_peri_set_bits',
           'BCM2835_GPFEN1', 'BCM2835_GPFEN0',
           'bcm2835PWMClockDivider', 'BCM2835_BSC_S',
           'bcm2835_peri_read', 'uint32_t', 'BCM2835_BSC_A',
           'RPI_V2_GPIO_P1_13', 'BCM2835_BSC_C',
           'BCM2835_SPI0_CS_CPOL', 'bcm2835_pads',
           'BCM2835_PAD_DRIVE_16mA', 'RPI_V2_GPIO_P1_11',
           'BCM2835_I2C_REASON_ERROR_DATA', 'RPiGPIOPin',
           'BCM2835_I2C_CLOCK_DIVIDER_148', 'BCM2835_SPI0_LTOH',
           'bcm2835_bsc1', 'bcm2835_bsc0', '__USE_XOPEN2K8',
           'BCM2835_GPLEN0', 'BCM2835_PWM_CLOCK_DIVIDER_512',
           'bcm2835_spi_chipSelect', 'int32_t',
           'BCM2835_SPI_CLOCK_DIVIDER_64', 'BCM2835_CORE_CLK_HZ',
           'bcm2835_i2c_setSlaveAddress', 'int_least32_t',
           '__STDC_IEC_559__', 'RPI_GPIO_P1_22', 'RPI_GPIO_P1_23',
           'RPI_V2_GPIO_P1_15', 'RPI_GPIO_P1_21', 'RPI_GPIO_P1_26',
           'RPI_V2_GPIO_P1_12', 'RPI_GPIO_P1_24', 'RPI_V2_GPIO_P1_10',
           'RPI_V2_GPIO_P1_19', 'RPI_V2_GPIO_P1_18',
           'BCM2835_PAD_DRIVE_12mA', '_ISOC95_SOURCE',
           '_ISOC99_SOURCE', 'bcm2835_gpio_clr_ren',
           'bcm2835_spi_writenb', 'bcm2835_spi_setDataMode',
           'BCM2835_GPFSEL2', 'BCM2835_GPFSEL1', 'BCM2835_GPFSEL0',
           'BCM2835_GPFSEL5', 'BCM2835_GPFSEL4', 'BCM2835_SPI0_BASE',
           'intmax_t', 'bcm2835_gpio_write',
           'BCM2835_PAD_GROUP_GPIO_28_45', 'BCM2835_SPI0_CS_REN',
           'BCM2835_BSC_S_TXE', 'BCM2835_BSC_S_TXD', 'int_least8_t',
           'BCM2835_GPHEN1', 'BCM2835_GPHEN0', 'BCM2835_BSC_S_TXW',
           'int_least16_t', 'BCM2835_I2C_CLOCK_DIVIDER_2500',
           'BCM2835_BSC_C_CLEAR_1', 'BCM2835_BSC_C_CLEAR_2',
           'BCM2835_SPI0_CS_DMAEN', 'bcm2835_gpio_aren',
           'BCM2835_ST_CS', 'bcm2835_st_read',
           'BCM2835_PWM_CLOCK_DIVIDER_64', '__USE_BSD',
           'bcm2835_gpio_pad', 'BCM2835_GPFSEL3', 'bcm2835_clk',
           'uint_least64_t', 'BCM2835_SPI0_CS_CSPOL2',
           'BCM2835_PWM1_OFFSTATE', 'BCM2835_SPI0_CS_CSPOL1',
           '__USE_UNIX98', 'BCM2835_PAD_DRIVE_10mA',
           'bcm2835FunctionSelect', 'BCM2835_BSC_C_READ',
           'BCM2835_PWM_PASSWRD', 'bcm2835_gpio_afen',
           'BCM2835_GPREN0', 'BCM2835_SPI0_CS_DMA_LEN',
           'BCM2835_PAGE_SIZE', 'bcm2835_set_debug', 'uintptr_t',
           'bcm2835PadGroup', 'BCM2835_PAD_DRIVE_14mA', 'int8_t',
           'BCM2835_CLOCK_BASE', '__STDC_IEC_559_COMPLEX__',
           'BCM2835_SPI_CLOCK_DIVIDER_16', 'bcm2835SPIChipSelect',
           'BCM2835_SPI_CLOCK_DIVIDER_1024', 'bcm2835I2CReasonCodes',
           'bcm2835_gpio_clr_multi', 'BCM2835_PWM_CLEAR_FIFO',
           'int64_t', '__WCHAR_MIN', 'BCM2835_SPI0_CS_INTD',
           'int_fast64_t', 'BCM2835_BSC_DEL', '_LARGEFILE64_SOURCE',
           'BCM2835_SPI0_CS_LEN', 'bcm2835_peri_read_nb',
           'BCM2835_SPI0_DLEN', 'bcm2835_i2c_set_baudrate',
           'bcm2835_close', 'uint_fast32_t', 'BCM2835_SPI0_CS',
           'BCM2835_SPI0_CS_TA', 'BCM2835_PAD_DRIVE_2mA']
