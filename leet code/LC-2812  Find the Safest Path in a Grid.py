class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dist = [[float("inf")] * n for _ in range(m)]

        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = deque()

        if grid[0][0] or grid[m-1][n-1]:
            return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))
        while q:
            x, y = q.popleft()
        
            for mr, mc in moves:
                nr, nc = mr + x, mc + y

                if 0 <= nr < m and  0 <= nc < n:
                    if dist[nr][nc] == float("inf"):
                        dist[nr][nc] = dist[x][y] + 1
                        q.append((nr, nc))
        def reach(mid):
            if dist[0][0] < mid:
                return False
            visited = [[False] * n for _ in range(m)]

            q = deque([(0, 0)])
            visited[0][0] = True

            while q:
                r, c  = q.popleft()

                if (r, c) == (m-1, n-1):
                    return True
                
                for mr, mc in moves:
                    nr, nc = r + mr, c + mc

                    if 0 <= nr < m and  0 <= nc < n and not visited[nr][nc] and dist[nr][nc] >= mid:
                        visited[nr][nc] = True
                        q.append((nr, nc))
            return False
        
        low = 0
        high = max(max(row) for row in dist)
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if reach(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans



        