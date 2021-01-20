from  array import *
ar1 = array("i",[2,3,-4,5,6,-5,8])
print(ar1)
'''print(ar1.buffer_info())
print(ar1.typecode)
print(ar1.pop(3)) #index
print(ar1.remove(3))
print(ar1)'''

ar2 = array(ar1.typecode,(a for a in ar1))
for i in ar2:
    print(i)