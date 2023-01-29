from tkinter import *  
import turtle

from PIL import Image

turtle.forward(100)
ts = turtle.getscreen()

print("get canva")
ts.getcanvas().postscript(file="duck.eps")
print("got canva successfully")

print("start converting")

eps_image = Image.open("./duck.eps")
eps_image.load(scale=10)
eps_image.save("./duck.png")

print("converted successfully")
