class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0

        for i in range(32):
            bit = n & 1
            ans = (ans << 1) | bit
            n = n >> 1
        return ans
        
        # pick last bit from n, 
        # left shit and create space as  0 by default, use or change it to 0, if segemented last value is 1,
        # then right shift and move for next last bit