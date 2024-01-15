"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
"""

from typing import List


class Solution:

    def gen_combinations(self, current_state: str, open_parenthesis: int, closed_parenthesis: int) -> List[str]:
        if open_parenthesis == 0:
            return [current_state + (")" * closed_parenthesis)]
        elif open_parenthesis < closed_parenthesis:
            add_open = self.gen_combinations(current_state + "(", open_parenthesis - 1, closed_parenthesis)
            add_closed = self.gen_combinations(current_state + ")", open_parenthesis, closed_parenthesis - 1)
            return add_open + add_closed
        else:
            return self.gen_combinations(current_state + "(", open_parenthesis - 1, closed_parenthesis)

    def generateParenthesis(self, n: int) -> List[str]:
        return self.gen_combinations("", n, n)


if __name__ == '__main__':
    s = Solution()
    print("1: " + str(s.generateParenthesis(1)))
    print("3: " + str(s.generateParenthesis(3)))