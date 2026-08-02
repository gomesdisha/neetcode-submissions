# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validity(node, leftmin, rightmax):
            if not node:
                return True
            if not(leftmin<node.val<rightmax):
                return False
            
            return (validity(node.left, leftmin, node.val) and validity(node.right, node.val, rightmax))
        
        return validity(root,float("-inf"),float("inf"))
        

        
        