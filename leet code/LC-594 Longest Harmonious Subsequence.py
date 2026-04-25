class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        v = 0

        for key in cnt:
            if key + 1 in cnt:
                v = max(v, cnt[key] + cnt[key + 1])

        return v