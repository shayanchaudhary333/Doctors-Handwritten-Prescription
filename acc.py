#Data structures are “containers” that organize and group data according to type. The data structures differ based on mutability and order.
a=[]
a=[1,2,3] #integer 
a=[12,23.3,"a"] #list with having mixed data type
a=[1,2,3,["a","b"],"apple"] #nested list

#to access element from list
print(a[0])
print(a[3][0])
print(a[4][2])

#negative indexing
a=["apple","a",1,2,3,12.52]
print(a[-1])
print(a[-6][-2])
print(len(a))

#list slicing

a=[1,2,3,4,5,6,7,8,9,10]
print(a[:])
print(a[:5])
print(a[5:])
print(a[2:6])
print(a[::2])
print(a[::-1])


#list methods
# a=[1,2,3,4,5,6,7,8,9,10]
# a[0]=-1
# print(a)
# a.append(12)
# print(a)

# a.insert(2,12)
# print(a)

# #add multiple element
# a.extend([11,12,13])
# print(a)

# #add multiple element using slicing


# a[2:2]=['x','y','z']
# print(a)


# #concate list
# b=['a','b','c']
# c=a+b
# print(c)

#repeate list
# a=[1,2,3]
# print(a*5)

#remove element
a=[1,2,'a',3,4,5,6,7,8,9,10]
a.remove('a') #specify element inside method
print(a)
del a[2:5]
print(a)

# a=[1,2,3,4,5,6,7,8,9,10]
# for i in a:
#     if i%2!=0:
#         del i
#     else:
#         a.append(i)
# print(a)


#pop
# a=[1,2,3,4,5]
# print(a.pop())
# print(a)
# print(a.pop(0))

# clear
# a=[1,2,3,4,5]
# a.clear()
# print(a)

# del a[3]
# print(a)
# del a
# print(a)

#index
# a=[1,2,3,4,5,2,3]
# print(a.index(3))

#sort
# a=[3,2,1,5,4]
# a.sort()
# print(a)

#reverse
# a=[3,2,1,5,4]
# # a.reverse()
# # print(a)
# a.sort(reverse=True)
# print(a)


#using slicing reversing list
'''a=[3,2,1,5,4]
print(a[::-1])
'''
#decending order sorting
# a = [3, 2, 1, 5, 4]
# print(sorted(a, reverse=True)) 

#count
# a=[1,2,3,4,5,1,2,3]
#( print(a.count(2))