from selenium import webdriver
import time

def fun():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.jianshu.com/p/c3cdd62435bc')

    title = driver.title
    print(title)
    time.sleep(5)

    driver.close()


fun()