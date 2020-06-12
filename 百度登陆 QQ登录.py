from selenium import webdriver
import time
import requests

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
driver.implicitly_wait(20)

driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text('QQ帐号').click()

#多窗口处理
#handle 窗口的句柄
handles = driver.window_handles
print(len(handles))

#跳转到第二窗口上面去
driver.switch_to.window(handles[1])

#跳转到frame中
driver.switch_to.frame('ptlogin_iframe')
#点击账号密码登录
driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').send_keys('QQ账号')
driver.find_element_by_id('p').send_keys('QQ密码')
driver.find_element_by_id('login_button').click()
