# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        ans = 0
        power = 0
        while prev:
            ans += (prev.val) *(2**power)
            power += 1
            prev = prev.next
        return ans
        