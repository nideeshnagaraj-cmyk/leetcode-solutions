def transformArray(nums):
    res=[]
    for i in nums:
        if i%2==0:
            res.insert(0,0)#res=[0]+res
        else:
            res.append(1)#res=res+[1]
    return res
print(transformArray( nums = [1,5,1,4,2]))
'''
even,odd=0,0
for i in nums:
    if i%2==0:
        even+=1
    else:
        odd+=1
return [0]*even+[1]*odd
'''