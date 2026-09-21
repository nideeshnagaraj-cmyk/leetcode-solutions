def searchInsert(num,target):
    for i in range(len(num)):
        if num[i]>=target:
            return i 
    else:
        return i+1
print(searchInsert([1,3,5,6],7))