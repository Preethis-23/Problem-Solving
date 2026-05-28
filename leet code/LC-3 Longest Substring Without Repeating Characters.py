class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=len(s)

        l=0
        sett=set()
        maxi=0

        for r in range(length):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
            cur=r-l+1
            maxi=max(cur,maxi)
            sett.add(s[r])
        return maxi
        