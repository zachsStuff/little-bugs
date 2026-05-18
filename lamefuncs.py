import pygame
import random
def randomStartPos(x,y):
    return [random.randint(20,x-20),random.randint(20,y-20)]
def colide(x,y,size,x2,y2,size2):
    xCol=False
    ycol=False
    if x+size<x2-size2 and x+size>x2+size2:
        xCol=True
    if y+size<y2-size2 and y+size>y2+size2:
        ycol=True
    if ycol and xcol:
        return True