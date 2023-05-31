class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_s=root.val
        print(max_s)


        def mps(root):
            nonlocal max_s
            if root==None:
                return 0
            
            left=max(mps(root.left),0)
            right=max(mps(root.right),0)

            if left+right+root.val>max_s:
                max_s=max(left+right+root.val,root.val)
            return root.val+max(left,right)
        
        mps(root)
        return max_s