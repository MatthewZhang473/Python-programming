from turtle import left


class Solution:
    def missingElement(self,nums,k):
        the_position = self.binary_search(nums,k,0,len(nums)-1)

        actual_misses = self.number_of_misses(nums,the_position)

        if actual_misses < k:
            return nums[the_position] + k-actual_misses

        elif actual_misses == k:
            return nums[the_position] - 1
        else:
            return nums[the_position] - (actual_misses-k)-1
        
        
        
    def number_of_misses(self,nums,index):
        return nums[index] - nums[0] - index
    
    def binary_search(self,nums,k,left_index,right_index):

        #print([left_index,right_index])
        if left_index == right_index:
            return left_index
        else:
            mid = int((left_index + right_index)/2)
            if self.number_of_misses(nums,mid)<k:
                return self.binary_search(nums,k,mid+1,right_index)
            else:
                return self.binary_search(nums,k,left_index,mid)
            
        
s = Solution()
print(s.missingElement([4,7,9,10],1))