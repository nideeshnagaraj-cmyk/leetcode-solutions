def findFinalValue(nums, original):
    while original in nums:
        original*=2
    return original
print(findFinalValue(nums = [2,7,9], original = 4))