class Solution:
    def __init__(self):
        self.map = {}

    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        res = []
        self.find(root, target)
        self.dfs(root, target, K, self.map[root], res)
        return res

    def find(self, root: TreeNode, target: TreeNode) -> int:
        if not root:
            return -1
        if root == target:
            self.map[root] = 0
            return 0
        left = self.find(root.left, target)
        if left >= 0:
            self.map[root] = left + 1
            return left + 1
        right = self.find(root.right, target)
        if right >= 0:
            self.map[root] = right + 1
            return right + 1
        return -1
    
    def dfs(self, root, target, K, length, res):
        if not root:
            return
        if root in self.map:
            length = self.map[root]
        if length == K:
            res.append(root.val)
        self.dfs(root.left, target, K, length + 1, res)
        self.dfs(root.right, target, K, length + 1, res)
