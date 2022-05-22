import turtle as t 
#import sympy as s
#import time as te

# 显示方式:  0（默认）、1（高亮）、22（非粗体）、4（下划线）、24（非下划线）、 5（闪烁）、25（非闪烁）、7（反显）、27（非反显）
# 前景色:   30（黑色）、31（红色）、32（绿色）、 33（黄色）、34（蓝色）、35（洋红）、36（青色）、37（白色）
# 背景色:   40（黑色）、41（红色）、42（绿色）、 43（黄色）、44（蓝色）、45（洋红）、46（青色）、47（白色）
# \033[显示方式；背景色；前景色  m (数字无重复 不改可不写)
# \033[0m 结尾




def setting():
	global rate     # 全局变量
	print("\033[0;36m 窗口尺寸400，800 / rate=10 / 显示坐标轴以及单位长度 \033[0m")      # \033[0;36m 起始并设置背景色黑色，前景色青色  \033[0m 结尾
	set1=eval(input("是否更改设置：1-是，2-否:"))
	if set1==1:
		cl, ch=eval(input("窗口尺寸(推荐800，800 用逗号隔开，下同):"))
		rate=eval(input("绝对坐标=相对坐标*rate 推荐10，rate="))
		xOy_display=eval(input("1-显示 / 2-不显示："))
	else:
		cl=400
		ch=800
		rate=10
		xOy_display=1


	print("\033[0;36m 画笔尺寸 / 背景颜色 / 图形颜色 / 画笔显示（默认不显示）\033[0m")
	set2=eval(input("更多设置：1-是 / 2-否:"))
	if set2==1:
		ccol = input("背景颜色(英文):")
		psize=eval(input("画笔尺寸(1～10):"))
		pcol=input("图形颜色(英文):")
		pen_display = eval(input("1-显示画笔 / 2-不显示画笔："))
	else:
		psize = 1
		ccol = "white"
		pcol = "black"
		pen_display = 2

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
		t.goto(-30 * rate, 0)
		t.pendown()
		t.goto(30 * rate, 0)
		t.penup()
		t.goto(0, -30 * rate)
		t.pendown()
		t.goto(0, 30 * rate)
		t.penup()
		t.goto(rate, 1)
		t.pendown()
		t.goto(rate, -1)
		t.penup()
		t.goto(0, 0)
		t.pencolor(f"{pcol}")
	else:
		pass





def line():
	sx0 = eval(input("起始x坐标(相对)："))
	sx = rate * sx0  # 绝对坐标
	x = sx
	print("\033[0;36m Ax+By+C=0 \033[0m")
	a, b, c = eval(input("a,b,c(用逗号隔开)="))
	k = -(a / b)
	n = -(c / b)
	print("\033[0;36m k=" + str(k) + " n=" + str(n) + "\033[0m")
	t.penup()
	t.goto(x, k * x + n)
	t.pendown()
	while sx <= x <= -sx:
		t.goto(x, k * x + n)
		x += 1
	pass
	t.penup()

def circle():
	a0, b0 = eval(input("圆心坐标x，y(相对)："))
	r0 = eval(input("半径(相对):"))
	ra = eval(input("弧度(绝对，整圆360):"))
	a = a0 * rate
	b = b0 * rate
	r = r0 * rate
	t.penup()
	t.goto(a, b - r)
	t.pendown()
	t.circle(r, ra)
	pass
	t.penup()

def ellipse():
	a0, b0 = eval(input("a,b:"))
	c0 = (a0 ** 2 - b0 ** 2) ** 0.5
	print("c=", c0)
	a = a0 * rate
	b = b0 * rate
	x = -a
	y = 0
	t.penup()
	t.goto(x, y)
	t.pendown()
	while -a <= x <= a:
		y = (b ** 2 - (b ** 2 / a ** 2) * x ** 2) ** 0.5
		t.goto(x, y)
		x += 1
	t.penup()
	x = -a
	y = 0
	t.goto(x, y)
	t.pendown()
	while -a <= x <= a:
		y = (b ** 2 - (b ** 2 / a ** 2) * x ** 2) ** 0.5
		t.goto(x, -y)
		x += 1
	t.penup()
	pass

def addpointposition():
	rt = rate
	add_x, add_y = eval(input("顶点相对坐标："))
	return (add_x * rt, add_y * rt)

def polygon():
	point_list = []
	c_side = 1
	n_side = eval(input("边数："))
	while c_side <= n_side:
		print("按一定的时钟顺序输入")
		point_group = addpointposition()
		point_list.append(point_group)
		del point_group
		c_side += 1
	c_sidemake = 1
	while c_sidemake <= n_side + 1:
		if c_sidemake == 1:
			t.penup()
			t.goto(point_list[c_sidemake - 1][0], point_list[c_sidemake - 1][1])
			t.pendown()
			c_sidemake += 1
		elif c_sidemake != 1 and c_sidemake != n_side + 1:
			t.goto(point_list[c_sidemake - 1][0], point_list[c_sidemake - 1][1])
			c_sidemake += 1
		elif c_sidemake == n_side + 1:
			t.goto(point_list[0][0], point_list[0][1])
			t.penup()
			c_sidemake += 1

def found():
	global sx0
	global sx
	dec1=eval(input("图形类型：1-直线 / 2-圆(弧) / 3-椭圆 / 4-双曲线 / 5-抛物线 / 6-函数图形 / 7-多边形:"))

	if dec1==1:
		line()

	elif dec1==2:
		circle()

	elif dec1==3:
		ellipse()

	elif dec1==7:
		polygon()


	dec2=eval(input("继续创建图形对象：1-是 / 2-否："))
	if dec2==1:
		found()
	else:
		pass


if __name__ == '__main__':
	print("\033[0;36m 绘图程序 \033[0m")
	setting()
	found()
	print("\033[0;36m 画布悬停中，手动退出 \033[0m")
	t.done()
