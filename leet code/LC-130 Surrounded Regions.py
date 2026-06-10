class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(x, y):

            if x < 0 or y < 0 or x >= m or y >=n:
                return False
            if board[x][y] != 'O':
                return

            board[x][y] = 'S'
            
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        m = len(board)
        n = len(board[0])
            
        for j in range(n):
            dfs(0, j)        
            dfs(m - 1, j)   

        for i in range(m):
            dfs(i, 0)       
            dfs(i, n - 1)   
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'