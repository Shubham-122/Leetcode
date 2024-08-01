# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        s = []
        q = deque([root])
        
        while q:
            curNode = q.popleft()
            if curNode is None:
                s.append("#,")
            else:
                s.append(str(curNode.val) + ',')
                q.append(curNode.left)
                q.append(curNode.right)
        
        return ''.join(s)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        s = data.split(',')
        root = TreeNode(int(s[0]))
        q = deque([root])
        index = 1
        
        while q:
            node = q.popleft()
            
            # For left child
            if s[index] == "#":
                node.left = None
            else:
                node.left = TreeNode(int(s[index]))
                q.append(node.left)
            index += 1
            
            # For right child
            if s[index] == "#":
                node.right = None
            else:
                node.right = TreeNode(int(s[index]))
                q.append(node.right)
            index += 1
        
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))