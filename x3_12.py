from math import *
import turtle

def setpoint( x, y, R, angle ):
    xx = x + R*cos(angle)
    yy = y + R*sin(angle)
    #check = (xx - x)*(xx - x) + (yy - y)*(yy-y)
    #print("sprawdzenie r->(r^2):? ", check )
    return (xx, yy)

def generate( x, y, R, p): #p - ilosc punktow
    angle = 0
    step = 360/p
    for i in range (p):
        yield setpoint(x, y, R, angle)
        angle = angle + step
        
#for x in generate( 1, 1, 5, 6 ):
#	print(x)

#------zabawa zolwiem
colors = [
    "#880000", "#884400", "#888800", "#008800",
    "#008888", "#000088", "#440088", "#880088",
    "#880000", "#884400", "#888800", "#008800"
]
#turtle.width(50)
#angle = 360/len(colors)

#for color in colors:
    #turtle.color(color)
    #turtle.circle(150, angle)
i=0
turtle.penup()
for x in generate( 30, 30, 50, 10 ):
	 turtle.setx(x[0] - 50)
	 turtle.sety(x[1] - 50)
	 turtle.color(colors[i])
	 i = i+1
	 turtle.pendown()
	 turtle.circle(10)
	 turtle.penup()

    
#-----SYMBOL NEWTONA-----------

def silnia(n):
    if n==1:
        return 1
    if n==0:
        return 1
    else:
        return silnia(n-1)*n

print ( silnia(5) )
