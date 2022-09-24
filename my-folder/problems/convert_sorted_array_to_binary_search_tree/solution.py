# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(l,r):
            if l>r:
                print("returning none")
                return None
                
            m=(l+r)//2
            print("lmr:"+str(l)+str(m)+str(r))

            
            print("entering root"+str(l)+str(m)+str(r))
            root=TreeNode(nums[m])
            print(root)
            
            print("entering left m:"+str(l)+str(m)+str(r))
            root.left=helper(l,m-1)
            
            print("entering right l,m,r:"+str(l)+str(m)+str(r))
            root.right=helper(m+1,r)
            
            print("returning root"+str(l)+str(m)+str(r))
            return root
        
        print("returning helper")
        return helper(0,len(nums)-1)

