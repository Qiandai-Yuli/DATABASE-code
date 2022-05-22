#!/usr/bin/env python3
import datetime
import time as t


def clock():
    now = datetime.datetime.now()
    if len(str(now.hour)) == 1:
        hour = "0" + str(now.hour)
    else:
        hour = str(now.hour)
    if len(str(now.minute)) == 1:
        minute = "0" + str(now.minute)
    else:
        minute = str(now.minute)
    if len(str(now.second)) == 1:
        second = "0" + str(now.second)
    else:
        second = str(now.second)
    time_0 = hour + ":" + minute + ":" + second + "." + str(now.microsecond)[0:2]
    time_ = "\r" + time_0
    print(f"\033[36m {time_} \033[0m", end="", flush=True)
    t.sleep(0.01)





if __name__ == '__main__':

    # print(time_0)
    # print(now.microsecond, str(now.microsecond)[0:2])
    while True:
        clock()
