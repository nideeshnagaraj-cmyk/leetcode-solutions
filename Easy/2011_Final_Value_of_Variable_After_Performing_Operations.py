def finalValueAfterOperations(operations):
    s=0
    for i in operations:
        if i=='X++' or i=='++X':
            s+=1
        else:
            s-=1
    return s
print(finalValueAfterOperations(operations = ["--X","X++","X++"]))
'''
x1=operations.count('X++')+operations.count('++X')
x2=operations.count('X--')+operations.count('--X')
return x1-x2
'''