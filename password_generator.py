import sys
import random
import string

from numpy import character

password = []

number_of_characters_left = -1

def update_characters_left (number_of_characters):
    
    global number_of_characters_left
    
    if number_of_characters < 0 or number_of_characters > number_of_characters_left:
        print ("Number of characters from outside rage 0 - ", number_of_characters_left)
        sys.exit(0)
    else:
        number_of_characters_left -= number_of_characters
        print ("Characters left: ", number_of_characters_left)

password_length = int(input ("How long will be the password? "))

if password_length < 8:
    print ("Password is too short. It must have at least 8 characters, try again ")
    sys.exit(0)

else:
    number_of_characters_left = password_length

lowercase_letters = int(input("How many small letters will have password? "))

update_characters_left(lowercase_letters)

uppercase_letters = int(input("How many big letters will have password? "))

update_characters_left(uppercase_letters)

special_characters = int(input("How many special characters will have password? "))

update_characters_left(special_characters)

digits = int(input("How many digits will have password? "))

update_characters_left(digits)

if number_of_characters_left > 0:
    print ("Not all characters are used. Password will be fill in small letters ")
    lowercase_letters += number_of_characters_left

print()
print ("Password length: ", password_length)
print ("Small letters: ", lowercase_letters)
print ("Big letters: ", uppercase_letters)
print ("Special characters: ", special_characters)
print ("Digits: ", digits)

for _ in range (password_length):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(password)
print("Password: ", "".join(password))