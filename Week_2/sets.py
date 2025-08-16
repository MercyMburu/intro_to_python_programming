numbers=(1,1,2,3,4)
uniques=set(numbers)
print(uniques)

second={1,4}
second.add(5)
print(second)

second={1,2,3,4}
second.remove(2)
print(second)
print(len(second))

second={1,2,3,4,"banana","car",9.20}
print (second)

a1={1,2,3}
a2={2,3,4}
a3={3,4,5}

a4=a1.intersection(a2,a3)
print(a4)

a2={2,3,4}
a3={3,4,5}

a4=a2.symmetric_difference(a3)
print(a4)


numbers=[1,1,2,3,4]
uniques=list(set(numbers))
print(uniques)


Sets
unordered items
no duplicates
{}

numbers=[1,1,2,3,4]
uniques=set(numbers)
print(uniques)

numbers=[1,1,2,3,4]
uniques=list(set(numbers))
print(uniques)

numbers={1,1,2,3,4}
print(numbers)

fruits={"banana","mango","guava","orange"}
print(fruits)

print(fruits[1])

print("mango" in fruits)
first={1,5,7,6}
if 1 in first:
    print("yes")
    
#add
# second={1,4}
# second.add(5)
# print(second)

#update
second={1,4}
second.update([6,7,8])
print(second)

remove
second.remove(5)
print(second)

second.discard(4)
print(second)int(type(fruits))

fruits={"banana","mango","guava","orange"}


len
numbers={1,2,3,4}
print(len(numbers))

intersection method

b1={1,2,3}
b2={2,3,4}
b3={3,4,5}
b4=b1.intersection(b2)
print(b4)

print(b1&b2)
print(b1|b2)

#Difference Method
b1={1,2,3}
b2={2,3,4}
b3={3,4,5}

print(b1.difference(b2))
print(b1-b2)








