#(c)2025:me, fuck you
from Jsun import *
from lamefuncs import *
from coolfuncs import *
import pygame
pygame.init()
X=1400
Y=700
pygame.display.set_icon(pygame.image.load('little bugs\\rsrc\\little bugs ICON.png'))
screen = pygame.display.set_mode((X,Y))

pygame.display.set_caption("little bugs")
clock = pygame.time.Clock()
running = True
dt=0
bugStart=40
bugArray={}
enemieArray={}
speed=5
def bugINIT():
    global bugArray
    
    maxBugs=loadInt("bug count")
    b=0
    stopReloading=False
    if not stopReloading:
      for i in range(loadInt("bug count")+1):
        if i in bugArray:
            b+=1
            if b==20:
                break        
        else:    
            bugArray[i]=[randomStartPos(X,Y),0,loadFloat("hunger max"),loadInt("sight distance"),3]
            print("bug made ::",bugArray[i])
def enemyINIT():
    global enemieArray
    
    maxBugs=loadInt("enemies")
    b=0
    stopReloading=False
    if not stopReloading:
      for i in range(loadInt("enemies")+1):
        if i in enemieArray:
            b+=1
            if b==20:
                break
        else:                 
            enemieArray[i]=[randomStartPos(X,Y),0,loadFloat("hunger max"),loadInt("sight distance")]
            #ill work on states later, but for now 0=board/satifyed
            print("rat made ::",enemieArray[i])
        

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((23,200,24))

    bugINIT()
    enemyINIT()

    for bug in bugArray:
        pygame.draw.circle(screen, (0,55,255),(bugArray[bug][0][0],bugArray[bug][0][1]),3)
        nothing=board(bugArray[bug][0][0],bugArray[bug][0][1],speed)
        if not nothing==None:
            if nothing[1]=="x":
                bugArray[bug][0]=nothing[0]
            else:
                bugArray[bug][0]=nothing[0]
            
    for rat in enemieArray:
        pygame.draw.circle(screen, (255,55,0),(enemieArray[rat][0][0],enemieArray[rat][0][1]),5)
        
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()