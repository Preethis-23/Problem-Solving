class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        def backtrack(ind, path):
            if ind == len(s):
                result.append(path)
                return
            if s[ind].isdigit():
                backtrack(ind + 1, path + s[ind])
                return
            
            backtrack(ind + 1, path + s[ind].lower())
            backtrack(ind + 1, path  + s[ind].upper())
        
        backtrack(0, "")
        return result