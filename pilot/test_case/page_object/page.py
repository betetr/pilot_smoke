# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import os
import shutil


class Page(object):
    pilot_url = 'http://172.16.130.109:8086/'
    '''
基本类，用于所页面的继承
'''
    def __init__(self, selenium_driver, base_url = pilot_url, parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent
        self.tabs = {}

    def wait(self, method):
        return WebDriverWait(self.driver, 10).until(method)

    def open(self):
        self._open(self.url)

    def _open(self, url):
        if url[:4]== 'http':
            url_ = url
        else:
            url_ = self.base_url + url
        self.driver.get(url_)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    def find_element_by_css_selector(self,loc):
        return self.driver.find_element_by_css_selector(loc)

    def move_to_element(self, *loc):
        wait = self.find_element(*loc)
        return ActionChains(self.driver).move_to_element(wait).perform()

    def click(self):
        return self.driver.click()

    def back(self):
        return self.driver.back()

    def maximize_window(self):
        return self.driver.maximize_window()

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def script(self,src):
        return self.driver.execute_script(src)

    def send_keys(self,loc,value,clear_first=True,click_first=True):
        try:
            loc = getattr(self,'_%s'%loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
                print('%s page does not have "%s" locator' %(self,loc))








