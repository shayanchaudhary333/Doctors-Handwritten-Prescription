a="shayan",
print(type(a))
#tuple with no element
# a=()

#tuple with integer
# b=(1,2,3,4,5)

#tuple with string
# c=('apple','banana','cherry')

#tuple with mixed data type
# d=(1,'apple',2.5,'banana')

#tuple with nested tuple
# e=(1,2,3,(4,5,6))

#tuple with list
# e=(1,2,3,[4,5,6],[1,2,3])
# e[4][1]=-1
# print(e)
# print(e[4][1])




#tuple with one element
# a=("shayan")
# print(type(a))
# g=(1,)
# print(type(g))


#tuple unpacking
# a=("shayan",27,"BE-EXTC")
# name,age,qualification=a
# print(name)
# print(age)
# print(qualification)

#tuple methods
#1.index()
# b=(1,2,3,4,5)
# print(b.index(2))

 #2. count()
# f=(1,2,3,4,5,1,2,2)
# print(f.count(1))

#delete
# a=(1,2,3)
# del a


#3. len()
# b=(1,2,3,4,5)
# print(len(b))

#4. max()
# b=(1,2,3,4,5)
# print(max(b))

#5. min()
# b=(1,2,3,4,5)
# print(min(b))

#6. sum()
# b=(1,2,3,4,5)
# print(sum(b))

#7. tuple()
# a=[1,2,3,4]
# print(tuple(a))

# a={}
# print(type(a))
# a=set()
# print(type(a))
# # # print(len(a))

a={1,2,3,4,5,6,1,2,3,4}
print(a)

#set 
a={1,23.56,"shayan"}#mixed data type set
print(a)
print(set((1,2,3,4,1,2)))

# Adding elements to a set
# a=set()
# a.add(1)
# print(a)
# a.add(2)
# a.add(3)
# print(a)

#update
# a.update([7,8,9])
# print(a)

# # Removing all elements from a set
# a.clear()
# print(a)

# Removing an element from a set using discard method 
#set remains unchanged when element is not present
# a={1,2,3,4,5,6,7,8,9}
# a.discard(10)
# print(a)

#Removing elements from a set
#raise an error when element is not present
# a={1,2,3,4,5,6,7,8,9}
# a.remove(10)
# print(a)

#pop method
a={11,0,1,2,3,4,5,6,7,8,9}
print(a.pop())
print(a)

# b={"shayan",0.11,23,456}
# print(b.pop())
# print(b)

# Union of two sets
a={1,2,3}
b={4,5,6}
print(a | b)
print(a.union(b))

# Intersection of two sets
# a={1,2,3,4,5}
# b={4,5,6}
# print(a & b)
# print(a.intersection(b))

# Difference of two sets
# a={1,2,3,4,5}
# b={4,5,6}
# print(b-a)
# print(a-b)
# print(a.difference(b))

# Difference of two sets with the original set
# a={1,2,3,4,5}
# b={4,5,6}
# print(a^b)
# print(a.symmetric_difference(b))

# Clearing the set
# a={1,2,3,4,5}
# a.clear()                                                         
# print(a)

#isdisjoint
#It returns True if the sets have no common elements and False otherwise. 
# a={1,2,3}
# b={6,7,8}
# print(a.isdisjoint(b))

#differance update

# a={1,2,3}
# b={4,5,6}
# a-=b
# a.difference_update(b)
# print(a)

#intersection update
# a={1,2,3}
# b={4,5,6}
# #a&=b
# a.intersection_update(b)
# print(a)

#issubset
# a<=b
# a={1,2,3}
# b={1,2,3,4,5}
# print(a.issubset(b))

# #issuperset example
# # a>=b

a={1,2,3}
b={1,2,3,4,5}
print(a.issuperset(b))

# #symmetric difference update
# #a^=b
# a={1,2,3,11,4}
# b={4,5,6}
# a.symmetric_difference_update(b)
# print(a)

a={1,23,43,45,67,2}
print(sorted(a))