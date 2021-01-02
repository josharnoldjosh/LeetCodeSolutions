class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        
        result = ""
        
        for i in range(0, min(map(len, strs))):
            if all(x[i] == strs[0][i] for x in strs):
                result += strs[0][i]
            else:
                break
                
        return result            
