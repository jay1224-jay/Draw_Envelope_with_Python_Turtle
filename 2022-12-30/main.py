
import time
import turtle as screen
import math
# import random


"""
be able to draw lines
and can change pattern function
"""



#get screen canvas
cv = screen.getcanvas()
#cv.bind('<Motion>', on_motion)

screen_height = 700
screen_width = 800
#set screen size
screen.setup(screen_width, screen_height)

# time.sleep(5)

turtle = screen.Turtle()

# ========= all of arguments =========

radius = 300
n = 1000
turtle.speed(10)

turtle.penup()
turtle.goto( -1*(screen_width/2) + 10, (screen_height/2) - 50 )
turtle.write(
        f"radius = {radius}, n = {n}\nwin_height = {screen_height}, win_width = {screen_width}", move=False,
            align='left', font=('Arial', 15, 'normal'))

# ========= all of arguments =========




#set turtle speed
screen.delay(0)

#get screen information
win_width  = screen.window_width()
win_height = screen.window_height()

#set turtle pensize()
turtle.pensize(2)

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

def power(number, exp):

    n = 1
    for _ in range(exp):
        n *= number
    return n

def pattern_function(n):

    return power(n, 11)

def draw_between_2_points(p1, p2):

    turtle.penup()
    turtle.goto(p1)
    turtle.pendown()
    turtle.goto(p2)
    turtle.penup()


# ======= draw points =======

#set turtle speed
screen.delay(0)

all_points = []

print(f"drawing {n} points")

turtle.color("black")
turtle.pensize(3)
for k in range(1, n + 1):
    degree = (360 * ( k - 1 ) )/ n
    x_coord = radius * math.sin(math.radians(degree))
    y_coord = radius * math.cos(math.radians(degree))

    # store all of the points
    all_points.append([x_coord, y_coord])

    turtle.penup()
    turtle.goto(x_coord, y_coord)
    turtle.dot()
    turtle.pendown()

# ======= draw points =======



# ======= draw lines =======

turtle.color("blue")
screen.delay(0)
turtle.pensize(0.5)

for number in range(1, n+1):  # n is the number of points
    p1 = all_points[number - 1]
    p2 = all_points[
            (pattern_function(number) - 1) % n
            ]

    draw_between_2_points(p1, p2)


# ======= draw lines =======


screen.done()
