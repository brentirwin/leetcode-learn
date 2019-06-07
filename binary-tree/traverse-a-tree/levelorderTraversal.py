# Binary Tree Level Order Traversal
# Input: [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = []
        output = []
        if root:
            queue.append(root)
        while len(queue):
            level_nodes = queue.copy()
            level_output = []
            queue = []
            for node in level_nodes:
                if node:
                    level_output.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if len(level_output):
                output.append(level_output)
        return output