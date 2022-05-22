n = eval(input("n:"))
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
