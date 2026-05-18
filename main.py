#(c)2025:me, fuck you
from Jsun import *
from lamefuncs import *
from coolfuncs import *
import pygame
pygame.init()
X=1400
Y=700
pygame.display.set_icon(pygame.image.load('rsrc\little bugs ICON.png'))
screen = pygame.display.set_mode((X,Y))

pygame.display.set_caption("little bugs")
clock = pygame.time.Clock()
running = True
dt=0
bugStart=40
bugArray={}
enemieArray={}
speed=1
running=3
ratSpeed=2
with open("config.json","r") as cfg:
#this may not work at points for somereason, but hopefully its working right now

    data=json.load(cfg)
def bugINIT(arr,data):
    #global bugArray
    
    maxBugs=loadInt("bug count",data)
    b=0
    stopReloading=False
    if not stopReloading:
      for i in range(loadInt("bug count",data)+1):
        if i in arr:
            b+=1
            if b==20:
                break        
        else:    
            arr[i]=[randomStartPos(X,Y),0,loadFloat("hunger max",data),loadInt("sight distance",data),3]
            print("bug made ::",arr[i])
def enemyINIT(arr,data):
    
    
    maxBugs=loadInt("enemies",data)
    b=0
    stopReloading=False
    if not stopReloading:
      for i in range(loadInt("enemies",data)+1):
        if i in arr:
            b+=1
            if b==20:
                break
        else:                 
            arr[i]=[randomStartPos(X,Y),0,loadFloat("hunger max",data),loadInt("sight distance",data)]
            #ill work on states later, but for now 0=board/satifyed
            print("rat made ::",arr[i])
        

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((23,200,24))

    bugINIT(bugArray,data)
    enemyINIT(enemieArray,data)
    
    for bug in bugArray:
        nothing=board(bugArray[bug][0][0],bugArray[bug][0][1],speed)
        pygame.draw.circle(screen, (0,55,255),(bugArray[bug][0][0],bugArray[bug][0][1]),3)
        
        if not nothing==None:
            
            bugArray[bug][0]=nothing
            
            
    for rat in enemieArray:
        Enothing=board(enemieArray[rat][0][0],enemieArray[rat][0][1],ratSpeed)
        pygame.draw.circle(screen, (255,55,0),(enemieArray[rat][0][0],enemieArray[rat][0][1]),5)
        
        if not Enothing==None:
            
            enemieArray[rat][0]=Enothing
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()