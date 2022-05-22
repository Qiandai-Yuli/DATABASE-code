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

            list_str.append(list_cont[i - 1])
            strs += str(list_str[i - 1])
            if i == len(list_cont):
                print(f"\033[{hl};36m {strs} \033[0m", flush=True)
            else:
                print(f"\033[{hl};36m {strs} \033[0m", end='', flush=True)
            time.sleep(times / len(list_cont))
            i += 1


def loadPrint(cont, T, n):
    # 后两个阶段{}不与前后分割，不然会报错

    t = T / 3
    strs = "\r"
    list_c = []
    list_s_1 = ["@", "*", "^", "%", "1", "!", "~", "?", "<", "0", "e", "x", "+", ";", "&", ">"]
    list_s_2 = ["⁊", "†", "&", "‡", "¿", "ℑ", "∇", "∄", "⨊", "⊣", "⪥", "⟐", "⟡", "⟖", "⧱", "❖"]

    if n == 2:
        list0 = list_s_2
    else:
        list0 = list_s_1

    for lr in cont:
        list_c.append(lr)
    i = 1

    # print(list_c)

    while i <= len(cont):
        strs += "/"
        print(f"\033[36m {strs} \033[0m", end='', flush=True)
        time.sleep(t / len(cont))
        i += 1

    s = list(strs)
    i = 1
    while i <= len(cont):

        # print("a")

        j = 1
        while j <= i:
            c = int(random.uniform(0, 16))
            s[j] = list0[c]
            j += 1
        for lr in s:
            print(f"\033[36m{lr}\033[0m", end='', flush=True)

        time.sleep(t / len(cont))
        i += 1

    i = 1
    while i <= len(cont):

        # print("b")

        s[i] = list_c[i - 1]
        j = i + 1
        while j <= len(cont):
            c = int(random.uniform(0, 16))
            s[j] = list0[c]
            j += 1
        for lr in s:
            print(f"\033[36m{lr}\033[0m", end='', flush=True)

        time.sleep(t / len(cont))
        i += 1


def randomProcess(percent, n):
    list_s_1 = ["@", "*", "^", "%", "1", "!", "~", "?", "<", "0", "e", "x", "+", ";", "&", ">"]
    list_s_2 = ["⁊", "†", "&", "‡", "¿", "ℑ", "∇", "∄", "⨊", "⊣", "⪥", "⟐", "⟡", "⟖", "⧱", "❖"]

    if n == 2:
        list0 = list_s_2
    else:
        list0 = list_s_1

    i = 1
    ty = ""
    while i <= int(percent * 0.2):
        ty = ty + list0[int(random.uniform(0, 16))]
        i += 1
    __process = ty + "-" * (20 - int(percent * 0.2))
    inf_start = "|"
    inf_end = f"|{format(percent, '.1f')}%"  # 'format(float, '.nf')' means keep .0 * n
    str = "\r" + inf_start + __process + inf_end  # '\r' means reload
    print(f"\033[31m {str} \033[0m", end="", flush=True)


"""
globals()[name] = value
make string 'name' as variate with the 'value'
"""


def process(percent):
    # process = "■" * int(percent * 0.2) + "-" * (20 - int(percent * 0.2))
    __process = "⟐" * int(percent * 0.2) + "-" * (20 - int(percent * 0.2))
    inf_start = "|"
    inf_end = f"|{format(percent, '.1f')}%"  # 'format(float, '.nf')' means keep .0 * n
    str = "\r" + inf_start + __process + inf_end  # '\r' means reload
    print(f"\033[31m {str} \033[0m", end=" ", flush=True)


def fake_process(percent):
    t_f = 0
    while percent <= 100.0:
        process(percent)
        time.sleep(0.01)
        if percent < 99:
            percent += 1 + random.uniform(0, 0.5)
            if percent > 100:
                percent = 99
            else:
                pass
        else:
            percent += 100.0 - percent
        if percent == 100.0:
            t_f += 1
        if t_f > 1:
            break


def loading(s):
    t_l = 1
    list0 = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "■", "■", "■", "■", " ", " ", " ",
             " ", " ", " ", " ", " ", " ", " ", " "]
    m = 14
    n = 25
    k = 0
    while t_l <= s:
        if t_l != s:
            if k == 0:
                if m <= 14:
                    if m != 0:
                        c = m
                        strs = "\r"
                        while c <= n:
                            strs = strs + list0[c]

                            c += 1
                        print(strs, end="", flush=True)
                        # print(m, " ", n)
                        time.sleep(0.1)
                        m -= 1
                        n -= 1
                    if m == 0:
                        if m <= 14:
                            c = m
                            strs = "\r"
                            while c <= n:
                                strs = strs + list0[c]

                                c += 1
                            print(strs, end="", flush=True)
                            # print(m, " ", n)
                            time.sleep(0.1)

                        k = 1
                        m += 1
                        n += 1
            else:
                if m <= 14:
                    c = m
                    strs = "\r"
                    while c <= n:
                        strs = strs + list0[c]
                        c += 1
                        # print(strs)
                    print(strs, end="", flush=True)
                    # print(m, " ", n)
                    time.sleep(0.1)
                    m += 1
                    n += 1
                if m == 14:
                    t_l += 1
                    k = 0
        else:
            strs = "\r" + "done"
            print(strs)
            t_l += 1


def countDown(secs):
    c = secs - 1
    while 0 <= c <= secs:
        num = "\r" + str(c) + "\n"
        print(num, end='', flush=True)
        c -= 1
        time.sleep(1)
    # print("\r")


def ask(que):
    i = 1
    string = '| '
    while i <= len(que):
        string += f"{i}-{que[i - 1]} | "
        i += 1
    printwithcol(string, 0)
    decs = input("选择:")
    return decs


if __name__ == "__main__":
    # printwithcol(input("content:"), input("highlight:"))
    # percent = 0
    # t = 0
    # while percent <= 100.0:
    #     process(percent)
    #     time.sleep(0.05)
    #     if percent < 99:
    #         percent += 1 + random.uniform(0, 0.5)
    #         if percent > 100:
    #             percent = 99
    #         else:
    #             pass
    #     else:
    #         percent += 100.0 - percent
    #     if percent == 100.0:
    #         t += 1
    #     if t > 1:
    #         break

    # loading(4)

    # percent = 0
    # t = 0
    # fake_process(percent)
    # print('\n')
    # proPrint("Times", 0, 1)

    # loadPrint("莫高窟门外，有一条河。过河有一片空地，高高低低建着几座僧人圆寂塔。", 3, 2)

    countDown(4)
