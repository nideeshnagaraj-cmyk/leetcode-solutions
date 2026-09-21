def smallerNumbersThanCurrent(nums):
    min=[]
    for i in nums:
        x=0
        for j in nums:
            if i>j:
                x+=1
        min.append(x)
    return min
print(smallerNumbersThanCurrent(nums = [8,1,2,2,3]))