def addDigits(num):
    num=str(num)
    while len(num)!=1:
        nums=list(num)
        num=sum(list(map(int,nums)))
        num=str(num)
    return int(num)
print(addDigits(24242))