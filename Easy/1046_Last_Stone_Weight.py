def lastStoneWeight(stones):
    while len(stones)>1:
        max1=max(stones)
        stones.remove(max1)
        max2=max(stones)
        stones.remove(max2)
        stones.append(abs(max1-max2))
    return stones[0]
print(lastStoneWeight(stones = [2,7,4,1,8,1]))