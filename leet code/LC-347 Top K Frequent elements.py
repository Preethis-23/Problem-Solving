class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = Counter(nums)

        return(sorted(list(s.keys()), key = lambda x: (-s[x], x)))[:k]
        
        '''
         s = defaultdict()
        result = []

        for x in nums:
            s[x] = s.get(x, 0) + 1
        result = sorted(s.keys(), key = lambda x : s[x], reverse = True)[:k]
        #for key, value in s.items():
            #result.append(key)
        return result
        '''

        
        