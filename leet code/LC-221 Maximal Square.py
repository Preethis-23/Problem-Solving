class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0]*n for _ in range(m)]
        length = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if str(i) == '0' or str(j) == '0':
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
                    length = max(length, dp[i][j])
        return length * length
                    