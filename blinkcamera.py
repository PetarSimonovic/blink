from time import sleep
from picamera import PiCamera

class BlinkCamera:

	def take_photo(self):
		camera = PiCamera()
		camera.start_preview()
		# Camera warm-up time
		sleep(2)
		camera.capture('blink.jpg')
		camera.close()


