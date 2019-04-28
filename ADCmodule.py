import time
import board
import busio
import digitalio
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# Create SPI bus
ADC1spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
ADC1cs = digitalio.DigitalInOut(board.D5)
ADC1mcp = MCP.MCP3008(ADC1spi, ADC1cs)
ADC1channel = AnalogIn(ADC1mcp, MCP.P0)

ADC2spi = busio.SPI(clock=board.SCK_1, MISO=board.MISO_1, MOSI=board.MOSI_1)
ADC2cs = digitalio.DigitalInOut(board.D5)
ADC2mcp = MCP.MCP3008(ADC2spi, ADC2cs)
ADC2channel = AnalogIn(ADC2mcp, MCP.P0)

def main():
	BatteryLevel = 2*ADC1channel.voltage
	BatteryLife = round(100*(BatteryLevel/6))
	power = ((ADC2channel.voltage)*(BatteryLevel))/(10*1000)

	print("Battery (%):  {}".format(BatteryLife).ljust(30) + "|" + " Power Consumption (mW):   {}".format(round(power, 2)).ljust(36) + "|")

main()
