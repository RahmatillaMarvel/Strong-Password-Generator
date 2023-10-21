import random
import re
from english_words import get_english_words_set

password = input("Write your password: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@?_-."

# Function to generate a random strong password
def generateStrongPassword():
    def main_generator(pwlen, nxlen):
        strong_password = ""

        # Replacing one character from the input password with a symbol
        strong_password += password
        main_char = random.choice(strong_password)
        strong_password = strong_password.replace(main_char, random.choice(symbols))

        # Adding random numbers to the password
        for i in range(random.randint(2, pwlen)):
            random_number = random.choice(numbers)
            strong_password += random_number

        # Adding a random English word from 'web2' dictionary in lowercase
        web2lowerset = list(get_english_words_set(['web2'], lower=True))
        random_extraw = random.choice(web2lowerset)
        while len(random_extraw) >= nxlen:
            random_extraw = random.choice(web2lowerset)

        strong_password += random_extraw
        return strong_password

    if len(password) >= 8:
        return main_generator(4, 5)
    elif 8 > len(password) >= 4:
        return main_generator(8, 6)
    else:
        return main_generator(6, 12)

print(generateStrongPassword())
