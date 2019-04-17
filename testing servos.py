import serial
import sys
import time


#define serial communication
ssc32 = serial.Serial('COM3', 115200)

#center servo
ssc32.write("#0P1500\r".encode())

#infinite loop
var = 1
while var ==1:
    x=input()
    if x == 'a':

        ssc32.write("#0P2000\r".encode())
    if x == 'd':
        ssc32.write("#0P1000\r".encode())
    

