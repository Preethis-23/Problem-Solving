class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l = max(weights)
        r = sum(weights)

        while l <= r:

            mid = (l + r) // 2

            curr = 0
            needed_days = 1

            for w in weights:

                if curr + w > mid:
                    needed_days += 1
                    curr = w
                else:
                    curr += w

            if needed_days > days:
                l = mid + 1
            else:
                r = mid - 1

        return l