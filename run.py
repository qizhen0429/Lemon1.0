

from selenium import webdriver
from ui_web.common import web_ui   # 导入ui_web.common文件夹下的web_ui文件
from ui_web.test_data import web_data   # 导入测数据文件

driver = webdriver.Chrome()
driver.implicitly_wait(10)

'''通过字典取值，读取数据'''
url = web_data.data["url"]
username = web_data.data["username"]
password = web_data.data["password"]
s_key = web_data.data["s_key"]


'''调用查询函数'''
result_unm = web_ui.serch_key(driver=driver,url=url,username=username,password=password,s_key=s_key)

if s_key in result_unm:
    print('这条用例通过')
else:
    print('这条用例不通过')



