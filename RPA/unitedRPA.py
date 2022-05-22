import pyautogui
import xlrd
import pyperclip
from cF import commonFunction as cF
import time
import datetime

list_instruct = ["/Users/mac/Desktop/ALLDATA/程序/自动化/指令文件/chrome_private",
                 "/Users/mac/Desktop/ALLDATA/程序/自动化/指令文件/sign_in",
                 "/Users/mac/Desktop/ALLDATA/程序/自动化/指令文件/InPrivate"]

list_option = ["ChP", "SgI", "InP"]

list_sys = ["执行一次", "循环"]


# 定义鼠标事件

# pyautogui库其他用法 https://blog.csdn.net/qingfengxd1/article/details/108270159

def mouseClick(clickTimes, lOrR, img, reTry):
    reTry_count = 0
    if reTry == 1:
        while True:
            # 定位图像位置
            location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
            if location is not None:
                pyautogui.click(location.x, location.y, clicks=clickTimes, interval=0.2, duration=0.2, button=lOrR)
                break
            reTry_count += 1
            print("未找到匹配图片,0.2秒后重试")
            time.sleep(0.2)
            if reTry_count == 6:
                print("重试次数超出预设阈值")
                break

    elif reTry == -1:
        while True:
            location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
            if location is not None:
                pyautogui.click(location.x, location.y, clicks=clickTimes, interval=0.2, duration=0.2, button=lOrR)
            time.sleep(0.1)
    elif reTry > 1:
        i = 1
        while i < reTry + 1:
            location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
            if location is not None:
                pyautogui.click(location.x, location.y, clicks=clickTimes, interval=0.2, duration=0.2, button=lOrR)
                print("重复")
                i += 1
            time.sleep(0.1)


# 数据检查
# cmdType.value  1.0 左键单击    2.0 左键双击  3.0 右键单击  4.0 输入  5.0 等待  6.0 滚轮
# ctype     空：0
#           字符串：1
#           数字：2
#           日期：3
#           布尔：4
#           error：5


def dataCheck(sheets):
    checkcmd = True
    # 行数检查
    if sheets.nrows < 2:
        print("无数据")
        checkcmd = False
    # 每行数据检查
    i = 1
    while i < sheets.nrows:
        # 第1列 操作类型检查
        cmdType = sheets.row(i)[0]
        if cmdType.ctype != 2 or (cmdType.value != 1.0 and cmdType.value != 2.0 and cmdType.value != 3.0
                                  and cmdType.value != 4.0 and cmdType.value != 5.0 and cmdType.value != 6.0):
            print('第', i + 1, "行,第1列数据有误")
            checkcmd = False
        # 第2列 内容检查
        cmdValue = sheets.row(i)[1]
        # 读图点击类型指令，内容必须为字符串类型
        if cmdType.value == 1.0 or cmdType.value == 2.0 or cmdType.value == 3.0:
            if cmdValue.ctype != 1:
                print('第', i + 1, "行,第2列数据有误")
                checkcmd = False
        # 输入类型，内容不能为空
        if cmdType.value == 4.0:
            if cmdValue.ctype == 0:
                print('第', i + 1, "行,第2列数据有误")
                checkcmd = False
        # 等待类型，内容必须为数字
        if cmdType.value == 5.0:
            if cmdValue.ctype != 2:
                print('第', i + 1, "行,第2列数据有误")
                checkcmd = False
        # 滚轮事件，内容必须为数字
        if cmdType.value == 6.0:
            if cmdValue.ctype != 2:
                print('第', i + 1, "行,第2列数据有误")
                checkcmd = False
        i += 1
    return checkcmd


# 任务
def mainWork():
    i = 1
    while i < sheet.nrows:
        # 取本行指令的操作类型
        cmdType = sheet.row(i)[0]
        # 1 代表单击左键
        if cmdType.value == 1.0:
            # 取目录、图片名称
            dirname = list_instruct[dec - 1]
            imgname = sheet.row(i)[1].value
            img = f"{dirname}/{imgname}"  # 输入变量值最优方案
            reTry = 1
            if sheet.row(i)[2].ctype == 2 and sheet.row(i)[2].value != 0:
                reTry = sheet.row(i)[2].value
            mouseClick(1, "left", img, reTry)
            print("单击左键", imgname)
        # 2 代表双击左键
        elif cmdType.value == 2.0:
            # 取目录、图片名称
            dirname = list_instruct[dec - 1]
            imgname = sheet.row(i)[1].value
            img = f"{dirname}/{imgname}"  # 输入变量值最优方案
            # 取重试次数
            reTry = 1
            if sheet.row(i)[2].ctype == 2 and sheet.row(i)[2].value != 0:
                reTry = sheet.row(i)[2].value
            mouseClick(2, "left", img, reTry)
            print("双击左键", imgname)
        # 3 代表右键
        elif cmdType.value == 3.0:
            # 取目录、图片名称
            dirname = list_instruct[dec - 1]
            imgname = sheet.row(i)[1].value
            img = f"{dirname}/{imgname}"  # 输入变量值最优方案
            # 取重试次数
            reTry = 1
            if sheet.row(i)[2].ctype == 2 and sheet.row(i)[2].value != 0:
                reTry = sheet.row(i)[2].value
            mouseClick(1, "right", img, reTry)
            print("右键", imgname)
        # 4 代表输入
        elif cmdType.value == 4.0:
            inputValue = sheet.row(i)[1].value
            pyperclip.copy(inputValue)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.5)
            print("输入:", inputValue)
        # 5 代表等待
        elif cmdType.value == 5.0:
            waitTime = sheet.row(i)[1].value
            time.sleep(waitTime)
            print("等待", waitTime, "秒")
        # 6 代表滚轮
        elif cmdType.value == 6.0:
            scroll = sheet.row(i)[1].value
            pyautogui.scroll(int(scroll))
            print("滚轮滑动", int(scroll), "距离")
        i += 1


def mainWork_SgI():
    while True:
        now = datetime.datetime.now()
        timing = str(now.hour) + ":" + str(now.minute)

        if now.hour == 6:

            if timing == "6:51":
                mainWork()
                cF.printwithcol("完成早上的签到任务", 0)
                time.sleep(20)

            elif now.hour == 6 and now.minute > 51:
                cF.printwithcol(f"现在时间{timing},待命三十分钟", 0)
                time.sleep(1800)

            else:
                cF.printwithcol(f"现在时间{timing},等待一分钟", 0)
                cF.countDown(60)

        elif now.hour == 12:

            if 44 <= now.minute <= 51:
                mainWork()
                cF.printwithcol("完成中午的签到任务", 0)
                time.sleep(20)

            elif now.hour == 12 and now.minute > 51:
                cF.printwithcol(f"现在时间{timing},待命三十分钟", 0)
                time.sleep(1800)

            else:
                cF.printwithcol(f"现在时间{timing},等待一分钟", 0)
                cF.countDown(60)

        else:
            cF.printwithcol(f"现在时间{timing},待命三十分钟", 0)
            time.sleep(1800)


# 初始化

def toStart():
    global checkCmd
    global sheet
    global dec
    wb = xlrd.open_workbook(filename=file)
    # 通过索引获取表格sheet页
    print('集合 自动化')

    dec = eval(cF.ask(list_option))
    if dec < 1:
        print("错误")
        cF.countDown(3)
        quit()
    sheet = wb.sheet_by_index(dec - 1)
    # 数据检查
    checkCmd = dataCheck(sheet)

# 格式函数

# 现已更新至cF

# def ask(que):
#     i = 1
#     string = '| '
#     while i <= len(que):
#         string += f"{i}-{que[i - 1]} | "
#         i += 1
#     cF.printwithcol(string, 0)
#     decs = input("选择:")
#     return decs


if __name__ == '__main__':
    global dec
    file = '/Users/mac/Desktop/ALLDATA/程序/自动化/指令文件/cmd.xls'
    # 打开文件

    toStart()

    if checkCmd:
        key = cF.ask(list_sys)
        if key == '1':
            # 循环拿出每一行指令

            if dec == 2:

                # sign_in 特别版

                mainWork_SgI()

            else:

                # 通用版

                mainWork()


        elif key == '2':
            if dec == 2:
                cF.printwithcol("SgI不适合循环模式", 0)
                cF.countDown(3)
                quit()
            while True:
                mainWork()
                time.sleep(0.1)
                print("等待0.1秒")
    else:
        print('输入有误或者已经退出!')
