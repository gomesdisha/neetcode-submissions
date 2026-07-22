# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #L & R subtree of "every" node's height difference <= 1
        #not just root node
        res = 1
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            lmax = dfs(root.left)
            rmax = dfs(root.right)
            if abs(lmax-rmax)>1:
                res = 0
            return 1 + max(lmax,rmax)
        dfs(root)
        return True if res == 1 else False
            

        