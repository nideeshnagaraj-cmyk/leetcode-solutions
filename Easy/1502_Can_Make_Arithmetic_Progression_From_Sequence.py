def canMakeArithmeticProgression(arr):
    arr=sorted(arr)
    dif=abs(arr[0]-arr[1])
    for i in range(len(arr)-1):
        if abs(arr[i]-arr[i+1]) != dif:
            return False
    return True
print(canMakeArithmeticProgression(arr=[1,2,4]))