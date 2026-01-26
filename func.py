def greet(name="guest"): #default arg
    print(f"hello {name} welcome")


greet("divi")

def iterate(*args): #positional argument
    for i in args:
        print(i)


iterate(1,2,3,4,5,"divsiaaaa")

def detail(**kwargs): #keyword argument
    for k,v in kwargs.items():
        print(k,v)



detail(name="divisha",age=9,para = 9)

def strong(password):
    if len(password)<8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return false;

    return True

s = "madadem"
i = 0
j = len(s)-1
while i<j:
    if s[i]!=s[j]:
        print("no")
        break;
    
    i = i+1
    j = j-1




    