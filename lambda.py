
from functools import  reduce
a = map(lambda  x : x+5,[1,2,3,4,5,6,8])
print(list(a))
b = filter(lambda  x: x>3,[2,3,4,55,6,5,3,1,3,4])
print(list(set(b)))

c = map(lambda x:x+3,filter(lambda x:x>10,[3,5,6,7,34,24,643,23]))
print(list(c))

d = filter(lambda  x:(x>=10),map(lambda x: x+3,[1,2,2,3,4,5,6,7,8,9,10]))
print(list(d))

e = reduce(lambda x,y:x+y,map(lambda x:(x+5),filter(lambda x: x>5,[1,2,3,4,5,6,7])))
print(e)


f = reduce(lambda x,y: x/y,[1,2,3,4,5])
print(f)