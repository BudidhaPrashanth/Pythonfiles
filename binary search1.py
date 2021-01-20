pos = 1

def search(list1,n):
    l = 0  # lower index
    u = len(list1) - 1  # upper index

    while l <= u:
        mid = (l+u)//2
        if list1[mid] == n:
            globals()['pos'] = mid
            return True

        else:
            if list1[mid] < n:
                l = mid+1
            else:
                u = mid -1
    return False

list1 = [2,8,24,54,75,99,103,134,176,206,374,549,773,999,4366]
n = 4366

if search(list1,n):
    print("Found at",pos+1)
else:
    print("Not found")
