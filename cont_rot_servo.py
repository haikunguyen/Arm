import serial
import sys
import time

ssc32 = serial.Serial('COM3', 115200, timeout=1.0)

#default positions
s1pos = 1500
s2pos = 1500
s3pos = 1500
s4pos = 1500
s5pos = 1500
s6pos = 1500

while (1)
x = input()
#new positions
if x = 'w'
    s1posnew = s1posnew+100
if x='s'
    s1posnew = s1posnew-100


#s2posnew = s2posnew+100
#s3posnew = s3posnew+100
#s4posnew = s4posnew+100
#s5posnew = s5posnew+100

print("start")

ssc32.write("#0 P1500\r".encode())
ssc32.write("#1 P1500\r".encode())

ssc32.write("#2 P1500\r".encode())
ssc32.write("#3 P1500\r".encode())


