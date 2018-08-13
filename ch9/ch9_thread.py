import math
from threading import Thread
import time


class SquareRootCalculator:
    """

    """

    def __init__(self, target):
        """

        :param target:
        """
        self.results = []
        counter = self.CalculatorThread(self, target)
        print("线程运行中")
        counter.start()
        while len(self.results) < target:
            print("%d " % len(self.results))
            time.sleep(1)
        print("")

    class CalculatorThread(Thread):
        """

        """

        def __init__(self, controller, target):
            """

            :param controller:
            :param target:
            """
            Thread.__init__(self)
            self.controller = controller
            self.target = target
            self.setDaemon(True)

        def run(self):
            """

            :return:
            """
            for i in range(1, self.target + 1):
                self.controller.results.append(math.sqrt(i))


if __name__ == '__main__':
    import sys

    limit = None
    if len(sys.argv) > 1:
        limit = sys.argv[1]
        try:
            limit = int(limit)
        except ValueError:
            print("错误")
# SquareRootCalculator(limit)
help(SquareRootCalculator)
