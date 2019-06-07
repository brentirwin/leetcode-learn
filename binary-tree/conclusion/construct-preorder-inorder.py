# Construct Binary Tree from Inorder and Postorder Traversal

'''
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

Output:
    3
   / \
  9  20
    /  \
   15   7
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # Top root is the first item in preorder
        if not len(preorder):
            return None
        
        val = preorder[0]
        del preorder[0]
        root = TreeNode(val)
        
        # Left and right can be determined by splitting inorder around val
        index = inorder.index(val)
        inorder_left = inorder[:index]
        inorder_right = inorder[index+1:]
        preorder_left = preorder[:len(inorder_left)]
        preorder_right = preorder[-len(inorder_right):] \
            if len(inorder_right) else []
        
        # Create child nodes recursively
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        
        # return node with its children
        return root