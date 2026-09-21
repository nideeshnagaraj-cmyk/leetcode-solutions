def findMedianSortedArrays(nums1, nums2):
        z=sorted(nums1 + nums2)
        n = len(z)
        if n%2==1:
            return float(z[n//2])
        else:
            return (z[n//2]+z[n//2-1])/2.0
print(findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))