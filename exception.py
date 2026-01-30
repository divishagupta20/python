try:
    a=b

except NameError as e:
    print(e)


try:
    1/0
except ZeroDivisionError as ex:
    print(ex)
    print("enter other denominator ")

try:
    1/2
    a=b
except ZeroDivisionError as ex:
    print("will not be called for a=b")
except Exception as ex:
    print("this is the parent class of exception")

try:
    num = "he;;po"
    result = 10/num
except ValueError as ex:
    print("imvalid")
except ZeroDivisionError as ex:
    print("will not be called for a=b")
except Exception as ex:
    print("this is the parent class of exception")
else:
    print(f"the result is {result}")
finally:
    print("execution done")

try:
  with open('f.txt','r') as file:
    cont = file.read()
except FileNotFoundError:
     print("not found")

else:
    print(cont)
    file.close()

    
