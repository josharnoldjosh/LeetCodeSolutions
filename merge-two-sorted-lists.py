# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
​
​
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        
        dummy = head = ListNode()
        
        data = []
        
        while l1:
            data.append(l1.val)
            l1 = l1.next
            
        while l2:
            data.append(l2.val)
            l2 = l2.next
            
        data.sort()
        
        while data:
            x = data.pop(0)
            head.next = ListNode(x)
            head = head.next
            
            
        return dummy.next
            
    
    
"""
​
some case:
​
- first list is sequential, and second list just continues after the first list
    - first list cycle to end and append second list
    
- first list interweaves with second
    - interweave them
​
"""
        
                
                
