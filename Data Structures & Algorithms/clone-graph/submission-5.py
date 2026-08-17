"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        start = node
        stk = [start]
        o_to_n = {} #hashmap to link old node reference to new node ref
        seen = set()
        seen.add(start)

        while stk: #to create value copy
            node = stk.pop()
            o_to_n[node] = Node(val=node.val) 
            #create new node w same val as og, we only copy val here not neighbours. no connections for new node yet

            for nei in node.neighbors:
                if nei not in seen:
                    seen.add(nei)
                    stk.append(nei)
        
        for old_node,new_node in o_to_n.items(): #to create connection
            #taking key,val from hashmap
            for nei in old_node.neighbors:
                new_nei = o_to_n[nei] #all old node:new node vals in hashmap already we making neigh connections now
                new_node.neighbors.append(new_nei)

        return o_to_n[start]


                
        