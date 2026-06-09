class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        extras = []
        zeros = []

        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    zeros.append((i, j))
                elif grid[i][j] > 1:
                    val = grid[i][j] - 1
                    for _ in range(val):
                        extras.append((i, j))
        used = [False] * len(zeros)
        out = float("inf")

        def backtrack(ind, cur_sum):
            nonlocal out
            if ind == len(zeros):
                out = min(out, cur_sum)
                return
            for x in range(len(zeros)):
                if used[x]:
                    continue
                used[x] = True
                x1, y1 = extras[ind]
                x2, y2 = zeros[x]
                backtrack(ind + 1, cur_sum + abs(x1-x2) + abs(y1 - y2) )
                used[x] = False
        backtrack(0, 0)
        return out