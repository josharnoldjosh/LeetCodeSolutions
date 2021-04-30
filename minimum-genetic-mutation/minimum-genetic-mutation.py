class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        def is_mutation(s, e):
            s = collections.Counter([(i, c) for i, c in enumerate(s)])
            e = collections.Counter([(i, c) for i, c in enumerate(e)])
            return sum(((s | e) - (s & e)).values()) == 2
        
        queue = collections.deque([(start, 0, bank)])
        seen = set()        
        
        while queue:
            s, num_mutations, bnk = queue.popleft()
            if s == end:
                return num_mutations
            for i in bnk:
                if is_mutation(s, i):
                    queue.append((i, num_mutations+1, [j for j in bnk if j != i]))
            
        return -1