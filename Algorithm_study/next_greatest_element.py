class Solution:
    def nextGreaterElement(self, nums1, nums2):
        the_stack =[]
        dic = {}

        for i in range(len(nums2)):
            new_value = nums2[i]
            j = len(the_stack) -1
            while(j>=0 and the_stack[j] < new_value):
                #print(new_value)
                dic[the_stack[j]] = new_value
                the_stack.pop()
                j-=1
            the_stack.append(new_value)
        #print(dic)
        for i in range(len(nums1)):
            if nums1[i] in dic:
                nums1[i] = dic[nums1[i]]
            else:
                nums1[i] = -1
        return nums1
                
s = Solution()


print(s.nextGreaterElement([2,4],[1,2,3,4]))


            
        