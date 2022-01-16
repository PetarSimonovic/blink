# blink

blink is a timelapse photography tool for raspberry pi zero fitted with a camera module.

It will initially take a photo a day over the course of a year. 

Each day it adjusts the time that the photo is taken: it starts just before dawn on day one and ends just after sunset on day 365.

After it takes the photo, blink logs into a user-specified gmail address and sends the image to a user-specified recipient.

The user will need to create a file called email_env.py in which to store three string variables:

password = "the password for the sender's email account"
sender = "the sender's email address"
recipient = "the recipient's email address"
