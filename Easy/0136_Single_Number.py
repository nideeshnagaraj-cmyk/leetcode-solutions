def singleNumber(nums):
    x=list(set(nums))
    for i in x:
        if nums.count(i) == 1:
            return i
print(singleNumber(nums = [4,1,2,1,2]))