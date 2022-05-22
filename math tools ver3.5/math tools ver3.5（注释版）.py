from sympy import *

list_v = []
list_f = []
list_a = []
print("equations or limit or prime?")
#选择工具功能：方程，极限，质数
print("1 for equations,2 for limit,3 for prime")
de1 = eval(input("decision:"))
#询问选择
if de1 == 1:
    nun = eval(input("the count of the value:"))
    #询问变量数
    for i in range(0, nun):
        if i == nun:
            pass
        else:
            list_v.append(input("the name of value:"))
            #询问变量名
            list_v[i] = Symbol(list_v[i])
    for i in range(0, nun):
        if i == nun:
            pass
        else:
            print("the equations only receive '***==0' form and leave the '==0'")
            #“方程只接受‘***==0’并省略’==0‘的形式”
            list_f.append(input("the equations:"))
            #提示输入方程
    list_a.append(solve(list_f, list_v))
    print(list_a)
elif de1 == 2:
    list_f0 = [Symbol(input("the name of function:"))]
    #询问函数名
    list_v = [Symbol(input("the name of the value:"))]
    #询问变量名
    print("the function only receives '* = ****' form and leave'* = '")
    #函数只接受‘* = ****’并省略‘* = ’的形式
    list_f = [input("the function:")]
    #提示输入函数
    list_f0[0] = list_f[0]
    de2 = input("left limit or right limit or the limit at some point?")
    #询问所求为左极限，右极限还是某点的极限
    if de2 == "right limit":
        list_a = [limit(list_f0[0], list_v[0], 00)]
    elif de2 == "left limit":
        list_a = [limit(list_f0[0], list_v[0], -00)]
    else:
        z0 = eval(input("the point to take limit:"))
        #提示输入求极限的点
        list_a = [limit(list_f[0], list_v[0], z0, dir="+")]
    print(list_a)
elif  de1 == 3:
    print("if you want to find primes from '0' or other number?")
    #询问从0寻找质数还是在某区间寻找质数
    print("1 for '0' and 2 for other number")
    de3=eval(input("decision:"))
    #同上
    if de3==1:
        n = eval(input("the value of n(stop number):"))
        #从0寻找的终止数
        i = 4
        c = 2
        list_p = [3]
        list_t = []
        while i <= n:
            if c == i - 1:
                list_p.append(i)
                i += 1
                c = 2
                continue
            if 0 in list_t:
                i += 1
                c = 2
                list_t = []
            else:
                if i % c == 0:
                    list_t.append(0)
                else:
                    c += 1
        print(list_p)
    elif de3==2:
        m=eval(input("the value of m(strat number):"))
        n = eval(input("the value of n(stop number):"))
        ##某区间的起点和终点
        i = m
        c = 2
        list_p = []
        list_t = []
        while i <= n:
            if c == i - 1:
                list_p.append(i)
                i += 1
                c = 2
                continue
            if 0 in list_t:
                i += 1
                c = 2
                list_t = []
            else:
                if i % c == 0:
                    list_t.append(0)
                else:
                    c += 1
        print(list_p)

    
