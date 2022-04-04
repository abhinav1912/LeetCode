# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count, curr, n1 = 0, head, None
        while curr:
            count += 1
            if count == k:
                n1 = curr
            curr = curr.next
        curr = head
        n = count
        count = 0
        while curr:
            count += 1
            if count == n-k+1:
                curr.val, n1.val = n1.val, curr.val
                break
            curr = curr.next
        return head
