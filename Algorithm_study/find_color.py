class Solution:
    def shortestDistanceColor(self, colors,queries):
        ones = []
        twos = []
        threes = []
        for i in range(len(colors)):
            if colors[i] == 1:
                ones.append(i)
            elif colors[i] == 2:
                twos.append(i)
            else:
                threes.append(i)

        for i in range(len(queries)):
            if queries[i][1] == 1:
                the_array = ones
            elif queries[i][1] == 2:
                the_array = twos
            else:
                the_array = threes
            if len(the_array) == 0:
                queries[i] = -1
                continue
            close_position = self.binary_search(the_array,queries[i][0],0,len(the_array)-1)
            #print(close_position)
            a1 = abs(the_array[close_position] - queries[i][0])
            a2 = abs(queries[i][0] - the_array[close_position-1])
            queries[i] = min(a1,a2)
        #print(ones,twos,threes)
        #print(queries)

        return queries
            

        
    def binary_search(self,array,val,l,r):
        if val > array[-1]:
            return len(array)-1
        elif l == r:
            return l
        else:
            mid = int((r+l)/2)
            if array[mid] < val:
                return self.binary_search(array,val,mid+1,r)
            else:
                return self.binary_search(array,val,l,mid)
        
            



s = Solution()
print(s.shortestDistanceColor([2,1,2,2,1],
[[1,1],[4,3],[1,3],[4,2],[2,1]]))

        