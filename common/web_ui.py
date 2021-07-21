

from selenium import webdriver
import time
driver = webdriver.Chrome()   # 启动浏览器
driver.implicitly_wait(10)    # 隐式等待10秒钟
'''打开网址封装函数'''
def open_url(driver,url):
    driver.get(url)   # 打开网址
'''登录封装函数'''
def login(driver,username,password):
    driver.find_element_by_id('username').send_keys(username)   # 输入登录账号
    driver.find_element_by_id('password').send_keys(password)   # 输入密码
    driver.find_element_by_id('btnSubmit').click()    # 点击登录按钮
'''查询零售出库封装函数'''
def serch_key(driver,url,username,password,s_key):
    open_url(driver,url)
    login(driver,username,password)
    ''' 输入单据编号，点击搜索 '''
    driver.find_element_by_xpath("//span[text()='零售出库']").click()
    time.sleep(2)
    driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@src="/pages/materials/retail_out_list.html"]'))
    driver.find_element_by_id('searchNumber').send_keys(s_key)
    driver.find_element_by_id("searchBtn").click()
    '''返回查询结果'''
    num = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]//div').text
    return num









