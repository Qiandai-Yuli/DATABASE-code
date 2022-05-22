import math
from sympy import *

print("Set new inspection or use model?")
print("input 1 for new inspection and 2 for model")
c = eval(input("decision:"))
f0 = input("the name of function:")
list_f0 = [Symbol(f0)]
list_f = [f0, "="]
if c == 1:
    n = eval(input("the quantity of limits:"))
    limit_a = []
    function_a = []
    x = eval(input("value:"))
    for i in range(1, n + 1):
        limit_i = eval(input("limit_i:"))
        limit_a.append(limit_i)
        function_i = eval(input("function_i:"))
        function_a.append(function_i)
    function_i = eval(input("function_i:"))
    function_a.append(function_i)
    for i in range(1, n + 2):
        if i == 1:
            list_f0[0] = function_a[0]
        elif i == n + 1:
            list_f0[0] = function_a[-1]
        elif limit_a[i - 2] < x <= limit_a[i - 1]:
            list_f0[0] = function_a[i - 1]
        print("----", i, "----")
        print("<<<", list_f0[0], ">>>")
        print("the value of x is:", x)
        list_f.append(list_f0[0])
        if i <= n - 1:
            k0 = (limit_a[i - 1] - x) / i
            k1 = (limit_a[i] - x) / i
            print("the next limit is:", limit_a[i - 1])
            print("///WARNING/// k should be bigger than", math.ceil(k0), "and smaller than", math.ceil(k1),
                  "///WARNING///")
            k = eval(input("k:"))
            x += i * k
        elif i == n:
            k0 = (limit_a[i - 1] - x) / i
            print("the next limit is:", limit_a[i - 1])
            print("///WARNING/// k should be bigger than", math.ceil(k0), "///WARNING///")
            k = eval(input("k:"))
            x += i * k
        else:
            print("Out of the last limit.The inspection is finished.")
            print(list_f)
elif c == 2:
    print("Our model has three limits.")
    print("Four functions are:x**2,6*x-10,233-x,(x-23)**2.")
    limit1, limit2, limit3 = eval(input("lim1/2/3:"))
    x = eval(input("value:"))
    limit = [limit1, limit2, limit3]
    for i in range(1, 5):
        if x <= limit1:
            list_f0[0] = x ** 2
        elif x <= limit2:
            list_f0[0] = 6 * x - 10
        elif x <= limit3:
            list_f0[0] = 233 - x
        else:
            list_f0[0] = (x - 23) ** 2
        print("----", i, "----")
        print("<<<", list_f0[0], ">>>")
        print("the value of x is:", x)
        list_f.append(list_f0[0])
        if i <= len(limit) - 1:
            k0 = (limit[i - 1] - x) / i
            k1 = (limit[i] - x) / i
            print("the next limit is:", limit[i - 1])
            print("///WARNING/// k should be bigger than", k0, "and smaller than", k1,
                  "///WARNING///")
            k = eval(input("k:"))
            x += i * k
        elif i == len(limit):
            k0 = (limit[i - 1] - x) / i
            print("the next limit is:", limit[i - 1])
            print("///WARNING/// k should be bigger than", k0, "///WARNING///")
            k = eval(input("k:"))
            x += i * k
        else:
            print("Out of limit3.The inspection is finished.")
            print(list_f)
