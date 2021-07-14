email = input("Enter Your email: ").strip()
username = email[:email.index("@")]
domain = email[email.index("@")+1:]
print("Your email is {} and domain is {}".format(username, domain))
