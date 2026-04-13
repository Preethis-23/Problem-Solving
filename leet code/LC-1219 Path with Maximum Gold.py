class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        moves = [(0,1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False]*n for _ in range(m)]
        
        result = []

        def backtrack(r, c, gold_value):
            if r<0 or c<0 or r>=m or c>=n or grid[r][c]==0 or visited[r][c]:
                result.append(gold_value)
                return False
            visited[r][c]=True
            gold_value = gold_value + grid[r][c]
            for mr, mc in moves:
                nr, nc = mr + r, mc + c
                backtrack(nr, nc, gold_value)
            visited[r][c] = False
        for i in range(m):
            for j in range(n):
                backtrack(i, j, 0)
        return max(result)