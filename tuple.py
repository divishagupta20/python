arr = (1,2,3,"harry",False)
tpl = tuple()
t = tuple([1,2,3,4])
l = list((3,4,5,6))

print(t+arr)

unpacked_tuple = 1,"hello",9.8;
print(unpacked_tuple)
a,b,c = unpacked_tuple;
print(a,b,c)

v = ((1,2,3),(4,5,6),(7,8,9))

for i in v:
    for j in i:
        print(j,end=" ")
    print()

    