def kidsWithCandies(candies,extraCandies):
    high=max(candies)
    result=[]
    for i in candies:
        result.append((i+extraCandies)>= high)
    return result
print(kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))