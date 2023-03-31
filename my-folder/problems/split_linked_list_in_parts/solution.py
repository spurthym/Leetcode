class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        temp = head
        c = 0
        while temp:
            c += 1
            temp = temp.next

        each_s = c // k
        rem = c % k

        res = []
        t1 = head

        for i in range(k):
            res1 = ListNode(0)
            tail = res1
            for j in range(each_s + (i < rem)):
                if t1:
                    tail.next = ListNode(t1.val)
                    t1 = t1.next
                tail = tail.next
            res.append(res1.next)

        return res