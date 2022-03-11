# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        n, curr = 0, head
        while curr:
            curr = curr.next
            n += 1
        k = k%n
        if not k:
            return head
        x = n-k-1
        curr = head
        while x:
            curr = curr.next
            x -= 1
        temp = curr.next
        curr.next = None
        curr = temp
        while curr.next:
            curr = curr.next
        curr.next = head
        return temp
