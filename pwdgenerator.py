# password generator in .py 
# we wuz generating random pwd n shieeeet

import random
import string

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    password = ''.join(random.choice(characters) for i in range(10))
    return password

print(generate_password())
