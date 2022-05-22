#!/usr/bin/env python3
import time as t
import datetime


def start():

    now_0_hour = int(datetime.datetime.now().hour)
    now_0_minute = int(datetime.datetime.now().minute)
    now_0_second = int(datetime.datetime.now().second)
    # print(str(datetime.datetime.now().microsecond)[0:2])
    now_0_microsecond = int(str(datetime.datetime.now().microsecond)[0:2])
    STL_0 = [now_0_hour, now_0_minute, now_0_second, now_0_microsecond]
    return STL_0


def counter(startTimeList):
    count_hour = int(datetime.datetime.now().hour) - startTimeList[0]
    if count_hour > 0:
        count_hour -= 1
        count_minute = int(datetime.datetime.now().minute) + 60 - startTimeList[1]
    else:
        count_minute = int(datetime.datetime.now().minute) - startTimeList[1]

    if count_minute > 0:
        count_minute -= 1
        count_second = int(datetime.datetime.now().second) + 60 - startTimeList[2]
    else:
        count_second = int(datetime.datetime.now().second) - startTimeList[2]

    if count_second > 0:
        count_second -= 1
        count_microsecond = int(str(datetime.datetime.now().microsecond)[0:2]) + 100 - startTimeList[3]
    else:
        count_microsecond = int(str(datetime.datetime.now().microsecond)[0:2]) - startTimeList[3]

    if count_microsecond >= 100:
        count_microsecond -= 100
        count_second += 1
    if count_second >= 60:
        count_second -= 60
        count_minute += 1
    if count_minute >= 60:
        count_minute -= 60
        count_hour += 1


    if len(str(count_microsecond)) == 1:
        str_microsecond = "0" + str(count_microsecond)
    else:
        str_microsecond = str(count_microsecond)


    if len(str(count_hour)) == 1:
        str_hour = "0" + str(count_hour)
    else:
        str_hour = str(count_hour)

    if len(str(count_minute)) == 1:
        str_minute = "0" + str(count_minute)
    else:
        str_minute = str(count_minute)

    if len(str(count_second)) == 1:
        str_second = "0" + str(count_second)
    else:
        str_second = str(count_second)

    now = str_hour + ":" + str_minute + ":" + str_second + "." + str_microsecond

    return now



if __name__ == '__main__':




    STL = start()

    while True:

        NOW = "\r" + counter(startTimeList=STL)
        print(f"\033[36m {NOW} \033[0m", end="", flush=True)
        t.sleep(0.01)


