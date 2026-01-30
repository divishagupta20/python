import numpy as np;

arr = np.array([1,2,3,4,5])
print(arr)
print(arr.shape)
arr.reshape(1,5)
print(arr)
print(arr.shape)

arr1 = np.array([[1,2,3,4,5],[2,3,4,6,7]])
print(arr1.shape)
arr2 = np.arange(0,10)
print(arr2)
print(np.arange(0,10,2).reshape(5,1))
print(np.ones((3,4)))
print(np.eye(4))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

a = np.array([[1,2,3,4],[4,5,6,5]])
print(a[0:2][0:3])
print(a.size)
print(a.ndim)
print(a.shape)
print(a.dtype)

v = np.array([1,2,3,4,5])
c = np.array([6,7,8,9,0])
print(v+c)
print(np.sqrt(v))
print(np.sin(c))
print(a[0:2,2:])
print(np.mean(c))
print(np.std(c))
print(np.var(c))
normalized_data = (c-np.mean(c))/np.std(c)
print(normalized_data)

x = c-4
print(x)
print(c>5)
