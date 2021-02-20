class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
                        
        queue = collections.deque([])        
        window = set()
        result = 0
        pointer = 0
        
        while pointer < len(s):
            
            c = s[pointer]
            
            if c in window:
                while queue:
                    prev = queue.popleft()
                    window.remove(prev)
                    if prev == c:
                        break
                
            window.add(c)
            queue.append(c)
            result = max(result, len(window))
            pointer += 1
            
        return result
                
            
            
        
        
    
"""
- try every substring via recursion
- counter, most common
- record length...

T(n) = 2*T(n -1) + n
= 2^(n-1)*n = 2^n

----

set expansion?
- start at each character
- try to expand right?
- stop if existing character is found?

aaaaaaaaaa -> O(n)

abcdefg -> n^2 runtime

----

sliding window

start adding to a queue,
- when existing value is encountered, pop queue until value gone and add new value?
- use a set to make it fast
-> O(n)??

abca
"""