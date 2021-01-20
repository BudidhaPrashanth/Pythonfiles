pos =  -1 #give any value
def search(list,n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return  True
        i +=1
    return  False
list = [4,8,5,4,7,10,54]
n = 54
if search(list,n):
    print("found at",pos+1)
else:
    print("not found")