import turtle 
import numpy 
t=-400
#//////////speedupboard////////////
U1=eval(input("the U of speed up board:"))
#//////////offsetboard/////////////
L=eval(input("the length of offset board:"))
"U2_X=t"
"U2_Y=200*numpy.sin(t)"
d=eval(input("the wideth of offset board:"))
#//////////recievingboard//////////
s=eval(input("the distance of recieving board:"))
lah=eval(input("the size of recieving board:"))
#//////////offseting///////////////
turtle.screensize(lah,lah)
turtle.pencolor("red")
#turtle.penup()
#turtle.goto(-400,0)
while t<=400:
	U2_X=t
	U2_Y=20*numpy.sin(t)
	X=(L**2+2*s*L)*U2_X/4*U1*d
	Y=(L**2+2*s*L)*U2_Y/4*U1*d
	turtle.pendown() #?
	turtle.goto(X,Y)
	turtle.penup()   #?
	t+=3
