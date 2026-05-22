class Solution:
    def countAndSay(self, n: int) -> str:

        r = "1"

        for _ in range(n - 1):

            result = ""

            cnt = 1

            for i in range(1, len(r)):

                if r[i] == r[i - 1]:
                    cnt += 1

                else:
                    result += str(cnt) + r[i - 1]
                    cnt = 1

            result += str(cnt) + r[-1]

            r = result

        return r