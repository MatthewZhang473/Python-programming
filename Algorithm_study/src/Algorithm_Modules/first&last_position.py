import bisect
import math
class Solution:
    def searchRange(self, nums, target):
        p1 = bisect.bisect_left(nums,target)
        p2 = bisect.bisect_right(nums,target)
        if p1 == p2:
            return [-1,-1]
        else:
            return [p1,p2-1]

    def binary_search_left(self,array,target,left,right):
        # return the position i such that:
        # array[j] < target for all j in [0,target]
        # array[j] >= target for all j in [target,len(array)]

        if left == right or left == right+1:
            return left

        else:
            mid = int((left+right)/2)
            val = array[mid]
            if val < target:
                return self.binary_search_left(array,target,mid+1,right)
            else:
                return self.binary_search_left(array,target,left,mid)

    def binary_search_right(self,array,target,left,right):
        # return the position i such that:
        # array[j] < target for all j in [0,target]
        # array[j] >= target for all j in [target,len(array)]
        print(left,right)

        if left == right or left == right+1:
            return left

        else:
            mid = math.ceil((left+right)/2)
            val = array[mid]
            if val <= target:
                return self.binary_search_right(array,target,mid,right)
            else:
                return self.binary_search_right(array,target,left,mid-1)


a = [1,2,3,3,3,3,3,3,3,3,5,6,7]

s = Solution()
#print(s.binary_search_left(a,3,0,len(a)))
print(s.binary_search_right(a,3,0,len(a)))

