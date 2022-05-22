from sympy import *

list_v = []
list_f = []
list_a = []
print("if you want to solve the equations or find out the limit?")
print("input 1 for equations and 2 for limit")
de1 = eval(input("decision:"))
if de1 == 1:
    nun = eval(input("the count of the value:"))
    for i in range(0, nun):
        if i == nun:
            pass
        else:
            list_v.append(input("the name of value:"))
            list_v[i] = Symbol(list_v[i])
    for i in range(0, nun):
        if i == nun:
            pass
        else:
            print("the equations only receive '***==0' form and leave the '==0'")
            list_f.append(input("the equations:"))
    list_a.append(solve(list_f, list_v))
    print(list_a)
elif de1 == 2:
    list_f0 = [Symbol(input("the name of function:"))]
    list_v = [Symbol(input("the name of the value:"))]
    print("the function only receives '* = ****' form and leave'* = '")
    list_f = [input("the function:")]
    list_f0[0] = list_f[0]
    de2 = input("left limit or right limit or the limit at some point?")
    if de2 == "right limit":
        list_a = [limit(list_f0[0], list_v[0], 00)]
    elif de2 == "left limit":
        list_a = [limit(list_f0[0], list_v[0], -00)]
    else:
        z0 = eval(input("the point to take limit:"))
        list_a = [limit(list_f[0], list_v[0], z0, dir="+")]
    print(list_a)
