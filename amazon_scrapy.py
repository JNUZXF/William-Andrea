
import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random
import os
import pandas as pd
import gc

def MakePath(path):
    # 引入模块
    import os
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        # print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建,并提示目录已存在
        # print(path + ' 目录已存在')
        return False


options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9999")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
driver = webdriver.Chrome(options = chrome_options)

#输入要打开的网址
driver.switch_to.new_window('tab')
driver.get("https://www.amazon.de/gp/bestsellers/industrial/6589299031/ref=pd_zg_hrsr_industrial")
time.sleep(1)
st = time.time()
com_name = driver.find_element(By.XPATH, '''//*[@id="B071DM81ZK"]/a[2]/span/div''').text
com_name

'''
比较关注的几个信息：
上架时间，评价数量，星级，售价，排名，历史销售数据，增长趋势，
什么产品，产品规格（尺寸，重量等），卖家所在国家等
'''

'''
一款功能强大且操作简单的亚马逊选品工具，
帮助卖家实现一键查看现有产品的所有销售数据表现。
替代传统的选品插件，实现高效的数据挖掘，助力卖家快速且精准地选出心仪的产品。
'''






