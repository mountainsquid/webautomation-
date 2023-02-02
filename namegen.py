# randomly generates first and last name 
# n shieeet. we wuz generating names.

import random

first_names = ['Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia', 'Charlotte', 'Mia', 'Amelia', 'Harper', 'Evelyn']
last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']

def generate_username():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return first_name + ' ' + last_name

print(generate_username())
