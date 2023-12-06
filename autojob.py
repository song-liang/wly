#!/usr/bin/env python
# -*- coding:utf-8 -*-
# LiangLiang  2023.12.6

import webbrowser
import pyautogui
import time
import logging
from wly import wly
from config import *


# 浏览器打开认证地址登录
def login(url, name, passwd):
    webbrowser.get().open_new_tab(url)
    time.sleep(3)
    # 执行tab跳至输入用户名框，输入用户名
    pyautogui.press('tab')
    pyautogui.typewrite(name, interval=0.25)
    # tab跳至输入密码框，输入密码
    pyautogui.press('tab')
    pyautogui.typewrite(passwd, interval=0.25)
    # 执行enter键 登录
    pyautogui.press('enter')
    logging.info("----------" + "登录" + "----------")


# 浏览器访问角色游戏地址，开始执行任务
def execute_job(url):
    # 打开系统默认浏览器 执行任务
    logging.info("----------" + "开始执行" + "----------")
    logging.info("----------" + url + "----------")
    webbrowser.get().open_new_tab(url)      # 打开新标签
    time.sleep(25)                          # 游戏界面加载等待

    pyautogui.click(x=100, y=200)           # 随便点击一下页面退出登陆后的弹窗
    wly()                                   # 执行wly任务
    pyautogui.hotkey('ctrl', 'w')     # 关闭浏览器当前标签

    logging.info("----------" + "执行结束" + "----------")


if __name__ == '__main__':
    # 登录
    login(login_url, username, password)
    # 执行任务
    execute_job(role_weiwu)
    execute_job(role_linghu)
    execute_job(role_guihai)
    # 关闭浏览器
    pyautogui.hotkey('ctrl', 'shift', 'q')


