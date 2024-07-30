# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def f(self, root, ans):
        if root:
            if not root.left and not root.right:
                ans.append(root.val)
            self.f(root.left, ans)
            self.f(root.right, ans)
    
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        ans=[]
        self.f(root1, ans)
        ans2=[]
        self.f(root2, ans2)
        return ans==ans2 
        