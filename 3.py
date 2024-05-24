"""
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        start_idx = 0 # inclusive
        end_idx = 0 # inclusive
        max_len = 1

        while end_idx < len(s):
            while s[end_idx] in s[start_idx:end_idx] and start_idx < end_idx:
                start_idx += 1

            max_len = max(max_len, end_idx - start_idx + 1)

            end_idx += 1
        return max_len

s = Solution()

print(s.lengthOfLongestSubstring("abcabcbb"))