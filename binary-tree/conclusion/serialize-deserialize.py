# Still working on this.

# Serialize and Deserialize Binary Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = []
        output = []
        if root:
            queue.append(root)
        while len(queue):
            level = queue.copy()
            queue = []
            for node in level:
                if node:
                    output.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    output += 'null'
        return ','.join(output)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        queue = []
        tree = data.split(',')
        root = TreeNode(None)
        if root:
            root = TreeNode(tree[0])
            queue = 
        while len(queue):
            level = queue.copy()
            queue = []
            for node in level:

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))