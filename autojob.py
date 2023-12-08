#!/usr/bin/env python
# -*- coding:utf-8 -*-
# LiangLiang  2023.12.6

import os  
import time
from wly import logging

# 启动deepin桌面，桌面比较消耗资源增加功耗，所有停掉了
logging.info("启动桌面")
os.system('sudo systemctl start lightdm.service')           # 需要先设置sudo免密
#os.system('sudo systemctl start x11vnc')
time.sleep(5)

# 设置DISPLAY变量，指定程序运行的图形界面
os.environ['DISPLAY'] = ':0'  # 设置 DISPLAY 环境变量  
logging.info("DISPLAY=" + os.environ['DISPLAY'])  # 打印 DISPLAY 环境变量的值
os.system('py3env/bin/python wly.py')

# # 运行结束，关闭桌面
time.sleep(5)
os.system('sudo systemctl stop lightdm.service')
logging.info("关闭桌面")


