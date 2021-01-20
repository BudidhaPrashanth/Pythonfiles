import operator

print(operator.sub(5,4))
print(operator.add(5,4))
print(operator.mul(5,4))
print(operator.truediv(5,4))
print(operator.floordiv(5,4))
print(operator.pow(3,2))
print(operator.mod(21,6))#%%%%%%%
print(operator.le(3,2))
print(operator.lt(3,2))
print(operator.eq(3,3))
print(operator.gt(3,2))
print(operator.ge(3,2))
print(operator.ne(2,2))
colours = ['black','white','blue','pink','red']
print(operator.getitem(colours,2))
print(operator.setitem(colours,0,"green"))        #(object,position,value)
print(colours)
print(operator.delitem(colours,4))
print(colours)
codes = "bablu goud"
a = "goud"
#print(operator.concat(colours,codes))
print(operator.contains(codes,a))
print(operator.and_(2,3))
print(operator.or_(34,32))
print(operator.xor(20,12))