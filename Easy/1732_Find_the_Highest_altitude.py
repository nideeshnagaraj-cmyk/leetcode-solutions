def largestAltitude(gain):
    high=0
    x=[0]
    for i in range(len(gain)):
        x.append(x[i]+gain[i])
    return max(x)
print(largestAltitude(gain = [-5,1,5,0,-7]))