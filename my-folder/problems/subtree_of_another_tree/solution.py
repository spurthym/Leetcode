class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
            
        def is_subtree_helper(root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
            if not root:
                return False
            if is_same_tree(root, sub_root):
                return True
            return is_subtree_helper(root.left, sub_root) or is_subtree_helper(root.right, sub_root)
        
        return is_subtree_helper(root, subRoot)
