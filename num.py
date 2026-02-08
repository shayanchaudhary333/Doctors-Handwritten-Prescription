import random

# multiple times inputs
while True:

    a = int(input("Guess a number from 0 to 99 \n"))

    #if - else statement
    if((random.randint(0,99))==a):
        print("Victory!!!")
    else:
        print("Defeat!!!")    

     