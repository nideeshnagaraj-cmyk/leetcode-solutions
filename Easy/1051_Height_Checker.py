def heightChecker(heights):
    expected=sorted(heights)
    k=0
    for i in range(len(heights)):
        if heights[i]!=expected[i]:
            k+=1
    return k
print(heightChecker(heights = [1,1,4,2,1,3]))