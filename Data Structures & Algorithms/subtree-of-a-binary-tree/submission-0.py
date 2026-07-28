# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(root1,root2) -> bool:
            if not root1 and not root2:
                return True
            elif not root1 or not root2:
                return False
            elif root1.val != root2.val:
                return False
                
            return bool(sameTree(root1.left,root2.left) and sameTree(root1.right,root2.right))

        def has_subtree(root)->bool:
            if not root:
                return False
            if sameTree(root,subRoot):
                return True
            return bool(has_subtree(root.left) or has_subtree(root.right))

        return has_subtree(root)


                
        