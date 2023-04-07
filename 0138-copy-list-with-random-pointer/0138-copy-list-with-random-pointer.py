"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dict1 = {None:None}
        curr = head
        while curr:
            temp = Node(curr.val)
            dict1[curr] = temp
            curr = curr.next
        curr = head
        while curr:
            temp = dict1[curr]
            temp.next = dict1[curr.next]
            temp.random = dict1[curr.random]
            curr = curr.next
        return dict1[head]
            
            
        