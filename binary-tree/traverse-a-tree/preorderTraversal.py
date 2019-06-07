# Binary Tree Preorder Traversal
# Input: [1,null,2,3]
# Output: [1,2,3]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive solution
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        if root:
            output += [root.val] \
            + self.preorderTraversal(root.left) \
            + self.preorderTraversal(root.right)
        return output

# TODO: Iterative solution