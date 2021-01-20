a= (1,2,3,4,5,6,8)
b =5,
'''print(a+(9,10,11)) #add
print(len(a))
print(a[5])
print(type(a))
print(type(b))
a = tuple((2,4,6,8,10)
print(type(a)))
#a = 3,4,5,6
#print(type(a))#tuple
a=('a','b','c','d','f')
print("".join(a))'''
'''tup = (("A",1),("b",2),('c',3),('d',4))
result = dict((x,y) for x,y in tup)
print(result)
a= [("A", 1), ("b", 2), ('c', 3), ('d', 4)]
print(list(zip(*a)))'''

'''l = [("A", 1), ("b", 2), ('c', 3), ('d', 4)]
d = {}
for k,v in l:
    d.setdefault(k,[]).append(v)
print(d)
import operator
l = [(10,70,30), (4000,80,60), (1000,20.90)]
l =  [i[:-1]+(100,) for i in l]
print(l)'''
l = [("A", 5.53), ("d", 4.5442), ('c', 2.74), ('b', 3.765)]
print(sorted(l,key = lambda x : x[1]))