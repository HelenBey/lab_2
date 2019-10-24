import time

class timer():
    def __enter__(self):
        self.start = time.monotonic();
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.monotonic()
        print(self.end - self.start)
