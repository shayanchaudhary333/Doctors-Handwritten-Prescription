yr = int(input("Enter leap year:"))
if yr%4==0;
    if yr%100==0:
        if yr%400==0:
            print("Leap yr")
        else:
            print("not a leap year")
    else:
        print ("Leap year")
else:
    print("not a leap year")     

if yr%4 ==0 and (yr%100!=0 or yr%400==0):
    print("Leap yr")
else:
    print("Not a leap yr")        