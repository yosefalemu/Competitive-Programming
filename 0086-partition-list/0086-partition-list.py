# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode()
        dummy2 = ListNode()
        partitionOne = dummy1
        partitionTwo = dummy2
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
        