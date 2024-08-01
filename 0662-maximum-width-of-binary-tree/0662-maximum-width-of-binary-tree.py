# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res= 0
        q= deque([[root, 1, 0]]) # node, heap number for every node, level of the node
        preLevel, preNum= 0,1
        
        while q:
            node, num, level= q.popleft()
            
            if level>preLevel:
                preLevel= level
                preNum= num
                
            res= max(res, num- preNum +1)
            
            if node.left:
                q.append([node.left, num*2, level+1])
            
            if node.right:
                q.append([node.right, (num*2)+1, level+1])
        
        return res
                
        