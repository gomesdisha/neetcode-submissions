# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        cnt = k

        def dfs(node):
            nonlocal ans,cnt
            if not node:
                return
            dfs(node.left)
            if cnt == 1:
                ans = node.val
            cnt-=1
            if cnt>0:
                dfs(node.right)
        
        dfs(root)
        return ans

