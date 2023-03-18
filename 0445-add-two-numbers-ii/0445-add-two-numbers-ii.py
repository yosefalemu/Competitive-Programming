# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev1 = prev2 = None
        while l1:
            temp = l1.next
            l1.next = prev1
            prev1 = l1
            l1 = temp
        while l2:
            temp = l2.next
            l2.next = prev2
            prev2 = l2
            l2 = temp
        carry = 0
        dummy = ListNode()
        curr = dummy
        while prev1 or prev2 or carry:
            num1 = prev1.val if prev1 else 0
            num2 = prev2.val if prev2 else 0
            
            temp = num1 + num2 + carry
            resultSum = temp % 10
            carry = temp // 10
            
            curr.next = ListNode(resultSum)
            curr = curr.next
            prev1 = prev1.next if prev1 else None
            prev2 = prev2.next if prev2 else None
        prev3 = None
        curr = dummy.next
        while curr:
            temp = curr.next
            curr.next = prev3
            prev3 = curr
            curr = temp
        return prev3
        
        