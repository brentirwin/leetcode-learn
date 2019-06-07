# Binary Tree Inorder Traversal
# Input: [1,null,2,3]
# Output: [3,2,1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive solution
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        if root:
            output += self.postorderTraversal(root.left) \
            + self.postorderTraversal(root.right) \
            + [root.val]
        return output

# TODO: Iterative solution