def shuffle(nums, n):
        z=[]
        for i in range(n):
            z.append(nums[i])
            z.append(nums[i+n])
        return z
print(shuffle(nums = [2,5,1,3,4,7], n = 3))