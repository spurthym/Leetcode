class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break

        if not fast or not fast.next:
            return None

        # Reset one pointer to the head and move both pointers at the same speed
        # until they meet at the cycle's starting point (entry node).
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast
