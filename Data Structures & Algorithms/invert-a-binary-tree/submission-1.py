# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # using recursion
        if not root: #base case
            return 
        root.left, root.right = root.right , root.left#swap condn
        self.invertTree(root.left)#left subtree
        self.invertTree(root.right)#right subtree
        return root#final return after recursion
        