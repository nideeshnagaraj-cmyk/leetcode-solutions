def buildArray(target, n):
    opp=[]
    top=max(target)
    i=1
    while i<=top:
        opp.append('Push')
        if i not in target:
            opp.append('Pop')
        i+=1    
    return opp
print(buildArray(target = [1,3,4], n = 4))