import time
import random

# 显示方式:  0（默认）、1（高亮）、22（非粗体）、4（下划线）、24（非下划线）、 5（闪烁）、25（非闪烁）、7（反显）、27（非反显）
# 前景色:   30（黑色）、31（红色）、32（绿色）、 33（黄色）、34（蓝色）、35（洋红）、36（青色）、37（白色）
# 背景色:   40（黑色）、41（红色）、42（绿色）、 43（黄色）、44（蓝色）、45（洋红）、46（青色）、47（白色）
# \033[显示方式；背景色；前景色  m (数字无重复 不改可不写)
# \033[0m 结尾


def printwithcol(cont, highlight):
    """
    highlight == 1, none == 0
    """

    print(f"\033[{highlight};36m {cont} \033[0m")


def proPrint(cont, hl, times):
    if times == 0:
        print(f"\033[{hl};36m {cont} \033[0m")
    else:
        list_cont = []
        for w in cont:
            list_cont.append(w)
        i = 1
        list_str = []
        strs = '\r'
        while i <= len(list_cont):

            list_str.append(list_cont[i-1])
            strs += str(list_str[i-1])
            print(f"\033[{hl};36m {strs} \033[0m", end='', flush=True)
            time.sleep(times/len(list_cont))
            i += 1







"""
globals()[name] = value
make string 'name' as variate with the 'value'
"""


def process(percent):
    process = "■" * int(percent * 0.2) + "-" * (20 - int(percent * 0.2))
    inf_start = "|"
    inf_end = f"|{format(percent, '.1f')}%"     # 'format(float, '.nf')' means keep .0 * n
    str = "\r" + inf_start + process + inf_end  # '\r' means reload
    print(f"\033[31m {str} \033[0m", end="", flush=True)


def fake_process(percent, t):
    while percent <= 100.0:
        process(percent)
        time.sleep(0.01)
        if percent <= 99:
            percent += 1 + random.uniform(0, 0.5)
            if percent > 100:
                percent = 99
            else:
                pass
        else:
            percent += 100.0 - percent
        if percent == 100.0:
            t += 1
        if t > 1:
            break




if __name__ == "__main__":
    #printwithcol(input("content:"), input("highlight:"))


    percent = 0
    t = 0
    fake_process(percent, t)
    print('\n')
    proPrint("Times", 0, 4)


