import smtplib

def automatic_email():
    user = input("Enter your name: \n")
    email = input("Enter your Email ID: \n")
    #print(email)
    message = (f"Dear {user}, Welcome to the Clever Programmer")
    receiver = "khanarshad811@yahoo.com"
    #pwd = "Jhelolr12"
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login('khanarshad9930@gmail.com', 'svxuzzfqqlflxipl')
    s.sendmail(email, receiver, message)
    print("Email sent Successfully")


automatic_email()
