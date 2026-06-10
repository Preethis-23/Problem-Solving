class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        cnt = 0

        def dfs(x, y):

            if x < 0 or y < 0 or x >= m or y >= n:
                return 0
            if grid[x][y] == 0:
                return 0
            
            grid[x][y] = 0

            return (1 + dfs(x + 1, y) + dfs(x, y + 1) + dfs(x - 1, y) + dfs(x, y - 1))



        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count = dfs(i, j)
                    cnt = max(cnt, count)

        return cnt