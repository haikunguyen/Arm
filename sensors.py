# This python script combines the functionality of the magnetometer and the temperature, air pressure, humidity sensor

import time

import board
import busio
import digitalio
import adafruit_bme280

import smbus

#********************Magnetometer (MLX90393) Code**********************
# Get I2C bus
bus = smbus.SMBus(1)

# MLX90393 address, 0x0C(12)
# Select write register command, 0x60(96)
# AH = 0x00, AL = 0x5C, GAIN_SEL = 5, Address register (0x00 << 2)
config = [0x00, 0x5C, 0x00]
bus.write_i2c_block_data(0x0C, 0x60, config)

# Read data back, 1 byte
# Status byte
data = bus.read_byte(0x0C)
# MLX90393 address, 0x0C(12)

# Select write register command, 0x60(96)
# AH = 0x02, AL = 0xB4, RES for magnetic measurement = 0, Address register (0x02 << 2)
config = [0x02, 0xB4, 0x08]
bus.write_i2c_block_data(0x0C, 0x60, config)

# Read data back, 1 byte
# Status byte
data = bus.read_byte(0x0C)
# MLX90393 address, 0x0C(12)

#*****************Environmental Sensor (BME280) Code**************************
#Temperature, Air pressure, humidity sensor code
spi = busio.SPI(board.SCK, board.MOSI, board.MISO) #create spi object
bme_cs = digitalio.DigitalInOut(board.D5)
bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)

#change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25

#Loop to continuously read and output data from both sensors
while True:
	# Start single meaurement mode, X, Y, Z-Axis enabled
	bus.write_byte(0x0C, 0x3E)
	# Read data back, 1 byte
	# Status byte
	data = bus.read_byte(0x0C)
	# MLX90393 address, 0x0C(12)

	# Read data back from 0x4E(78), 7 bytes
	# Status, xMag msb, xMag lsb, yMag msb, yMag lsb, zMag msb, zMag lsb
	data = bus.read_i2c_block_data(0x0C, 0x4E, 7)

	# Convert the data
	xMag = data[1] * 256 + data[2]
	if xMag > 32767 :
  		xMag -= 65536
	yMag = data[3] * 256 + data[4]
	if yMag > 32767 :
		yMag -= 65536
	zMag = data[5] * 256 + data[6]
	if zMag > 32767 :
		zMag -= 65536

	#Condition to threshold whether something is magnetic
	threshold = 1000
	if abs(zMag) > threshold or abs(yMag) > threshold or abs(xMag) > threshold:
		Mag = "YES"
	else:
		Mag = "NO"

	#Print values
	print("{: <30}".format("MAGNETIC FIELD") + "| " + "{: <30}".format("ENVIRONMENTAL CONDITIONS") + "|")
	print("X-Axis: {}".format(xMag).ljust(30) + "| " + "Temperature (C): {}".format(round(bme280.temperature, 2)).ljust(30) + "|")
	print("Y-axis: {}".format(yMag).ljust(30) + "| " + "Humidity (%): {}".format(round(bme280.humidity, 2)).ljust(30) + "|")
	print("Z-axis: {}".format(zMag).ljust(30) + "| " + "Pressure (kPa): {}".format(round((bme280.pressure*0.1), 2)).ljust(30) + "|")
	print("Magnetic?: {}".format(Mag).ljust(30) + "| " + "Altitude (m): {}".format(round(bme280.altitude, 2)).ljust(30) + "|")
	print("\n")

	time.sleep(1)
