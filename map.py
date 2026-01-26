def square(x):
    return x**2


numbers = [1,2,3,4,5]
s = list(map(square,numbers))
print(s)

print(list(map(lambda x:x**2,numbers)))

num1 = [1,2,3]
num2 = [4,5,6]

added = list(map(lambda x,y:x+y,num1,num2))

print(added)

str = ['1','2','3','4']

int_num = list((map(int,str)))
print(int_num)

def func(people):
    return people["name"]


d = [
    {"name":"divisha","age": 40},
    {"name":"diva","age":40},
    {"name":"disha","age" :40}
]

print(list(map(func,d)))