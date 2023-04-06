import string
import random

ALL_CHARACTERS = list(string.printable)

PASSWORD_LENGTH = random.randint(10,50)

password = []

for i in range (PASSWORD_LENGTH):
    password.append(random.choice(ALL_CHARACTERS))

print("".join(password))


