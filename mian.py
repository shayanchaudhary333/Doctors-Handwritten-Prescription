total=0
while True:
     num=int(input("Enter a number (0 to exit): "))
     if num<0 :
         continue
     elif num==0:
         break
     total+=num
 print("Total:",total)

a=123456789
count_digit=0
while a!=0:
    a//=10
    count_digit+=1
print("Number of digits:",count_)