import lamefuncs
import random
import pygame
X=1400
Y=700
def board(x,y,speed):
    global X
    global Y
    dosomething=random.randint(0,101)
    canChangeDir=random.randint(0,16)
    changeDir=random.randint(0,3)
    direction=0
    #return [x+speed,y],"x"
    if x<0:
        direction=0
    if x>X:
        direction=1
    if y<0:
        direction=2
    if y>Y:
        direction=3    
    if canChangeDir>5:
        direction=changeDir
    if dosomething>85:
        if direction==0:
            return [x+speed,y],"x"
        if direction==1:
            return [x-speed,y],"x"
        if direction==2:
            return [x,y+speed],"y"
        if direction==3:
            return [x,y-speed],"y"
