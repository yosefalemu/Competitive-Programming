# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.sum = root.val
        def maxHelper( root: Optional[TreeNode]) -> int:
            l, r = 0, 0
            if root.left != None:
                l += maxHelper(root.left)
            if root.right != None:
                r += maxHelper(root.right)

            sum1, sum2 = root.val, root.val
            if l > 0:
                sum1 += l
            if r > 0:
                sum1 += r
            
            if l > 0 or r > 0:
                sum2 += l if l > r else r

            self.sum = sum2 if self.sum < sum2 else self.sum
            self.sum = sum1 if self.sum < sum1 else self.sum
            return sum2
        if root:
            maxHelper(root)
        return self.sum
        