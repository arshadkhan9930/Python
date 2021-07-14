import random
import math
import smtplib

digits = "0123456789"
OTP = ""

for i in range(6):
    OTP += digits[math.floor(random.random()*10)]

msg = OTP
s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
receiver = "khanarshad811@yahoo.com"
s.login("khanarshad9930@gmail.com", 'svxuzzfqqlflxipl')
email_id = input("Enter your email ID\n")
s.sendmail(email_id, email_id, msg)
a = input("Enter your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")

