class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 1

        while i<n and nums[i-1]<nums[i]:
            i += 1
        p = i - 1

        while i<n and nums[i-1]>nums[i]:
            i += 1
        q = i - 1

        while i<n and nums[i-1]<nums[i]:
            i += 1
        r = i - 1

        return (p!=0) and (q!=0) and (r!=q and r==n-1)
        
        