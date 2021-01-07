# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        data = []
        
        while head:
            data.append(head.val)
            head = head.next
            
        N = len(data)
        
        if N % 2 == 0:
            print(data[:(N//2)], data[N//2:][::-1])
            return data[:N//2] == data[N//2:][::-1]
        
        return data[:N//2] == data[(N//2)+1:][::-1]
