class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1

        strt, end = -1, -1
        while l<=r:
            mid = ( l + r ) // 2

            if nums[mid] < target:
                l = mid + 1
            else:
                if nums[mid] == target:
                    strt = mid
                r = mid - 1
                
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            else:
                if nums[mid] == target:
                    end = mid
                l = mid + 1
        return [strt, end]