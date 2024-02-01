#!/usr/bin/python3

# Task 3:password generator
import string

import random

length = int(input("Enter password length: "))


print('''Choose character set for password from these :

         1. Digits

         2. Letters

         3. Special characters

         4. Exit''')


CharacterList = ""

while(True):

    choice = int(input("Pick a number "))

    if(choice == 1):

        CharacterList += string.ascii_letters

    elif(choice == 2):

        CharacterList += string.digits

    elif(choice == 3):

        CharacterList += string.punctuation

    elif(choice == 4):

        break

    else:

        print("Please pick a valid option!")

password = []

for i in range(length):

    randomchar = random.choice(CharacterList)

    password.append(randomchar)

print("The random password is " + "".join(password))