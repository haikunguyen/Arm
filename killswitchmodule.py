import board
import digitalio

killpin = digitalio.DigitalInOut(board.D17) #assign killcmd to GPIO pin 18 on Raspberry Pi
killpin.direction = digitalio.Direction.OUTPUT #assign direction of pin to output/write
killpin.value = False #initialize pin value to 0

#wait for user input to either activate/deactivate switch
def kill_reboot():
        cmd = input()
        if cmd == "k":
                return True
        elif cmd == "r":
                return False

def main():
	#print("k = kill\nr = reboot")
	switch = kill_reboot()
	killpin.value = switch

main()
