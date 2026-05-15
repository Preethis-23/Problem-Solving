class Solution:
    def rotatedDigits(self, n: int) -> int:

        good = ['2', '5', '6', '9']
        valid = {'0', '1', '2', '5', '6', '8', '9'}

        dic = {
            '2': '5',
            '5': '2',
            '6': '9',
            '9': '6',
            '8': '8',
            '0': '0',
            '1': '1'
        }

        cnt = 0

        for i in range(1, n + 1):

            i = str(i)

            chck = True

            if len(i) == 1:

                if i in good:
                    cnt += 1

            else:

                result = ''

                for ch in i:

                    if ch in valid:
                        result += dic[ch]

                    else:
                        chck = False
                        break

                if chck and i != result:
                    cnt += 1

        return cnt