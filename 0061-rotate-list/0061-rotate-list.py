# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        tempHead = head
        while tempHead:
            length += 1
            tempHead = tempHead.next
        if length == 0:
            return head
        temp = k % length
        if temp == 0:
            return head
        dummy = ListNode()
        curr = dummy
        while length > temp:
            curr.next = head
            curr = curr.next
            head = head.next
            length -= 1
        curr.next = None
        tempHead = head
        while tempHead:
            if tempHead.next == None:
                tempHead.next = dummy.next
                break
            tempHead = tempHead.next
        return head
                
        