class Solution:
    def maxArea(self, height: List[int]) -> int:
        nums = height
        r = len(nums) - 1
        l = 0

        water = 0

        while l<r:
            width = r - l
            length = min(nums[l], nums[r])
            contain = length * width

            water = max(water, contain)

            if nums[l]<nums[r]:
                l += 1
            else:
                r -= 1
        return water
        