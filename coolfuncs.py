import lamefuncs
import random
import pygame
#this is for stuff like the state 
#of an NPC and crap like that
X=1400
Y=700
direction=0
def board(x,y,speed,state):  

    
    global X
    global Y#i know i said i removed all globals, 
    #butttttt.......
    global direction
    dosomething=random.randint(0,101)
    canChangeDir=random.randint(0,21)
    changeDir=random.randint(0,4)
    
    #return [x+speed,y],"x"
    if x<0:
        direction=0
    if x>X:
        direction=1
    if y<0:
        direction=2
    if y>Y:
        direction=3    
    if canChangeDir>19:
        direction=changeDir
    if dosomething>79:
        if direction==0:
            return [x+speed,y]

        if direction==1:
            return [x,y+speed]
            
            
        if direction==2:
            return [x-speed,y]

        if direction==3:
            return [x,y-speed]




def hunting(selfPos,targetPos):#for rats only
    pass
def running():
    pass