import math
from typing import List


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        # does not handle invalid input
        operators = {'+', '-', '*', '/'}
        stack = []
        for token in tokens:
            if token in operators:
                second = int(stack.pop())
                first = int(stack.pop())
                match token:
                    case '+':
                        stack.append(first + second)
                    case '-':
                        stack.append(first - second)
                    case '*':
                        stack.append(first * second)
                    case '/':
                        stack.append(int(first / second))
            else:
                stack.append(token)
        return stack[0]


if __name__ == '__main__':
    s = Solution()
    print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
