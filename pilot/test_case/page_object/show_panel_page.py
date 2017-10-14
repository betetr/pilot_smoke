from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from pilot.test_case.page_object.page import Page
from pilot.test_case.page_object.login_page import LoginPage
from pilot.test_case.model.function import insert_img
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

class show_all_panel(Page):
    url = 'dashboard/list/'
    get_page_num_loc = (By.XPATH, '//div[@class="panel-bottom"]/ul/li')
    get_table_num_loc = (By.CSS_SELECTOR, '.ant-table-row')
    page_next_loc = (By.CSS_SELECTOR, '.ant-pagination-next')
    table_loc = 'tr.ant-table-row:nth-child(%s) > td:nth-child(3) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)'
    page_num_loc = 'li.ant-pagination-item:nth-child(%s)'
    tiao_loc = (By.CSS_SELECTOR, '.ant-pagination-options-quick-jumper > input:nth-child(1)')
    highl_loc = (By.CSS_SELECTOR, 'li.ant-pagination-item:nth-child(5)')

    def open(self):
        self._open(self.url)

    def get_highl(self, page_number):
        locate = 'li.ant-pagination-item:nth-child(%s)' % str(page_number+1)
        highl_loc = (By.CSS_SELECTOR, locate)
        return highl_loc

    def get_table_loc(self, num):
        locate_table = self.table_loc % str(num)
        table_l = (By.CSS_SELECTOR, locate_table)
        return table_l

    def next_page(self, page_number):
        self.open()
        sleep(0.5)
        input_num = self.wait(EC.presence_of_element_located(self.tiao_loc))
        input_num.clear()
        input_num.send_keys(page_number)
        input_num.send_keys(Keys.ENTER)
        try:
            self.wait(EC.text_to_be_present_in_element(self.get_highl(page_number), str(page_number)))
        except TimeoutException:
            pass

    def show_all(self):
        cs = 1
        num = 0
        # 获取页数
        page_ele = self.find_elements(*self.get_page_num_loc)
        page_num_all = len(page_ele)
        #print(page_num_all)
        for page_num in range(1, page_num_all-1):
            self.next_page(page_num)
            sleep(0.1)
            # 获取每页工作表数量
            table_ele = self.find_elements(*self.get_table_num_loc)
            table_num = len(table_ele) + 1
            #print(table_num)
            try:
                for i in range(1, table_num):
                    self.wait(EC.element_to_be_clickable(self.get_table_loc(i))).click()
                    sleep(5)
                    file_name = '%s_panel%s.png' % (str(cs), str(num))
                    insert_img(self.driver, file_name)
                    num += 1
                    self.back()
                    self.next_page(page_num)
            except TimeoutException:
                pass
        self.open()


    def show_PANEL(self):
        self.open()
        self.show_all()


'''

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    login_o = LoginPage(driver)
    login_o.open()
    login_o.pilot_login('admin','123456')
    show_all = show_all_panel(driver)
    show_all.open()
    show_all.show_all(2)
    sleep(2)
    driver.close()
    /home/lc/PycharmProjects/pilot_smoke/pilot/upload_image
'''
