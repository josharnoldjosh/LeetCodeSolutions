class MovingAverage:

    def __init__(self, size: int):
        self.sum = 0
        self.size = size
        self.queue = collections.deque([])

    def next(self, val: int) -> float:
        self.sum += val
        self.queue.append(val)
        
        while len(self.queue) > self.size:
            self.sum -= self.queue.popleft()
            
        return self.sum / min(self.size, len(self.queue))
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)