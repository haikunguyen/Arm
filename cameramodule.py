from picamera import PiCamera
from time import sleep

camera = PiCamera()
def main():
	camera.start_preview()
	sleep(1)
	camera.stop_preview()

main()
