#         #Hybrid Inheritence...
# class A():
#     def add(self):
#         self.a = 30
#         self.b = 20
#         self.c = self.a + self.b
#         print(self.c)
# class B(A):
#     def sub(self):
#         self.d = 30
#         self.e = 10
#         self.f = self.d - self.e
#         print(self.f)
# class C(A):
#     def mul(self):
#         self.g = 5 
#         self.h = 10
#         self.i = self.g * self.h
# class D(A):
#     def div(self):
#         self.j = 10
#         self.k = 2
#         self.l = self.j / self.k
#         print(self.l)
# class E(B,C,D):
#     def avg(self):
#         self.n = 20
#         self.o = (self.m + self.n) / 2
#         print(self.o)
# obj = E()
# obj.add()
# obj.sub()
# obj.mul()
# obj.div()

# class A():
#    def __init__(self):
#       print("Welcome")
# object = A()   

# class A():
#       def __init__ (self):
#          self.earning = 50000#
#          self.profit =  60000
# class B(A):
#       def total(self):
#          self.c = self.earning + self.profit
#          print(self.c)

# object=B()
# object.total()
#METHOD OVERRIDING
# class dog():
#     def sound(self):
#         print("bhoo bhoo")
# class monkey(dog):
#     def sound(self):
#         super().sound()
#         print("ghu ghu")
# class donkey(monkey):
#     def sound(self):
#         super().sound()
#         print("bha bha")               
 
# abc = donkey()
# abc.sound()       

#METHOD OVERLOADING
# class board():
#     def data(self,name,address = ""):
#          print("Welcome")
#          print("Welcome to"+name,address)
        

# aa = board()
# aa.data("Livetech","Thane")

#DATA ABSTRACTION
from abc import ABC
class vehicle (ABC):
    def speed (self):
        pass
class maruti_car(vehicle):
    def speed(self):
        print("Marutical speed 900/km")
class swift_car(vehicle):
    def speed(self):
        print("swift car speed 1000/km")
aa = swift_car()
aa.speed()        
    
    #ENCAPSULATION




























































          
 