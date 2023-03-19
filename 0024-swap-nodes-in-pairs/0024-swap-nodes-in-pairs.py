# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy= ListNode()
        curr = dummy
        curr.next = head
        while head and head.next:
            tempHead1 = head
            tempHead2 = tempHead1.next
            tempHead3 = tempHead2.next
            
            curr.next = tempHead2
            tempHead2.next = tempHead1
            tempHead1.next = tempHead3
            
            curr = tempHead1
            head = tempHead3
        return dummy.next
            
            
            
        