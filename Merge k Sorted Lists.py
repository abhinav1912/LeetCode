# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return self.merge(lists[0], lists[1])
        l, r = self.mergeKLists(lists[0:len(lists)//2]), self.mergeKLists(lists[len(lists)//2:])
        return self.merge(l, r)
    
    def merge(self, ll, rl):
        p = ListNode()
        d = p
        l, r = ll, rl
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r
        return d.next
