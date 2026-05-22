import re
from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:

        order = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }

        pattern = re.compile(r'^[A-Za-z0-9_]+$')

        result = []

        for i in range(len(code)):

            if (
                isActive[i]
                and businessLine[i] in order
                and pattern.fullmatch(code[i])
            ):

                result.append((order[businessLine[i]], code[i]))

        result.sort()

        return [x[1] for x in result]

# sort based on the business line