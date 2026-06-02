class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        s1 = set()
        s2 = set()
        result = []

        for i in range(0, len(s) - 10 + 1):
            string = s[i:i+10]

            if string not in s1:
                s1.add(string)
            else:
                if string not in s2:
                    s2.add(string)
                    result.append(string)
        return result