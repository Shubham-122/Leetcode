# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# l_l=longest_length
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def l_l(root, k, isleft):
            if root:
                if isleft:
                    return max(l_l(root.left, 1, True), l_l(root.right, k+1, False))
                else:
                    return max(l_l(root.left, k+1, True), l_l(root.right, 1, False))
            return k-1
        return l_l(root, 0, True)
        