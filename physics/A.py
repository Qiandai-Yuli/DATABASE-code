import math 
import time
import turtle
if __name__ == '__main__':


    g=10
    m1=eval(input("the mass of object:"))
    print("if the plane is smooth,input '0' for Uf")
    u1=eval(input("the Uf of plane:"))
    F=eval(input("the force :"))
    agree=eval(input("the agree of the force:"))
    t=eval(input("the time of the action of the force:"))
    am_F=((m1*g-F*math.sin(agree))-F*math.cos(agree))*u1/m1
    am_0=-(u1*m1*g)
    print("if the object is static,input '0' for v0")
    Vm10=eval(input("the v0 of m1:"))
    Vm1_F=Vm10+am_F*t
    if am_0 != 0:
        t_0=(0-Vm1_F)/am_0
    else:
        t_0 = 0
    Xm1_F=Vm10*t+(1/2)*am_F*t**2
    Xm1_0=Vm1_F*t_0+(1/2)*am_0*t_0**2
    Xm1=Xm1_F+Xm1_0
    print("the max V of object is",Vm1_F,"the X of object is",Xm1 )



    r=20
    turtle.setup(1000,1000,0,0)
    turtle.pencolor("blue")
    turtle.penup()
    turtle.goto(-500,-200)
    turtle.pendown()
    turtle.forward(1000)
    turtle.goto(-500+r,-200)
    turtle.circle(r)
    turtle.penup()
    turtle.goto(-500+r+Xm1*20,-200)
    turtle.pendown()
    turtle.circle(r)

    time.sleep(10)