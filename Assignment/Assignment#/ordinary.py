def make_pretty(func):
    def inner():
        print("I got Decorated")
        func()
    return inner
@make_pretty
def ordinary():
     print("I am ordinary")
decorated_func =make_pretty(ordinary)
decorated_func()
# decorators modifies a function
 
def greet(fx):
    def mfx(*args,**kwargs):
       print("Good Morning")
       fx(*args,**kwargs)
       print("Thanks for using this function")
    return  mfx()
@greet
def hello():
    print("Hello Sir")
@greet
def add(a=4,b= 5):
    print(a+b)

decorated_func ()   
#greet (add)