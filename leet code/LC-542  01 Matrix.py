class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

                
        m = len(mat)
        n = len(mat[0])

        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                elif mat[i][j] == 1:
                    mat[i][j] = -1
        
        while q:
            r, c = q.popleft()
            
            for mr, mc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + mr, c + mc
                if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1
                    q.append((nr, nc))
            
        return mat
