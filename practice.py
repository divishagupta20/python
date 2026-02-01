import numpy as np
import random

arr = np.arange(1,26).reshape(5,5)

for i in range(5):
    for j in range(5):
        arr[i][j] = random.randint(1,25)

print(arr)
a = np.arange(1,10).reshape(3,3);

print(a)

for i in range(0,3):
    for j in range(0,3):
        a[i][j] = arr[i+1][j+1]

print(arr)
print(a)

m = int(np.mean(a))
print(m)
arr[2][2] = m
print(arr)