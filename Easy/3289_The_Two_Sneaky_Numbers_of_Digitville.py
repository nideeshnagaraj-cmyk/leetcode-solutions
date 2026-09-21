def getSneakyNumbers(nums):
    dup=[]
    for i in set(nums):
        if nums.count(i)>1:
            dup.append(i)
        if len(dup)==2:
            break
    return dup
print(getSneakyNumbers(nums = [0,3,2,1,3,2]))