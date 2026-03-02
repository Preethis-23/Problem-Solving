class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        cnt = 0
        n = len(grid)
        for i in range(n):
            tot_zero = n-1-i

            j = i
            while j<n:
                zero_cnt = 0

                for k in range(n-1, -1, -1):
                    if grid[j][k] == 0:
                        zero_cnt += 1
                    else:
                        break
                if zero_cnt>=tot_zero:
                    break
                j+=1
            if j==n:
                return -1
            
            while j>i:
                grid[j], grid[j-1] = grid[j-1], grid[j]
                j -= 1
                cnt+=1
        return cnt
