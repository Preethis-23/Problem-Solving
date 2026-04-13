class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        n = len(nums)
        left = 1
        for i in range(n):
            result[i] = left
            left *= nums[i]

        right = 1
        for i in range(n-1, -1, -1):
            result[i] *= right
            right *= nums[i]
        return result
        