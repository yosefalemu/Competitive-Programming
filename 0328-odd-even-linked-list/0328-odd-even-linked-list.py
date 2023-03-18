# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy1 = ListNode()
        dummy2 = ListNode()
        curr1 = dummy1
        curr2 = dummy2
        counter = 1
        while head:
            if counter % 2 != 0:
                curr1.next = head
                curr1 = curr1.next
            else:
                curr2.next = head
                curr2 = curr2.next
            head = head.next
            counter += 1
        curr2.next = None
        curr1.next = dummy2.next
        return dummy1.next
            
        