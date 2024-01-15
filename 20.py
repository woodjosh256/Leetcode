"""
20. Valid Parentheses
Easy
Topics
Companies
Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        s_list = list(s)
        char_stack = []
        while len(s_list) > 0:
            c = s_list.pop(0)
            if c in ["(", "{", "["]:
                char_stack.append(c)
            else:
                if len(char_stack) == 0:
                    return False
                popped = char_stack.pop()
                if (popped == "(" and c != ")") or \
                        (popped == "{" and c != "}") or \
                        (popped == "[" and c != "]"):
                    return False
        return len(char_stack) == 0


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()"))
