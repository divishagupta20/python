l = ["hello",1,1,8.9,True]
print(l)
print(l[-1])
print(l[1:3])
print(l[2:])
l[1:] = "watermelon"
print(l)
l.append(98)
l.insert(3,88)


l.append(1)
l.append(77)
l.append(1)
l.remove(1)
last = l.pop()
print(last)
print(l)
print(l.index(77))
l.count("hello")
l.reverse()
l.clear()
arr = [1,2,3,4,5,6,7,8,9]
print(arr[2:5])
print(arr[:5])
print(arr[1:])
print(arr[::])

print(arr[::-1])
'''for i in arr:
    print(i)'''

for index,num in enumerate(arr):
    print(index,num)

print([x**2 for x in range(10)])
even = [n//2 for n in range(10) if n%2==0]
print(even)
print([(i,j) for i in arr for j in even])
print(l+arr)