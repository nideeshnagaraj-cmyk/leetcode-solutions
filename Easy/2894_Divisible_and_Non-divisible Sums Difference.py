def differenceOfSums(n,m):
    s1,s2=0,0
    for i in range(1,n+1):
        if i%m==0:
            s2+=i
        else:
            s1+=i
    return s1-s2
print(differenceOfSums(n = 10, m = 3))

'''
x=[i for i in range(1,n+1) if i%m==0]
y=[i for i in range(1,n+1) if i%m!=0]
return sum(y)-sum(x)
'''

'''
x,y=[],[]
for i in range(1,n+1):
    if i%m==0:
        x.append(i)
    else:
        y.append(i)
return sum(y)-sum(x)
'''