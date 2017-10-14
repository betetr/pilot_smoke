# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os
import shutil
#截图函数
def insert_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    #print(base_dir)
    base_dir = str(base_dir)
    #print(base_dir)
    base_dir = base_dir.replace('\\', '/')
    #print(base_dir)
    base = base_dir.split('/pilot')[0]
    #print(base)
    file_path = base + '/pilot_smoke/pilot/report/image/' + file_name
    #print(file_path)
    driver.get_screenshot_as_file(file_path)
#打印提示信息
def info_print(name):
    for i in range(61):
        if i==30:
            print(name, end='')
        else:
            print('*', end='')
    print('')
#装饰器
def log(name):
    def deco(func):
        def warp(*args, **kw):
            start = name + '----开始执行'
            end = name + '----结束'
            need_time = name + '-----执行时间'
            info_print(start)
            t1 = time.time()
            func(*args, **kw)
            t2 = time.time()
            info_print(end)
            info_print(need_time)
            print(t2 - t1)
            return func
        return warp
    return deco
#上传图片
def upload_image():
        dir_upfile = os.getcwd() + '/upload_image/upload_img.sh'
        os.system(dir_upfile)
#操作目录
@log('操作目录')
def operation_dir():
        dir_image = os.getcwd() + '/report/image'
        #print(dir_image)
        if os.path.exists(dir_image):
            info_print('删除image目录')               #打印提示信息
            shutil.rmtree(dir_image)
            info_print('创建image目录')               #打印提示信息
            os.mkdir(dir_image)
        else:
            pass



#用于验证该脚本是否有效
'''
if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('http://www.baidu.com')
    insert_img(driver, 'baidu.png)
    driver.quit()

'''


