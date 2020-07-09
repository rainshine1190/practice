
import unittest
from HTMLTestRunner import HTMLTestRunner
import time

def creatReport(suite,name):

    print('suite********',suite,name)

    #报告
    timestr = str(time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime(time.time())))
    # print(timestr)
    fname = name + '_' + 'report.html'
    print(fname)
    file = open(fname,'wb')

    runner = HTMLTestRunner(stream=file,description='Myreport1',title='test report')
    runner.run(suite)


    file.close()


if __name__ == '__main__':
    pass