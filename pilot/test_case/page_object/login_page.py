# -*- coding: utf-8 -*-

from time import sleep
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from pilot.test_case.page_object.page import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage(Page):

    url = 'login/'
    username_loc = (By.ID, "username")                                         #用户名定位
    password_loc = (By.ID, "password")                                        #密码定位
    submit_loc = (By.CSS_SELECTOR, "input.btn")                                #登录按钮定位

    #打开登录页面
    def open(self):
        self._open(self.url)
    #pilot登录操作
    def pilot_login(self, username, password):
        try:
            #输入用户名
            input_usr = self.wait(EC.presence_of_element_located(self.username_loc))
            input_usr.clear()
            input_usr.send_keys(username)
            #输入密码
            input_pwd = self.wait(EC.presence_of_element_located(self.password_loc))
            input_pwd.clear()
            input_pwd.send_keys(password)
            #点击提交
            submit = self.wait(EC.element_to_be_clickable(self.submit_loc)).click()
        except TimeoutException:
            print('timeout')

    def login_start(self, username, password):
        self.open()
        self.pilot_login(username, password)





'''
if __name__ == '__main__':
    driver = webdriver.Firefox()
    lo = LoginPage(driver)
    lo.open()
    lo.pilot_login('admin','123456')
    driver.close()
'''




