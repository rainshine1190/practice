
from appium import webdriver
import time,os



def starUp():


    desire_caps = {
      "deviceName": "D5F7N18313000594",
      "platformName": "Android",
      "platformVersion": "10",
      "appPackage": "com.ss.android.article.news",
      "appActivity": "com.ss.android.article.news.activity.MainActivity",
      "noReset": True,
      "unicodeKeyboard": True
    }


    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desire_caps)


    time.sleep(10)


    #1-定位目标元素，操作目标元素
    driver.find_element_by_id("com.ss.android.article.news:id/c4c").click()

    # driver.find_element_by_android_uiautomator(new UiSelector.text("发布"))[0].click()




    driver.close()



starUp()