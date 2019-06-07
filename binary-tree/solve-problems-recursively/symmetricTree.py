# Symmetric Tree

# Input: [1,2,2,3,4,4,3]
# Output: True

# Input: [1,2,2,null,3,null,3]
# Output: False

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive solution
class Solution:
    def isMirror(self, left, right) -> bool:
        if not left or not right:
            return left == right
        return left.val == right.val \
            and self.isMirror(left.left, right.right) \
            and self.isMirror(left.right, right.left)
    
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)

# TODO: Iterative solution