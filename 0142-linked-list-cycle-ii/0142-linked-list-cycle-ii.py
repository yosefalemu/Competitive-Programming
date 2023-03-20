# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dict1 = {}
        while head:
            if head in dict1:
                return head
            else:
                dict1[head] = 1
            head = head.next
        return None
            
        