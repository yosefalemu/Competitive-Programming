# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        count = 1
        dummy = ListNode()
        curr = dummy
        while prev:
            if count != n:
                curr.next = prev
            else:
                curr.next = prev.next
            curr = prev
            prev = prev.next
            count += 1
        head = dummy.next
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
            
            
            
                
            
        