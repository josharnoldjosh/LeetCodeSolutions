class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:        
        
        @functools.lru_cache(maxsize=None)
        def recurse(i, width, height):            
            if width < 0: return float('inf')
            if i >= len(books): return height
            w, h = books[i]
            add_to_cur_row = recurse(i+1, width-w, max(height, h))
            start_new_row = height + recurse(i+1, shelf_width-w, h)
            return min(add_to_cur_row, start_new_row)
        
        return recurse(0, shelf_width, 0)