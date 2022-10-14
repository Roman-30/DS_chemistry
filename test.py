from threading import Thread
from time import sleep


class CustomThread(Thread):
    def __init__(self, limit):
        Thread.__init__(self)
        self._limit = limit

    def run(self):
        for i in range(10000000):
            inw = i * 0.001
        print(self._limit)


cth = CustomThread(0)
cth1 = CustomThread(1)
cth2 = CustomThread(2)
cth.start()
cth1.start()
cth2.start()

