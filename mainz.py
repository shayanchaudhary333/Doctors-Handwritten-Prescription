s=int(input("Enter start range of table:"))
e=int(input("Enter end range of table:"))
for i in range(s,e+1):
    for j in range(1,11):
        print(i,"x",j,"=",i*j)
        