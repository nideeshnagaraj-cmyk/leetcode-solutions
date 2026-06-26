def findErrorNums(nums):
        n=len(nums)
        s=set(nums)
        duplicate=sum(nums)-sum(s)
        missing=sum(range(1,n+1))-sum(s)
        return [duplicate,missing]
print(findErrorNums(nums = [1,2,2,4]))