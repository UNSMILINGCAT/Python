import unittest


class ArithTestSuper(unittest.TestCase):
    def setUp(self):
        print("这是setUp")

    def tearDown(self):
        print("结束时调用")


class ArithTest(ArithTestSuper):
    def runTest(self):
        """

        :return:
        """
        print("运行测试例子")
        self.failUnless(1 + 1 == 2, 'one plus one fails!')
        self.failIf(1 + 1 != 2, 'one plus one fails again!')
        self.failUnlessEqual(1 + 1, 2, 'more trouble with one plus one!')


class ArithTestFail(ArithTestSuper):
    def runTest(self):
        """

        :return:
        """
        print("运行测试失败")
        self.failUnless(1 + 1 == 2, 'one plus one fails!')
        self.failIf(1 + 1 != 2, 'one plus one fails again!')
        self.failUnlessEqual(1 + 1, 2, 'more trouble with one plus one!')
        self.failIfEqual(1 + 1, 2, 'expected failure here')
        self.failIfEqual(1 + 1, 2, 'second failure')


class ArithTest2(unittest.TestCase):
    def setUp(self):
        print("测试2的开始")

    def tearDown(self):
        print("测试2的结束")

    def runArithTest(self):
        """

        :return:
        """
        print("运行测试例子在测试2中")
        self.failUnless(1 + 1 == 2, 'one plus one fails')
        self.failIf(1 + 1 != 2, 'one plus one fails again')
        self.failUnlessEqual(1 + 1, 2, 'more trouble with one plus one')

    def runArithTestFail(self):
        """

        :return:
        """
        print("运行ArithTestFail在 ArithTest2")
        self.failUnless(1 + 1 == 2, 'one plus one fails')
        self.failIf(1 + 1 != 2, 'one plus one fails again')
        self.failUnlessEqual(1 + 1, 2, 'more trouble with one plus one')
        self.failIfEqual(1 + 1, 2, 'expected failure here')
        self.failIfEqual(1 + 1, 2, 'second failure')


def suite():
    suite = unittest.TestSuite()
    # 第一种样式
    suite.addTest(ArithTest())
    suite.addTest(ArithTestFail())
    # 第二种样式
    suite.addTest(ArithTest2("runArithTest"))
    suite.addTest(ArithTest2("runArithTestFail"))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
