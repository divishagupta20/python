d = dict()
m = {"name":"divisha","age":34,7:8}
print(m['name'])
#print(m["gjh"])
print(m.get("n","not available"))
m[7] = 99
m[56] = "hgjy"
print(m)
del m[7]
print(m)
print(m.keys())
print(m.values())
print(m.items())
#shallow
l = m
m["name"]="molly"
print(l)
print(m)

#deep
s = m.copy()
m["name"] = 22

print(m)
print(s)

for keys in m.keys():
    print(m[keys])

for key,val in m.items():
    print(f"{key}:{val}")

students = {
    "student1":{1:2,3:4},
    "student2":{5:2,6:4}

}

print(students["student1"][1])

for studentid,studentinfo in students.items():
    print(studentid,studentinfo)
    for item in studentinfo.items():
        print(item)



squares = {x:x**2 for x in range(5)}
print(squares)
numbers = (1,2,2,3,3,3,4,4,4,4)
freq = {}

for i in numbers:
    freq[i] = freq.get(i, 0) + 1
    

print(freq)

dict1 = {"a":1,"b":2}
dict2 = {"b":3,"c":4}
merged_dict = {**dict1,**dict2}
print(merged_dict)