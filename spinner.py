import sys
import time
import threading

class spinner:
    def __init__(self, message="Loading"):
        self.message = message
        self._stop = False
        self._chars = ['/', '-', '\\', '|']
        
    def s1(self):
        i = 0
        while not self._stop:
            sys.stdout.write(f"\r{self.message} {self._chars[i % len(self._chars)]}")
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1
        sys.stdout.write("\r" + " " * (len(self.message) + 2) + "\r")
        
    def __enter__(self):
        self._thread = threading.Thread(target=self.s1)
        self._thread.start()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._stop = True
        self._thread.join()
