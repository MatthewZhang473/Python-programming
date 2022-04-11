class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = " "+s+" "

        the_stack = []
        result = ""
        tail = 0

        for head in range(0,len(s)):
            if s[head] == " ":
                while True:
                    if s[head+1] == ""
                the_stack.append(self.cut(s,head,tail))
                tail = head
        for i in range(len(the_stack)):
            result += the_stack.pop()
            result+=" "
        return result[0:-1]


    def cut(self,s,head,tail):
        sum = ""
        for i in range(tail,head):
            if s[i] == " ":
                continue
            sum += s[i]
        return sum
s = Solution()
print(s.reverseWords("example   good a"))