# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = deque()
        q.append(root)
        level = 0

        while q:
            temp = []
            level_size = len(q)  # Get the number of nodes in the current level

            if level % 2 == 0:
                for i in range(level_size):
                    curr = q.popleft()
                    temp.append(curr.val)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
            else:
                for i in range(level_size):
                    curr = q.pop()
                    temp.append(curr.val)
                    if curr.right:
                        q.appendleft(curr.right)
                    if curr.left:
                        q.appendleft(curr.left)

            level += 1
            res.append(temp)

        return res
