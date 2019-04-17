import serial
import sys
import time


#define serial communication
ssc32 = serial.Serial('COM3', 115200)

#center servo
ssc32.write("#0P1500\r".encode())

#infinite loop
start= 1600
while 1:
    x=input()
    if x == 'a':
        start = 300 + start
        command = "#0P" + str(start)+ "\r"
        ssc32.write(command.encode())
        print(command)
    if x == 'd':
        start = start- 300
        command = "#0P" + str(start)+ "\r"
        ssc32.write(command.encode())
        print(command)

