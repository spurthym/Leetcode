class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root or (not root.left and not root.right):
            return root
        
        if root.left and root.right:
            root.left.next = root.right
            root.right.next = self.get_next_has_children_node(root)
        
        if root.left is None:
            root.right.next = self.get_next_has_children_node(root)
        
        if root.right is None:
            root.left.next = self.get_next_has_children_node(root)
        
        root.right = self.connect(root.right)
        root.left = self.connect(root.left)
        
        return root
    
    def get_next_has_children_node(self, root: 'Node') -> 'Node':
        while root.next:
            if root.next.left:
                return root.next.left
            if root.next.right:
                return root.next.right
            root = root.next
        
        return None
