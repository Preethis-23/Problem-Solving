class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        arr = [i for i in range(1, max(nums)+1)]

        l = 1
        r = max(arr)
        result = r

        while l <= r:
            mid = (l + r) // 2

            temp = sum(ceil(num/mid) for num in nums)

            if temp <= threshold:
                result = mid
                r = mid - 1
            else:
                l = mid + 1
        return result