class Solution:
    def missingElement(self,nums,k):
        missing_numbers = self.find_missing_numbers(nums,k)
        print(missing_numbers)
        if len(missing_numbers) == k:
            return missing_numbers[k-1]
        else:
            return (k-len(missing_numbers)) + nums[-1]

    def find_missing_numbers(self, nums,k) -> int:
        pointer = 1
        val = nums[0]
        missing_nums = []
        
        while pointer < len(nums):
            if nums[pointer] == val+1:
                pointer += 1
                val +=1
            else:
                for i in range(val+1,nums[pointer]):
                    missing_nums.append(i)
                    if len(missing_nums) == k:
                        return missing_nums
                val = nums[pointer]
                pointer += 1
        return missing_nums
            
            

s= Solution()
print(s.missingElement([1,2,4],3))
