from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for str in strs:
            final += f"{len(str)}#{str}"
        return final


    def decode(self, s: str) -> List[str]:
        char_index = 0
        strs = []
        while char_index < len(s):
            next_delim = char_index + s[char_index:].find("#")
            count_str = s[char_index:next_delim]
            count = int(count_str)
            strs.append(s[char_index + len(count_str) + 1:char_index + len(count_str) + 1 + count])
            char_index += count + len(count_str) + 1
        return strs

s = Solution()
val = s.encode(["we","say",":","yes","!@#$%^&*()"])
print(val)
print(s.decode(val))