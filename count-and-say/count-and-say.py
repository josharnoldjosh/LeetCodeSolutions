class Solution:
    def countAndSay(self, n: int) -> str:
        
        def build(text):          
            """Does the 'count and say' for a given str."""
            data, result = [[None]], ""
            
            # Split by unique contiguous occurances
            # e.g, [[1,1,1], [2,2,2,], [3]]
            for i in text:
                if i == data[-1][-1]: data[-1].append(i)
                else: data.append([i])
                     
            # Append into one string
            # e.g, 313213
            for i in data[1:]:
                result += f"{len(i)}{i[0]}"                
                
            return result
                    
        
        ans = "1"
        
        for _ in range(n-1):
            ans = build(ans)
            
        return ans
