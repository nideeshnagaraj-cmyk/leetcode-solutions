def pivotInteger(n):
    y=[i for i in range(1,n+1)]
    x=[n]
    for i in range(0,n):
        if sum(x)==sum(y):
            pivot=x[0]
            break
        else:
            x.insert(0,n-i-1)
            y.pop()
            pivot=-1
    return pivot
print(pivotInteger(n=8))