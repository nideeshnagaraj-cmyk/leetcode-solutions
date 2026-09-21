def countPrefixes(words,s):
    Count=0
    x=[]
    for i in range(len(s)):
        x.append(s[:i+1])
    for j in words:
        if j in x:
            Count+=1
    return Count
print(countPrefixes(words = ["a","b","c","ab","bc","abc"], s = "abc"))