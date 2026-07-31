# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        stack = [(root,float('-inf'))]

        while stack:
            node,maxval = stack.pop()
            if node.val >= maxval:
                good+=1
            maxval = max(node.val,maxval)
            if node.right:
                stack.append((node.right,maxval))
            if node.left:
                stack.append((node.left,maxval))
        return good
        