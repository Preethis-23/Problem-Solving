class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        lst = prices

        dp = [0]*(n)
        mini = lst[0]

        for i in range(1, n):
            if mini<lst[i]:
                dp[i] = max(dp[i-1], lst[i] - mini)

            else:
                mini = min(mini, lst[i])
                dp[i] = dp[i-1]
        return max(dp)
        