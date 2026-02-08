a="python is easy to learn "
c=0
v=0
for i in a:
    if i in "AEIOUaeiou":
        v+=1
    else:
        c+=1

print(v)
print(c)        

total=0
for i in range(21,2,2):
    print(i)
    total+=i
    print ("total:",total)