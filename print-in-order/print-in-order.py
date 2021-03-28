class Foo:
    
    def __init__(self):
        self.called = set([1, 2, 3])


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.called.remove(1)


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        while 1 in self.called: pass                                    
        printSecond()
        self.called.remove(2)


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        while 2 in self.called: pass                                    
        printThird()
        self.called.remove(3)
        
"""
the method tells us which blah...
- do we block, or enqueue
"""