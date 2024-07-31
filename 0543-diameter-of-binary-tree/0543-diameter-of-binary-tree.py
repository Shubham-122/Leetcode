# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0
        self.max_depth(root, self.diameter)
        return self.diameter
    
    def max_depth(self, root, diameter):
        if not root:
            return 0
        
        lh= self.max_depth(root.left, self.diameter)
        rh= self.max_depth(root.right, self.diameter)
        
        self.diameter= max(self.diameter, lh+rh)
        
        return max(lh, rh) +1
    
    

        
        
        
        