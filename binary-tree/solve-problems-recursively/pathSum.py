# Path Sum

'''
Input: sum=22
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

Output: True
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        dif = sum - root.val
        if dif == 0 and not root.left and not root.right:
            return True
        return self.hasPathSum(root.left, dif) or \
            self.hasPathSum(root.right, dif)
        return False