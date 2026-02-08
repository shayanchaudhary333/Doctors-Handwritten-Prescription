# CHITS Game

import random
#create 16 chits
chits = list(range(1,17))
random.shuffle(chits)

while True:
    drawn_chit = int(input("\n Press Enter to draw a chit!"))
    drawn_chit = chits.pop()                                   
    print(f"You drew chit number:,{drawn_chit}")
    print(f"Chits remaining:len{chits}")
    print("\nAll chits haver been drawn!")
    print("Game Over!!!")