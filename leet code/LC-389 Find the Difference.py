class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor = 0

        for x in s:
            xor ^= ord(x)
        for y in t:
            xor ^= ord(y)
        return chr(xor)