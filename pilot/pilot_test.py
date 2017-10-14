# coding = utf-8
from time import sleep
import time
from selenium import webdriver

from pilot.test_case.page_object.page import Page
from pilot.test_case.page_object.login_page import LoginPage
from pilot.test_case.page_object.create_conn_page import Create_Conn
from pilot.test_case.page_object.create_table_page import Create_Table
from pilot.test_case.page_object.open_tables_page import open_all_tables
from pilot.test_case.page_object.create_panel_page import Create_Panel
from pilot.test_case.page_object.show_panel_page import show_all_panel

from pilot.test_case.model.function import *
from pilot.test_case.model.driver import *

class PilotTest(Page):
    @log('登陆')
    def login(self):
        po_l = LoginPage(self.driver)
        po_l.login_start('admin', '123456')
        sleep(0.5)
    @log('创建连接')
    def conn(self):
        # 创建inceptor链接
        inceptor_name = 'test-inceptor9289'  # 设置链接名称
        po_conn = Create_Conn(self.driver)  # 实例一个创建链接对象
        po_conn.connnect(inceptor_name)  # 创建链接
        sleep(0.5)
    @log('创建工作表')
    def create_table(self):
        #创建工作表
        po_c = Create_Table(self.driver)
        po_c.open()
        table_name = 'test9289'
        po_c.dist_bars(table_name)
        sleep(1)
    @log('打开工作表')
    def open_table(self):
        # 展示工作表
        po_o = open_all_tables(self.driver)
        po_o.open_TABLE()
        sleep(1)
    @log('创建仪表板')
    def create_panel(self):
        # 创建仪表盘
        po_panel = Create_Panel(self.driver)
        panel_name = 'test92289'
        po_panel.create_PANEL(panel_name)
    @log('展示仪表板')
    def show_panel(self):
        # 展示仪表板
        po_s = show_all_panel(self.driver)
        po_s.show_PANEL()
        sleep(2)

    def test_pilot(self):
        operation_dir()
        # self.login()
        # self.conn()
        # try:
        #     self.create_table()
        # except Exception as e:
        #     print(e)
        # self.open_table()
        # self.create_panel()
        # self.show_panel()

if __name__ == '__main__':
    driver = browser()
    pt = PilotTest(driver)
    pt.test_pilot()
    #upload_image()
    # sleep(1)
    driver.close()


