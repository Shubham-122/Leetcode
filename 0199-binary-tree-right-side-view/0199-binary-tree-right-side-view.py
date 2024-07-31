from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res= []
        self.right_traversal(root, 0, res)
        return res
    
    def right_traversal(self,root, level, res):
        if not root:
            return
        
        if len(res) == level:
            res.append(root.val)
            
        self.right_traversal(root.right, level+1, res)
        self.right_traversal(root.left, level+1, res)
            
        