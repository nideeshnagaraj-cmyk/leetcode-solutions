def alternatingSum(nums):
    s=0
    for i in range(len(nums)):
        if i%2==0:
            s+=nums[i]
        else:
            s-=nums[i]
    return s
print(alternatingSum(nums = [1,3,5,7]))