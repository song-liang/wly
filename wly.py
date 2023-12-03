#!/usr/bin/env python
# -*- coding:utf-8 -*-
# LiangLiang  2023.7.29
# 游奇乐趣卧龙吟网页游戏，鼠标自动点击领取日常奖励和执行任务
import time
import pyautogui


# 查找图标位置，点击鼠标
def ui_click(name, pause=2, confidence=0.85):
    try:
        print(name)
        pyautogui.PAUSE = pause  # 延迟停顿秒
        point = pyautogui.locateOnScreen('png/' + name + '.png', confidence=confidence, grayscale=True)  # 寻找按钮
        center = pyautogui.center(point)  # 寻找图片的中心
        pyautogui.click(center)  # 点击
    except TypeError:
        print("'NoneType' object is not subscriptable", "寻找不到图片位置")
    except pyautogui.ImageNotFoundException:
        print("pyautogui.ImageNotFoundException", "寻找不到图片位置")

# 传入点击步骤列表，进行点击执行, 可选择需要停顿等待加载数据的步骤名字和时间
def step_exec(step_list, pause=1.5, confidence=0.85, step_pause=None, step_pause_time=3):
    for step in step_list:
        ui_click(step, pause, confidence)
        if step == step_pause:
            time.sleep(step_pause_time)  # 延迟等待加载数据


# 执行小秘书
def xiaomishu():
    step_exec(step_list=['xiaomishu', 'xiaomishu-zhixing', 'guanbi', 'xiaomishu-tuichu'], pause=1.5, confidence=0.85)


# 新世界
def xinshijie():
    step_exec(step_list=['xinshijie', 'xinshijie-lingqu', 'xinshijie-guozhanjiangli', 'xinshijie-guozhanjiangli-lingqu',
                         "xinshijie-guozhanjiangli-queding", 'guanbi'], confidence=0.80)


# 日常
def richang_dengluli():
    step_exec(step_list=["richang-fengshang", "richang-zhizunli", 'richang-dengluli', "richang-dengluli-lingqu",
                         "ricahng-youjian", "ricahng-youjian-lingqu", "ricahng-youjian-fanhui"], confidence=0.8)


# 日常-缤纷礼
def richang_binfenli():
    step_exec(confidence=0.80, step_list=["richang-binfenli", 'richang-binfenli-baoxiang',
                                          "richang-binfenli-kaiqibaoxiang", "richang-binfenli-fanhui"])


# 市场-商铺
def shichang_shangpu():
    step_exec(step_list=["shichang", "shichang-shangpu", 'shichang-lingqu', "shichang-queding",
                         "shichang-shangpu-huanhui", "guanbi"])


# 军团奖励
def juntuan():
    step_exec(step_list=["juntuan", "juntuan-lingqujiangli", 'juntuan-qiandao', "jumtuan-fanhui"])


# 古城探秘
def richang_gucheng():
    step_exec(step_list=['richang', 'richang-guchengtanmi', 'richang-guchengtanmi-jindu',
                         'richang-guchengtanmi-lianxusaodang', 'richang-guchengtanmi-kaishisaodang',
                         "guanbi", "richang-guchangtanmi-fanhui"],
              step_pause="richang-guchengtanmi-kaishisaodang", step_pause_time=8)


# 古城虎牢关
def richang_hulaoguan():
    # 点击进入日常,等待加载页面数据
    # ui_click("richang")
    # time.sleep(1)

    # 滑动屏幕到虎牢关
    ui_click("richang-dianjiyidong")
    pyautogui.dragRel(-1000, 0, duration=1)
    # 点击进入虎牢关
    ui_click("richang-hulaoguan")

    # 虎牢关攻击吕布5次
    n = 0
    while n < 5:
        n += 1
        step_exec(step_list=['richang-hulaoguan-gongji', 'richang-hulaoguan-tiaoguo', 'richang-hulaoguan-tuichu'],
                  step_pause="richang-hulaoguan-gongji", step_pause_time=3)

    # 虎牢关结束，返回主城
    step_exec(step_list=["richang-hulaoguan-quxiao", "richang-hulaoguan-fanhui"])


# 日常-群雄逐鹿
def richang_qunxiongzhulu():

    # 滑动屏幕到群雄逐鹿
    ui_click("richang-dianjiyidong")
    pyautogui.dragRel(-1000, 0, duration=1)
    # 点击进入群雄逐鹿
    ui_click("richang-qunxiongzhulu")

    # 匹配挑战15次
    n = 0
    while n < 15:
        n += 1
        step_exec(
            step_list=['richang-qunxiongzhulu-pipei', 'richang-qunxiongzhulu-tiaoguo', 'richang-qunxiaongzhulu-tuichu'],
            step_pause="richang-qunxiongzhulu-pipei", step_pause_time=8)

    # 领取奖励,退出返回主城
    step_list = ['richang-qunxiongzhulu-jiangli', 'richang-qunxiongzhulu-jianglilingqu', 'guanbi',
                 "richang-fanhui", "richang-fanhui"]
    for step in step_list:
        ui_click(step)
        # 领取所有奖励
        if step == "richang-qunxiongzhulu-jianglilingqu":
            m = 0
            while m < 6:
                m += 1
                ui_click(step)


# 世界-田矿
def shijie_ziyuan():
    step_exec(step_list=["shijie", "shijie-ziyuan", 'shijie-ziyuan-tiankuang', "shijie-ziyuan-zhanling", "guanbi",
                         "shijie"], confidence=0.7, step_pause="shijie", step_pause_time=4)


# 世界-刺探
def shijie_citan():
    step_list = ["shijie-yunnan", "shijie-citan", "guanbi",
                 'shijie-chibi', "shijie-citan", "guanbi",
                 "shijie-maichen", "shijie-zhengcha", "shijie-zhengcha", "shijie-zhengcha-guanbi", "guanbi",
                 "guanbi", "zhucheng"]
    for step in step_list:
        ui_click(step, confidence=0.90)
        # if step == 'shijie-shan':
        #     pyautogui.dragRel(0, -250, duration=3)      # 点击向上拖动屏幕


# 军事府
def junshifu():
    # 领取奖励
    step_exec(step_list=["junshifu", "junshifu-paiqian", "junshifu-yijianlingqu"])

    # 派遣
    n = 0
    while n < 10:
        n += 1
        step_exec(step_list=["junshifu-paiqian-paiqian", "junshifu-paiqian-yijianpaiqian", "junshifu-paiqian-chufa"])

    # 返回主城
    step_exec(step_list=["junshifu-fanhui", "guanbi"], confidence=0.8)


# 府邸-马场
def fudi_machang():
    # 进入马场
    step_exec(step_list=["fudi", "fudi-machang"])
    # 互动两次
    n = 0
    while n < 2:
        n += 1
        step_exec(step_list=["fudi-machang-hudong", "fudi-machang-queding"])
    # 返回主城
    step_exec(step_list=["fudi-machang-fanhui", "fudi-fanhui"], confidence=0.80)


# 武将技能升级
def wujiang_jinengshengji(name):
    step_exec(step_list=["wujiang", "wujiang-" + name, "wujiang-jineng", "wujiang-shengji", "wujiang-huode",
                         "wujiang-yijiansaodang", "guanbi", "guanbi", "guanbi", "wujiang-fanhui"],
              step_pause='wujiang-huode', step_pause_time=2)


# 竞技场
def jingjichang():
    # 日常奖励领取
    step_exec(step_list=["jingjichang", "jingjichang-baoxiang", "jingjichang-jiangli-queding"], confidence=0.8)

    # 挑战
    n = 0
    while n < 5:
        n += 1
        step_exec(step_list=["jingjichang-tiaozhan", "jingjichang-tiaozhan-guanbi", 'jingjichang-tiaozhan-tiaoguo',
                             "jingjichang-tiaozhan-tuichu"], pause=3)

    # 竞技场退出
    step_exec(step_list=["jingjichang-tiaozhan-quxiao", "jingjichang-tiaozhan-fanhui"])


# 征程活跃奖励
def zhengcheng():
    step_exec(step_list=["richang-zhengcheng", "richang-zhengcheng-renwu", 'richang-zhengcheng-lingqu',
                         "richang-zhengcheng-fanhui"])


# 活跃界面购买军令
def huoyue_maijunling():
    step_list = ["huoyue-maijunling", "huoyue-maijunling-queding", "huoyue-maijunling-lingqu"]
    for step in step_list:
        print(step)
        pyautogui.PAUSE = 1  # 延迟停顿秒
        try:
            point = pyautogui.locateOnScreen('png/' + step + '.png', confidence=0.95, grayscale=True)
            x, y = pyautogui.center(point)  # 寻找图片的中心
            if step == "huoyue-maijunling":
                x = x + 1100
            pyautogui.click(x, y)  # 点击
            # pyautogui.moveRel(1100, 0, duration=1)      # 鼠标相对于当前位置x坐标右移1100个距离，1秒内完成
        except TypeError:
            print("'NoneType' object is not subscriptable", "寻找不到图片位置")


# 活跃奖励
def huoyue():
    step_exec(step_list=["huoyue", "huoyue-meiriyiqian", "huoyue-yijianlingqu"])  # 一件领取活跃值

    huoyue_maijunling()  # 买军令

    step_exec(step_list=["huoyue-60", "huoyue-80", "huoyue-100", "huoyue-120", "huoyue-140", "huoyue-160"],
              pause=4)  # 领取活跃奖励, 停顿4.5秒，避免文字挡住图标
    step_exec(step_list=["huoyue-fanhui"])


def fuben():
    n = 0
    while n < 20:
        n += 1
        # 寻找副本

        while True:
            time.sleep(0.4)
            point = pyautogui.locateOnScreen('png/fuben-guotu.png', confidence=0.7, grayscale=True)
            if point is not None:
                center = pyautogui.center(point)  # 寻找图片的中心
                pyautogui.click(center)  # 点击
                print("点击副本")
                break
            else:
                print("找不到副本图")

        # 副本攻击
        step_list = ["fuben-gongji", "fuben-tiaoguo", "fuben-tuichu"]
        for name in step_list:
            try:
                print(name)
                pyautogui.PAUSE = 2  # 延迟停顿秒
                point = pyautogui.locateOnScreen('png/' + name + '.png', confidence=0.8, grayscale=True)  # 寻找按钮
                center = pyautogui.center(point)  # 寻找图片的中心
                pyautogui.click(center)  # 点击
            except TypeError:
                print("'NoneType' object is not subscriptable", "寻找不到图片位置")


def main():
    richang_dengluli()          # 日常登录礼
    xiaomishu()                 # 小秘书
    xinshijie()                 # 新世界领奖
    shichang_shangpu()          # 市场-商铺
    juntuan()                   # 军团领奖
    richang_binfenli()          # 缤纷-开宝箱
    richang_gucheng()           # 日常-古城探秘
    richang_hulaoguan()         # 日常-虎牢关
    richang_qunxiongzhulu()     # 日常-群雄逐鹿
    jingjichang()               # 竞技场
    fudi_machang()              # 府邸-马场
    wujiang_jinengshengji("gongsunxiu")  # 武将技能升级
    shijie_ziyuan()             # 世界-资源田矿
    shijie_citan()              # 世界-刺探
    junshifu()                  # 军事府
    huoyue()                    # 活跃奖励
    zhengcheng()                # 征程奖励
    # fuben()


if __name__ == '__main__':
    main()
