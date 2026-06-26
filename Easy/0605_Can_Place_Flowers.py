def canPlaceFlowers(flowerbed,n):
    count=0
    if len(flowerbed)>1:
        if flowerbed[0]==0 and flowerbed[1]==0:
            flowerbed[0]=1
            count+=1
    else:
        if flowerbed[0]==0:
            count+=1
    for i in range(1,len(flowerbed)):
        if i==(len(flowerbed)-1):
            if flowerbed[i]==0 and flowerbed[i-1]==0:
                flowerbed[i]=1
                count+=1
        elif (flowerbed[i-1]==0 and flowerbed[i+1]==0) and flowerbed[i]==0:
            flowerbed[i]=1
            count+=1
    return (count>=n)
print(canPlaceFlowers(flowerbed = [0,0,1,0,0], n = 1))
print(canPlaceFlowers(flowerbed = [0], n = 0))