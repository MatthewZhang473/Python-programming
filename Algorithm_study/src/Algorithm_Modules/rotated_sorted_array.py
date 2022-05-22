class Solution:
    def search(self, nums, target: int) -> int:
        p = self.find_reverse(nums,0,len(nums)-1)
        print(p)
        return self.binary(nums,target,0,len(nums)-1,p)
        
    def find_reverse(self,nums,left,right):
        if len(nums) == 2:
            if nums[1]<nums[0]:
                return 1
            else:
                return 0

        if right == left +1:
            return right


        else:
            mid = int((left+right)/2)
            val = nums[mid]
            if nums[left] > val:
                return self.find_reverse(nums,left,mid)
            elif nums[right] < val:
                return self.find_reverse(nums,mid,right)
            else:
                return 0




    def binary(self,nums,target,left,right,p):
        real_l = (left + p)%len(nums)
        real_r = (right + p)%len(nums)

        #print(left,right)

        if left >= right:
            if nums[real_l] == target:
                return real_l
            else:
                return -1
        else:
            mid = int((left + right)/2)
            real_m = (mid + p) % len(nums)

            if nums[real_m] == target:
                return real_m
            if nums[real_m] < target:
                return self.binary(nums,target,mid+1,right,p)
            if nums[real_m] > target:
                return self.binary(nums,target,left,mid-1,p)







    

a = [3,1]
s = Solution()
print(s.search(a,1))
        
