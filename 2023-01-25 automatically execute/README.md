# Workflow for automation

files: 

```main.py```:           control all programs

```draw.py```:            draw Envelope by given pattern, such as n -> n^2 , n -> 2n

```image_process.py```:   process image program. get Turtle screenshot, convert .eps to .png.

## 1. Setting patterns (in ```main.py```)
Tell Python what pattern to draw

## 2. Drawing (in ```main.py```, ```draw.py```)
```main.py``` will tell ```draw.py``` what pattern to draw.

## 3. Processing image from Turtle (in ```draw.py```, ```image_process.py```)
After ```draw.py``` completes, ```image_process.py``` will take screenshot in Turtle screen and convert the .eps file to .png file

## 4. Re-executing (in ```main.py```)
After ```image_process.py``` completes, ```main.py``` will tell ```draw.py``` what to draw next. (go to 2. step)

End until all works has been completed.




# Dev log

## date: 2023/1/29

created 3 file: main.py, draw.py, and image_process.py

#### main.py:

test creating a range of patterns ( n^1, n^2, n^3, ..., n^10 ) in __list__ using __Generator__.

#### draw.py

convert the original drawing code to __class__

#### image_process.py

None.

------------------------------------


## date: 2023/1/30

#### main.py

Change __*patterns*__ format: __*n \*\* 2*__ -> __*math.pow(n, 2)*__  because *\*(asterisk)* seems to have trouble being shown in file name.

#### draw.py

add 
```python
class draw_class:
    def __init__(self, pattern=None, n=100, radius=300):
```
```python
print("start processing image")
image_process.image_process(screen=screen.getscreen(), pattern=self.pattern)        
print("all done")
```
Allow __main.py__ to change __*n*__ and __*radius*__ .

#### image_process.py

Finished ```image_process.py```.

2 args in function __image_process__: __*screen*__ and __*pattern*__

__*screen*__:

Give __image_process__ the turtle screen which will be processed to be .png file later.

__*pattern*__:

Tell __image_process__ the pattern you use. (which is actually the .png file name)

code:
```python
from PIL import Image

def image_process(screen, pattern):

    """
    args:

    screen:
    import turtle 
    screen = turtle.getscreen()

    pattern:
    pattern = "n**2"
    """

    eps_file_name   = pattern + ".eps"
    image_file_name = pattern + ".png"

    print("start converting to .eps")
    screen.getcanvas().postscript(file = eps_file_name)
    print("converted to .eps successfully")

    print("load .eps file")
    eps_image = Image.open("" + eps_file_name)
    eps_image.load(scale=10)

    print("start converting from .eps to .png")
    eps_image.save("./" + image_file_name)
    print("converted successfully")
```

----------------------------------------------

## date:2023/1/31

Generated plenty of pictures of envelope with different patterns.


#### main.py

None.

#### draw.py

None.

#### image_process.py

Changed the format of the file name.
Replace __\*__ (asterisk) with __x__ to avoid not being found by OS.

__old:__
```python
eps_file_name   = pattern + ".eps"
image_file_name = pattern + ".png"
```

__new:__
```python
eps_file_name   = f"{pattern}_{n}_{radius}.eps".replace("*", "x") 
image_file_name = f"{pattern}_{n}_{radius}.png".replace("*", "x") 
```

----------------------------------------------

## date:2023/2/3

Fix wrong envelope and too large pictures of envelope by reducing scale from 10 to 5.
If there's any pattern involving exponent, use *n \*\* 2* rather than *math.pow(n, 2)* because it will generate wrong envelope.

#### main.py

None.

#### draw.py

add *scale* argument in *draw_class*

```python
class draw_class:
    def __init__(self, pattern=None, n=500, radius=300, scale=5):
```

#### image_process.py

add *scale* in file name format

```python

eps_file_name   = f"{pattern}_{n}_{radius}_{scale}.eps".replace("*", "x") 
image_file_name = f"{pattern}_{n}_{radius}_{scale}.png".replace("*", "x") 
```

