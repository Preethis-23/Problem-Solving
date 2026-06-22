class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        result = 0

        for x in s:
            if x - 1 not in s:
                start = x
                length = 1

                while start + 1 in s:
                    length += 1
                    start += 1
                result = max(result, length)
        return result



        