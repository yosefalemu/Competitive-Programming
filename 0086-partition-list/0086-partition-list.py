# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        partitionOne = ListNode()
        partitionTwo = ListNode()
        currOne = partitionOne
        currTwo = partitionTwo
        while head:
            if head.val < x:
                currOne.next = head
                currOne = currOne.next
            else:
                currTwo.next = head
                currTwo = currTwo.next
            head = head.next
        currTwo.next = None
        currOne.next = partitionTwo.next
        return partitionOne.next
        