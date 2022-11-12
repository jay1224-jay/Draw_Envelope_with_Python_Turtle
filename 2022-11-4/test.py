
import time
import turtle as screen


#get screen canvas
cv = screen.getcanvas()
#cv.bind('<Motion>', on_motion)

#set screen size
screen.setup(1000, 600)

time.sleep(10)
turtle = screen.Turtle()

#get screen information
win_width  = screen.window_width()
win_height = screen.window_height()

#set turtle pensize()
turtle.pensize(5)

#draw x-axis
turtle.penup()
turtle.goto( -1 * int(win_width/2), 0)
print("drawing x-axis")
turtle.pendown()
turtle.goto( int(win_width/2), 0)

#draw y-axis
turtle.penup()
turtle.goto(0, int(win_height/2))
print("drawing y-axis")
turtle.pendown()
turtle.goto(0, -1 * int(win_height/2))


turtle.color("blue")
turtle.penup()

radius = 200

turtle.goto(0, 0-radius)
print("drawing circle")
turtle.pendown()
turtle.circle(radius)

screen.done()
