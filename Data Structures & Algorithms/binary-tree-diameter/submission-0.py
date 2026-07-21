# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0 #initially 0, its basically lmaxh+rmaxh

        def maxh(root): #recursive function to find left and right height and dia
            nonlocal diameter #nonlocal says its global var not local, so outside diameter gets updated
            if not root:
                return 0
            
            lmax = maxh(root.left)
            rmax = maxh(root.right)#normal depth recursion used
            diameter = max(diameter,lmax+rmax)#calculates dia at each node and stores max
            return 1 + max(lmax,rmax) 

        maxh(root)#run recursive fn. starting pt
        return diameter #reqd diameter int is returned
        
        