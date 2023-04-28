class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = 0

        def sumroot(root, val):
            nonlocal res
            if not root:
                return
            if root.left==None  and root.right==None:
                
                val = val * 2 + root.val
                
                res += val
                return
            val = val * 2 + root.val
            sumroot(root.left, val)
            sumroot(root.right, val)

        sumroot(root, 0)
        return res