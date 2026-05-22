class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        freq = {}

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        duplicate = -1
        missing = -1

        for i in range(1, n+1):
            if i not in freq:
                missing = i
            elif freq[i] == 2:
                duplicate = i
        
        return [duplicate, missing]
            
