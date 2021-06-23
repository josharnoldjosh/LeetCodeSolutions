class Solution:
    def thousandSeparator(self, n: int) -> str: 
        return f"{n:,}".replace(',', '.')
    
"""
One line:
```python
return "".join([str(n)[::-1][i:i+3]+"." for i in range(0, len(str(n)), 3)])[::-1][1:]
```

More readable:
```python
def thousandSeparator(n): 

    reversed_str = str(n)[::-1]
    chunk_size = 3
    result = ""

    for i in range(0, len(reversed_str), chunk_size):
        result += reversed_str[i:i+chunk_size] + "."

    return result[::-1][1:]
```
"""
        