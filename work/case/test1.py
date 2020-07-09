from selenium import webdriver
import time
import unittest,os

from threading import Thread
from HTMLTestRunner import HTMLTestRunner
from work.case.create import creatReport

class myTest1(unittest.TestCase):


    def testA1(self):
        driver = webdriver.Chrome()
        driver.get('http://www.baidu.com')
        driver.maximize_window()
        # time.sleep(15)

        # logging.info('执行testA结束')
        driver.quit()

    def testA2(self):
        driver = webdriver.Chrome()
        driver.get('http://www.xiaomi.com')
        driver.maximize_window()
        # time.sleep(15)

        # logging.info('执行testA结束')
        driver.quit()

if __name__ == '__main__':
    suite = unittest.makeSuite(myTest1)

    reprot_name = os.path.split(__file__)[1].strip('.py')
    # print('****', name)
    creatReport(suite,reprot_name)
