# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowpt = fastpt = head
        while fastpt and fastpt.next: 
            slowpt = slowpt.next
            fastpt = fastpt.next.next
            if slowpt == fastpt:
                return True
        return False