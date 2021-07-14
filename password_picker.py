import string
import random
print("Welcome to Password Picker")

adjectives = ['sleepy', 'slow', 'smelly', 'wet', 
              'fat', 'red', 'orange', 'yellow', 'green', 
              'blue', 'purple', 'fluffy', 'white', 'proud', 'brave']

nouns = ['apple', 'dinosaur', 'ball', 'toaster', 
         'goat', 'dragon', 'hammer', 'duck', 'panda']

adjective = random.choice(adjectives)
#print(adjective)
noun = random.choice(nouns)
#print(noun)

number = random.randrange(0, 100)
#print(number)
special_char = random.choice(string.punctuation)
#print(special_char)
print("Your password is :", adjective + noun + str(number) + special_char)
#print(f"Your password is : {adjective}{noun}str{number}{special_char} ")
#print("your password is : {}{}{}{}".format(adjective,noun,str(number),special_char))
