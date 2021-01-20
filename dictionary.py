d = dict()
print(d)
d["a"] = 1
d["b"] = 2
d["c"] = 3
print(d)
print(d.keys())
print(d.values())
print(d.items())

del d["c"]
print(d)
d2 = {"d": 4}
d.update(d2)
print(d)

print(d.get("b"))
print(d.pop("a"))
print(d)

print(d.popitem())
print(d)

print(d.clear())
print(d)