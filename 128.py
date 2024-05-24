class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for num in num_set:
            if num - 1 not in num_set:
                iterable_num = num
                while iterable_num + 1 in num_set:
                    iterable_num += 1
                max_length = max(max_length, iterable_num - num + 1)

        return max_length