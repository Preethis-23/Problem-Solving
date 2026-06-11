class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in nums:
            xor ^= i
        for i in range(len(nums) + 1):
            xor ^= i
        return xor