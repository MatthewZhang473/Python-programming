class Solution:
    def nearestValidPoint(self, x: int, y: int, points) -> int:
        smallest_val = 100000
        the_index = -1
        for i in range(len(points)):
            if self.is_valid([x,y], points[i]):
                dis = self.Manhanttan([x,y],points[i])
                print("The distance of the {}th point is {}".format(i,dis))
                if dis < smallest_val:
                    smallest_val = dis
                    the_index = i
        return the_index
        
        
        
    def Manhanttan(self,p1,p2):
        return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
    
    def is_valid(self,p_origin,p_other):
        if p_origin[0]  == p_other[0]:
            return True
        if p_origin[1] == p_other[1]:
            return True
        return False
        

s = Solution()
print(s.nearestValidPoint(3,4,[[1,2],[3,1],[2,4],[2,3],[4,4]]))