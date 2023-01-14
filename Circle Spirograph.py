import turtle as t

t.bgcolor("black")  #for background color
t.pen(5)    #pentool & 2 means thickness of color
t.speed(0)

for i in range(6):
    for color in ['white','cyan','blue','yellow','red','green']:
        t.color(color)  #for using color kon color hbe ta
        t.circle(130)   #color drawn ta kamn hbe circle na rectangle
        t.right(15)  #akber ankoner pr 10 degree sorbe
    t.hideturtle() # tir chinho ta ke hide kre





