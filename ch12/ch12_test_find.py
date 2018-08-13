import unittest
from ch12 import find
import os, os.path


def filename(ret):
    return ret[1]


class FindTest(unittest.TestCase):
    def setUp(self):
        os.mkdir("_test")
        os.mkdir(os.path.join("_test", "subdir"))
        f = open(os.path.join(("_test", "file1.txt")), "w")
        f.write("""第一行
        第二行
        第三行
        第四行""")
        f.closed()
        f = open(os.path.join("_test", "file2.py"), "w")
        f.write("""这是一个测试文件
        它包含了一些单词
        这里结束""")
        f.close()

    def tearDown(self):
        os.unlink(os.path.join("_test", "file1.txt"))
        os.unlink(os.path.join("_test", "file2.py"))
        os.rmdir(os.path.join("_test", "subdir"))
        os.rmdir("_test")

    def test_01_SearchAll(self):
        """

        :return:
        """
        res = find.find(r"*", start="_test")
        self.failUnless(map(filename, res) == ['file1.txt', 'file2.py'], 'wrong results')

    def test_02_SearchFileName(self):
        """

        :return:
        """
        res = find.find(r"file", start="_test")
        self.failUnless(map(filename, res) == ['file1.txt', 'file2.py'], 'wrong results')

if __name__ == '__main__':
    unittest.main()
