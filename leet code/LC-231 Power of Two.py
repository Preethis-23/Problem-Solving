class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        cnt = 0

        while n:
            n = n & (n - 1)
            cnt += 1
            if cnt > 1:
                return False
        if cnt == 0:
            return False
        return True

