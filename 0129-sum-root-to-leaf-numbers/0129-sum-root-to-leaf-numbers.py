# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calculate_sum(self, root, summ):
        if root:
            summ = (summ*10) + root.val
            if not root.left and not root.right:
                return summ
            return self.calculate_sum(root.left, summ) + self.calculate_sum(root.right, summ)
        return 0
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.calculate_sum(root, 0)
        