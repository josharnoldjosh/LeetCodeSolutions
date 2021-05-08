# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummy = cur = ListNode()
        
        carry = 0
        
        while l1 or l2 or carry:            
                        
            val, carry = carry, 0
                        
            if l1:
                val += l1.val
                l1 = l1.next
                
            if l2:
                val += l2.val
                l2 = l2.next
                       
            if val >= 10:
                carry = 1
                val -= 10
                    
            cur.next = ListNode(val)
            cur = cur.next
        

        return dummy.next
    
"""
001
001
---
002
"""