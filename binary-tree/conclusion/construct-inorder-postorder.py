# Construct Binary Tree from Inorder and Postorder Traversal

'''
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # Top root is the last item in postorder
        if not len(postorder):
            return None
        
        val = postorder[-1]
        del postorder[-1]
        root = TreeNode(val)
        
        # Left and right can be determined by splitting inorder around val
        index = inorder.index(val)
        inorder_left = inorder[:index]
        inorder_right = inorder[index+1:]
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[-len(inorder_right):] \
            if len(inorder_right) else []
        
        # Create child nodes recursilvely
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)
        
        # return node with its children
        return root