def scoreValidator(events):
    x=[0,0]
    for i in events:
        if x[1]==10:
            break
        if i=='WD' or i=='NB':
            x[0]+=1
        elif i in ['0','1','2','3','4','5','6']:
            x[0]+=int(i)
        else:
            x[1]+=1
    return x
print(scoreValidator(events = ["WD","NB",'6','4','4','0']))
'''
x=[0,0]
for i in events:
    if x[1]==10:
        break
    if i=='WD' or i=='NB':
        x[0]+=1
    elif i=='W':
        x[1]+=1
    else:
        x[0]+=int(i)
return x'''