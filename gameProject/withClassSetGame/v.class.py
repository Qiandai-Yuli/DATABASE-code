from commonFunctions import commonFunction as cF
from xlutils.copy import copy
import xlrd

filepath = "/Users/mac/Desktop/ALLDATA/程序/gameProject/withClassSetGame/settings.xls"

list_1 = ["开始新游戏", "设置", "存档"]
list_1_2 = ["读取设置", "写入设置"]
list_1_3 = ["存档1", "存档2", "存档3"]



def ask(que):
    global dec
    i = 1
    string = '| '
    while i <= len(que):
        string += f"{i}-{que[i - 1]} | "
        i += 1
    cF.printwithcol(string, 0)
    dec = input("选择:")


'---------------------------------------'


class characters:
    def __init__(self, name, HP, stress, like, health):
        self.name = name
        self.HP = HP
        self.stress = stress
        self.like = like
        self.health = health


class objective:
    def __init__(self, name, amount, quality):
        self.name = name
        self.amount = amount
        self.quality = quality


class env:
    def __init__(self, name, level, knowing, amount_hc):
        self.name = name
        self.level = level
        self.knowing = knowing
        self.amount_hc = amount_hc


class bag:
    """
           bag's class
           name is substance's name (self.name)
           'bag_' + self.name is class example's name
           class function needs class example's name

    """
    sum_sort = 0
    list_name = []

    def __init__(self, name, amount, quality):
        self.name = name
        self.amount = amount
        self.quality = quality
        bag.sum_sort += 1
        bag.list_name.append("bag_" + name)

    def bagCheck(self):
        if "bag_" + self.name in bag.list_name:
            cF.printwithcol(f"{self.name}: {self.amount} {self.quality}", 0)


def bagAppend(name, amount, quality):
    bag_in_name = "bag_" + name
    globals()[bag_in_name] = bag(name, amount, quality)


'--------------------'


class font:
    def __init__(self, font, V):
        self.font = font
        self.V = V


'---------------------------------------'


def toStart():
    global dec
    global sy
    global dia
    global cho

    global k
    global yuli
    global yuqing
    global g1
    global g2
    global b1
    global b2
    global mainRole
    global food
    global water
    global firewood
    global clothes
    global camp
    global lake
    global beach
    global bay
    global anoIsland

    dec = ""
    wb = xlrd.open_workbook(filename=filepath)
    sheet = wb.sheet_by_index(0)
    k = int(sheet.cell(1, 4).value)
    readSettings(Filename=filepath)
    readArchive(k, Filename=filepath)


def readSettings(Filename=filepath):
    global sy
    global dia
    global cho

    wb = xlrd.open_workbook(filename=Filename)
    sheet = wb.sheet_by_index(0)
    sy = font(sheet.cell(1, 1).value, sheet.cell(1, 2).value)
    dia = font(sheet.cell(2, 1).value, sheet.cell(2, 2).value)
    cho = font(sheet.cell(3, 1).value, sheet.cell(3, 2).value)


def setIn():
    global sy
    global dia
    global cho
    setOut()
    wb = xlrd.open_workbook(filename=filepath)
    wb = copy(wb)
    sheet = wb.get_sheet(0)
    print("30（黑色）、31（红色）、32（绿色）、 33（黄色）、34（蓝色）、35（洋红）、36（青色）、37（白色）")
    cF.proPrint("无需更改键入'n", 0, sy.V)

    i_sy_font = input("系统字体：")
    i_sy_V = input("系统显示速度：")
    i_dia_font = input("对话字体：")
    i_dia_V = input("对话显示速度：")
    i_cho_font = input("选项字体：")
    i_cho_V = input("选项显示速度：")

    if i_sy_font != "n":
        sheet.write(1, 1, eval(i_sy_font))
    if i_sy_V != "n":
        sheet.write(1, 2, eval(i_sy_V))
    if i_dia_font != "n":
        sheet.write(2, 1, eval(i_dia_font))
    if i_dia_V != "n":
        sheet.write(2, 2, eval(i_dia_V))
    if i_cho_font != "n":
        sheet.write(3, 1, eval(i_cho_font))
    if i_cho_V != "n":
        sheet.write(3, 2, eval(i_cho_V))

    wb.save(filepath)


def setOut():
    global sy
    global dia
    global cho
    cF.proPrint(f"系统字体：{sy.font}", 0, sy.V)
    cF.proPrint(f"系统显示速度：{sy.V} s", 0, sy.V)
    cF.proPrint(f"对话字体：{dia.font}", 0, sy.V)
    cF.proPrint(f"对话显示速度：{dia.V} s", 0, sy.V)
    cF.proPrint(f"选项字体：{cho.font}", 0, sy.V)
    cF.proPrint(f"选项显示速度：{cho.V} s", 0, sy.V)


def readArchive(k, Filename=filepath):
    global yuli
    global yuqing
    global g1
    global g2
    global b1
    global b2
    global mainRole
    global food
    global water
    global firewood
    global clothes
    global camp
    global lake
    global beach
    global bay
    global anoIsland

    wb = xlrd.open_workbook(filename=Filename)
    sheet = wb.sheet_by_index(k)
    yuli = characters("yuli", sheet.cell(1, 1).value
                      , sheet.cell(1, 2).value
                      , sheet.cell(1, 3).value
                      , sheet.cell(1, 4).value)
    yuqing = characters("yuqing", sheet.cell(2, 1).value
                        , sheet.cell(2, 2).value
                        , sheet.cell(2, 3).value
                        , sheet.cell(2, 4).value)
    g1 = characters("g1", sheet.cell(3, 1).value
                    , sheet.cell(3, 2).value
                    , sheet.cell(3, 3).value
                    , sheet.cell(3, 4).value)
    g2 = characters("g2", sheet.cell(4, 1).value
                    , sheet.cell(4, 2).value
                    , sheet.cell(4, 3).value
                    , sheet.cell(4, 4).value)
    b1 = characters("b1", sheet.cell(5, 1).value
                    , sheet.cell(5, 2).value
                    , sheet.cell(5, 3).value
                    , sheet.cell(5, 4).value)
    b2 = characters("b2", sheet.cell(6, 1).value
                    , sheet.cell(6, 2).value
                    , sheet.cell(6, 3).value
                    , sheet.cell(6, 4).value)
    if sheet.cell(1, 5).value == 1:
        mainRole = 'yuli'

    food = objective("食物", sheet.cell(1, 8).value, sheet.cell(1, 9).value)
    water = objective("水", sheet.cell(2, 8).value, sheet.cell(2, 9).value)
    firewood = objective("柴火", sheet.cell(3, 8).value, sheet.cell(3, 9).value)
    clothes = objective("衣物", sheet.cell(4, 8).value, sheet.cell(4, 9).value)

    camp = env("营地", sheet.cell(1, 12).value, sheet.cell(1, 13).value, sheet.cell(1, 14).value)
    lake = env("岛中湖", sheet.cell(2, 12).value, sheet.cell(2, 13).value, sheet.cell(2, 14).value)
    beach = env("海滩", sheet.cell(3, 12).value, sheet.cell(3, 13).value, sheet.cell(3, 14).value)
    bay = env("岛湾", sheet.cell(4, 12).value, sheet.cell(4, 13).value, sheet.cell(4, 14).value)
    anoIsland = env("外岛", sheet.cell(5, 12).value, sheet.cell(5, 13).value, sheet.cell(5, 14).value)


def archiveCheck():
    global list_check
    global k
    list_check = []
    ac = 0
    strings = "| "
    wb = xlrd.open_workbook(filename=filepath)
    for ki in [1, 2, 3]:
        sheet = wb.sheet_by_index(ki)
        arc0 = sheet.cell(1, 22).value
        if arc0 == 1:
            ac += 1
            list_check.append("存档" + str(ki))
            strings += "存档" + str(ki) + " | "
    cF.proPrint(f"可用存档数为:{ac}", 0, sy.V)
    cF.proPrint(f"可用存档为:{strings}", 0, sy.V)
    cF.proPrint(f"上次使用的存档为:{'存档' + str(k)}", 0, sy.V)


def archiveOut():
    global yuli
    global yuqing
    global g1
    global g2
    global b1
    global b2
    global mainRole
    global food
    global water
    global firewood
    global clothes
    global camp
    global lake
    global beach
    global bay
    global anoIsland

    print("\033[4;32m 人物 \033[0m")
    for c in [yuli, yuqing, g1, g2, b1, b2]:
        print(c.name)
        for i in ["HP", "精神压力", "好感度", "健康值"]:
            if i == "HP":
                strs = f"{i}:{c.HP}"
            if i == "精神压力":
                strs = f"{i}:{c.stress}"
            if i == "好感度":
                strs = f"{i}:{c.like}"
            if i == "健康值":
                strs = f"{i}:{c.health}"
            cF.proPrint(strs, 0, sy.V)

    print("\033[4;32m 物品 \033[0m")
    for ob in [food, water, firewood, clothes]:
        print(ob.name)
        cF.proPrint(f"数量:{ob.amount}", 0, sy.V)
        cF.proPrint(f"品质:{ob.quality}", 0, sy.V)

    print("\033[4;32m 环境 \033[0m")
    for e in [camp, lake, beach, bay, anoIsland]:
        print(e.name)
        for i in ["等级", "探明度", "可容纳人数"]:
            if i == "等级":
                strs = f"{i}:{e.level}"
            if i == "探明度":
                strs = f"{i}:{e.knowing}"
            if i == "可容纳人数":
                strs = f"{i}:{e.amount_hc}"
            cF.proPrint(strs, 0, sy.V)


def archive():
    archiveCheck()
    cF.proPrint("选择需要读取的存档", 0, sy.V)

    ask(list_check)
    if eval(dec) > len(list_check):
        cF.proPrint("存档不存在", 0, sy.V)
        archive()
    if eval(dec) != k:
        wb = xlrd.open_workbook(filename=filepath)
        wb = copy(wb)
        sheet = wb.get_sheet(0)
        sheet.write(1, 4, eval(dec))
        wb.save(filepath)
        readArchive(eval(dec), Filename=filepath)
    archiveOut()


if __name__ == "__main__":

    toStart()

    print(type(sy.V))
    ask(list_1)

    if dec == "2":
        ask(list_1_2)
        if dec == "1":
            setOut()
        if dec == "2":
            setIn()

    if dec == "3":
        archive()
