class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def l(head):
            c = 0
            while head:
                c += 1
                head = head.next
            return c
        m,n = l(headA), l(headB)
        x = abs(m-n)
        if m > n:
            for i in range(x):
                headA = headA.next
        elif n > m:
            for i in range(x):
                headB = headB.next
        for i in range(min(m,n)):
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
