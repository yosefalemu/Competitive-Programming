# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lengthNodeA = 0
        lengthNodeB = 0
        tempA = headA
        tempB = headB
        while tempA:
            lengthNodeA += 1
            tempA = tempA.next
        while tempB:
            lengthNodeB += 1
            tempB = tempB.next
        while lengthNodeA > lengthNodeB:
            lengthNodeA -= 1
            headA = headA.next
        while lengthNodeB > lengthNodeA:
            lengthNodeB -= 1
            headB = headB.next
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
        
        
            
        