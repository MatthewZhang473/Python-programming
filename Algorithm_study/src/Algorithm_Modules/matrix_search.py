class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        # m rows, n columns
        m = len(matrix)
        n = len(matrix[0])

        return self.binary_search(matrix,target,0,m*n-1)

    def binary_search(self,matrix,target,l,r):
        #print([l,r])
        if l >r :
            return False

        if l == r:
            pos = self.num_to_coor(matrix,l)
            return matrix[pos[0]][pos[1]] == target
        else:
            mid = int((l+r)/2)
            pos_mid = self.num_to_coor(matrix,mid)
            m_mid = matrix[pos_mid[0]][pos_mid[1]]
            if m_mid == target:
                return True
            elif m_mid < target:
                return self.binary_search(matrix,target,mid+1,r)
            else:
                return self.binary_search(matrix,target,l,mid-1)

    def num_to_coor(self,matrix,num):
        n = len(matrix[0])
        return [int(num/n),num%n]
    def coor_to_num(self,matrix,coor):
        n = len(matrix[0])
        return coor[0] * n + coor[1]

s = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(s.searchMatrix(matrix,target))