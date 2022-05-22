import turtle as t
import xlwt
import xlrd
from xlutils.copy  import copy


filepath = "/Users/mac/Desktop/ALLDATA/程序/physics 1.1/setting.xls"
global settingtype
global maysave
global list_settingsaver



def setting():
	maysave = False
	
	settingtype = "normal" 
	
	list_settingsaver = []

	global rate     # 全局变量
	print("\033[0;36m 窗口尺寸800，800 / rate=15 / 显示坐标轴以及单位长度 (默认显示) \033[0m")      # \033[0;36m 起始并设置背景色黑色，前景色青色  \033[0m 结尾
	set1=eval(input("是否更改设置:1-是，2-否:"))
	if set1 == 1:
		cl, ch = eval(input("窗口尺寸(推荐800，800 用逗号隔开，下同):"))
		rate = eval(input("绝对坐标=相对坐标*rate 推荐15，rate="))
		xOy_display = eval(input("1-显示 / 0-不显示:"))
	else:
		cl = 800
		ch = 800
		rate = 15
		xOy_display = 1


	print("\033[0;36m 画笔尺寸 / 背景颜色 / 图形颜色 / 画笔显示（默认显示）\033[0m")
	set2 = eval(input("更多设置:1-是 / 2-否:"))
	if set2 == 1:
		ccol = input("背景颜色(英文):")
		psize = eval(input("画笔尺寸(1～10):"))
		pcol = input("图形颜色(英文):")
		pen_display = eval(input("1-显示画笔 / 0-不显示画笔:"))
	else:
		ccol = "white"
		psize = 1
		pcol = "black"
		pen_display = 1

	list_settingsaver.append(cl)
	list_settingsaver.append(ch)
	list_settingsaver.append(rate)
	list_settingsaver.append(xOy_display)
	list_settingsaver.append(ccol)
	list_settingsaver.append(psize)
	list_settingsaver.append(pcol)
	list_settingsaver.append(pen_display)

	if set1 == 1 or set2 == 1:
		maysave = True
	else:
		maysave = False

	setting_save(maysave, filepath, settingtype, list_settingsaver)

	t.screensize(cl, ch, f"{ccol}")
	t.pensize(psize)
	t.pencolor(f"{pcol}")
	if pen_display == 1:
		t.showturtle()
	else:
		t.hideturtle()

	if xOy_display == 1:
		t.pencolor("black")
		t.penup()
		t.goto(-22 * rate, 0)
		t.pendown()
		t.goto(22 * rate, 0)
		t.penup()
		t.goto(0, -22 * rate)
		t.pendown()
		t.goto(0, 22 * rate)
		t.penup()
		t.pencolor("red")
		t.goto(rate, 1)
		t.pendown()
		t.goto(rate, -1)
		t.penup()
		t.goto(0, 0)
		t.pencolor(f"{pcol}")
	else:
		pass

# wb.write(a,b,c)  a 行  b 列  c 内容
# sheet1: (1,0,cl) (1,1,ch) (1,2,rate) (1,3,xOy) (1,4,ccol) (1,5,psize) (1,6,pcol) (1,7,pen_d)



def setting_save(maysave, filepath, settingtype, list_settingsaver):
	if not maysave:
		pass

	elif maysave:
		print("\033[0;36m 保存此次设置？\033[0m")
		dec_saveornot = eval(input("1-保存 / 2—不保存:"))
		if dec_saveornot == 1:
			wb_readnewsavingposition = xlrd.open_workbook(filename = filepath)
			sheet_readnewsavingposition = wb_readnewsavingposition.sheet_by_index(0)
			NSP = int(sheet_readnewsavingposition.cell(0, 0).value)
			wb = copy(wb_readnewsavingposition)
			if settingtype == "normal":
				i = 0
				sheet = wb.get_sheet(0)
				while i <= 7:
					sheet.write(NSP, i, list_settingsaver[i])
					i += 1
			else:
				pass ##
			sheet.write(0, 0, NSP+1)
			wb.save(filepath)


def setting_read():
	print("\033[0;36m 设置类型 \033[0m")
	dec_settingreadtype = eval(input("1-通用设置 / 2-场设置 / 3-粒子设置:"))
	if dec_settingreadtype == 1:
		wb = xlrd.open_workbook(filename=filepath)
		sheet = wb.sheet_by_index(0)
		nrow = sheet.nrows
		ncol = sheet.ncols
		i = 2
		print("\033[0;36m cl / ch / rate / xOy / ccol / psize / pcol / pen_dis \033[0m")
		while 2 <= i <= nrow-1:
			j = 0
			while 0 <= j <= ncol-1:
				if j == ncol-1:
					end = "\n"
				else:
					end = " / "
				print(sheet.cell(i, j).value, end= f"{end}")
				j += 1
			i += 1
	elif dec_settingreadtype == 2:
		pass ##

	elif dec_settingreadtype == 3:
		pass ##

def setting_use():
	pass ##


def tuple_addposition(c_sidepoint):
	rt = rate
	add_x, add_y = eval(input(f"场顶点相对坐标{c_sidepoint}:"))
	return (add_x * rt, add_y * rt)



def field_orientation():
	rt = rate
	n_field = eval(input("场数量:"))
	c_field = 1
	while c_field <= n_field:
		print("\033[0;36m 场形状 \033[0m")
		dec_field_shapetype = eval(input("1-圆 / 2-矩形 / 3-其他:"))
		if dec_field_shapetype == 1:
			a0, b0 = eval(input("场圆心相对坐标(x,y):"))
			r0 = eval(input("场半径(相对):"))
			a = a0 * rt
			b = b0 * rt
			r = r0 * rt
			t.goto(a, b-r)
			t.pendown()
			t.circle(r)
			t.penup()

			print("\033[0;36m 场类型 \033[0m")
			dec_field_type = eval(input("1-E / 2-B:"))
			if dec_field_type == 1:
				t.pencolor("blue")
				print("\033[0;36m 场方向 \033[0m")
				dec_field_direction_E = eval(input("1-V / 2-^ / 3-< / 4-> :"))
				if dec_field_direction_E == 1:
					t.goto(a, b+r)
					t.pendown()
					t.goto(a, b-r)
					t.goto(a-2, b-r+4)
					t.penup()
					t.goto(a+2, b-r+4)
					t.pendown()
					t.goto(a, b-r)
					t.penup()
					t.pencolor("black")
				elif dec_field_direction_E == 2:
					t.goto(a, b-r)
					t.pendown()
					t.goto(a, b+r)
					t.goto(a-2, b+r-4)
					t.penup()
					t.goto(a+2, b+r-4)
					t.pendown()
					t.goto(a, b+r)
					t.penup()
					t.pencolor("black")
				elif dec_field_direction_E == 3:
					t.goto(a+r, b)
					t.pendown()
					t.goto(a-r, b)
					t.goto(a-r+4, b+2)
					t.penup()
					t.goto(a-r+4, b-2)
					t.pendown()
					t.goto(a-r, b)
					t.penup()
					t.pencolor("black")
				elif dec_field_direction_E == 4:
					t.goto(a-r, b)
					t.pendown()
					t.goto(a+r, b)
					t.goto(a+r-4, b+2)
					t.penup()
					t.goto(a+r-4, b-2)
					t.pendown()
					t.goto(a+r, b)
					t.penup()
					t.pencolor("black")


			elif dec_field_type == 2:
				print("\033[0;36m 场方向 \033[0m")
				dec_field_direction_B = eval(input("1-* / 2-0 :"))
				if dec_field_direction_B == 1:
					t.goto(a-8, b+8)
					t.pendown()
					t.goto(a+8, b-8)
					t.penup()
					t.goto(a+8, b+8)
					t.pendown()
					t.goto(a-8, b-8)
					t.penup()
				elif dec_field_direction_B == 2:
					t.goto(a, b-4)
					t.pendown()
					t.fillcolor("black")
					t.begin_fill()
					t.circle(4)
					t.end_fill()
					t.penup()
			c_field += 1

		elif dec_field_shapetype == 2:
			delta_x0, delta_y0 = eval(input("场相对长度(x,y):"))
			x_lu0, y_lu0 = eval(input("场左上顶点相对坐标(x,y):"))
			delta_x = delta_x0 * rt
			delta_y = delta_y0 * rt
			x_lu = x_lu0 * rt
			y_lu = y_lu0 * rt
			t.goto(x_lu, y_lu)
			t.pendown()
			t.goto(x_lu + delta_x, y_lu)
			t.goto(x_lu + delta_x, y_lu - delta_y)
			t.goto(x_lu, y_lu - delta_y)
			t.goto(x_lu, y_lu)
			t.penup()

			print("\033[0;36m 场类型 \033[0m")
			dec_field_type = eval(input("1-E / 2-B:"))
			if dec_field_type == 1:
				t.pencolor("blue")
				print("\033[0;36m 场方向 \033[0m")
				dec_field_direction_E = eval(input("1-V / 2-^ / 3-< / 4-> :"))
				if dec_field_direction_E == 1:
					t.goto(x_lu+2, y_lu)
					t.pendown()
					t.goto(x_lu+2, y_lu-delta_y)
					t.goto(x_lu, y_lu-delta_y+4)
					t.penup()
					t.goto(x_lu+4, y_lu-delta_y+4)
					t.pendown()
					t.goto(x_lu+2, y_lu-delta_y)
					t.penup()
					t.pencolor("black")
				elif dec_field_direction_E == 2:
					t.goto(x_lu+2, y_lu-delta_y)
					t.pendown()
					t.goto(x_lu+2, y_lu)
					t.goto(x_lu, y_lu-4)
					t.penup()
					t.goto(x_lu+4, y_lu-4)
					t.pendown()
					t.goto(x_lu+2, y_lu)
					t.penup()
					t.pencolor("black")
				elif dec_field_direction_E == 3:
					t.goto(x_lu+delta_x, y_lu-2)
					t.pendown()
					t.goto(x_lu, y_lu-2)
					t.goto(x_lu+4, y_lu)
					t.penup()
					t.goto(x_lu+4, y_lu-4)
					t.pendown()
					t.goto(x_lu, y_lu-2)
					t.penup()
					t.pencolor("black")
				elif dec_field_direction_E == 4:
					t.goto(x_lu, y_lu-2)
					t.pendown()
					t.goto(x_lu+delta_x, y_lu-2)
					t.goto(x_lu+delta_x-4, y_lu)
					t.penup()
					t.goto(x_lu+delta_x-4, y_lu-4)
					t.pendown()
					t.goto(x_lu+delta_x, y_lu-2)
					t.penup()
					t.pencolor("black")

			elif dec_field_type == 2:
				print("\033[0;36m 场方向 \033[0m")
				dec_field_direction_B = eval(input("1-* / 2-0 :"))
				if dec_field_direction_B == 1:
					t.goto(x_lu, y_lu)
					t.pendown()
					t.goto(x_lu+8, y_lu-8)
					t.penup()
					t.goto(x_lu+8, y_lu)
					t.pendown()
					t.goto(x_lu, y_lu-8)
					t.penup()
				elif dec_field_direction_B == 2:
					t.goto(x_lu+4, y_lu-8)
					t.pendown()
					t.fillcolor("black")
					t.begin_fill()
					t.circle(4)
					t.end_fill()
					t.penup()
			c_field += 1

		elif dec_field_shapetype == 3:
			point_list = []
			point_x_s = 0
			point_y_s = 0
			c_sidepoint = 1
			c_sidemake = 1
			n_side = eval(input("场边界数:"))
			print("\033[0;36m 按一定的时钟顺序输入 \033[0m")
			while c_sidepoint <= n_side:
				point_group = tuple_addposition(c_sidepoint)
				point_list.append(point_group)
				point_x_s += point_list[c_sidepoint-1][0]
				point_y_s += point_list[c_sidepoint-1][1]
				del point_group
				c_sidepoint += 1

			while c_sidemake <= n_side + 1:
				if c_sidemake == 1:
					t.penup()
					t.goto(point_list[c_sidemake-1][0], point_list[c_sidemake-1][1])
					t.pendown()
					c_sidemake += 1
				elif c_sidemake != 1 and c_sidemake != n_side + 1:
					t.goto(point_list[c_sidemake - 1][0], point_list[c_sidemake - 1][1])
					c_sidemake += 1
				elif c_sidemake == n_side + 1:
					t.goto(point_list[0][0], point_list[0][1])
					t.penup()
					c_sidemake += 1
			
			print("\033[0;36m 场类型 \033[0m")
			dec_field_type = eval(input("1-E / 2-B:"))
			if dec_field_type == 1:
				print("\033[0;36m 场方向 \033[0m")
				dec_field_direction_E = eval(input("1-V / 2-^ / 3-< / 4-> :"))
				if dec_field_direction_E == 1:
					t.pencolor("blue")
					t.goto(point_x_s / n_side - 2, point_y_s / n_side + 2)
					t.pendown()
					t.goto(point_x_s / n_side , point_y_s / n_side - 2)
					t.goto(point_x_s / n_side + 2, point_y_s / n_side + 2)
					t.pencolor("black")
					t.penup()
				elif dec_field_direction_E == 2:
					t.pencolor("blue")
					t.goto(point_x_s / n_side - 2, point_y_s / n_side - 2)
					t.pendown()
					t.goto(point_x_s / n_side , point_y_s / n_side + 2)
					t.goto(point_x_s / n_side + 2, point_y_s / n_side - 2)
					t.pencolor("black")
					t.penup()
				elif dec_field_direction_E == 3:
					t.pencolor("blue")
					t.goto(point_x_s / n_side + 2, point_y_s / n_side + 2)
					t.pendown()
					t.goto(point_x_s / n_side - 2, point_y_s / n_side )
					t.goto(point_x_s / n_side + 2, point_y_s / n_side - 2)
					t.pencolor("black")
					t.penup()
				elif dec_field_direction_E == 4:
					t.pencolor("blue")
					t.goto(point_x_s / n_side - 2, point_y_s / n_side + 2)
					t.pendown()
					t.goto(point_x_s / n_side + 2, point_y_s / n_side )
					t.goto(point_x_s / n_side - 2, point_y_s / n_side - 2)
					t.pencolor("black")
					t.penup()

			elif dec_field_shapetype == 2:
				print("\033[0;36m 场方向 \033[0m")
				dec_field_direction_B = eval(input("1-* / 2-0 :"))
				if dec_field_direction_B == 1:
					t.goto(point_x_s / n_side - 4, point_y_s / n_side + 4)
					t.pendown()
					t.goto(point_x_s / n_side + 4, point_y_s / n_side - 4)
					t.penup()
					t.goto(point_x_s / n_side + 4, point_y_s / n_side + 4)
					t.pendown()
					t.goto(point_x_s / n_side - 4, point_y_s / n_side - 4)
					t.penup()
					
			c_field += 1
	t.goto(0, 0)

def particle_defi():
	pass


if __name__ == '__main__':
	setting_read()
	setting()
	field_orientation()
	t.done()
