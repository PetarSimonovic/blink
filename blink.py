import smtplib
import imghdr
import ssl
from email.message import EmailMessage
from blinkcamera import BlinkCamera

# create an environment file called email_env - password, sender and recipient are all string variables
# password and sender are the gmail account from which the image will be sent
# recipient is the email account that will receive the image

from email_env import password
from email_env import sender
from email_env import recipient

class Blink:

	def __init__(self):
		self.password = password
		self.sender = sender
		self.recipient = recipient
		self.camera = BlinkCamera()


	def take_photo(self):
		self.camera.take_photo()
		print("photo taken")

	def send_frame(self):
		file = "claude.jpg"
		msg = EmailMessage()
		msg['Subject'] = "Today's frame"
		msg['From'] = self.sender
		msg['To'] = self.recipient

		with open(file, 'rb') as fp:
			print("generating img_data")
			img_data = fp.read()
			msg.add_attachment(img_data, maintype='image', subtype=imghdr.what(None, img_data))
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
			print("Trying to send")
			server.login(self.sender, self.password)
			print("logged in")
			server.sendmail(self.sender, self.recipient, msg.as_string())
			print("Sent")



def start_blink():
	blink = Blink()
	blink.take_photo()
	blink.send_frame()

start_blink()

