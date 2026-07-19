# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #dummy node at start, so that we land at prev  node of node to delete
        #start l from dummy and r from nth pos
        #so that when r reaches last node, l can directly be linked to its next.next
        dummy = ListNode(0,head)#next of dummy is head
        l = dummy
        r = head
        #move r to nth pos from beg
        while r and n>0:
            r=r.next
            n-=1
        #move both l and r by one step each:
        while r:
            r=r.next
            l=l.next
        #we reach at a pos after n from the end 
        #change the links:
        l.next = l.next.next
        return dummy.next   