#Import Phase

#Import scripts
import sensorsmodule
import ADCmodule
#import killswitchmodule
#import cameramodule

#ADC imports
import time
import board
import busio
import digitalio
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

#Magnetometer imports
import smbus

#BME imports
import adafruit_bme280

#Camera imports
#from picamera import PiCamera
#from time import sleep


#Setup Phase

# Create ADC SPI buses
ADC1spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
ADC1cs = digitalio.DigitalInOut(board.D5)
ADC1mcp = MCP.MCP3008(ADC1spi, ADC1cs)
ADC1channel = AnalogIn(ADC1mcp, MCP.P0)

ADC2spi = busio.SPI(clock=board.SCK_1, MISO=board.MISO_1, MOSI=board.MOSI_1)
ADC2cs = digitalio.DigitalInOut(board.D5)
ADC2mcp = MCP.MCP3008(ADC2spi, ADC2cs)
ADC2channel = AnalogIn(ADC2mcp, MCP.P0)

#Create Magnetometer I2C bus
bus = smbus.SMBus(1)
config = [0x00, 0x5C, 0x00]
bus.write_i2c_block_data(0x0C, 0x60, config)
data = bus.read_byte(0x0C)
config = [0x02, 0xB4, 0x08]
bus.write_i2c_block_data(0x0C, 0x60, config)
data = bus.read_byte(0x0C)

#Create BME I2C bus
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
bme280.sea_level_pressure = 1013.25

#Create camera
#camera = PiCamera()

#Create killswitch
killpin = digitalio.DigitalInOut(board.D17)
killpin.direction = digitalio.Direction.OUTPUT
killpin.value = False



#Main Phase: Call modules
while True:
	sensorsmodule.main()
	ADCmodule.main()
	#killswitchmodule.main()
	#cameramodule.main()
	print('\n')
	time.sleep(5)
