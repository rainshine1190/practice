from selenium import webdriver
import time,logging,unittest

from work.case.create import creatReport

class myTest2(unittest.TestCase):


    def testB1(self):
        driver = webdriver.Chrome()
        driver.get('http://www.taobao.com')
        driver.maximize_window()
        # time.sleep(15)

        # logging.info('执行testA结束')
        driver.quit()

    def testB2(self):
        driver = webdriver.Chrome()
        driver.get('http://www.hao123.com')
        driver.maximize_window()
        # time.sleep(15)

        # logging.info('执行testA结束')
        driver.quit()

if __name__ == '__main__':
    suite = unittest.makeSuite(myTest2)
    creatReport(suite)