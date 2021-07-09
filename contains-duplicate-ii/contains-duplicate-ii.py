class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # O(n)
        counts = collections.Counter(nums)
        nums = [(idx, i) for idx, i in enumerate(nums) if counts[i] > 1]
        graph = collections.defaultdict(list)        
        for item in nums: graph[item[-1]].append(item)
                        
        for arr in graph.values():
            for i in range(len(arr)-1):
                for j in range(i+1, len(arr)):
                    if abs(arr[i][0]-arr[j][0]) > k: continue                    
                    return True
              
        return False
            