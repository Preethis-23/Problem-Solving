class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        result = []

        l = max(nums)
        r = sum(nums)

        while l <= r:

            mid = (l + r)//2
            tot = 0
            part = 1

            for x in range(len(nums)):
                if tot + nums[x] <= mid:
                    tot += nums[x]
                else:
                    part += 1
                    tot = nums[x]
            if part <= k:
                result.append(mid)
                r = mid - 1
            else:
                l = mid + 1
        #return min(result)
        return l


