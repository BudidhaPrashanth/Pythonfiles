l = [2,3,4,5,6,76,8,99,54]
a = iter(l)

#print(a.__next__())
'''while True:
    try:
        print(next(a))
    except:
        pass'''

l = a.__iter__()
try:
    print(next(l))
    print(next(l))
    print(next(l))
    print(next(l))
    print(next(l))
    print(next(l))
    print(next(l))
    print(next(l))
    print(next(l))
    print(next(l))

except:
    print(" i cant count more ")


