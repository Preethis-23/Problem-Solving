class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {0: 1}

        for num in nums:

            nxt = {}

            for s in dp:

                plus = s + num
                minus = s - num

                nxt[plus] = nxt.get(plus, 0) + dp[s]
                nxt[minus] = nxt.get(minus, 0) + dp[s]

            dp = nxt

        return dp.get(target, 0)