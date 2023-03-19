# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy= ListNode()
        curr = dummy
        while head and head.next:
            temp = head.next.next
            prev  = head
            
            curr.next = head.next
            head.next.next = prev
            
            curr = prev
            head = temp
        curr.next = head
        return dummy.next
            
            
            
        