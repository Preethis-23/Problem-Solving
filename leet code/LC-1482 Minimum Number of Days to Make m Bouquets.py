class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        l = min(bloomDay)
        r = max(bloomDay)

        if m * k > len(bloomDay):
            return -1
        while l <= r:
            flowers = 0
            bouquet = 0

            mid = (l + r)//2

            for x in bloomDay:
                if x <= mid:
                    flowers += 1
                
                    if flowers == k:
                        bouquet += 1
                        flowers = 0
                else:
                    flowers = 0
            if bouquet >= m:
                r = mid - 1
            else:
                l = mid + 1
        return l
        