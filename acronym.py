words = str(input("Enter the Acronym words: \n"))
text = words.split()
#print(text)
a = ""
#print(type(a))

for i in text:
    a = a+str(i[0]).upper()
    #print(i)

print(a)
