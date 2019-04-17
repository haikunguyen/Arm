import serial
import sys
import time

ssc32 = serial.Serial('COM3', 115200)


ssc32.write("#0P1600\r".encode())

