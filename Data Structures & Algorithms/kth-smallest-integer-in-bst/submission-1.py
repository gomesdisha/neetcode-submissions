# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []
        def dfs(node,inorder):
            if not node:
                return inorder 
            inorder = dfs(node.left,inorder) # goes till left end
            inorder.append(node.val) #appends from left end subtree till root
            inorder = dfs(node.right,inorder) #appends right subbtree also by going till left end of it
            return inorder #we need to return the list everytime
        inorder = dfs(root,inorder)
        return inorder[k-1]
        