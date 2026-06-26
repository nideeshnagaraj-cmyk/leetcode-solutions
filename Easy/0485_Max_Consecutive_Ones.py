def findMaxConsecutiveOnes(nums):
        seen=0
        n=[]
        for i in nums:
            if i==1:
                seen+=1
            else:
                n.append(seen)
                seen=0
        else:
            n.append(seen)
        return max(n)
print(findMaxConsecutiveOnes(nums = [1,1,0,1,1,1]))