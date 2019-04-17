import serial
import sys
import time


#define serial communication
ssc32 = serial.Serial('COM3', 115200)

#center servo
ssc32.write("#0P1500\r".encode())

#infinite loop
var = 1
pos1=1600
while var ==1:
    x=input()
    
    if x == 'a':
        ssc32.write("#0" "P" "1500" "\r".encode())
    if x == 'd':
        ssc32.write("#0P1000\r".encode())

    if x == '8':
        ssc32.write("#1P1400\r".encode())
    if x == '9':
        ssc32.write("#1P1500\r".encode())
    if x == '0':
        ssc32.write("#1P1600\r".encode())
        
    

