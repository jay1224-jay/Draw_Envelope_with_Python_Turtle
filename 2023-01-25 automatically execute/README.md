# Workflow for automation

files: 

```main.py```:           control all programs

```draw.py```:            draw Envelope by given pattern, such as n -> n^2 , n -> 2n

```image_process.py```:   process image program. get Turtle screenshot, convert .eps to .png.

## 1. Setting patterns (in ```main.py```)
Tell Python what pattern to draw

## 2. Drawing (in ```main.py```, ```draw.py```)
```main.py``` will tell ```draw.py``` what pattern to draw.

## 3. Processing image from Turtle (in ```main.py```, ```image_process.py```)
After ```draw.py``` completes, ```main.py``` will tell ```image_process.py``` to take screenshot in Turtle screen and convert the .eps file to .png file

## 4. Re-executing (in ```main.py```)
After ```image_process.py``` completes, ```main.py``` will tell ```draw.py``` what to draw next. (go to 2. step)

End until all works has been completed.




# Dev log

date: 2023/1/29

created 3 file: main.py, draw.py, and image_process.py

## maih.py:

test creating a range of patterns ( n^1, n^2, n^3, ..., n^10 ) in __list__ using __Generator__.

## draw.py

convert the original drawing code to __class__

