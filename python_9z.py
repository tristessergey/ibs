from threading import Thread
from time import sleep
class qq(Thread):
    def __init__(self, limit):
        Thread.__init__(self)
        self._limit = limit
    def run(self):
        while self._limit > 0:
            print(f"qq {self._limit}")
            self._limit -= 1
            sleep(1)

class qw(Thread):
    def __init__(self, limit):
        Thread.__init__(self)
        self._limit = limit
    def run(self):
        while self._limit > 0:
            print(f"qw {self._limit}")
            self._limit -= 1
            sleep(1)
cth = qq(10)
qqq = qw(10)
cth.start()
qqq.start()
