import os
import time

#    r+ :可读、可写，文件不存在也会报错，写操作时会覆盖
#    w+ :可读，可写，文件不存在先创建，会覆盖
#    a+ :可读、可写，文件不存在先创建，不会覆盖，追加在末尾
#    os.remove(path)  # path是文件的路径，如果这个路径是一个文件夹，则会抛出OSError的错误，这时需用用rmdir()来删除
#    os.rmdir(path)  # path是文件夹路径，注意文件夹需要时空的才能被删除
#    file = open("test.txt", 'w').close()   清空文件内容
#    shutil.rmtree()函数能够直接删除一个文件夹，不管里面有没有内容！

def file_write():
    #path = input("可写入文件的路径：")
    bol1 = os.path.exists(path)
    bol2 = os.path.isfile(path)
    if bol1 == False and bol2 == False:
        print("路径不存在")
        time.sleep(2)
        quit()
    elif not bol2:
        print("文件不存在，自动创建文件")

    file = open(path, "a+")
    while True:
        print("是否换行？")
        dec1 = eval(input("1-是 2-否："))
        if dec1 == 1:
            file.writelines("\n")     # 实现换行输入
            file.writelines(input("输入内容："))
        else:
            file.write(input("输入内容："))
        print("继续写入？")
        dec2 = eval(input("1-是 2-否："))
        if dec2 == 1:
            pass
        else:
            file.close()
            break

def file_output():
    #path = input("待输出文件的路径：")
    file = open(path, "r")
    print("读取方式")
    dec3 = eval(input("1-全部读取 2-读取指定行数 3-读取指定单元格 ...:"))
    if dec3 == 1:
        print(file.read())
    elif dec3 == 2:
        n = eval(input("读取行数："))
        print(file.readlines(n))
    elif dec3 == 3:
        rowx = eval(input("行索引："))
        colx = eval(input("列索引："))
        print(file.cell(rowx, colx))
    file.close()

def operate():
    while True:
        global path
        path = input("待操作的路径：")
        incheck = bool(".txt" in path)
        if os.path.exists(path) == False and incheck == False:
            print("路径不存在,即将退出")
            time.sleep(2)
            quit()
        elif os.path.exists(path) == False and incheck == True:
            print("检测", path, "为不存在的文本文件，自动创建")
            file = open(path, "a+")
            file.close()

        print("选取操作类型")
        dec4 = eval(input("1-写入 2-读取 3-清空 4-删除 ...:"))
        if dec4 == 1:
            file_write()
        elif dec4 == 2:
            file_output()
        elif dec4 == 3:
            file = open(path, "w")
            file.close()
        elif dec4 == 4:
            if os.path.isfile(path):
                os.remove(path)
            else:
                os.rmdir(path)
        print("继续操作？")
        dec5 = eval(input("1-继续 2-退出："))
        if dec5 == 1:
            pass
        else:
            time.sleep(2)
            quit()


if __name__ == '__main__':
    print("文件操作程序")
    operate()

    # /Users/mac/Desktop/ALLDATA/程序/文件/file_test
