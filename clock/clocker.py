#!/usr/bin/env python3

import datetime
import time as ti
from timer import start, counter

G = "   "
G_P_1 = "   "
G_P_2 = " ■ "
type_1 = "■ ■ ■ ■ ■"
type_2 = "        ■"
type_3 = "■       ■"
type_4 = "■        "

queList = ["timer", "clock"]


def printwithcol(cont, highlight):
    """
    highlight == 1, none == 0
    """

    print(f"\033[{highlight};36m {cont} \033[0m")



def ask(que):
    i = 1
    strings = '| '
    while i <= len(que):
        strings += f"{i}-{que[i - 1]} | "
        i += 1
    printwithcol(strings, 0)
    decs = eval(input("选择:"))
    return decs


def read(decision):

    global X1L1
    global X1L2_4
    global X1L5
    global X1L6_8
    global X1L9
    global X2L1
    global X2L2_4
    global X2L5
    global X2L6_8
    global X2L9
    global X3L1
    global X3L2_4
    global X3L5
    global X3L6_8
    global X3L9
    global L1
    global L2_4
    global L5
    global L6_8
    global L9
    global STL

    if decision == 1:

        # print(STL)

        if counter(startTimeList=STL)[0] == "0":
            H = counter(startTimeList=STL)[1]
        else:
            H = counter(startTimeList=STL)[0:2]

        if counter(startTimeList=STL)[3] == "0":
            M = counter(startTimeList=STL)[4]
        else:
            M = counter(startTimeList=STL)[3:5]

        if counter(startTimeList=STL)[6] == "0":
            S = counter(startTimeList=STL)[7]
        else:
            S = counter(startTimeList=STL)[6:8]

    if decision == 2:

        now = datetime.datetime.now()

        H = str(now.hour)
        M = str(now.minute)
        S = str(now.second)

    if len(H) == 1:
        if H == "4":
            X1L1 = type_1 + G + type_3 + G
        elif H == "1":
            X1L1 = type_1 + G + type_2 + G
        else:
            X1L1 = type_1 + G + type_1 + G
        if H in ["1", "2", "3", "7"]:
            X1L2_4 = type_3 + G + type_2 + G
        elif H in ["4", "8", "9", "0"]:
            X1L2_4 = type_3 + G + type_3 + G
        elif H in ["5", "6"]:
            X1L2_4 = type_3 + G + type_4 + G
        if H in ["1", "7"]:
            X1L5 = type_3 + G + type_2 + G
        elif H == "0":
            X1L5 = type_3 + G + type_3 + G
        else:
            X1L5 = type_3 + G + type_1 + G
        if H == "2":
            X1L6_8 = type_3 + G + type_4 + G
        elif H in ["6", "8", "0"]:
            X1L6_8 = type_3 + G + type_3 + G
        else:
            X1L6_8 = type_3 + G + type_2 + G
        if H in ["1", "4", "7", "9"]:
            X1L9 = type_1 + G + type_2 + G
        else:
            X1L9 = type_1 + G + type_1 + G
    else:
        if H[0] == "1":
            if H[1] == "4":
                X1L1 = type_2 + G + type_3 + G
            elif H[1] == "1":
                X1L1 = type_2 + G + type_2 + G
            else:
                X1L1 = type_2 + G + type_1 + G
            if H[1] in ["1", "2", "3", "7"]:
                X1L2_4 = type_2 + G + type_2 + G
            elif H[1] in ["4", "8", "9", "0"]:
                X1L2_4 = type_2 + G + type_3 + G
            elif H[1] in ["5", "6"]:
                X1L2_4 = type_2 + G + type_4 + G
            if H[1] in ["1", "7"]:
                X1L5 = type_2 + G + type_2 + G
            elif H[1] == "0":
                X1L5 = type_2 + G + type_3 + G
            else:
                X1L5 = type_2 + G + type_1 + G
            if H[1] == "2":
                X1L6_8 = type_2 + G + type_4 + G
            elif H[1] in ["6", "8", "0"]:
                X1L6_8 = type_2 + G + type_3 + G
            else:
                X1L6_8 = type_2 + G + type_2 + G
            if H[1] in ["1", "4", "7", "9"]:
                X1L9 = type_2 + G + type_2 + G
            else:
                X1L9 = type_2 + G + type_1 + G
        else:
            if H[0] == "4":
                X1L1_1 = type_3 + G
            elif H[0] == "1":
                X1L1_1 = type_2 + G
            else:
                X1L1_1 = type_1 + G

            if H[0] in ["1", "2", "3", "7"]:
                X1L2_4_1 = type_2 + G
            elif H[0] in ["4", "8", "9", "0"]:
                X1L2_4_1 = type_3 + G
            elif H[0] in ["5", "6"]:
                X1L2_4_1 = type_4 + G

            if H[0] in ["1", "7"]:
                X1L5_1 = type_2 + G
            elif H[0] == "0":
                X1L5_1 = type_3 + G
            else:
                X1L5_1 = type_1 + G

            if H[0] == "2":
                X1L6_8_1 = type_4 + G
            elif H[0] in ["6", "8", "0"]:
                X1L6_8_1 = type_3 + G
            else:
                X1L6_8_1 = type_2 + G

            if H[0] in ["1", "4", "7", "9"]:
                X1L9_1 = type_2 + G
            else:
                X1L9_1 = type_1 + G

            if H[1] == "4":
                X1L1 = X1L1_1 + type_3 + G
            elif H[1] == "1":
                X1L1 = X1L1_1 + type_2 + G
            else:
                X1L1 = X1L1_1 + type_1 + G
            if H[1] in ["1", "2", "3", "7"]:
                X1L2_4 = X1L2_4_1 + type_2 + G
            elif H[1] in ["4", "8", "9", "0"]:
                X1L2_4 = X1L2_4_1 + type_3 + G
            elif H[1] in ["5", "6"]:
                X1L2_4 = X1L2_4_1 + type_4 + G
            if H[1] in ["1", "7"]:
                X1L5 = X1L5_1 + type_2 + G
            elif H[1] == "0":
                X1L5 = X1L5_1 + type_3 + G
            else:
                X1L5 = X1L5_1 + type_1 + G
            if H[1] == "2":
                X1L6_8 = X1L6_8_1 + type_4 + G
            elif H[1] in ["6", "8", "0"]:
                X1L6_8 = X1L6_8_1 + type_3 + G
            else:
                X1L6_8 = X1L6_8_1 + type_2 + G
            if H[1] in ["1", "4", "7", "9"]:
                X1L9 = X1L9_1 + type_2 + G
            else:
                X1L9 = X1L9_1 + type_1 + G

    if len(M) == 1:
        if M == "4":
            X2L1 = G + type_1 + G + type_3 + G
        elif M == "1":
            X2L1 = G + type_1 + G + type_2 + G
        else:
            X2L1 = G + type_1 + G + type_1 + G
        if M in ["1", "2", "3", "7"]:
            X2L2_4 = G + type_3 + G + type_2 + G
        elif M in ["4", "8", "9", "0"]:
            X2L2_4 = G + type_3 + G + type_3 + G
        elif M in ["5", "6"]:
            X2L2_4 = G + type_3 + G + type_4 + G
        if M in ["1", "7"]:
            X2L5 = G + type_3 + G + type_2 + G
        elif M == "0":
            X2L5 = G + type_3 + G + type_3 + G
        else:
            X2L5 = G + type_3 + G + type_1 + G
        if M == "2":
            X2L6_8 = G + type_3 + G + type_4 + G
        elif M in ["6", "8", "0"]:
            X2L6_8 = G + type_3 + G + type_3 + G
        else:
            X2L6_8 = G + type_3 + G + type_2 + G
        if M in ["1", "4", "7", "9"]:
            X2L9 = G + type_1 + G + type_2 + G
        else:
            X2L9 = G + type_1 + G + type_1 + G
    else:
        if M[0] == "1":
            if M[1] == "4":
                X2L1 = G + type_2 + G + type_3 + G
            elif M[1] == "1":
                X2L1 = G + type_2 + G + type_2 + G
            else:
                X2L1 = G + type_2 + G + type_1 + G
            if M[1] in ["1", "2", "3", "7"]:
                X2L2_4 = G + type_2 + G + type_2 + G
            elif M[1] in ["4", "8", "9", "0"]:
                X2L2_4 = G + type_2 + G + type_3 + G
            elif M[1] in ["5", "6"]:
                X2L2_4 = G + type_2 + G + type_4 + G
            if M[1] in ["1", "7"]:
                X2L5 = G + type_2 + G + type_2 + G
            elif M[1] == "0":
                X2L5 = G + type_2 + G + type_3 + G
            else:
                X2L5 = G + type_2 + G + type_1 + G
            if M[1] == "2":
                X2L6_8 = G + type_2 + G + type_4 + G
            elif M[1] in ["6", "8", "0"]:
                X2L6_8 = G + type_2 + G + type_3 + G
            else:
                X2L6_8 = G + type_2 + G + type_2 + G
            if M[1] in ["1", "4", "7", "9"]:
                X2L9 = G + type_2 + G + type_2 + G
            else:
                X2L9 = G + type_2 + G + type_1 + G
        else:
            if M[0] == "4":
                X2L1_1 = G + type_3 + G
            elif M[0] == "1":
                X2L1_1 = G + type_2 + G
            else:
                X2L1_1 = G + type_1 + G

            if M[0] in ["1", "2", "3", "7"]:
                X2L2_4_1 = G + type_2 + G
            elif M[0] in ["4", "8", "9", "0"]:
                X2L2_4_1 = G + type_3 + G
            elif M[0] in ["5", "6"]:
                X2L2_4_1 = G + type_4 + G

            if M[0] in ["1", "7"]:
                X2L5_1 = G + type_2 + G
            elif M[0] == "0":
                X2L5_1 = G + type_3 + G
            else:
                X2L5_1 = G + type_1 + G

            if M[0] == "2":
                X2L6_8_1 = G + type_4 + G
            elif M[0] in ["6", "8", "0"]:
                X2L6_8_1 = G + type_3 + G
            else:
                X2L6_8_1 = G + type_2 + G

            if M[0] in ["1", "4", "7", "9"]:
                X2L9_1 = G + type_2 + G
            else:
                X2L9_1 = G + type_1 + G

            if M[1] == "4":
                X2L1 = X2L1_1 + type_3 + G
            elif M[1] == "1":
                X2L1 = X2L1_1 + type_2 + G
            else:
                X2L1 = X2L1_1 + type_1 + G
            if M[1] in ["1", "2", "3", "7"]:
                X2L2_4 = X2L2_4_1 + type_2 + G
            elif M[1] in ["4", "8", "9", "0"]:
                X2L2_4 = X2L2_4_1 + type_3 + G
            elif M[1] in ["5", "6"]:
                X2L2_4 = X2L2_4_1 + type_4 + G
            if M[1] in ["1", "7"]:
                X2L5 = X2L5_1 + type_2 + G
            elif M[1] == "0":
                X2L5 = X2L5_1 + type_3 + G
            else:
                X2L5 = X2L5_1 + type_1 + G
            if M[1] == "2":
                X2L6_8 = X2L6_8_1 + type_4 + G
            elif M[1] in ["6", "8", "0"]:
                X2L6_8 = X2L6_8_1 + type_3 + G
            else:
                X2L6_8 = X2L6_8_1 + type_2 + G
            if M[1] in ["1", "4", "7", "9"]:
                X2L9 = X2L9_1 + type_2 + G
            else:
                X2L9 = X2L9_1 + type_1 + G

    if len(S) == 1:
        if S == "4":
            X3L1 = G + type_1 + G + type_3
        elif S == "1":
            X3L1 = G + type_1 + G + type_2
        else:
            X3L1 = G + type_1 + G + type_1
        if S in ["1", "2", "3", "7"]:
            X3L2_4 = G + type_3 + G + type_2
        elif S in ["4", "8", "9", "0"]:
            X3L2_4 = G + type_3 + G + type_3
        elif S in ["5", "6"]:
            X3L2_4 = G + type_3 + G + type_4
        if S in ["1", "7"]:
            X3L5 = G + type_3 + G + type_2
        elif S == "0":
            X3L5 = G + type_3 + G + type_3
        else:
            X3L5 = G + type_3 + G + type_1
        if S == "2":
            X3L6_8 = G + type_3 + G + type_4
        elif S in ["6", "8", "0"]:
            X3L6_8 = G + type_3 + G + type_3
        else:
            X3L6_8 = G + type_3 + G + type_2
        if S in ["1", "4", "7", "9"]:
            X3L9 = G + type_1 + G + type_2
        else:
            X3L9 = G + type_1 + G + type_1
    else:
        if S[0] == "1":
            if S[1] == "4":
                X3L1 = G + type_2 + G + type_3
            elif S[1] == "1":
                X3L1 = G + type_2 + G + type_2
            else:
                X3L1 = G + type_2 + G + type_1
            if S[1] in ["1", "2", "3", "7"]:
                X3L2_4 = G + type_2 + G + type_2
            elif S[1] in ["4", "8", "9", "0"]:
                X3L2_4 = G + type_2 + G + type_3
            elif S[1] in ["5", "6"]:
                X3L2_4 = G + type_2 + G + type_4
            if S[1] in ["1", "7"]:
                X3L5 = G + type_2 + G + type_2
            elif S[1] == "0":
                X3L5 = G + type_2 + G + type_3
            else:
                X3L5 = G + type_2 + G + type_1
            if S[1] == "2":
                X3L6_8 = G + type_2 + G + type_4
            elif S[1] in ["6", "8", "0"]:
                X3L6_8 = G + type_2 + G + type_3
            else:
                X3L6_8 = G + type_2 + G + type_2
            if S[1] in ["1", "4", "7", "9"]:
                X3L9 = G + type_2 + G + type_2
            else:
                X3L9 = G + type_2 + G + type_1
        else:
            if S[0] == "4":
                X3L1_1 = G + type_3 + G
            elif S[0] == "1":
                X3L1_1 = G + type_2 + G
            else:
                X3L1_1 = G + type_1 + G

            if S[0] in ["1", "2", "3", "7"]:
                X3L2_4_1 = G + type_2 + G
            elif S[0] in ["4", "8", "9", "0"]:
                X3L2_4_1 = G + type_3 + G
            elif S[0] in ["5", "6"]:
                X3L2_4_1 = G + type_4 + G

            if S[0] in ["1", "7"]:
                X3L5_1 = G + type_2 + G
            elif S[0] == "0":
                X3L5_1 = G + type_3 + G
            else:
                X3L5_1 = G + type_1 + G

            if S[0] == "2":
                X3L6_8_1 = G + type_4 + G
            elif S[0] in ["6", "8", "0"]:
                X3L6_8_1 = G + type_3 + G
            else:
                X3L6_8_1 = G + type_2 + G

            if S[0] in ["1", "4", "7", "9"]:
                X3L9_1 = G + type_2 + G
            else:
                X3L9_1 = G + type_1 + G

            if S[1] == "4":
                X3L1 = X3L1_1 + type_3
            elif S[1] == "1":
                X3L1 = X3L1_1 + type_2
            else:
                X3L1 = X3L1_1 + type_1
            if S[1] in ["1", "2", "3", "7"]:
                X3L2_4 = X3L2_4_1 + type_2
            elif S[1] in ["4", "8", "9", "0"]:
                X3L2_4 = X3L2_4_1 + type_3
            elif S[1] in ["5", "6"]:
                X3L2_4 = X3L2_4_1 + type_4
            if S[1] in ["1", "7"]:
                X3L5 = X3L5_1 + type_2
            elif S[1] == "0":
                X3L5 = X3L5_1 + type_3
            else:
                X3L5 = X3L5_1 + type_1
            if S[1] == "2":
                X3L6_8 = X3L6_8_1 + type_4
            elif S[1] in ["6", "8", "0"]:
                X3L6_8 = X3L6_8_1 + type_3
            else:
                X3L6_8 = X3L6_8_1 + type_2
            if S[1] in ["1", "4", "7", "9"]:
                X3L9 = X3L9_1 + type_2
            else:
                X3L9 = X3L9_1 + type_1


    L1 = X1L1 + G_P_1 + X2L1 + G_P_1 + X3L1

    L2_4 = X1L2_4 + G_P_2 + X2L2_4 + G_P_2 + X3L2_4

    L5 = X1L5 + G_P_1 + X2L5 + G_P_1 + X3L5

    L6_8 = X1L6_8 + G_P_2 + X2L6_8 + G_P_2 + X3L6_8

    L9 = X1L9 + G_P_1 + X2L9 + G_P_1 + X3L9


# def draw():
#     strs = "\r" + L1 + "\n" + L2_4 + "\n" + L5 + "\n" + L6_8 + "\n" + L9 + "\n"
    # 2_4 and 6_8 are both reduced to one line
#     print(f"\033[31m {strs} \033[0m", end=" ", flush=True)
    # print(f"\033[31m {L2_4} \033[0m", flush=True)
    # print(f"\033[31m {L2_4} \033[0m", flush=True)
    # print(f"\033[31m {L2_4} \033[0m", flush=True)
    # print(f"\033[31m {L5} \033[0m", flush=True)
    # print(f"\033[31m {L6_8} \033[0m", flush=True)
    # print(f"\033[31m {L6_8} \033[0m", flush=True)
    # print(f"\033[31m {L6_8} \033[0m", flush=True)
    # print(f"\033[31m {L9} \033[0m", flush=True)




if __name__ == '__main__':

    dec = ask(queList)

    STL = start()


    while True:
        read(dec)
        string = L1 + "\n" + L2_4 + "\n" + L5 + "\n" + L6_8 + "\n" + L9 + "\n"
        strs = "\r" + string
        # 2_4 and 6_8 are both reduced to one line
        # print(strs, end="", flush=True)

        print(f"\033[31m {strs} \033[0m", end="", flush=True)
        ti.sleep(1)
