 
import turtle

from PIL import Image 

Image.MAX_IMAGE_PIXELS = None

def image_process(screen, pattern, n, radius, scale=5):

    """
    args:

    screen:
    import turtle 
    screen = turtle.getscreen()

    pattern:
    pattern = "n**2"
    """

    eps_file_name   = f"{pattern}_{n}_{radius}_{scale}.eps".replace("*", "x") 
    image_file_name = f"{pattern}_{n}_{radius}_{scale}.png".replace("*", "x") 

    print("start converting to .eps")
    screen.getcanvas().postscript(file = eps_file_name)
    print("converted to .eps successfully")

    print("load .eps file")
    eps_image = Image.open(eps_file_name)
    eps_image.load(scale=scale)

    print("start converting from .eps to .png")
    eps_image.save("./envelope/tn+1_1000/" + image_file_name)
    print("converted successfully")


"""
# example:

turtle.forward(100)
ts = turtle.getscreen()

image_process(ts, "math.pow(n, 2)")



print("get canva")
ts.getcanvas().postscript(file="duck.eps")
print("got canva successfully")

print("start converting")

eps_image = Image.open("./duck.eps")
eps_image.load(scale=10)
eps_image.save("./duck.png")

print("converted successfully")

"""





