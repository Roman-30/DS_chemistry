from threading import Thread
from services import expression


class CustomThread(Thread):
    def __init__(self, _from, to, arr, x, y):
        Thread.__init__(self)
        self._from = _from
        self.to = to
        self.arr = arr
        self.x = x
        self.y = y

    def run(self):

        num = self.x.shape[0] - 1
        num2 = 1

        x = self.x[num]
        y = self.y[num]

        x2 = self.x[num2]
        y2 = self.y[num2]

        y1_err = abs(y) * 0.99
        y2_err = abs(y2) * 0.99

        for i in range(self._from, self.to):
            for j in range(self._from, self.to):
                ans = abs(expression(i / 4, j / 4, x))
                ans2 = abs(expression(i / 4, j / 4, x2))

                if (y1_err < ans < abs(y)) and (
                        y2_err < ans2 < abs(y2)):
                    self.arr.append((i / 4, j / 4))
