# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode
        dummy.next = head
        temp = dummy
        while head:
            if head.val == val:
                temp.next = head.next
                head = head.next
            else:
                temp = head
                head = head.next
        return dummy.next
                
        