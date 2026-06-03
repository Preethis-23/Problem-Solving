class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i not in '+-/*':
                stack.append(i)
            elif i == '+':
                b = int(stack.pop())
                a = int(stack.pop())

                stack.append(a+b)
            elif i == '-':
                b = int(stack.pop())
                a = int(stack.pop())

                stack.append(a-b)
            elif i == '*':
                b = int(stack.pop())
                a = int(stack.pop())

                stack.append(a*b)
            
            elif i == '/':
                b = int(stack.pop())
                a = int(stack.pop())

                stack.append(int(a/b))

        return int(stack.pop())
             
        
            
                
