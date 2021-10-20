# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        traverse_count = 0
        while head:
            if traverse_count < m-1:
                traverse_count += 1
            else:
                delete_count = 0
                while delete_count < n and head.next:
                    head.next = head.next.next
                    delete_count += 1
                traverse_count = 0
            head = head.next
        return dummy.next