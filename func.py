#def greet(name,msg="Hey"):
 #  print(f"{msg},{name}")
#greet("Shayan")    

#CALCULATOR
def add(n1,n2):
   return n1 + n2

def sub(n1, n2):
   return n1 - n2

def mul(n1,n2):
   return n1 * n2

def div(n1,n2):
   return n1 == n2
   if n2 == 0:
     return "Cannot divide by zero"
   else:
     return n1 / n2

def calculator():
    while True:
       print("CALCULATOR")
       ch = int(input("Please enter your choice for operation (1 to 5):"))
       if ch in range(1,5):
         a =  int (input("Enter the first number:"))
         b =  int (input("Enter the second number:"))
       if(ch==1):
         print(add(a,b))
       elif (ch == 2):
        print(sub(a,b))   
       elif (ch == 3):
        print(mul(a,b))   
       elif (ch == 4):
        print(div(a,b))   
       elif (ch == 5):
         print("Thanks for using Calculator!!")   
           #break
       else:
         print("Please enter a valid choice")
calculator()