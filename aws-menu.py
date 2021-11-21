import pyttsx3
import os
import speech_recognition as sr

print("\n")
print("\t\t\t\t-------------------------------------------------------------------------")
print("\t\t\t\t\t\t\t Welcome To My Intelligence World")
print("\t\t\t\t-------------------------------------------------------------------------")

pyttsx3.speak(" hello !! Please speak")
while True:
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('start saying...')
		audio = r.listen(source)
		print('stopped\n')
	s = r.recognize_google(audio) 
	

	if("hello" in s) or ("hey" in s) or ("hi" in s):
		pyttsx3.speak("how are you.")
	elif("good" in s) and ("you" in s):
		pyttsx3.speak("I am good too")
	elif("tell" in s) and ("yourself" in s):
		pyttsx3.speak("my name is joe. I am your personal assistant for operating your aws public cloud tell me how can i help you")
	elif("how" in s) and ("help" in s):
		pyttsx3.speak("I can help you in following ways:")
		print("\t\t\t\t\t\t\t***I can help you in following ways***")
		print("\t\t\t\t\t\t---------------------------------------------------")
		print("\n")
		pyttsx3.speak("creating new key pairs")
		print("\t\t\t\t\t\t\t\t*Creating  New  Key  Pairs")
		print("\n")
		pyttsx3.speak("creating new security groups")
		print("\t\t\t\t\t\t*Creating  Security  Groups")	
		print("\n")
		pyttsx3.speak("creating new instances")
		print("\t\t\t\t\t*Creating  New  Instance")
		print("\n")
		pyttsx3.speak("creating ebs volume")
		print("\t\t\t\t\t\t*Creating  Volumes")
		print("\n")
		pyttsx3.speak("attaching volume to the instance")
		print("\t\t\t\t\t\t\t\t*Attaching  Volumes  To  Instance")
		exit()
	elif("show" in s) and ("key" in s):
		pyttsx3.speak("okay I got it. All key pairs are")
		os.system("aws ec2 describe-key-pairs")
		exit()
	elif("create" in s) and ("key" in s):
		pyttsx3.speak("okay I got it, new key pair is created")
		os.system("aws ec2 create-key-pair --key-name aws_key")
		exit()
	elif("show" in s) and ("security" in s):
		pyttsx3.speak("okay I got it. security groups are")
		os.system("aws ec2 describe-security-groups")
		exit()
	elif("create" in s) and ("security" in s):
		pyttsx3.speak("okay I got it, new security group is created")
		os.system('aws ec2 create-security-group --description "my-aws-sg-group" --group-name new-sg ')
		exit()
	elif("show" in s) and ("instance" in s):
		pyttsx3.speak("okay I got it. All instances are")
		os.system("aws ec2 describe-instances")
		exit()
	elif("create" in s) and ("instance" in s):
		pyttsx3.speak("okay I got it, new instance is created")
		os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type t2.micro --count 1 --subnet-id subnet-7198e63d  --key-name aws_key --security-group-ids sg-0509fade21517d6a6")
		exit()
	elif("show" in s) and ("volume" in s):
		pyttsx3.speak("okay I got it. All volumes available are")
		os.system("aws ec2 describe-volumes")
		exit()
	elif("create" in s) and ("volume" in s):
		pyttsx3.speak("okay I got it, new volume is created")
		os.system("aws ec2 create-volume --availability-zone ap-south-1b --size 1 --volume-type gp2")
		exit()
	elif("attach" in s) and ("volume" in s):
		pyttsx3.speak("okay I got it. your volume is attached to your recently created instance")
		os.system("aws ec2 attach-volume  --device /dev/sdh --instance-id i-054153eccb58b48f2 --volume-id vol-0ecd2df436b5cddc1")
	else:
		pyttsx3.speak("thank you for using me !! Have a good day")
		exit()
