class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        total = sum(sum(x) for x in grid)

        top = 0
        for i in range(m-1):
            top += sum(grid[i])
            bottom = total - top

            if top == bottom:
                return True
            
        #each individual column sum
        csum = [0]*n
        for x in range(n):
            for y in range(m):
                csum[x] += grid[y][x]
        
        left=0
        for i in range(n-1):
            left += csum[i]
            right  = total - left
            if left==right:
                return True
        return False
        