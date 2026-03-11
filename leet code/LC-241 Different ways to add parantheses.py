class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        def express(arr):
            result = []

            for i in range(len(arr)):
                if arr[i] in "+-*%/":
                    left = express(arr[:i])
                    right = express(arr[i+1:])

                    for m in left:
                        for n in right:
                            if arr[i]=="+":
                                result.append(m+n)
                            elif arr[i]=="-":
                                result.append(m-n)
                            elif arr[i]=="*":
                                result.append(m*n)
                            elif arr[i]=="/":
                                result.append(m/n)
                            else:
                                result.append(m%n)

            if not result:
                return [int(arr)]
            return result
        return express(expression)