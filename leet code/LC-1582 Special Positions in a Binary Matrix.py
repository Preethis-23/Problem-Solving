class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        cnt = 0
        m = len(mat)
        n = len(mat[0])
        arr = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if mat[i-1][j-1]==1:
                    arr[i][j] = 1
                    arr[0][j]+=1
                    arr[i][0]+=1
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if mat[i-1][j-1]==1 and arr[i][0]==1 and arr[0][j]==1:
                    cnt+=1
        return cnt