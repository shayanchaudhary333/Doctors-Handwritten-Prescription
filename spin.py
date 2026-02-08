import random

#initialization of list
prize =["voucher","Free Ticket","Better Luck next Time","Jackpot!","Bonus spin"]

while True:

    #input from user 
    num = int(input("Enter 1 to  spin the wheel, Enter 2 to exit\n"))

    if(num==1):
       random.shuffle(prize)
       prize2=random.choice(prize)
       print(prize2)

    elif(num==2): 
         print("Exit the wheel")  

  
    else:
          print("Enter a unkown number")     
