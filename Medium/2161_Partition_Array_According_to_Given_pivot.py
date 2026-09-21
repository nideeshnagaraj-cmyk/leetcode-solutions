def pivotArray(nums,pivot):
    less,greater,equal=[],[],[]#less,greater,count=[],[],0
    for i in nums:
        if i<pivot:
            less.append(i)
        elif i>pivot:
            greater.append(i)
        else:
            equal.append(i)#count+=1
    return less+equal+greater#return less+[pivot]*count+greater
print(pivotArray(nums = [9,12,5,10,14,3,10], pivot = 10))