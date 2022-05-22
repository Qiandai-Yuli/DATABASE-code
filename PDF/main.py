from PyPDF2 import PdfFileReader, PdfFileWriter
import platform
import os
import time

list0 = ["连续", "分散"]

list_p = []


def printwithcol(cont, highlight):
    """
    highlight == 1, none == 0
    """

    print(f"\033[{highlight};36m {cont} \033[0m")


def ask(que):
    i = 1
    string = '| '
    while i <= len(que):
        string += f"{i}-{que[i - 1]} | "
        i += 1
    printwithcol(string, 0)
    decs = input("选择:")
    return decs


def countDown(secs):
    c = secs - 1
    while 0 <= c <= secs:
        num = "\r" + str(c)
        print(num, end='', flush=True)
        c -= 1
        time.sleep(1)
    print("\r")



def pdf_spilter(pdfIn, pdfOut, list_page):
    output = PdfFileWriter()

    with open(pdfIn, "rb") as oriPdf:
        file_pdf = PdfFileReader(oriPdf)
        try:
            for i in list_page:
                output.addPage(file_pdf.getPage(i - 1))
        except IndexError:
            printwithcol("错误:原文件不存在某些页数", 0)

        with open(pdfOut, "ab") as newPdf:
            output.write(newPdf)


if __name__ == '__main__':

    if platform.system() == "Windows":
        inPath = input("原文件名称:")
        outPath = input("新文件名称:")
        if not os.path.exists(inPath):
            printwithcol("请先将文件置于程序同一目录下再启动程序！", 1)
            countDown(3)
            quit()
    if platform.system() == "Darwin":
        inPath = input("原文件绝对路径:")
        checker = list(inPath)
        k = 1
        while k <= len(checker):
            # print(checker[-1])
            if checker[-1] != "/":
                checker = checker[:-1]
                k += 1
            else:
                break
        outPath_newDir = ""
        ln = 0
        while ln <= len(checker) - 1:
            outPath_newDir = outPath_newDir + checker[ln]
            ln += 1

        outPath_name = input("新文件名称:")
        outPath = outPath_newDir + outPath_name


    # print(checker)
    # print(outPath)
    print("拆分页连续或分散？")
    dec = ask(list0)
    if dec == "1":
        s = eval(input("起始页码:"))
        e = eval(input("结束页码:"))
        j = s
        while s <= j <= e:
            list_p.append(j)
            j += 1
    elif dec == "2":
        list_p = eval(input("拆分页码，英文逗号隔开:"))

    # print(list_p)
    pdf_spilter(inPath, outPath, list_p)
