def recoverOrder(order,friends):
    temp=[]
    for i in order:
        if i in friends:
            temp.append(i)
    return temp
print(recoverOrder(order = [3,1,2,5,4], friends = [1,3,4]))