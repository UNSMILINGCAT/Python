import sys


def name():
    if True:
        print(__name__)


def name_r():
    name()


name_r()
# print(list(sys.modules.keys()))
