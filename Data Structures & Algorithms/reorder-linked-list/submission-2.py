# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        slow = head
        fast = head.next

        while fast and fast.next: #to find middle(slow) and last(fast) ele
            slow = slow.next
            fast = fast.next.next

        #reverse the part after slow / the 2nd half since we need element from the end
        cur = slow.next
        prev = None #for the second half list beginning prev
        slow.next = None #for the first half list end

        while cur: #after rev: prev,cur,cur.next will become cur.next,cur,prev 
            temp = cur.next #assign
            cur.next = prev #link to 
            prev = cur #link to
            cur = temp #link to 
        head2 = prev #head of 2nd half reversed list. (last ele from og list)
        node = head #backup ptr for l1
        rnode = head2 #backup ptr for l2, attach next to node one by one

        while node and rnode:#merge to ll acc to need, one from node next from rnode
            temp = node.next
            temp2 = rnode.next
            node.next = rnode
            rnode.next = temp
            node = temp
            rnode = temp2
        return
            

        
            
        
        