class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        pushed, popped = collections.deque(pushed), collections.deque(popped)
        
        stack = []
        
        while pushed or popped:
            try:
                while not stack or stack[-1] != popped[0]:
                    stack += [pushed.popleft()]
                stack.pop(), popped.popleft()   
            except:
                return False
        
        return True
                
                
    
    
"""
1,2,3,4,5
1,2,3,4,5
"""