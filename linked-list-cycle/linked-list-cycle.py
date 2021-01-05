class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        
        p1, p2 = head, head.next
        
        while p1 != p2:
            try:
                p1 = p1.next
                p2 = p2.next.next
            except:
                return False
                            
        return True
