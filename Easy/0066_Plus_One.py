def plusOne(digits):
    s=0
    for i in range(0,len(digits)):
        s=s*10+digits[i]
    s+=1
    lst=list(map(int, str(s)))
    return lst
print(plusOne(digits = [4,3,2,1]))