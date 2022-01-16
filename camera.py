from time import sleep
from picamera import PiCamera

class Camera:
	
	def __init__(self):
		camera = PiCamera()

	def take_photo(self):
		camera = PiCamera()
		camera.start_preview()
		# Camera warm-up time
		sleep(2)
		camera.capture('claude.jpg')


camera = Camera()
camera.take_photo()

