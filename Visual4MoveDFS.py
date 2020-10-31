import pygame
import random
import sys
import time
from collections import defaultdict

#to have recursive DFS
sys.setrecursionlimit(1000000000)

pygame.init()

#colors
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)

width=1200
hight=700
win=pygame.display.set_mode((width,hight))
pygame.display.set_caption("DFS")

blockSize=10

win.fill(black)

clock=pygame.time.Clock()
FPS=20


font=pygame.font.SysFont('comicsansms',50)

def dfs(s,d):
    visited=set()
    call_dfs(visited,s,d)

def call_dfs(visited,s,d):
    pygame.draw.rect(win,white,[s[0],s[1],blockSize,blockSize])
    pygame.display.update()
    if s[0]>width-blockSize or s[0]<0 or s[1]>hight-blockSize or s[1]<0 or s in visited:
        return
    visited.add(s)
    if s==d:

        text=font.render('DONE!!!',True,green)
        win.blit(text,[500,300])
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        quit()
        #exit()
    call_dfs(visited,(s[0]+blockSize,s[1]),d)
    call_dfs(visited,(s[0],s[1]+blockSize),d)
    call_dfs(visited,(s[0]-blockSize,s[1]),d)

    call_dfs(visited,(s[0],s[1]-blockSize),d)






def getSourceDest():
    sX=int(round(random.randrange(0,width)/10.0)*10.0)
    sY=int(round(random.randrange(0,hight)/10.0)*10.0)
    dX=int(round(random.randrange(0,width)/10.0)*10.0)
    dY=int(round(random.randrange(0,hight)/10.0)*10.0)

    pygame.draw.rect(win,red,[sX,sY,blockSize,blockSize])
    pygame.draw.rect(win,blue,[dX,dY,blockSize,blockSize])

    return ((sX,sY),(dX,dY))


def gameloop():

    (s,d)=getSourceDest()
    time.sleep(1)
    pygame.display.update()
    text=font.render('press any key traverse DFS',True,green)
    win.blit(text,[300,300])
    pygame.display.update()
    exit=False
    while not exit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                text=font.render('press any key traverse DFS',True,black)
                win.blit(text,[300,300])
                pygame.display.update()
                dfs(s,d)
        pygame.display.update()

        #clock.tick(FPS)

gameloop()
