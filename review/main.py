import unittest
from HTMLTestRunner import HTMLTestRunner

discover = unittest.TestLoader().discover(
    start_dir=r'C:\Users\Administrator\PycharmProjects\practice\review',
    pattern='test*.py',
    top_level_dir=None
)
print('*****', discover)


if __name__ == '__main__':

    #1-先定义一个报名名称
    report =r'C:\Users\Administrator\PycharmProjects\practice\review'+ '\\'+  'report.html'

    #2-打开文件，准备写入
    fp = open(report,'wb')
    #实例化测试报告
    runner = HTMLTestRunner(stream=fp,
                            title='单元测试报告',
                            description='测试用例详情'
                            )
    #运行测试用例集
    runner.run(discover)
    #关闭报告
    fp.close()