def distributeCandies(candyType):
    n=int(len(candyType)/2)
    x=len(list(set(candyType)))
    ate=x if x<=n else n
    return ate
print(distributeCandies(candyType = [6,6,6,6]))