import random

NAMES = ["Stephen", "Daan", "Kees", "Kiki", "Lisa"]

def get_name():
    return random.choice(NAMES)

print("Hallo, ik ben {}".format(get_name))
