import serial
import sys
import time
from pynput.keyboard import Key, Controller
from pynput.keyboard import Key, Listener
from pynput.keyboard import KeyCode



#define serial communication, COM4 Baud Rate 9600
ssc32 = serial.Serial('COM4', 9600)





keyboard = Controller()
#Global start variables
#Note if these change, change the center servo positions
start1=1900
start2=2000
start3=1100
start4=1500
start5=2500

#center servo
ssc32.write("#1P1900\r".encode())
ssc32.write("#2P2000\r".encode())
ssc32.write("#3P1100\r".encode())
ssc32.write("#4P1500\r".encode())
ssc32.write("#5P2500\r".encode())
######################################
#Wiring info:
#Continuous Servo (Base) = 0
#Shoulder = 1
#Elbow = 2
#Wrist up down = 3
#Wrist rotate = 4
#Gripper = 5
#######################################




def on_press(key):
    global start1
    global start2
    global start3
    global start4
    global start5
    
    #print('{0} pressed'.format(
        #key))
    #Baud rate test
    if key == Key.up:
        print("Baud Rate * 10 ")
        command = "R4\r"
        ssc32.write(command.encode())
        ssc32.read(command.encode())
    #reset
    if key == Key.down:
        print("Master Reset")
        ssc32.write("#1P1900\r".encode())
        ssc32.write("#2P2000\r".encode())
        ssc32.write("#3P1100\r".encode())
        ssc32.write("#4P1500\r".encode())
        ssc32.write("#5P2500\r".encode())
    ############################SERVO CONTROL###############################

    #servo 0 continuous
    if key == Key.left:
        print("left")
        command = "#0P1000\r"
        ssc32.write(command.encode())
    if key == Key.right:
        print("right")
        command = "#0P2000\r"
        ssc32.write(command.encode())
    if key == Key.space:
        print("stop")
       # ssc32.write("1P100\r".encode())

    #shoulder pin 1
    if key == KeyCode.from_char('s'):
        start1 += 50
        if start1 == 2450:
            start1 -= 50
        print(start1)
        command = "#1P" + str(start1)+ "\r"
        ssc32.write(command.encode())
    if key == KeyCode.from_char('w'):
        start1 -= 50
        if start1 == 500:
            start1 += 50
        print(start1)
        command = "#1P" + str(start1)+ "\r"
        ssc32.write(command.encode())

    #elbow
    if key == KeyCode.from_char('d'):
        start2 += 50
        if start2 == 2450:
            start2 -= 50
        print(start2)
        command = "#2P" + str(start2)+ "\r"
        ssc32.write(command.encode())
    if key == KeyCode.from_char('e'):
        start2 -= 50
        if start2 == 500:
            start2 += 50
        print(start2)
        command = "#2P" + str(start2)+ "\r"
        ssc32.write(command.encode())
    #wrist up down
    if key == KeyCode.from_char('q'):
        start3 += 50
        if start3 == 2450:
            start3 -= 50
        print(start3)
        command = "#3P" + str(start3)+ "\r"
        ssc32.write(command.encode())
    if key == KeyCode.from_char('a'):
        start3 -= 50
        if start3 == 500:
            start3 += 50
        print(start3)
        command = "#3P" + str(start3)+ "\r"
        ssc32.write(command.encode())
        
    #wrist rotate
    if key == KeyCode.from_char(','):
        start4 += 50
        if start4 == 2450:
            start4 -= 50
        print(start4)
        command = "#4P" + str(start4)+ "\r"
        ssc32.write(command.encode())
    if key == KeyCode.from_char('.'):
        start4 -= 50
        if start4 == 500:
            start4 += 50
        print(start4)
        command = "#4P" + str(start4)+ "\r"
        ssc32.write(command.encode())
        
    #gripper
    if key == KeyCode.from_char('='):
        start5 += 50
        if start5 == 2450:
            start5 -= 50
        print(start5)
        command = "#5P" + str(start5)+ "\r"
        ssc32.write(command.encode())
    if key == KeyCode.from_char('-'):
        start5 -= 50
        if start5 == 500:
            start5 += 50
        print(start5)
        command = "#5P" + str(start5)+ "\r"
        ssc32.write(command.encode())

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.left:
        ssc32.write("#0P1500\r".encode())
    if key == Key.right:
        ssc32.write("#0P1500\r".encode())
    
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()







    

        

