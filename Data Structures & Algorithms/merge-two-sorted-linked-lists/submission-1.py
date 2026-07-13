# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()#create new list with dummy node as head 
        tail=dummy#dummy nodes head and tail same initially, we take tail so that we have head dummy to return later
        #cur1,cur2 = list1, list2 can be done too

        while list1 and list2:#both non empty lists
            if list1.val <= list2.val:#check which small, asc order
                tail.next=list1 #add value
                list1 = list1.next #move pointer
            else:
                tail.next=list2
                list2=list2.next
            tail = tail.next #move new lists ptr

        if list1: #if 1 list goes empty but other is non empty, we append remaining list  directly
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next

                

        
        