# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        deq = deque()
        deq.append(root)
        ans = []
        while deq:
            s = 0
            n = len(deq)
            for i in range(n):
                k = deq.popleft()
                s += k.val
                if k.right: deq.append(k.right)
                if k.left: deq.append(k.left)
            ans.append(s/n)
        return ans