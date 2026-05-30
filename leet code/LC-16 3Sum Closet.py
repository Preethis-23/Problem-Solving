class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mini = float("inf")
        nums.sort()
        out = 0
        for i in range(n):
            j = i+1
            k = n-1


            while j < k:
                total = nums[i] + nums[j] + nums[k]
                diff = abs(total - target)
                if total<target:
                    j += 1
                    #diff = abs(total) + target
                elif total > target:
                    k -= 1
                    #diff = abs(total - target)
                else:
                    # j += 1
                    # k -= 1
                    # diff = target
                    return total
                if diff < mini:
                    mini = diff
                    out = total
        return out