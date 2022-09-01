# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def rec(r,val):
            if val<=r.val:
                self.ans +=1
            if r.left:
                rec(r.left,max(val,r.left.val))
            if r.right:
                rec(r.right,max(val,r.right.val))
        rec(root,root.val)
        return self.ans