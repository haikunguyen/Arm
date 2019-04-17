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
	killpin = digitalio.DigitalInOut(board.D17)
	killpin.direction = digitalio.Direction.OUTPUT
	killpin.value = False

	print("k = kill\nr = reboot")

	while True:
		switch = kill_reboot()
		killpin.value = switch

main()
