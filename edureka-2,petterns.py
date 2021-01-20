
num = int(input("enter a num : "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=' ')
    print()


num = int(input("enter a num : "))
for i in range(num,0,-1):
    for j in range(1,i+1):
        print("*",end=' ')
    print()


num = int(input("enter a num : "))
for i in range(1,num+1):
    for j in range(1,num+1-i):
        print(end=' ')

    for j in range(1,i+1):
        print("*",end= ' ')
    print()

num = int(input("enter a num : "))
for i in range(num,0,-1):
    for j in range(1,num+1-i):
        print(end=' ')
    for j in range(1, i + 1):
        print("*", end=' ')
    print()


num = int(input("enter a num : "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=' ')
    print()
for i in range(num-1,0,-1):
    for j in range(1,i+1):
        print("*",end=' ')
    print()



num = int(input("enter a num : "))

for i in range(num-1,0,-1):
    for j in range(1,num+1-i):
        print(end=' ')
    for j in range(1, i + 1):
        print("*", end=' ')
    print()
for i in range(1,num+1):
    for j in range(1,num+1-i):
        print(end=' ')
    for j in range(1,i+1):
        print("*",end= ' ')
    print()




num = int(input("enter a num : "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end= " ")
    print()




num = int(input("enter a num : "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(i,end= " ")
    print()




n = 65
for i in range(1,27):
    ch = chr(n)
    n +=1
    for j in range(1,i+1):
        print(ch,end= " ")
    print()




num = int(input("enter a num : "))
n = 1
for i in range(1,num+1):
    for j in range(1,i+1):
        print(n,end= " ")
        n +=1
    print()



num = int(input("enter a num : "))
n = 65
for i in range(1,num+1):
    for j in range(1,i+1):
        print(chr(n),end= " ")
        n +=1
    print()
