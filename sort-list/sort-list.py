# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        sorted_values = []
        
        while head:
            sorted_values.append(head.val)
            head = head.next
            
        dummy = res = ListNode()    
        
        for i in sorted(sorted_values):
            res.next = ListNode(i)
            res = res.next
                                
        return dummy.next
            
        
        
        
    
"""
4,2,1,3
2,4,1,3
2,1,4,3
2,1,3,4
1,2,3,4
"""