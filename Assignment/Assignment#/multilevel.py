class A():

    def add (self):
         
         self.a = 20
         self.b = 40
         self.c = self.a  + self.b
         print("Addition = ",self.c)
class B(A):
    def sub(self):
       self.c = self.b - self.a
       print("Subtraction:",self.c)
class C(B):
    def mul(self):
        self.c = self.a * self.b
        print("Multiplication:",self.c)
class D(C):
    def div(self):
        self.c = self.a / self.b
        if self .b == 0:
            print("Error")
        else:
         print("Division:",self.c)                          
class E(A,B,C,D):
    a = int(input("Enter A number"))
    b = int(input("Enter B Number"))
obj = E()
obj.add()
obj.sub()
obj.mul()
obj.div()







