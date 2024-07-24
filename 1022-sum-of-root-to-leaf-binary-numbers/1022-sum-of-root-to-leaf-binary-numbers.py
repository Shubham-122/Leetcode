# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calculate_sum(self, root, summ):
        if root:
            ans = (2 * summ) + root.val
            if not root.left and not root.right:
                return ans
            return self.calculate_sum(root.left, ans) + self.calculate_sum(root.right, ans)
        return 0
        
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.calculate_sum(root, 0)
    
    

        