
import time
import turtle as screen
import math




#get screen canvas
cv = screen.getcanvas()
#cv.bind('<Motion>', on_motion)

screen_height = 600
screen_width = 1000
#set screen size
screen.setup(screen_width, screen_height)

#time.sleep(5)

turtle = screen.Turtle()

# ========= all of arguments =========

radius = 200
n = 32

turtle.penup()
turtle.goto( -1*(screen_width/2) + 10, (screen_height/2) - 50 )
turtle.write(
        f"radius = {radius}, n = {n}\nwin_height = {screen_height}, win_width = {screen_width}", move=False,
            align='left', font=('Arial', 15, 'normal'))

# ========= all of arguments =========




#set turtle speed
screen.delay(3)

#get screen information
win_width  = screen.window_width()
win_height = screen.window_height()

#set turtle pensize()
turtle.pensize(3)

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


#draw the circle
turtle.color("blue")
turtle.penup()


turtle.goto(0, 0-radius)
print("drawing circle")
turtle.pendown()
turtle.circle(radius)
turtle.penup()

# ======= draw points =======

#set turtle speed
screen.delay(5)

print(f"drawing {n} points")

turtle.color("black")
turtle.pensize(7)
for k in range(1, n + 1):
    degree = (360 * ( k - 1 ) )/ n
    x_coord = radius * math.sin(math.radians(degree))
    y_coord = radius * math.cos(math.radians(degree))

    turtle.penup()
    turtle.goto(x_coord, y_coord)
    turtle.dot()
    turtle.pendown()

# ======= draw points =======

screen.done()
