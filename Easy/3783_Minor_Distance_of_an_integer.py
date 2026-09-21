def mirrorDistance(n):
    n=str(n)
    rev=n[::-1]
    return abs(int(n)-int(rev))
print(mirrorDistance(7))