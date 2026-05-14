class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums = sorted(nums)

        n = len(nums)-1

        return nums == list(range(1, n+1))+[n]
        