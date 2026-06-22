class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        dic = defaultdict(list)

        for x in strs:
            dic[tuple(sorted(x))].append(x)
        
        return list(dic.values())