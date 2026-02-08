#reollin DICE

import random
total1 = 0
# Dice1 & dice 2 initialization
Dice1 = [1,2,3,4,5,6]
Dice2 = [1,2,3,4,5,6]

while True:
      total = random.choice(Dice1) +random.choice(Dice2)
      print(total)
    #store total of dice after each loop executuion
      total1=total
      #roll_again = input("Do you want to roll again?(yes/no):")
    #prints the result 
      if total1>=100:
        print(f"TOTAL AFTER EACH LOOP , GREATER THAN 100 :{result1}")    
    
     
     
     
     # if (roll_again != "yes"):
      # print(f" Thanks for playing!")    
       #break
    

