names = []
phone_numbers = []
num = 3

for i in range(num):
    name = input("Name: \n")
    phone_number = input("Phone Number: \n")
    
    names.append(name)
    phone_numbers.append(phone_number)

print("\nName\t\t\tPhone Number\n")

for i in range(num):
    print("{}\t\t\t{}".format(names[i], phone_numbers[i]))

search_item = input("\nEnter search item\n")

if search_item in names:
    index = names.index(search_item)
    phone_number = phone_numbers[index]
    print("Name: {}, Phone Number: {}".format(search_item, phone_number))
else:
    print("Name not found: ")
