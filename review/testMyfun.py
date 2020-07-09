
import unittest
from myfun import *
from HTMLTestRunner import HTMLTestRunner
# import HTMLTestRunner

class testMyfun(unittest.TestCase):

    def setUp(self) -> None:
        print('我是setUp')

    def tearDown(self) -> None:
        print('我是tearDown')

    # @unittest.skip('跳过')
    def test_add1(self):
        '''testadd1'''
        print('testadd1')
        result = add(1,2)
        expect = 3
        self.assertEqual(result,expect)

    def test_add2(self):
        '''testadd2'''
        print('testadd2')
        result = add(-1, 2)
        expect = 1
        self.assertEqual(result, expect)



if __name__ == '__main__':
    #1----------默认运行全部的测试用例
    unittest.main()

    # #2----------通过创建测试套件的用法
    # #1-实例化testsuite
    # suite = unittest.TestSuite()
    # #2-添加目标测试用例到测试用例集
    # suite.addTest(testMyfun('test_add1'))
    # suite.addTest(testMyfun('test_add2'))
    # runner = unittest.TestRunner()
    # runner.run(suite)


    # #3-----------通过discover方法
    # #1-实例化了testsuite；2-添加符合条件的测试用例到测试用例集
    # discover = unittest.defaultTestLoader.discover()
    # runner = unittest.TestRunner()
    # runner.run(discover)


    #报告
    # # #1-实例化testsuite
    # suite = unittest.TestSuite()
    # # #2-添加目标测试用例到测试用例集
    # suite.addTest(testMyfun('test_add1'))
    pass

