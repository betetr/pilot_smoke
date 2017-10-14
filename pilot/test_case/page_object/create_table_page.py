# coding=utf-8
from time import sleep
from selenium.webdriver.common.by import By
from pilot.test_case.page_object.page import Page
from pilot.test_case.page_object.login_page import LoginPage
from pilot.test_case.model.function import insert_img
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Create_Table(Page):
    url = 'slice/list/'
    create_new_loc = (By.CSS_SELECTOR, ".icon-plus")
    source_data_s = (By.CSS_SELECTOR, "#datasource_id")
    table_type_loc = (By.CSS_SELECTOR, "#viz_type")
    pro_loc = (By.CSS_SELECTOR, "#groupby")
    clear_dul_moreng = (By.CSS_SELECTOR, "#s2id_metrics > ul:nth-child(1) > li:nth-child(1) > a:nth-child(2)")
    du_l_loc = (By.CSS_SELECTOR, "#metrics")
    qurey_loc = (By.CSS_SELECTOR, "#query_button")
    save_loc1 = (By.CSS_SELECTOR, "#save_button")
    name_loc = (By.CSS_SELECTOR, "#save_modal > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(2)")
    save_table_loc =(By.CSS_SELECTOR, "#btn_modal_save")
    dialog_loc = (By.CSS_SELECTOR, "#save_modal > div:nth-child(1) > div:nth-child(1)")
    delete_table_loc = (By.CSS_SELECTOR, 'tr.ant-table-row:nth-child(1) > td:nth-child(9) > div:nth-child(1) > i:nth-child(3)')
    alert_loc = (By.CSS_SELECTOR, '.popup-content')
    alert_confirm_loc = (By.CSS_SELECTOR, '.tp-btn')


    def open(self):
        self._open(self.url)

    def create_new(self):
        self.wait(EC.element_to_be_clickable(self.create_new_loc)).click() #点击新增工作表

    def set_source_data(self):
        sour = self.find_element(*self.source_data_s)           #设置源数据
        Select(sour).select_by_value('10')

    def set_table_type(self):
        type = self.wait(EC.presence_of_element_located(self.table_type_loc))          #设置图表类型
        Select(type).select_by_value('dist_bar')

    def set_pro(self):
        pro = self.wait(EC.presence_of_element_located(self.pro_loc))                #设置项目
        Select(pro).select_by_value('state')

    def set_duliang(self):
        self.wait(EC.element_to_be_clickable(self.clear_dul_moreng)).click()    #清理默认度量函数
        du_l = self.wait(EC.presence_of_element_located(self.du_l_loc))
        Select(du_l).select_by_value("sum__sum_girls")
        Select(du_l).select_by_value("sum__sum_boys")

    def qurey_save(self, cs, table_name):
        self.wait(EC.element_to_be_clickable(self.qurey_loc)).click()    #点击查询
        #截取查询后，新建图表图片
        file_name = '%s_dist_bar.png' % str(cs)
        insert_img(self.driver, file_name)
        self.wait(EC.element_to_be_clickable(self.save_loc1)).click()  #点击保存
        #输入图表名称
        input_name = self.wait(EC.presence_of_element_located(self.name_loc))
        input_name.clear()
        input_name.send_keys(table_name)
        self.wait(EC.element_to_be_clickable(self.save_table_loc)).click()        #点击保存图表

    #创建分布柱状图
    def dist_bars(self, table_name):
        cs = 1
        self.open()
        self.create_new()
        self.set_source_data()
        self.set_table_type()
        self.set_pro()
        self.set_duliang()
        self.qurey_save(cs, table_name)
        self.wait(EC.element_to_be_clickable(self.delete_table_loc)).click()
        sleep(0.5)
        self.find_element(*self.alert_loc).click()
        self.wait(EC.element_to_be_clickable(self.alert_confirm_loc)).click()
        sleep(1)




'''
if __name__ == '__main__':
    driver = webdriver.Firefox()
    login_o = LoginPage(driver)
    login_o.open()
    login_o.pilot_login('admin','123456')
    #sleep(2)
    table_o = Create_Table(driver)
    table_o.dist_bars('1', '123')
    sleep(3)
    insert_img(driver, 'table' + str(int(time.time())) + '.png')
    driver.close()

'''





