from blinkmailer import BlinkMailer
from blinkcamera import BlinkCamera
from daysplicer import DaySplicer


# create an environment file called email_env - password, sender and recipient are all string variables
# password and sender are the gmail account from which the image will be sent
# recipient is the email account that will receive the image

from email_env import password
from email_env import sender
from email_env import recipient

class Blink:

	def __init__(self):
		self.camera = BlinkCamera()
		self.mailer = BlinkMailer()
		self.daysplicer = DaySplicer()

	def create_schedule(self):
		self.daysplicer.set_interval()
		

	def take_photo(self):
		self.camera.take_photo()
		print("photo taken")

	def send_frame(self):
		self.mailer.send_frame()
		

	def start(self):
		self.create_schedule()
		# self.take_photo()
		# self.send_frame()


def start_blink():
	blink = Blink()
	blink.start()

start_blink()

