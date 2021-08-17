class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        score, queue, seen = 0, collections.deque([]), set()
        
        for i in s:
            while i in seen:
                c = queue.popleft()
                seen.remove(c)
            queue.append(i)
            seen.add(i)
            score = max(score, len(queue))
                
        return score