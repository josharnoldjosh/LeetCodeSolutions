class Solution:
    
    def trap(self, height, result = 0):
    
        left, right = [], []
        
        for idx, (i, j) in enumerate(zip(height, height[::-1])):
            if idx == 0: left.append(i); right.append(j); continue
            if i > left[idx-1]: left.append(i)
            else: left.append(left[idx-1])                
            if j > right[idx-1]: right.append(j)
            else: right.append(right[idx-1])
                
        for idx, (i, j) in enumerate(zip(left, right[::-1])):
            result += min(i, j) - height[idx]
            
        return result
        
