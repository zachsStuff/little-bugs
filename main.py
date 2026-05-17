#
from Jsun import *
from functions import *
import pygame
pygame.init()
X=1400
Y=700
screen = pygame.display.set_mode((X,Y))
pygame.display.set_caption("little bugs")
clock = pygame.time.Clock()
running = True
dt=0
bugStart=40
bugArray={}
enemieArray={}
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
            bugArray[i]=(randomStartPos(X,Y))
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
                #print(enemieArray)
                break
        else:
            enemieArray[i]=(randomStartPos(X,Y))
            print("rat made ::",enemieArray[i])
       

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((23,200,24))
    bugINIT()
    enemyINIT()
    for bug in bugArray:
        pygame.draw.circle(screen, (0,55,255),(bugArray[bug][0],bugArray[bug][1]),3)
    for rat in enemieArray:
        pygame.draw.circle(screen, (255,55,0),(enemieArray[rat][0],enemieArray[rat][1]),5)
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()