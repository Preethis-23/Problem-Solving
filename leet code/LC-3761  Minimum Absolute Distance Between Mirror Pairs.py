
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:

        ans = float('inf')
        mp = {}

        for i in range(len(nums)):
            if nums[i] in mp:
                ans = min(ans, i - mp[nums[i]])
            rev = int(str(nums[i])[::-1])
            mp[rev] = i

        return ans if ans != float('inf') else -1