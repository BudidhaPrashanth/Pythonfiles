set_1 = {2,4,5,6,"bablu","vnr",2,6,10}
set_2 = {1,3,5,"prashanth","vnr",12,14,10}

print(set_1| set_2)
print(set_1 & set_2)
print(set_1 - set_2)
print(set_1 ^ set_2)
print(set_1.isdisjoint(set_2))
print(set_1.add("injus"))
print(set_1)


print(set_2.update({"ravi","prem"}))
print(set_2)

set_2.remove("prem")
set_1.remove(10)

print(set_2)
print(set_1)


set_2.discard("ravi")
set_1.discard("vnr")


print(set_2)
print(set_1)

set_3 = set_2.copy()
print(set_3)


print(set_3.pop())
print(set_3)


set_3.pop()
print(set_3)
