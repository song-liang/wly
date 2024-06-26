#!/usr/bin/env python
# -*- coding:utf-8 -*-
# LiangLiang  2023.7.29
# 游奇乐趣卧龙吟网页游戏，鼠标自动点击领取日常奖励和执行任务
import time
import pyautogui
import logging
import webbrowser
from config import *

logging.basicConfig(level=logging.INFO, datefmt=' %Y/%m/%d %H:%M:%S', filename='job.log', filemode='a',
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',)
logger = logging.getLogger(__name__)


# 查找图标位置，点击鼠标
def ui_click(name, pause=1.5, confidence=0.85):
    try:
        logging.info(name)
        pyautogui.PAUSE = pause  # 延迟停顿秒
        point = pyautogui.locateOnScreen('png/' + name + '.png', confidence=confidence, grayscale=True)  # 寻找按钮
        center = pyautogui.center(point)  # 寻找图片的中心
        pyautogui.click(center)  # 点击
    except TypeError as e:
        logging.warning(str(e) + ": 寻找不到图片位置")
    except pyautogui.ImageNotFoundException as e:
        logging.warning(str(e) + ": 寻找不到图片位置")


# 传入点击步骤列表，进行点击执行, 可选择需要停顿等待加载数据的步骤名字和时间
def step_exec(step_list, pause=1.5, confidence=0.85, step_pause=None, step_pause_time=3):
    for step in step_list:
        ui_click(step, pause, confidence)
        if step == step_pause:
            time.sleep(step_pause_time)  # 延迟等待加载数据


# 取消消费金币提示
def xitongshezhi():
    # 坐标点击进入信息设置
    pyautogui.click(80, 145)
    time.sleep(1.5)                          # 游戏界面加载等待
    step_exec(step_list=['xitongshezhi-xitong', 'xitongshezhi-xiaofeishezhi', "xitongshezhi-gouxuan", 
              "xitongshezhi-xitong-guanbi",'guanbi'], confidence=0.85)


# 执行小秘书
def xiaomishu():
    step_exec(step_list=['xiaomishu', 'xiaomishu-zhixing', 'guanbi', 'xiaomishu-tuichu'], pause=2, confidence=0.85)


# 新世界
def xinshijie():
    step_exec(step_list=['xinshijie', 'xinshijie-lingqu', 'xinshijie-guozhanjiangli', 'xinshijie-guozhanjiangli-lingqu',
                         "xinshijie-guozhanjiangli-queding", 'guanbi'], confidence=0.80)


# 日常
def richang_dengluli():
    step_exec(step_list=["richang-fengshang", "richang-zhizunli", 'richang-dengluli', "richang-dengluli-lingqu",
                         "ricahng-youjian", "ricahng-youjian-lingqu", "ricahng-youjian-fanhui"], confidence=0.75)


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
    step_exec(step_list=['richang', 'richang-guchengtanmi', 'richang-guchengtanmi-240',
                         'richang-guchengtanmi-lianxusaodang', 'richang-guchengtanmi-kaishisaodang',
                         "guanbi", "richang-guchangtanmi-fanhui"],
              step_pause="richang-guchengtanmi-kaishisaodang", step_pause_time=8, confidence=0.75, pause=2)


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
    ui_click("richang-qunxiongzhulu", confidence=0.80)

    # 匹配挑战10次
    n = 0
    while n < 12:
        n += 1
        step_exec(
            step_list=['richang-qunxiongzhulu-pipei', 'richang-qunxiongzhulu-tiaoguo', 'richang-qunxiaongzhulu-tuichu'],
            step_pause="richang-qunxiongzhulu-pipei", step_pause_time=8)

    # 领取奖励,退出返回主城
    step_list = ['richang-qunxiongzhulu-jiangli', 'richang-qunxiongzhulu-jianglilingqu', "richang-qunxiongzhulu-jifenjiangli",
                 'richang-qunxiongzhulu-jifenjianglilingqu', 'guanbi', "richang-fanhui", "richang-fanhui"]
    for step in step_list:
        ui_click(step)
        # 领取所有奖励
        if step == "richang-qunxiongzhulu-jianglilingqu":
            m = 0
            while m < 6:
                m += 1
                ui_click(step)


# 世界
def shijie():

    # 资源-田矿
    step_exec(step_list=["shijie", "shijie-ziyuan", 'shijie-ziyuan-tiankuang', "shijie-ziyuan-zhanling", "guanbi", "shijie"], 
              confidence=0.70, pause=2.5, step_pause="shijie", step_pause_time=4)

    # 世界-刺探
    step_list = ["shijie-changbanpo", "shijie-citan", "guanbi",
                 'shijie-maicheng', "shijie-citan", "guanbi",
                 "shijie-zhuzha", "shijie-zhengcha", "shijie-zhengcha", "shijie-zhengcha-guanbi", "guanbi",
                 "guanbi", "zhucheng"]
    for step in step_list:
        ui_click(step, confidence=0.80)
        if step == 'shijie-zhuzha':
            pyautogui.moveRel(0, 120, duration=1)       # 鼠标向下移动，1秒完成
            pyautogui.click()                           # 鼠标点击当前位置 


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


# 府邸
def fudi():
    # 点击坐标进入府邸 (直接使用坐标，避免四季图标变化找不到位置)
    pyautogui.click(1530, 770)

    # 府邸-马场
    ui_click("fudi-machang")
    # 互动两次
    n = 0
    while n < 2:
        n += 1
        step_exec(step_list=["fudi-machang-hudong", "fudi-machang-queding"])
    # 返回府邸
    ui_click("fudi-machang-fanhui")


    # 府邸-寻访
    ui_click("fudi-xunfang")
    # 15次会谈次数，进行高级寻访5次
    count, n = 15, 0  # 计数
    while n < 5:
        n += 1
        step_list = ["fudi-xunfang-gaojixunfang", "fudi-xunfang-shanggu", "fudi-xunfang-dagu", "fudi-xunfang-jufu", "fudi-xunfang-haozu"]
        count_except = 0  # 错误计数
        for step in step_list:
            try:
                logging.info(step)
                pyautogui.PAUSE = 2  # 延迟停顿秒
                point = pyautogui.locateOnScreen('png/' + step + '.png', confidence=0.85, grayscale=True)  # 寻找按钮
                center = pyautogui.center(point)  # 寻找图片的中心
                pyautogui.click(center)  # 点击
            except TypeError as e:
                logging.warning(str(e) + ": 寻找不到图片位置")
                count_except += 1
            except pyautogui.ImageNotFoundException as e:
                logging.warning(str(e) + ": 寻找不到图片位置")
                count_except += 1
        if count_except < 4:        # 4个商贾或豪族，寻访到一个商贾时，错误计数小于4，谈话次数减一
            count -= 1
    logging.info("剩余谈话次数：" + str(count))
    # 返回府邸
    ui_click("fudi-xunfang-fanhui")

    # 府邸-内堂
    ui_click("fudi-neitang")
    # 剩余谈话次数用完
    n = 0
    while n < count:
        n += 1
        ui_click("fudi-neitang-tanhua")

    # 返回主城
    step_exec(step_list=["fudi-neitang-fanhui", "fudi-fanhui"], confidence=0.80)



# 武将技能升级
def wujiang_jinengshengji(name):
    step_exec(step_list=["wujiang", "wujiang-" + name, "wujiang-jineng", "wujiang-shengji", "wujiang-huode",
                         "wujiang-yijiansaodang", "guanbi", "guanbi", "guanbi", "wujiang-fanhui"],
              step_pause='wujiang-huode', step_pause_time=2, confidence=0.75, pause=2)


# 竞技场
def jingjichang():
    # 点击坐标进入竞技场
    pyautogui.click(700, 470)
    # 日常奖励领取
    step_exec(step_list=["jingjichang-baoxiang", "jingjichang-jiangli-queding", 
                         "jingjichang-meiyoujiangli-guanbi"], confidence=0.8)

    # 挑战
    n = 0
    while n < 5:
        n += 1
        step_exec(step_list=["jingjichang-tiaozhan", "jingjichang-tiaozhan-guanbi", 'jingjichang-tiaozhan-tiaoguo',
                             "jingjichang-tiaozhan-tuichu"], pause=3)

    # 竞技场退出
    step_exec(step_list=["jingjichang-tiaozhan-quxiao", "jingjichang-tiaozhan-fanhui"])


# 活跃奖励
def huoyue():
    step_exec(step_list=["huoyue", "huoyue-meiriyiqian", "huoyue-yijianlingqu"],
              step_pause="huoyue-yijianlingqu", step_pause_time=4)      # 一键领取活跃值

   # 活跃界面购买军令
    step_list = ["huoyue-maijunling", "huoyue-maijunling-queding", "huoyue-maijunling-lingqu"]
    for step in step_list:
        logging.info(step)
        pyautogui.PAUSE = 1  # 延迟停顿秒
        # 方法一：先点击，移动后再点击
        ui_click(step)
        if step == "huoyue-maijunling":
            pyautogui.moveRel(1100, 0, duration=1)      # 鼠标相对于当前位置x坐标右移1100个距离，1秒内完成
            pyautogui.click()  # 点击

#       # 方法二 先判断中心点移动后点击
#       if step == "huoyue-maijunling":
#           try:
#               point = pyautogui.locateOnScreen('png/' + step + '.png', confidence=0.90, grayscale=True)
#               x, y = pyautogui.center(point)  # 寻找图片的中心
#               pyautogui.click(x+1100, y)      # 点击
#           except TypeError as e:
#               logging.warning(str(e) + ": 寻找不到图片位置")
#           except pyautogui.ImageNotFoundException as e:
#               logging.warning(str(e) + ": 寻找不到图片位置")
#       else:
#           ui_click(step)

    # 领取活跃奖励, 停顿4秒，避免文字挡住图标
    step_exec(step_list=["huoyue-60", "huoyue-80", "huoyue-100", "huoyue-120", "huoyue-140", "huoyue-160"], pause=4) 
    ui_click("huoyue-fanhui")


# 武魁高塔
def wukuigaota():
    ui_click("wukuigaota-qiehuan")                  # 向左切换到天狼
    ui_click("wukuigaota-xuanzedengji")             # 选择天狼等级
    pyautogui.dragRel(0, -260, duration=2)          # 向上拖拽出220级
    ui_click("wukuigaota-tianlang220", confidence=0.90)   # 选择220级
    # 攻击boss 3次
    n = 0
    while n < 3:
        n += 1
        step_exec(step_list=["wukuigaota-gongji", "wukuigaota-chuangjiantuiwu", "wukuigaota-kaizhan",
                             "wukuigaota-jiaru", "wukuigaota-queding"],
                  step_pause="wukuigaota-jiaru", step_pause_time=12)  # 等待攻击完

    # 返回
    ui_click("wukuigaota-fanhui")


# 征程活跃奖励
def zhengcheng():
    # 任务奖励
    step_exec(step_list=["richang-zhengcheng", "richang-zhengcheng-renwu", 'richang-zhengcheng-lingqu'])

    # 进入武魁高塔，先点击，移动后再点击
    ui_click("wukuigaota", confidence=0.75)
    pyautogui.moveRel(640, 0, duration=1)  # 鼠标相对于当前位置x坐标右移1100个距离，1秒内完成
    pyautogui.click()  # 点击

    # 武魁高塔
    wukuigaota()

    # 返回主城
    ui_click("richang-zhengcheng-fanhui")
    pyautogui.PAUSE = 2.5 # 延迟停顿秒
    ui_click("zhucheng")


# 节日活动
def huodong():
    # 节日签到
    step_exec(step_list=["huodong-qiandao", "huodong-qiandao-qiandao", "huodong-qiandao-guanbi"])
    # 节日积分奖励
    step_exec(step_list=["huodong-huodong", "huodong-jierihuodong", "huodong-jierihuodong-lingqu", "huodong-jierihuodong-fanhui"],
             step_pause="huodong-jierihuodong-lingqu", step_pause_time=12)      # 等待一键领取完



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
                logging.info("点击副本")
                break
            else:
                logging.info("找不到副本图")

        # 副本攻击
        step_list = ["fuben-gongji", "fuben-tiaoguo", "fuben-tuichu"]
        for name in step_list:
            try:
                logging.info(name)
                pyautogui.PAUSE = 2  # 延迟停顿秒
                point = pyautogui.locateOnScreen('png/' + name + '.png', confidence=0.8, grayscale=True)  # 寻找按钮
                center = pyautogui.center(point)  # 寻找图片的中心
                pyautogui.click(center)  # 点击
            except TypeError as e:
                logging.warning(str(e) + ": 寻找不到图片位置")
            except pyautogui.ImageNotFoundException as e:
                logging.warning(str(e) + ": 寻找不到图片位置")


def wly():
    xitongshezhi()              # 系统设置取消金币消费提醒
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
    fudi()                      # 府邸-马场-寻访-谈话
    wujiang_jinengshengji("simawei")  # 武将技能升级
    shijie()                    # 世界-资源田矿-城池刺探
    junshifu()                  # 军事府
    huoyue()                    # 活跃奖励
    zhengcheng()                # 征程奖励
    huodong()                   # 活动奖励
    # fuben()


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
    time.sleep(3)
    logging.info("----------" + "登录" + "----------")


# 浏览器访问角色游戏地址，开始执行任务
def execute_job(url):
    # 打开系统默认浏览器 执行任务
    logging.info("----------" + "开始执行" + "----------")
    logging.info("----------" + url + "----------")
    webbrowser.get().open_new_tab(url)      # 打开新标签
    time.sleep(30)                          # 游戏界面加载等待

    pyautogui.click(x=100, y=200)           # 随便点击一下页面退出登陆后的弹窗
    wly()                                   # 执行wly任务
    pyautogui.hotkey('ctrl', 'w')           # 关闭浏览器当前标签

    logging.info("----------" + "执行结束" + "----------")


if __name__ == '__main__':
    # 只单独执行任务
    # wly()
    # wujiang_jinengshengji("simawei")  # 武将技能升级
    # 登录
    login(login_url, username, password)
    # 执行任务
    execute_job(role_weiwu)
    execute_job(role_linghu)
    execute_job(role_guihai)
    # 关闭所有标签退出浏览器
    pyautogui.hotkey('ctrl', 'shift', 'w')
