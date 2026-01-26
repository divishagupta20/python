def even(num):
    return num%2==0


l = [1,2,3,4,5,6]
print(list(filter(even,l)))

print(list(filter(lambda x:x>5 and even,l)))

