import time
import random

def temperature_sensor():

    while True:
        yield round(random.uniform(20.0,30.0),2)
        time.sleep(1)
#sensor = temperature_sensor()
#for i in range (10):
 #   print(f"Temperature: {next(sensor)} °c")

#def fun(max):#func definition
 #   cnt = 1 #Initial counter
  #  while cnt <= max:#While loop > max 
  #      yield cnt # yield statemnet
   #     cnt +=1 #Increment

#ctr = fun(10) # Generato in action
#for n in ctr: # for llopp
   #  print(n) # output

#def temperature_sensor():
    while True():
         yield round(random.uniform(20.0,30.0))   
         time.sleep(5)  
sensor = temperature_sensor()         
for i in range(10):
    print(f"Temperature: {next(sensor)} °c")

def func(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1
temp = func(10)        
for j in temp():
    print(j)