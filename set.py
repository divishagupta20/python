s = set()
m = {1,2,3,4,5,5,6,7}
print(m)
m.add(8)
m.remove(3)
m.discard(11)
print(m.pop())
print(5 in m)

a = {1,2,3,4,5,6,7}
b = {6,7,8,9,10}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.intersection_update(b))
print(a.symmetric_difference(b))
print(a.issubset(b))

text = "this tutorial is about set and is about splliting"
words = text.split()
print(type(words))
ans = set(words)
print(ans)
print(len(a))

for i in m:
    print(i)