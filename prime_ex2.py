nums =[]
for n in range(100):
    if n >1:
        for i in range(2,n):
            if (n%i) ==0:
                break
        else:
            nums.append(n)
print(nums)