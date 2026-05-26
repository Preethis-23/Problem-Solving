class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        tot = 0
        result = float("inf")

        for i in range(n):
            tot += nums[i]
            while tot>=target:
                result = min(result, i - l + 1)
                total -= nums[l]
                l += 1
            
        return 0 if result == float("-inf") else result


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        ans = float('inf')

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                ans = min(ans, right - left + 1)

                total -= nums[left]
                left += 1

        return 0 if ans == float('inf') else ans