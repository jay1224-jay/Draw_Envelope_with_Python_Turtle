import turtle as screen
import math
import image_process


class draw_class:
    def __init__(self, pattern=None, n=500, radius=300, scale=5):

        screen.clearscreen()

        #get screen canvas
        self.cv = screen.getcanvas()

        self.screen_height = 800
        self.screen_width = 1000
        #set screen size
        screen.setup(self.screen_width, self.screen_height)  

        self.turtle = screen.Turtle()

        self.radius = radius
        self.n = n

        # do not use math.pow(n, 2) because it will become scientific notation.
        # After operations, it will become inacurrate, which will lead to wrong envelope.
        self.pattern = 'n ** 2'   

        if pattern:
            self.pattern = pattern

        print("pattern:", self.pattern)



        self.turtle.speed(10)
        
        self.turtle.penup()
        self.turtle.goto( -1*(self.screen_width/2) + 10, (self.screen_height/2) - 70 )
        self.turtle.write(
                f"radius = {self.radius}, n = {self.n}\nwin_height = {self.screen_height}, win_width = {self.screen_width}\npattern = {self.pattern}", move=False,
                    align='left', font=('Arial', 15, 'normal'))

        #set turtle speed
        screen.delay(0)

        self.draw_axis()
        self.draw_circle()
        self.draw_equal_division_points()
        self.draw_lines()

        print("start processing image")

        image_process.image_process(screen=screen.getscreen(), pattern=self.pattern, n = self.n, radius = self.radius, scale=scale)
        
        print("all done")
        
        

    def draw_axis(self):

        #set turtle pensize()
        self.turtle.pensize(2)
        
        #draw x-axis
        self.turtle.penup()
        self.turtle.goto( -1 * int(self.screen_width/2), 0)
        print("drawing x-axis")
        self.turtle.pendown()
        self.turtle.goto( int(self.screen_width/2), 0)
        
        #draw y-axis
        self.turtle.penup()
        self.turtle.goto(0, int(self.screen_height/2))
        print("drawing y-axis")
        self.turtle.pendown()
        self.turtle.goto(0, -1 * int(self.screen_height/2))

    def draw_circle(self):

        #draw the circle
        self.turtle.color("blue")
        self.turtle.penup()
        self.turtle.goto(0, 0-self.radius)
        print("drawing circle")
        self.turtle.pendown()
        self.turtle.circle(self.radius)
        self.turtle.penup()

    def draw_equal_division_points(self):

        #set turtle speed
        screen.delay(0)
        
        self.all_points = []
        
        print(f"drawing {self.n} points")
        
        self.turtle.color("black")
        self.turtle.pensize(3)
        for k in range(1, self.n + 1):
            degree = (360 * ( k - 1 ) )/ self.n
            x_coord = self.radius * math.sin(math.radians(degree))
            y_coord = self.radius * math.cos(math.radians(degree))
        
            # store all of the points
            self.all_points.append([x_coord, y_coord])
        
            self.turtle.penup()
            self.turtle.goto(x_coord, y_coord)
            self.turtle.dot()
            self.turtle.pendown()

    def draw_lines(self):

        self.turtle.color("blue")
        screen.delay(0)
        self.turtle.pensize(0.5)
        
        for number in range(1, self.n+1):  # n is the number of points
            p1 = self.all_points[number - 1]
            index = (self.pattern_function(number) - 1) % self.n
            p2 = self.all_points[index]
            # print(number, index)
        
            self.draw_between_2_points(p1, p2)

    def pattern_function(self, n):
    
        return int(eval(self.pattern))
        # return n ** 11
    
    def draw_between_2_points(self, p1, p2):
    
        self.turtle.penup()
        self.turtle.goto(p1)
        self.turtle.pendown()
        self.turtle.goto(p2)
        self.turtle.penup()


if __name__ == '__main__':
    draw_class()
