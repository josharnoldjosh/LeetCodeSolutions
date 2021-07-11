class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        f = lambda x: [list(group) for c, group in itertools.groupby(x)]
        name, typed = f(name), f(typed)
        if len(name) != len(typed): return False
        for i in range(len(name)):
            if not (name[i][0] == typed[i][0] and len(name[i]) <= len(typed[i])):
                return False
        return True
        
        
        