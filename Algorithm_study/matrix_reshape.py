class Solution:
    def matrixReshape(self, mat,r: int, c: int):
        m = len(mat)
        n = len(mat[0])
        if m*n  != r*c:
            return mat
        else:
            ans = [[] for j in range(r)]
            tot_len = r*c
            for i in range(tot_len):
                x1 = int(i/n)
                y1 = i%n
                x2 = int(i/c)
                #print(x1,y1,x2)
                ans[x2].append(mat[x1][y1])
            return ans
                
        
s = Solution()

test = [[1]]

print(s.matrixReshape(test,100,0))
