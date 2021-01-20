for row in range(1,10):
    for col in  range(1,6):
        if (col ==1) or ((row ==1 or row ==4) and (col>1)):
            print("*",end=" ")
        else:
            print(end = " ")
    print()

for row in range(1,7):
    for col in  range(1,7):
        if  col == 1 or col ==6 or (row ==col and (col >1 and col <6)) :
            print("*", end="")
        else:
            print(end=" ")
    print()

i = 2
j = 4
for row in range(1,6):
    for col in  range(1,10):
        if  (col == 1 or col ==9) or (row ==1 and col ==5) or (col - row ==4):
            print("*", end="")
        elif row == i and col ==j:
            print("*", end="")
            i +=1
            j -=1
        else:
            print(end=" ")
    print()






i = 1
j = 5
for row in range(1,6):
    for col in  range(1,6):
        if  row == i and col == j:
            print("*", end="")
            i += 1
            j -= 1
        elif (col == row):
            print("*", end="")
        else:
            print(end=" ")
    print()



for row in range(1,8):
    for col in  range(1,6):
        if (col >1 and col <5) and (row ==1 or row ==4 or row ==7) or (col ==1 and (row ==2 or row == 3)) or (col == 5 and (row ==5 or row ==6)):
            print("*", end="")
        else:
            print(end = " ")
    print()