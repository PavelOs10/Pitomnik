class Counter:
    def __init__(self):
        self.count = 0
        self.closed = False
    
    def add(self):
        if self.closed:
            raise RuntimeError("Counter is closed")
        self.count += 1
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.closed = True
        if exc_type:
            raise
    
    def check(self):
        if not self.closed:
            raise RuntimeError("Counter was not properly closed")