# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tempNode = None
        tempHead = head
        while tempHead:
            old = tempHead.next
            tempHead.next = tempNode
            tempNode = tempHead
            tempHead = old
        return tempNode
        