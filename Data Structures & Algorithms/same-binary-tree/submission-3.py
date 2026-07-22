# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False

        res = 1
        def dfs(p,q):
            nonlocal res
            if not p and not q:
                return 
            if not p or not q:
                res = 0
                return
            if p.val != q.val:
                res=0
            dfs(p.left,q.left)
            dfs(p.right,q.right)
        
        dfs(p,q)
        return True if res==1 else False
                
        