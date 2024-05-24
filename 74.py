from typing import List, Tuple


class Solution:

    def get_nth(self, n, rows, cols) -> Tuple[int, int]:
        row = n // cols
        col = n % cols
        return row, col

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left <= right:
            middle = left + (right - left) // 2
            mrow,  mcol = self.get_nth(middle, rows, cols)
            m_val = matrix[mrow][mcol]
            if m_val < target:
                left = middle + 1
            elif m_val > target:
                right = middle - 1
            else:
                return True
        return False
