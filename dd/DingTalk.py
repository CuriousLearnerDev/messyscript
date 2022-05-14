
import os
import psutil
import pyautogui 
import time
import random


admin="xxxxxxx" #账号
passwd="xxxxxxx" #密码




def choose_color_2(cb):

    i = random.choice(range(4))

    if i == 0:
        return "\033[1;32m{}\033[0m".format(cb)
    elif i == 1:
        return "\033[1;31m{}\033[0m".format(cb)
    elif i == 2:
        return "\033[1;33m{}\033[0m".format(cb)
    elif i == 3:
        return "\033[1;36m{}\033[0m".format(cb)


# 等待
def Check_in():
    while 1:
        print("正在签到检查中")
        time.sleep(60) # 暂停 60 秒 


def live_streaming():
    while 1:
        app_dir = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\钉钉\钉钉.lnk'
        os.startfile(app_dir)

        print("正在检查是否直播")
        time.sleep(3) # 暂停 1 秒
        try:
            
            number7_location = pyautogui.locateOnScreen('./lib/img/ad.png')    # locateOnScreen获得图片的位置
            button7location = pyautogui.center(number7_location) # 叫x,y输出出来
            print("位置在"+str(((button7location[0]),(button7location[1]))))  # 返回屏幕所在位置
            print("检查成功在直播！")
            pyautogui.click(button7location,button='left')#点击
            try:
                
                time.sleep(5) # 暂停 5 秒
                number7_location = pyautogui.locateOnScreen('./lib/img/b2.png')    # locateOnScreen获得图片的位置
                button7location = pyautogui.center(number7_location) # 叫x,y输出出来
                print(pyautogui.position()) 
                #print("位置在"+str((button7location[0]-479),(button7location[1]+216)))  # 返回屏幕所在位置
                print("播放成功")
                pyautogui.click(button7location,button='left')#点击
                pyautogui.click((button7location[0]-479),(button7location[1]+216),button='left')#点击
                #Check_in()
            except Exception:  
                print("播放失败")
                
            break
        
        except Exception:   
            print("没有在直播:会等待60秒后在进行检查")

            time.sleep(60) # 暂停 60 秒



def judgeprocess(processname):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == processname:
            print("进程pid："+str(pid))
            break
    else:
        print("启动失败")
        return


def empty():
    for _ in range(0,20):
        pyautogui.hotkey('right')
    for _ in range(0,20):
        pyautogui.hotkey('backspace')

def Log_in():    
    app_dir = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\钉钉\钉钉.lnk'
    os.startfile(app_dir)
    try:
        try:
            number7_location = pyautogui.locateOnScreen('./lib/img/125user.png')    # locateOnScreen获得图片的位置

            button7location = pyautogui.center(number7_location) # 叫x,y输出出来
            print("输入位置在"+str(((button7location[0]+100),(button7location[1]))))  # 返回屏幕所在位置
            pyautogui.click(((button7location[0]+100),(button7location[1])),button='left')#点击
        except Exception:   
            number7_location = pyautogui.locateOnScreen('./lib/img/100user.png')    # locateOnScreen获得图片的位置

            button7location = pyautogui.center(number7_location) # 叫x,y输出出来
            print("输入位置在"+str(((button7location[0]+100),(button7location[1]))))  # 返回屏幕所在位置
            pyautogui.click(((button7location[0]+100),(button7location[1])),button='left')#点击
    except Exception:
        print("用户检查输入失败")
        return

    # 清空用户
    empty()

    pyautogui.typewrite(admin)

    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    # 清空用户
    empty()

    pyautogui.typewrite(passwd)
    try:
        
        try:
            number7_location = pyautogui.locateOnScreen('./lib/img/100Log_in.png')    # locateOnScreen获得图片的位置
            button7location = pyautogui.center(number7_location) # 叫x,y输出出来
            pyautogui.click(button7location,button='left')#点击
        except Exception:
            number7_location = pyautogui.locateOnScreen('./lib/img/125Log_in.png')    # locateOnScreen获得图片的位置
            button7location = pyautogui.center(number7_location) # 叫x,y输出出来
            pyautogui.click(button7location,button='left')#点击
    except Exception:

        print("登录失败")
        return
    time.sleep(5) # 暂停 1 秒
    try:
        try:
            number7_location = pyautogui.locateOnScreen('./lib/img/125Log_in_true.png')    # locateOnScreen获得图片的位置
            
            print("钉钉登录成功")
            live_streaming()
        except Exception:
            print("登录不成功")
            return
    except Exception:
        print("登录不成功")
        return



def run():
    try:
        print("即将启动程序！")
        app_dir = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\钉钉\钉钉.lnk'

        os.startfile(app_dir)
    except Exception:
        print("自动启动失败!")
        return
    time.sleep(1) # 暂停 1 秒
    if judgeprocess('DingTalk.exe') == 0:
        print('成功')
    else:
        pass
    for _ in range(0,3):
        try:
            number7_location = pyautogui.locateOnScreen('./lib/img/100run.png')    # locateOnScreen获得图片的位置   
            print(number7_location)
            print("检查到界面了！")
            Log_in()
            break
        except Exception:
            pass

if __name__ == '__main__':
    banner_1 = r"""    
        ____  _                     _____     _ _    
        |  _ \(_)_ __   __ _        |_   _|_ _| | | __
        | | | | | '_ \ / _` |         | |/ _` | | |/ /
        | |_| | | | | | (_| |         | | (_| | |   < 
        |____/|_|_| |_|\__, |____ ____|_|\__,_|_|_|\_\
                    |___/_____|_____|   
        
        作者：w啥都学

        *输入1监听直播
        *输入2登录+监听直播

    --------------------------------------------------------------
    ！注意：用户和密码要到源代码里面修改
            win系统最好系统缩放布局设置100如果不是可能会导致程序无法检查到的情况
    """

    print(choose_color_2(banner_1))
    i=input(choose_color_2("请输入"))
    if i=="0":
        Check_in()
    elif i=="1":
        live_streaming()
    elif i=="2":
        run()
    else:
        print("输入错误！")