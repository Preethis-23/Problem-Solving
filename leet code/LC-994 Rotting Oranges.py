class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        moves = [(1,0), (0, 1), (-1, 0), (0, -1)]
        m = len(grid)
        n = len(grid[0])
        
        q = deque()
        fresh = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh += 1
        # if fresh == 0 :
        #     return -1
        
        cnt = 0

        while q:
            change = False
            for _ in range(len(q)):
                r, c = q.popleft()

                for mr, mc in moves:
                    nr, nc = r + mr, c + mc

                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        fresh -= 1
                        change = True
                        q.append((nr, nc))
                        grid[nr][nc]=2
            if change:
                cnt += 1
        if fresh==0:
            return cnt
        else:
            return -1
            
