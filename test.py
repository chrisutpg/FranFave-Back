# Testing verison control

import random

def r():
    i = ''
    for x in range(101):
        i = i + str(random.randint(0, 1000000))
    return i

print(r())