from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = Counter(t)
        cnt = len(t)
        l = 0
        out = ""

        for i in range(len(s)):
            if need[s[i]] > 0:
                cnt -= 1
            need[s[i]] -= 1

            while cnt == 0:
                string = s[l:i + 1]

                if out == "" or len(string) < len(out):
                    out = string
                
                need[s[l]] += 1

                if need[s[l]] > 0:
                    cnt += 1
                l += 1
        return out

        
        