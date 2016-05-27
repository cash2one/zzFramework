# -*- coding: utf-8 -*-
import time
import os
from .path import REPORT_PATH


def png_name(name):
    """
    name：自定义图片的名称
    """
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    fp = REPORT_PATH + day + "\\image"
    tm = save_time()
    type = ".png"
    if os.path.exists(fp):
        filename = str(fp)+"\\" + str(tm) + "_" + name + type
        return filename
    else:
        os.makedirs(fp)
        filename = str(fp)+"\\" + str(tm) + "_" + name + type
        return filename


def save_time():
    """
    返回当前系统时间以括号中（）展示
    """
    return time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))


def save_screen_shot(driver, name):
    """
    快照截图
    name:图片名称
    """
    image = driver.save_screenshot(png_name(name))
    return image