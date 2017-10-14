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
from pilot.test_case.model import function

import time

class Create_Panel(Page):
    url = 'dashboard/list/'
    new_button_loc = (By.CSS_SELECTOR, '.icon-plus')
    title_loc = (By.CSS_SELECTOR, 'div.dialog-item:nth-child(1) > div:nth-child(2) > input:nth-child(1)')
    add_table_loc = (By.CSS_SELECTOR, '.ant-select-search__field')
    confirm_loc = (By.CSS_SELECTOR, '.tp-btn')
    dialog_top_loc = (By.CSS_SELECTOR, '.popup-header')
    delete_panel_loc = (By.CSS_SELECTOR, 'tr.ant-table-row:nth-child(1) > td:nth-child(7) > div:nth-child(1) > i:nth-child(3)')
    alert_loc = (By.CSS_SELECTOR, '.popup-content')
    alert_confirm_loc = (By.CSS_SELECTOR, '.tp-btn')

    def open(self):
        self._open(self.url)

    def create_p(self, panel_name):
        data = ['Average and Sum Trends', 'Parallel Coordinates', 'Life Expectancy VS Rural %', 'Energy Force Layout']
        sleep(2)
        # 截取创建前的工作表图像
        file_name = '1_panel.png'
        insert_img(self.driver, file_name)

        self.wait(EC.element_to_be_clickable(self.new_button_loc)).click()
        self.wait(EC.presence_of_element_located(self.title_loc)).send_keys(panel_name)
        for da in data:
            da_loc = self.wait(EC.presence_of_element_located(self.add_table_loc))
            da_loc.send_keys(da)
            da_loc.send_keys(Keys.ENTER)

        self.find_element(*self.dialog_top_loc).click()
        sleep(2)
        self.wait(EC.element_to_be_clickable(self.confirm_loc)).click()
        sleep(2)
        # 截取创建后的工作表图像
        file_name = '2_panel.png'
        insert_img(self.driver, file_name)

        self.wait(EC.element_to_be_clickable(self.delete_panel_loc)).click()
        sleep(0.5)
        self.find_element(*self.alert_loc).click()
        self.wait(EC.element_to_be_clickable(self.alert_confirm_loc)).click()
        sleep(1.5)
        # 截取删除后的工作表图像
        file_name = '3_panel.png'
        insert_img(self.driver, file_name)

    def create_PANEL(self, panel_name):
        self.open()
        self.create_p(panel_name)
        sleep(3)
        file_name = '%s_panel.png' % str(1)
        function.insert_img(self.driver, file_name)
        sleep(1)


'''

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    login_o = LoginPage(driver)
    login_o.open()
    login_o.login_action('admin','123456')
    sleep(3)
    po_pan = Create_Panel(driver)
    data = ['Average and Sum Trends', 'Parallel Coordinates', 'Life Expectancy VS Rural %', 'Energy Force Layout']
    panel_name ='test9227'
    po_pan.open()
    po_pan.create_p(panel_name, data)
    sleep(3)
    driver.close()
    /home/lc/PycharmProjects/pilot_smoke/pilot/report/image

'''




