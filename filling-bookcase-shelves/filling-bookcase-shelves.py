class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:        
        
        @functools.lru_cache(None)
        def recurse(idx, row_width, row_height):
            if row_width > shelf_width: return float('inf')
            if idx >= len(books): return row_height
            w, h = books[idx]
            this_row = recurse(idx+1, row_width+w, max(row_height, h))
            next_row = row_height + recurse(idx+1, w, h)
            return min(this_row, next_row)
        
        return recurse(0, 0, 0)
        
        
        
    
"""
Actions:
- place book on current shelf
- place book on next shelf

- ask for forgiveness rather than permission
"""