class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = Counter(nums)

        return(sorted(list(s.keys()), key = lambda x: (-s[x], x)))[:k]


        
        