# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        count = 1
        while head:
            if count != left:
                curr.next = head
                head = head.next
                curr = curr.next
            else:
                prev = None
                hold = head
                while count <= right:
                    temp = head.next
                    head.next = prev
                    prev = head
                    head = temp
                    count += 1
                curr.next = prev
                while prev:
                    curr = curr.next
                    prev = prev.next
            count += 1
                
        return dummy.next
                
    
                    
        