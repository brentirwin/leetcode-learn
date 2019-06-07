# Binary Tree Inorder Traversal
# Input: [1,null,2,3]
# Output: [1,3,2]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive solution
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        if root:
            output += self.inorderTraversal(root.left) \
            + [root.val] \
            + self.inorderTraversal(root.right)
        return output

# TODO: Iterative solution