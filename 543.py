from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def calcDiameter(self, root: Optional[TreeNode]) -> Tuple[int, int]: # returns depth, max diameter
        if root is None:
            return 0, 0
        else:
            left_depth, left_diameter = self.calcDiameter(root.left)
            right_depth, right_diameter = self.calcDiameter(root.right)
            return max(left_depth, right_depth) + 1, max(left_depth + right_depth - 2, left_diameter, right_diameter)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.calcDiameter(root)[1]