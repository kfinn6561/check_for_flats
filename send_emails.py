import smtplib
from threading import Thread
from config import *
import os


def send_async_email(message):
        # Replace the number with your own, or consider using an argument\dict for multiple people.
	#to_email='kieran.finn@hotmail.com'
	auth = ('kieran.errors@gmail.com', os.environ['GMAIL_PASSWORD'])

	# Establish a secure session with gmail's outgoing SMTP server using your gmail account
	try:
		server = smtplib.SMTP( "smtp.gmail.com", 587 )
		server.starttls()
		server.login(auth[0], auth[1])

		# Send text message through SMS gateway of destination number
		for to_email in EMAIL_ADDRESSES:
			server.sendmail( auth[0], to_email, message)
	except:
		print('Error sending email')

	return 0

def send_email(message):
	Thread(target=send_async_email(message)).start()


# def send_email(message):
#         # Replace the number with your own, or consider using an argument\dict for multiple people.
# 	to_email='kieran.finn@hotmail.com'
# 	auth = ('kieran.errors@gmail.com', os.environ['GMAIL_PASSWORD'])
# 	server = smtplib.SMTP( "smtp.gmail.com", 587 )
# 	server.starttls()
# 	server.login(auth[0], auth[1])

# 	# Send text message through SMS gateway of destination number
# 	server.sendmail( auth[0], to_email, message)

# 	return 0