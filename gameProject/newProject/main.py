#import xlutils as xlu
from xlutils.copy import copy
import xlrd

# 显示方式:  0（默认）、1（高亮）、22（非粗体）、4（下划线）、24（非下划线）、 5（闪烁）、25（非闪烁）、7（反显）、27（非反显）
# 前景色:   30（黑色）、31（红色）、32（绿色）、 33（黄色）、34（蓝色）、35（洋红）、36（青色）、37（白色）
# 背景色:   40（黑色）、41（红色）、42（绿色）、 43（黄色）、44（蓝色）、45（洋红）、46（青色）、47（白色）
# \033[显示方式；背景色；前景色  m (数字无重复 不改可不写)
# \033[0m 结尾

#\033[{list_type[0]};{list_type[1]};{list_type[2]}m



filepath = "/Users/mac/Desktop/ALLDATA/程序/new project/setting.xls"

#选择列
list_dec_x__0 = ["开始新游戏", "设置", "读取存档"]
list_dec_2__3 = []
list_dec_2__4 = ["是", "否"]
list_dec_1__1 = ["字体"]
list_dec_1_1__2 = ["系统字体","对话字体","操作字体"]
list_dec_0__5 = ["存档一", "存档二", "存档三"]


List = [list_dec_x__0, list_dec_1__1,list_dec_1_1__2,list_dec_2__3,list_dec_2__4,list_dec_0__5]

#type列
list_type_s__0 = []
list_type_d__1 = []
list_type_o__2 = []

List_type = [list_type_s__0, list_type_d__1, list_type_o__2]




#存档

List_archive = [1, 2, 3]

#人物

main_like_1 = 0.5
main_like_0 = 0.5

dic_yuli = {"HP":100,"stress":0,"like":main_like_1,"health":100,"mainornot":True}
dic_yuqing = {"HP":100, "stress":0, "like":main_like_0, "health":100, "mainornot":False}
dic_fe1 = {"HP":100,"stress":0,"like":0.5,"health":100}
dic_fe2 = {"HP":100,"stress":0,"like":0.5,"health":100}
dic_me1 = {"HP":100,"stress":0,"like":0.5,"health":100}
dic_me2 = {"HP":100,"stress":0,"like":0.5,"health":100}

List_characterValueinC = ["体力", "精神压力", "好感度", "健康指数"]
List_characterValue = ["HP", "stress", "like", "health"]
List_characterName = ["yuli", "yuqing", "fe1", "fe2", "me1", "me2"]
List_character = [dic_yuli, dic_yuqing, dic_fe1, dic_fe2, dic_me1, dic_me2]

#物品

dic_food = {"amount":0, "quality":0}
dic_water = {"amount":0, "quality":0}
dic_firewood = {"amount":0, "quality":0}
dic_clothes = {"amount":0, "quality":0}

List_objectValueinC =["数量", "质量"]
List_objectValue = ["amount", "quality"]
List_objectName = ["食物", "水", "柴火", "衣物"]
List_object = [dic_food, dic_water, dic_firewood, dic_clothes]

#环境

dic_camp = {"level":"lv.0","knowing":"你对营地了如指掌","amount_humancan":3}
dic_lake = {"level":"lv.0","knowing":0,"amount_humancan":3}
dic_beach = {"level":"lv.0","knowing":0}
dic_bay = {"level":"lv.0","knowing":0}
dic_anotherisland = {"level":"lv.0","knowing":0,"amount_humancan":1}

List_environmentValueinC = ["等级", "探明度", "可容纳人数"]
List_environmentValue = ["level", "knowing", "amount_humancan"]
List_environmentName = ["营地", "岛中湖", "海滩", "海湾", "外岛"]
List_environment = [dic_camp, dic_lake, dic_beach, dic_bay, dic_anotherisland]
#背包

global alreadybringkg
global alreadybringamount

dic_1 = {"name":"None","amount":0,"singleweight":0}
dic_2 = {"name":"None","amount":0,"singleweight":0}
dic_3 = {"name":"None","amount":0,"singleweight":0}
dic_4 = {"name":"None","amount":0,"singleweight":0}
dic_5 = {"name":"None","amount":0,"singleweight":0}
dic_6 = {"name":"None","amount":0,"singleweight":0}
dic_7 = {"name":"None","amount":0,"singleweight":0}
dic_8 = {"name":"None","amount":0,"singleweight":0}
dic_9 = {"name":"None","amount":0,"singleweight":0}
dic_10 = {"name":"None","amount":0,"singleweight":0}

List_bagValueinC = ["名称", "数量", "单重"]
List_bagValue = ["name", "amount", "singleweight"]
List_bag = [dic_1, dic_2, dic_3, dic_4, dic_5, dic_6, dic_7, dic_8, dic_9, dic_10]
#序记录
list_choicerecord = []

def list_str(list_choicerecord):
    global list_str
    i = 0
    try:
        while i <= len(list_choicerecord)-1:
            list_str = str(list_choicerecord[i])
            i += 1
        return list_str
    except UnboundLocalError:
        print("序不存在")


def start():
    #字体部分

    global s_back
    global s_forw
    global s_dis
    global d_back
    global d_dis
    global d_forw
    global o_back
    global o_dis
    global o_forw
    global List_type
    global list_archiveExsist
    global c_archive

    wb = xlrd.open_workbook(filename=filepath)
    sheet = wb.sheet_by_index(0)
    s_dis = eval(sheet.cell(3, 2).value)
    s_forw = eval(sheet.cell(3, 4).value)
    s_forw_T = 33
    if sheet.cell(3, 6).value != "None":
        s_back = eval(sheet.cell(3, 6).value)
    else:
        s_back = ""

    d_dis = eval(sheet.cell(4, 2).value)
    d_forw = eval(sheet.cell(4, 4).value)
    if sheet.cell(4, 6).value != "None":
        d_back = eval(sheet.cell(4, 6).value)
    else:
        d_back = ""

    o_dis = eval(sheet.cell(5, 2).value)
    o_forw = eval(sheet.cell(5, 4).value)
    if sheet.cell(5, 6).value != "None":
        o_back = eval(sheet.cell(5, 6).value)
    else:
        o_back = ""
    list_type_s__0.append(s_dis)
    list_type_s__0.append(s_forw)
    list_type_s__0.append(s_back)
    list_type_s__0.append(s_forw_T)
    list_type_d__1.append(d_dis)
    list_type_d__1.append(d_forw)
    list_type_d__1.append(d_back)
    list_type_o__2.append(o_dis)
    list_type_o__2.append(o_forw)
    list_type_o__2.append(o_back)
    #存档部分
    wb = xlrd.open_workbook(filename=filepath)
    sheet = wb.sheet_by_index(0)
    list_archiveExsist = []
    if sheet.cell(15, 0).value != 0:
        list_archiveExsist.append("1")
    if sheet.cell(50, 0).value != 0:
        list_archiveExsist.append("2")
    if sheet.cell(85, 0).value != 0:
        list_archiveExsist.append("3")
    c_archive = len(list_archiveExsist)
    list_dec_2__3 = list_archiveExsist
    List[3] = list_dec_2__3



def proPrint(contentType,highlightornot,content):

    if contentType == "dia":
        list_type = List_type[1]
        if highlightornot == True:
            disType = 1
        else:
            disType = list_type[0]
        if list_type[2] != "":
            conj = ";"
        else:
            conj = ""
        print(f"\033[{disType};{list_type[1]}{conj}{list_type[2]}m {content} \033[0m")

    if contentType == "sy":
        list_type = List_type[0]
        if highlightornot == True:
            disType = 1
        else:
            disType = list_type[0]
        if list_type[2] != "":
            conj = ";"
        else:
            conj = ""
        print(f"\033[{disType};{list_type[1]}{conj}{list_type[2]}m {content} \033[0m")

    if contentType == "syt":
        list_type = List_type[0]
        disType = 1
        if list_type[2] != "":
            conj = ";"
        else:
            conj = ""
        print(f"\033[{disType};{list_type[3]}{conj}{list_type[2]}m {content} \033[0m")



def ask(que,n_list_dec,n_list_type):
    global dec
    list_decChoice = List[n_list_dec]
    list_type = List_type[n_list_type]
    if list_type[2] != "":
        conj = ";"
    else:
        conj = ""

    c_dec = len(list_decChoice)
    print(f"\033[1;{list_type[1]}m {que} \033[0m")
    i = 1
    while i <= c_dec:
        if i != c_dec:
            ending = " / "
        else:
            ending = "\n"
        print(f"\033[{list_type[0]};{list_type[1]}{conj}{list_type[2]}m {i}-{list_decChoice[i - 1]} \033[0m", end=ending)
        i += 1
    inp = input("选择:")
    if inp in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        dec = eval(inp)
    else:
        dec = inp


def set():
    ask("设置类型", 1, 0)
    if dec == 1:
        ask("设置类型", 2, 0)
        if dec == 1:
            print(" 显示方式:  0（默认）、1（高亮）、22（非粗体）、4（下划线）、24（非下划线）、 5（闪烁）、25（非闪烁）、7（反显）、27（非反显)")
            print(" 前景色:   30（黑色）、31（红色）、32（绿色）、 33（黄色）、34（蓝色）、35（洋红）、36（青色）、37（白色）")
            print(" 背景色:   40（黑色）、41（红色）、42（绿色）、 43（黄色）、44（蓝色）、45（洋红）、46（青色）、47（白色)")
            wb = xlrd.open_workbook(filename=filepath)
            wb = copy(wb)
            sheet = wb.get_sheet(0)
            sheet.write(3, 2, input("系统字体显示方式："))
            sheet.write(3, 4, input("系统字体前景色："))
            sheet.write(3, 6, input("系统字体背景色(非必须填入None)："))
            wb.save(filepath)
        elif dec == 2:
            print(" 显示方式:  0（默认）、1（高亮）、22（非粗体）、4（下划线）、24（非下划线）、 5（闪烁）、25（非闪烁）、7（反显）、27（非反显)")
            print(" 前景色:   30（黑色）、31（红色）、32（绿色）、 33（黄色）、34（蓝色）、35（洋红）、36（青色）、37（白色）")
            print(" 背景色:   40（黑色）、41（红色）、42（绿色）、 43（黄色）、44（蓝色）、45（洋红）、46（青色）、47（白色)")
            wb = xlrd.open_workbook(filename=filepath)
            wb = copy(wb)
            sheet = wb.get_sheet(0)
            sheet.write(4, 2, input("对话字体显示方式："))
            sheet.write(4, 4, input("对话字体前景色："))
            sheet.write(4, 6, input("对话字体背景色(非必须填入None)："))
            wb.save(filepath)
        elif dec == 3:
            print(" 显示方式:  0（默认）、1（高亮）、22（非粗体）、4（下划线）、24（非下划线）、 5（闪烁）、25（非闪烁）、7（反显）、27（非反显)")
            print(" 前景色:   30（黑色）、31（红色）、32（绿色）、 33（黄色）、34（蓝色）、35（洋红）、36（青色）、37（白色）")
            print(" 背景色:   40（黑色）、41（红色）、42（绿色）、 43（黄色）、44（蓝色）、45（洋红）、46（青色）、47（白色)")
            wb = xlrd.open_workbook(filename=filepath)
            wb = copy(wb)
            sheet = wb.get_sheet(0)
            sheet.write(5, 2, input("操作字体显示方式："))
            sheet.write(5, 4, input("操作字体前景色："))
            sheet.write(5, 6, input("操作字体背景色(非必须填入None)："))
            wb.save(filepath)



def archive_display():
    proPrint("syt", True, "人物")
    if dic_yuli["mainornot"]:
        proPrint("sy", False, "yuli是主人公")
    else:
        proPrint("sy", False, "yuqing是主人公")
    i = 0
    while i <= 5:
        proPrint("syt", True, List_characterName[i])
        j = 0
        while j <= 3:
            proPrint("sy", False, f"{List_characterValueinC[j]}:{List_character[i][List_characterValue[j]]}")
            j += 1
        i += 1

    proPrint("syt", True, "物品")
    i = 0
    while i <= 3:
        proPrint("syt", True, List_objectName[i])
        j = 0
        while j <= 1:
            proPrint("sy", False, f"{List_objectValueinC[j]}:{List_object[i][List_objectValue[j]]}")
            j += 1
        i += 1

    proPrint("syt", True, "环境")
    i = 0
    while i <= 4:
        proPrint("syt", True, List_environmentName[i])
        j = 0
        while j <= 1:
            proPrint("sy", False, f"{List_environmentValueinC[j]}:{List_environment[i][List_environmentValue[j]]}")
            j += 1
        if i in [0, 1, 4]:
            proPrint("sy", False, f"{List_environmentValueinC[2]}:{List_environment[i][List_environmentValue[2]]}")
        i += 1

    proPrint("syt", True, "背包")
    i = 0
    while i <= 9:
        proPrint("syt", True, List_bag[i]["name"])
        j = 1
        while j <= 2:
            proPrint("sy", False, f"{List_bagValueinC[j]}:{List_bag[i][List_bagValue[j]]}")
            j += 1
        i += 1
    proPrint("sy", True, f"剩余可容纳数:{alreadybringamount}")
    proPrint("sy", True, f"剩余可容纳千克数:{alreadybringkg}")


def archive_read(list_archiveExsist):
    global alreadybringamount
    global alreadybringkg
    wb = xlrd.open_workbook(filename=filepath)
    sheet = wb.sheet_by_index(0)
    if c_archive != 0:
        proPrint("sy", False, f"存档数为{c_archive}")
        proPrint("sy",False,"存在以下存档:")
        i = 0
        while i <= c_archive-1:
            proPrint("sy",False,list_archiveExsist[i])
            i += 1
        ask("选择想要查看的存档",3,0)
        # characters
        i = 0
        while i <= 5:
            List_character[i]["HP"] = sheet.cell(eval(list_archiveExsist[dec-1]) * 35 - 21 + i + 1,3).value
            i += 1

        i = 0
        while i <= 5:
            List_character[i]["stress"] = sheet.cell(eval(list_archiveExsist[dec-1]) * 35 - 21 + i + 1, 4).value
            i += 1

        i = 0
        while i <= 5:
            List_character[i]["like"] = sheet.cell(eval(list_archiveExsist[dec-1]) * 35 - 21 + i + 1, 5).value
            i += 1

        i = 0
        while i <= 5:
            List_character[i]["health"] = sheet.cell(eval(list_archiveExsist[dec-1]) * 35 - 21 + i + 1, 6).value
            i += 1

        # objects
        i = 0
        while i <= 3:
            List_object[i]["amount"] = sheet.cell(eval(list_archiveExsist[dec-1]) * 35 - 21 + i + 8, 3).value
            i += 1

        while i <= 3:
            List_object[i]["quality"] = sheet.cell(eval(list_archiveExsist[dec-1]) * 35 - 21 + i + 8, 3).value
            i += 1

        if sheet.cell(eval(list_archiveExsist[dec-1]) * 35 - 21 + 1, 7).value == 1:
            dic_yuli["mainornot"] = True
            dic_yuqing["mainornot"] = False
        else:
            dic_yuli["mainornot"] = False
            dic_yuqing["mainornot"] = True

        #environment
        i = 0
        while i <= 4:
            List_environment[i]["level"] = sheet.cell(List_archive[dec - 1] * 35 - 21 + i + 13, 3).value
            i += 1

        while i <= 4:
            List_environment[i]["knowing"] = sheet.cell(List_archive[dec - 1] * 35 - 21 + i + 13, 4).value
            i += 1

        for num in [0, 1, 4]:
            List_environment[num]["amount_humancan"] = sheet.cell(List_archive[dec - 1] * 35 - 21 + num + 13, 5).value

        #bag

        i = 0
        while i <= 9:
            List_bag[i]["name"] = sheet.cell(List_archive[dec - 1] * 35 - 21 + i + 22, 2).value
            i += 1

        i = 0
        while i <= 9:
            List_bag[i]["amount"] = sheet.cell(List_archive[dec - 1] * 35 - 21 + i + 22, 3).value
            i += 1

        i = 0
        while i <= 9:
            List_bag[i]["singleweight"] = sheet.cell(List_archive[dec - 1] * 35 - 21 + i + 22, 4).value
            i += 1

        alreadybringkg = sheet.cell(List_archive[dec - 1] * 35 - 21 + 23, 0).value
        alreadybringamount = sheet.cell(List_archive[dec - 1] * 35 - 21 + 25, 0).value
#

        proPrint("syt",True,f"存档{list_archiveExsist[dec-1]}")

#

        archive_display()



    else:
        proPrint("sy", False, "不存在可用存档")


    if c_archive > 1:
        ask("查看其他存档？", 4, 0)
        if dec == 1:
            archive_read(list_archiveExsist=list_archiveExsist)

        else:
            pass

    t = 0
    ask("读取哪一存档？", 3, 0)
    i = 0
    while i <= 5:
        List_character[i]["HP"] = sheet.cell(List_archive[dec - 1] * 35 - 21 + i + 1, 3).value
        i += 1

    i = 0
    while i <= 5:
        List_character[i]["stress"] = sheet.cell(List_archive[dec - 1] * 35 - 21 + i + 1, 4).value
        i += 1

    i = 0
    while i <= 5:
        List_character[i]["like"] = sheet.cell(List_archive[dec - 1] * 35 - 21 + i + 1, 5).value
        i += 1

    i = 0
    while i <= 5:
        List_character[i]["health"] = sheet.cell(List_archive[dec - 1] * 35 - 21 + i + 1, 6).value
        i += 1

    # objects
    i = 0
    while i <= 3:
        List_object[i]["amount"] = sheet.cell(List_archive[dec - 1] * 35 - 21 + i + 8, 3).value
        i += 1

    while i <= 3:
        List_object[i]["quality"] = sheet.cell(List_archive[dec - 1] * 35 - 21 + i + 8, 3).value
        i += 1

    if sheet.cell(List_archive[dec - 1] * 35 - 21 + 1, 7).value == 1:
        dic_yuli["mainornot"] = True
        dic_yuqing["mainornot"] = False
    else:
        dic_yuli["mainornot"] = False
        dic_yuqing["mainornot"] = True

    # environment
    i = 0
    while i <= 4:
        List_environment[i]["level"] = sheet.cell(List_archive[dec - 1] * 35 - 21 + i + 13, 3).value
        i += 1

    while i <= 4:
        List_environment[i]["knowing"] = sheet.cell(List_archive[dec - 1] * 35 - 21 + i + 13, 4).value
        i += 1

    for num in [0, 1, 4]:
        List_environment[num]["amount_humancan"] = sheet.cell(List_archive[dec - 1] * 35 - 21 + num + 13,
                                                              5).value

    # bag

    i = 0
    while i <= 9:
        List_bag[i]["name"] = sheet.cell(List_archive[dec - 1] * 35 - 21 + i + 22, 2).value
        i += 1

    i = 0
    while i <= 9:
        List_bag[i]["amount"] = sheet.cell(List_archive[dec - 1] * 35 - 21 + i + 22, 3).value
        i += 1

    i = 0
    while i <= 9:
        List_bag[i]["singleweight"] = sheet.cell(List_archive[dec - 1] * 35 - 21 + i + 22, 4).value
        i += 1

    alreadybringkg = sheet.cell(List_archive[dec - 1] * 35 - 21 + 23, 0).value
    alreadybringamount = sheet.cell(List_archive[dec - 1] * 35 - 21 + 25, 0).value
    t += 1
    if t == 1:
        exit()

# noinspection PySimplifyBooleanCheck
def archive_save():
    wb = xlrd.open_workbook(filename=filepath, formatting_info=True)
    wb_r = copy(wb)
    wb_w = wb_r.get_sheet(0)

    ask("选择保存的位置：", 5, 0)

    # characters
    wb_w.write(List_archive[dec - 1] * 35 - 21 + 1, 0, 1)
    i = 0
    while i <= 5:
        print(List_archive[dec - 1] * 35 - 21 + i + 1)
        wb_w.write(List_archive[dec - 1] * 35 - 21 + i + 1, 3,List_character[i]['HP'])
        i += 1

    i = 0
    while i <= 5:
        wb_w.write(List_archive[dec - 1] * 35 - 21 + i + 1, 4,List_character[i]["stress"])
        i += 1

    i = 0
    while i <= 5:
        wb_w.write(List_archive[dec - 1] * 35 - 21 + i + 1, 5,List_character[i]["like"])
        i += 1

    i = 0
    while i <= 5:
        wb_w.write(List_archive[dec - 1] * 35 - 21 + i + 1, 6,List_character[i]["health"])
        i += 1

    # objects
    i = 0
    while i <= 3:
        wb_w.write(List_archive[dec - 1] * 35 - 21 + i + 8, 3, List_object[i]["amount"])
        i += 1

    while i <= 3:
        wb_w.write(List_archive[dec - 1] * 35 - 21 + 1, 7, 1)
        i += 1

    if dic_yuli["mainornot"] == True:
        wb_w.write(List_archive[dec - 1] * 35 - 21 + 1, 7, 1)
    else:
        wb_w.write(List_archive[dec - 1] * 35 - 21 + 1, 7, 0)
    # environment
    i = 0
    while i <= 4:
        wb_w.write(List_archive[dec - 1] * 35 - 21 + i + 13, 3, List_environment[i]["level"])
        i += 1

    while i <= 4:
        wb_w.write(List_archive[dec - 1] * 35 - 21 + i + 13, 4, List_environment[i]["knowing"])
        i += 1

    for num in [0, 1, 4]:
        wb_w.write(List_archive[dec - 1] * 35 - 21 + num + 13, 5, List_environment[num]["amount_humancan"])


    # bag

    i = 0
    while i <= 9:
        wb_w.write(List_archive[dec - 1] * 35 - 21 + i + 22, 2, List_bag[i]["name"])
        i += 1

    i = 0
    while i <= 9:
        wb_w.write(List_archive[dec - 1] * 35 - 21 + i + 22, 3, List_bag[i]["amount"])
        i += 1

    i = 0
    while i <= 9:
        wb_w.write(List_archive[dec - 1] * 35 - 21 + i + 22, 4, List_bag[i]["singleweight"])
        i += 1

    wb_w.write(List_archive[dec - 1] * 35 - 21 + 23, 0, alreadybringkg)      #
    wb_w.write(List_archive[dec - 1] * 35 - 21 + 25, 0, alreadybringamount)  #
    wb_r.save(filepath)


#














if __name__ == '__main__':
    start()
    dec = 0
    ask("选择操作", 0, 0)
    if dec == 2:
        set()
    elif dec == 3:
        # noinspection PyUnboundLocalVariable
        archive_read(list_archiveExsist=list_archiveExsist)
    ask("是否存档：",4,0)
    if dec == 1:
        archive_save()

#开发日志
#注意：xlutils引用脱离   #if isinstance(inp, str):           # 表达式中判断变量的类型并返回TorF
#已完成：设置与存档文件部分读写基础、ask（）函数各类型普适性改造、初始化函数start（）函数基础、属性字典库、存档读与写
#待完成：无
#下一步：构造主体