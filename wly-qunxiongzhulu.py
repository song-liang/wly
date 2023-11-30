#!/usr/bin/env python
# -*- coding:utf-8 -*-
# LiangLiang  2023.7.29

import pyautogui
from wly import ui_click, step_exec


# 日常-群雄逐鹿
def richang_qunxiongzhulu():

    # 点击进入日常,等待加载页面数据
    ui_click("richang")
    # time.sleep(1)

    # 滑动屏幕到虎牢关
    # ui_click("richang-dianjiyidong")
    # pyautogui.dragRel(-1000, 0, duration=1)

    # 点击进入群雄逐鹿
    # ui_click("richang-qunxiongzhulu")

    # 匹配挑战15次
    n = 0
    while n < 30:
        n += 1
        step_exec(step_list=['richang-qunxiongzhulu-pipei', 'richang-qunxiongzhulu-tiaoguo',
                             'richang-qunxiaongzhulu-tuichu'],
                  step_pause="richang-qunxiongzhulu-pipei", step_pause_time=8)

    # 群雄逐鹿，返回主城
    # step_exec(step_list=["richang-qunxiongzhulu-quxiao", "richang-qunxiongzhulu-fanhui", "richang-fanhui"])


if __name__ == '__main__':
    richang_qunxiongzhulu()
