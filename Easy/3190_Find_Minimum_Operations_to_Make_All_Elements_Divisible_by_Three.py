def minimumOperations(nums):
    operation=0
    for i in nums:
        if i%3!=0:
            operation+=1
    return operation
print(minimumOperations(nums = [1,2,3,4])) 