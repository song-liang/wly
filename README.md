# wly
卧龙吟鼠标执行每日任务挂机脚本

使用PyAutoGUI模块，查找任务的图标，操作鼠标点击图标执行任务
```
# 安装虚拟环境
apt-get install python3-dev python3-venv libjpeg-dev python3-tk gnome-screenshot at-spi2-core

python3 -m venv py3env
source py3env/bin/activate

# 安装PyAutoGUI模块
pip install pyautogui numpy opencv-python

# 修改配置账号
vim config.py

# 执行
python autojob.py
```
