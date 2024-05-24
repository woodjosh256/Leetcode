"""
110. Balanced Binary Tree
Easy
Topics
Companies
Given a binary tree, determine if it is
height-balanced
.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def calcWhetherBalanced(self, root: Optional[TreeNode]) -> Tuple[int, bool]: # depth, isBalanced
        if root is None:
            return 0, True

        left_depth, left_balanced = self.calcWhetherBalanced(root.left)
        right_depth, right_balanced = self.calcWhetherBalanced(root.right)

        balanced = (abs(left_depth - right_depth) <= 1
                    and left_balanced and right_balanced)
        depth = max(left_depth, right_depth) + 1

        return depth, balanced

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.calcWhetherBalanced(root)[1]
