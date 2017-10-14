# coding = utf-8
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from pilot.test_case.page_object.page import Page
from pilot.test_case.page_object.login_page import LoginPage
from pilot.test_case.model.function import insert_img
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class Create_Conn(Page):
    url = 'database/list/'
    #inceptor_name = 'test-inceptor927'
    inceptor_str = 'inceptor://hive:123456@172.16.1.198:10000/default'
    inceptor_conn_str = '{"connect_args": {"framed": 0,"hive": "Hive Server 2","mech": "LDAP"}}'

    source_data_loc = (By.CSS_SELECTOR, 'li.dropdown:nth-child(4) > a:nth-child(1)')
    link_loc = (By.CSS_SELECTOR, 'li.dropdown:nth-child(4) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)')
    add_link_loc = (By.CSS_SELECTOR, '.icon-plus')
    inceptor_loc = (By.CSS_SELECTOR, '.selection-section > ul:nth-child(1) > li:nth-child(1)')
    inceptor_name_loc = (By.CSS_SELECTOR, '.popup-body > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)')
    inceptor_str_loc = (By.CSS_SELECTOR, '.popup-body > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > input:nth-child(1)')
    inceptor_conn_loc = (By.CSS_SELECTOR, '.popup-body > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > textarea:nth-child(1)')
    dialog_top_loc = (By.CSS_SELECTOR, '.popup-header')
    test_conn_loc = (By.CSS_SELECTOR, '.test-connect')
    confirm_loc = (By.CSS_SELECTOR, '.tp-btn')
    delete_conn_loc = (By.CSS_SELECTOR, 'tr.ant-table-row:nth-child(1) > td:nth-child(6) > div:nth-child(1) > i:nth-child(3)')


    #打开创建连接页面
    def open(self):
        self._open(self.url)

    def create_conn(self,inceptor_name):
        cishu = 1
        self.move_to_element(*self.source_data_loc)     #鼠标悬停在数据源上
        self.wait(EC.element_to_be_clickable(self.link_loc)).click()  #点击‘连接’
        # 截取‘连接’页面图像
        file_name = '%s_conn1.png' % str(cishu)
        insert_img(self.driver, file_name)
        self.wait(EC.element_to_be_clickable(self.add_link_loc)).click() #点击添加连接按钮
        self.wait(EC.element_to_be_clickable(self.inceptor_loc)).click()  #选择添加inceptor连接
        #输入inceptor连接名字
        input_name = self.wait(EC.presence_of_element_located(self.inceptor_name_loc))
        input_name.clear()
        input_name.send_keys(inceptor_name)
        #输入新的连接字符串
        input_conn = self.wait(EC.presence_of_element_located(self.inceptor_str_loc))
        input_conn.clear()
        input_conn.send_keys(self.inceptor_str)
        #输入新的参数
        input_can = self.wait(EC.presence_of_element_located(self.inceptor_conn_loc))
        input_can.clear()
        input_can.send_keys(self.inceptor_conn_str)
        #点击测试连接
        self.wait(EC.element_to_be_clickable(self.test_conn_loc)).click()
        #点击确认
        try:
            self.wait(EC.element_to_be_clickable(self.confirm_loc)).click()
        except TimeoutException:
            self.wait(EC.element_to_be_clickable(self.confirm_loc)).click()
        #截取新建连接后的图像
        sleep(2)
        file_name = '%s_conn2.png' % str(cishu)
        insert_img(self.driver, file_name)
        #删除新建连接
        self.wait(EC.element_to_be_clickable(self.delete_conn_loc)).click()
        sleep(0.5)
        self.find_element(*self.dialog_top_loc).click()
        self.wait(EC.element_to_be_clickable(self.confirm_loc)).click()
        sleep(0.5)

    def connnect(self, inceptor_name):
        self.open()
        self.create_conn(inceptor_name)






'''
if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    login_o = LoginPage(driver)
    login_o.open()
    login_o.pilot_login('admin','123456')
    sleep(3)
    po_conn = Create_Conn(driver)
    #po_conn.open()
    po_conn.create_conn('1', 'test112')
    driver.close()



'''


