class Counter:
    def init(self):
        self.count = 0
        self.closed = False

    def add(self):
        if self.closed:
            raise RuntimeError("Counter is closed")
        self.count += 1

    def enter(self):
        return self

    def exit(self, exc_type, exc_val, exc_tb):
        self.closed = True
        if exc_type:
            raise

    def check(self):
        if not self.closed:
            raise RuntimeError("Counter was not properly closed")