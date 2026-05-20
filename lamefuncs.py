import pygame
import random
#this is for stuff like colisions and
#crap like that
def randomStartPos(x,y):
    return [random.randint(20,x-20),random.randint(20,y-20)]
def colide(x,y,size,x2,y2,size2):
    #if mouse[0]>x-sx and mouse[0]<x+sx and mouse[1]>y-sy/4 and mouse[1]<y+sy:
    #    canClick=True
    if x>x2-size2/2 and x<x2+size2/2 and y>y2-size2/2 and y<y2+size2/2:
        
        return True