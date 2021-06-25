class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
                
        def match(i):
            queue = collections.deque([c for c in pattern])
            for c in i:
                if queue and c == queue[0]:
                    queue.popleft()
                elif c.isupper():
                    return False
                else:
                    continue
            return not queue
                
        return [
            True
            if match(i)
            else False
            for i in queries
        ]
    
"""
BarFoo

FooBar
FoBa

"""