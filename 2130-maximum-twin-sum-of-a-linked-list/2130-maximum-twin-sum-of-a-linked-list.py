# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        prev = None
        nex = None
        slow = head
        output = None
        fast = head

        while fast and fast.next:
            fast = fast.next.next

            nex = slow.next
            slow.next = prev
            prev = slow
            slow = nex

        while slow and prev:
            if(output == None or slow.val + prev.val > output):
                output = slow.val + prev.val
            prev = prev.next
            slow = slow.next

        return output