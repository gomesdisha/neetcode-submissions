# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        res = []

        while q:#level order traversal
            #ans = []
            n = len(q)
            for i in range(n):#each level append and store last node of level
                node = q.popleft()
                if i == n-1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
        return res
                




        