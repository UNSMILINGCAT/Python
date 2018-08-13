import os


def test():
    """
    测试函数
    :return:
    """
    path_tuple = os.path.split(os.getcwd())
    print(path_tuple)
    print(os.stat('.'))
    print(os.listdir('..'))

if __name__ == '__main__':
    test()
