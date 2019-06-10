# Serialze and Deserialize Binary Tree

'''
Example:
You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
'''

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

        if not root or root.val is None:
            return '[]'
        queue.append(root)
        while len(queue):
            # level is this level
            # queue is the next level
            level = queue.copy()
            queue = []
            # if a node is a node, record its value and queue its children
            # if it is not a node, enter null
            for node in level:
                if node:
                    output.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    output.append('null')
        # remove trailing nulls at the end and return as string
        while len(output) and output[-1] == 'null':
            output = output[:-1]
        return '[' + ','.join(str(x) for x in output) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # turn string to array and initialize queue
        if data == '[]':
            return None
        data = data[1:-1].split(',')
        data.append(None)

        # Create TreeNodes
        def createNode(value) -> TreeNode:
            if value == 'null' or not value:
                return None
            return TreeNode(int(value))

        # Give node children
        def addChildren(prev, left=None, right=None):
            prev.left = left
            prev.right = right

        # first level
        root = createNode(data[0])
        data = data[1:]
        queue = [root]

        while len(queue):
            # Add children if queue[0] is a real node
            if queue[0]:
                for i in range(0,2):
                    if data[0]:
                        node = TreeNode(data[0])
                        queue.append(node)
                        if i == 0:
                            queue[0].left = node
                        elif i == 1:
                            queue[0].right = node
                        data = data[1:]
                    else:
                        queue.append(None)
                        break
            # Remove first node in queue
            queue = queue[1:]
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))