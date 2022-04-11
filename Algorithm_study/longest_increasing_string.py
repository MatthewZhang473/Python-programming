from bisect import bisect, bisect_left


class Solution:
    def lengthOfLIS(self, nums) -> int:
        min_ending = [-9999999]

        for i in range(len(nums)):
            adding_pos = bisect_left(min_ending,nums[i])
            if adding_pos >= len(min_ending):
                min_ending.append(nums[i])
            else:
                min_ending[adding_pos] = min(min_ending[adding_pos],nums[i])
        print(min_ending)
        return len(min_ending) - 1

s = Solution()
print(s.lengthOfLIS(
[0,1,0,3,2,3]))
