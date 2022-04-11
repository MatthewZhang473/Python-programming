class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
    def find_max_sub(self,s,l,r):
        if l < r:
            return 0
        elif l==r:
            return 1
        else:
            mid = int(l+r)
            max_left = self.find_max_sub(s,l,mid-1)
            max_right = self.find_max_sub(s,mid+1,r)
            
            pointer1 = mid
            letters = {s[mid]}
            while len(letters) <= 2:
                pointer+=1
                letters.add(s[pointer1])

            pointer
                
                
        