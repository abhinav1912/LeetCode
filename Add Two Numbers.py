# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x, y, carry, prev = l1, l2, 0, None
        if not l1:
            return l2
        if not l2:
            return l1
        while x and y:
            x.val += y.val + carry
            if x.val > 9:
                x.val %= 10
                carry = 1
            else:
                carry = 0
            prev = x
            x = x.next
            y = y.next
        while x:
            x.val += carry
            if x.val > 9:
                x.val %= 10
                carry = 1
            else:
                carry = 0
            prev = x
            x = x.next
        if y:
            prev.next = y
        while y:
            y.val += carry
            if y.val > 9:
                y.val %= 10
                carry = 1
            else:
                carry = 0
            prev = y
            y = y.next
        if carry:
            prev.next = ListNode(1, None)
        return l1
