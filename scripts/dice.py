# A simple Dice game

import time
import random

while True:
    guess = input("Please select a number from 1 to 6: ")
    dice = random.randint(1,6)
    time.sleep(1)
    print ("The dice throws........and its a.. ")
    time.sleep(1)
    print (dice, "!!!")
    time.sleep(1)
    if int(guess) == int(dice):
        print ("You lucky bastard, YOU WIN!")
    else:
        print ("I am sorry bro, you lose!")
    time.sleep(1)
