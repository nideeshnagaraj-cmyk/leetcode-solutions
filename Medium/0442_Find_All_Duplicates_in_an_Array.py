def findDuplicates(nums):
    dup = []
    present = [0] * (len(nums) + 1)
    for i in nums:
        if present[i] == -1:
            dup.append(i)
        else:
            present[i] = -1
    return dup
'''
result = []
for i in range(len(nums)):
    index = abs(nums[i]) - 1
    if nums[index] < 0:
        result.append(abs(nums[i]))
    else:
        nums[index] = -nums[index]
return result
'''
print(findDuplicates(nums = [4,3,2,7,8,2,3,1]))