def cellsInRange(s):
    cells=[]
    for i in range(ord(s[0]),ord(s[3])+1):
        for j in range(int(s[1]),int(s[-1])+1):
            n=chr(i)+str(j)
            cells.append(n)
    return cells
print(cellsInRange("U7:X9"))