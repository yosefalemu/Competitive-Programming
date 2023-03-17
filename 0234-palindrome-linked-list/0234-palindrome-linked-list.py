# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        leftpt = 0
        rigthpt = len(temp) - 1
        while leftpt < rigthpt:
            if temp[leftpt] != temp[rigthpt]:
                return False
            leftpt += 1
            rigthpt -= 1
        return True
        