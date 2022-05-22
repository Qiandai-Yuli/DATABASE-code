#!/usr/bin/env python3
import time as t

ms = 0
s = 0
m = 0
h = 0

if __name__ == '__main__':

    while True:
        ms += 1
        if ms >= 100:
            ms -= 100
            s += 1
        if s >= 60:
            s -= 60
            m += 1
        if m >= 60:
            m -= 1
            h += 1

        if len(str(h)) == 1:
            H = "0" + str(h)
        else:
            H = str(h)

        if len(str(m)) == 1:
            M = "0" + str(m)
        else:
            M = str(m)

        if len(str(s)) == 1:
            S = "0" + str(s)
        else:
            S = str(s)

        if len(str(ms)) == 1:
            MS = "0" + str(ms)
        else:
            MS = str(ms)

        times_0 = H + ":" + M + ":" + S + "." + MS

        times = "\r" + times_0

        print(f"\033[36m {times} \033[0m", end="", flush=True)

        t.sleep(0.01)

