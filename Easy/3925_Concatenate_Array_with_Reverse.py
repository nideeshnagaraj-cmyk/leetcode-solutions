def concatWithReverse(nums):
    ans=nums*2
    n=len(nums)
    for i in range(n):
        ans[n+i]=nums[n-i-1]
    return ans
print(concatWithReverse(nums=[1,2,3]))