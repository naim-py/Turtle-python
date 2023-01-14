import turtle
s=turtle.Screen()
p=turtle.Turtle()
def drawsqr():
    for i in range(4):
        p.forward(30)
        p.left(90)
    p.forward(30)
if __name__ == "__main__":
    s.setup(600,600)
    p.speed(20)
    for i in range(8):
        p.up()
        p.setpos(0,30*i)
        p.down()
        for j in range(8):
            if (i+j)%2==0:
                col='black'
            else:
                col='white'
            p.fillcolor(col)
            p.begin_fill()
            drawsqr()
            p.end_fill()
        p.hideturtle()



