class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        s = Counter(words)
        return sorted(list(s.keys()), key=lambda x: (-s[x], x))[:k]
    

    #here we used lambda function to sort keys, based on it values in desscending order by converting it as negative value :)
