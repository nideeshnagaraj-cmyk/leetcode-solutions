def judgeCircle(moves):
    position=[0,0]
    for i in moves:
        if i=='U':
            position[0]+=1
        elif i=='D':
            position[0]-=1
        elif i=='R':
            position[1]+=1
        else:
            position[1]-=1
    return position==[0,0]
print(judgeCircle("UDUUDDRLRLRL"))
'''The correct alternate solution is 
number(U) is equal to number(D) 
            and 
number(R) is equal to number(L)'''