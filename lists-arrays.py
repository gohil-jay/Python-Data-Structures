a = [1,2,7,34,5,6,7,8,7,9]
b = (1,2,3)
c = {'a':1}

print(type(a)) #returns list (but can be used as array)
print(type(b)) #returns tuple
print(type(c)) #returns dictionary

print("The length of array 'a' is : ", len(a)) #prints length of list or array

print("The fourth element of array 'a' is : ", a[3])

a.append(23)
a.append(39)
print(a) #returns new list

for i in a:  #returns all elements (loop way1)
    print(i)

for i in range(0, len(a)):  #returns all elements (loop way2)
    print(a[i])

a.pop()
print(a) #returns poped (last element deleted) array

a.pop(3)
print(a) #returns array with 4th element deleted

a.remove(8)
print(a) #returns array with '34' deleted

a.insert(1, 'new element')
print(a)

x = a.count(7) #returns the number of times an argument is there in array
print("The number of times '7' occurs is : ", x)

z = a.index(7) #returns the index of the first time the argument element occurs in array
print("The index of first '7' is : ", z)

a.reverse() #reverses an array
print("Reversed array is : ", a)

m = [11, 12, 13]
a.extend(m)
print("See how extend combines 'm' into 'a' : ", a)

a.sort() #sorts the array
print("The sorted array : ", a)

b = a.copy() #a.copy() returns a copy of the list
print(b)

d = a #easy and direct way of copying.
print(d) 

a.clear()
print(a) #returns empty array
