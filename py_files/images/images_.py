import numpy as np
from PIL import Image, ImageDraw
from random import randint

image = Image.open("spider.jpg")
draw = ImageDraw.Draw(image)
width, height = image.size
pix = image.load()
rand_value = 144
factor = 25

def black_and_white(a, b, c):
    if (int(a) + int(b) + int(c)) > 364:
        return 256, 256, 256
    else:
        return 0, 0, 0
    
def randomizer(a, b, c):
    rand = lambda x: x + randint(-rand_value, rand_value + 1)
    return rand(a), rand(b), rand(c)

def lighter(a, b, c):
    return a + factor, b + factor, c + factor

def negihter(a, b, c):
    return a - factor, b - factor, c - factor
    
def main(func):
    
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            draw.point((i, j), func(a, b, c))
            
    image.save("kek.jpg")
    
main(negihter)
del draw