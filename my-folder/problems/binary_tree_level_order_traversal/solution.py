# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        q=deque()
        res=[]
        def bfs(root):
            if not root:
                return
            
            q.append(root)
            
            while q:
                qlen=len(q)
                curr_level=[]

                for _ in range(qlen):
                    curr_node=q.popleft()

                    curr_level.append(curr_node.val)
                    if curr_node.left:
                        q.append(curr_node.left)
                    if curr_node.right:
                        q.append(curr_node.right)
                res.append(curr_level)
        bfs(root)
        return res
