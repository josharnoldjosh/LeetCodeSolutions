class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        non_symmetric = {'2', '4', '7'}
        graph = {
            '1': '1',
            '2': '#',
            '3': '#',
            '4': '#',
            '5': '#',
            '6': '9',
            '7': '#',
            '8': '8',
            '9': '6',
            '0': '0'
        }
        
        result = ""
        
        for c in num:
            result += graph[c]
            
        return result[::-1] == num
            