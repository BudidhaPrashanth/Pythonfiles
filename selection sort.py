def sort(nums):
    for i  in range(5):
        min = i
        for j in range(i,6):
            if nums[j] < nums[min]:
                min = j
            temp = nums[i]
            nums[i] = nums[min]
            nums[min] = temp
        print(nums)
nums = [5,3,8,6,7,2]
print(sort(nums))
print(nums)