# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None #return listNode not list, not []

        prev = None
        cur = head
        while cur: #rev list
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        head2=prev
        if n==1:
            head2 = head2.next 
        else:
            i = 1 #reach node to delete
            node = head2
            prev2 = node
            while i<n:
                prev2 = node
                node = node.next
                i+=1
            prev2.next = node.next #break link
            node.next = None # removed node links

        #reverse list again:
        prev = None
        while head2:
            temp = head2.next
            head2.next = prev
            prev = head2
            head2 = temp

        return prev

        
        
        



        
        