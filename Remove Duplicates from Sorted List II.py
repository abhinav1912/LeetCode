# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy_node = ListNode(None, head)
        slow_ptr, fast_ptr = dummy_node, head
        
        while fast_ptr:
            if fast_ptr.next and fast_ptr.val == fast_ptr.next.val:
                curr_val = fast_ptr.val
                while fast_ptr.next and fast_ptr.next.val == curr_val:
                    fast_ptr = fast_ptr.next
                slow_ptr.next = fast_ptr.next
            else:
                slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        return dummy_node.next
