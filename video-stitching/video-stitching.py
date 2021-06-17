class Solution:
    def videoStitching(self, clips, T):
                
        a, b, count = -1, 0, 0
                
        for i, j in sorted(clips):
                        
            if i > b or b >= T: break
                            
            if a < i <= b:
                a, count = b, count + 1
                            
            b = max(b, j)             
            
        return count if b >= T else -1
    
    
    """
    def videoStitching(clips, T):
	
	
		
		
		
	
    """
    
    
#     def videoStitching(self, clips: List[List[int]], time: int) -> int:
                        
#         cur_end, limit, count = -1, 0, 0
        
#         for i, j in sorted(clips):
            
#             # There is a gap, or we've succeeded
#             if i > limit or i >= time:
#                 break
            
#             # Should we "merge" this interval, or "absorb" it?
#             if cur_end < i <= limit:    
#                 cur_end = limit
#                 count += 1
            
#             limit = max(limit, j)
                
#         return count if limit >= time else -1
        
        
    
"""
First idea, basically a BFS where we try multiple options! (Unfortuntely it TLE's)

```python
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
            
        clips.sort()
                
        queue = collections.deque([([0, 0], 0, -1, 0)])
                
        while len(queue) > 0:
                                   
            clip, max_start, ignore, score = queue.popleft()
                                    
            if clip[-1] >= T: return score
            
            for idx, (a, b) in enumerate(clips):   
                if idx <= ignore: continue
                if a <= max_start:
                    queue.append(
                        (
                            [clip[0], max(clip[1], b)],
                            b,
                            idx,
                            score + 1
                        )
                    )
                                            
        return -1
```
"""