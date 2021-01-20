set_1 = {1,2,3,4,5,6,6,7,9}
set_2 = {4,5,9,20,21,22,21,1}
set_1.add(10)
set_1.remove(5)
set_1.update({11,12,13})
set_1.discard(11)
print(set_1.isdisjoint(set_2)) # gives flase
print(set_1&set_2) # intersection
print(set_1^set_2)# symmetric
print(set_1-set_2)#diffrence
print(set_1|set_2) #union
print(len(set_2))
set_3 = set_1.copy()
print(set_3)
a = frozenset(set_1)
#print(a.add(199)) gives error bcz frozenset
set_1.pop() #removes lower element
#print(set_1)
a = {1,2,3,4,4,5,6,7,8,}
b ={7,1,2,3,4}
print(b.issubset(a))
print(a.issuperset(b))
print(a.isdisjoint(b))

a ={1,2,3,4,5}
b ={6,7,8,9}
print(a.isdisjoint(b))#gives true bcz no  coonection
a ={1,2,3,4,5}
b ={5,6,7,9}
print(a.isdisjoint(b))#gives false bcz is thre connection
