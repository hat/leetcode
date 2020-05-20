"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def _helper(self, node: TreeNode, k: int, kth):
        if node.left != None:
            left = self._helper(node.left, k, kth)
            if kth[0] == k:
                return left
        kth[0] += 1
        if kth[0] == k:
            return node.val
        if node.right != None:
            right = self._helper(node.right, k, kth)
            if kth[0] == k:
                return right
        return node.val
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # find smallest element by recusring left
        return self._helper(root, k, [0])

class TestSolution:

    def setup(self):
        self.answer = Solution()

    def test_one(self):
        assert self.answer.kthSmallest([3,1,4,None,2], 1)