def binaryadditionn(a,b):
    if len(a)>len(b):
        b='0'*(len(a)-len(b))+b
    elif len(a)<len(b):
        a='0'*(len(b)-len(a))+a
    carry=0
    result=''
    for i in range(len(a)-1,-1,-1):
        sum=int(a[i])+int(b[i])+carry
        if sum==0:
            result='0'+result
            carry=0
        elif sum==1:
            result='1'+result
            carry=0
        elif sum==2:
            result='0'+result
            carry=1
        else:
            result='1'+result
            carry=1
    if carry==1:
        result='1'+result
    return result
a='1010'
b='1011'    
print(binaryadditionn(a,b))