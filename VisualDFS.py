import pygame
import random
import sys
from time import sleep
sys.setrecursionlimit(1000000000)

from collections import defaultdict
pygame.init()
#colors
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)

width=600
hight=600
win=pygame.display.set_mode((width,hight))
pygame.display.set_caption("DFS")

blockSize=10
#pix=pygame.PixelArray(win)
#print(pix)
win.fill(black)
font=pygame.font.SysFont('comicsansms',50)
clock=pygame.time.Clock()
FPS=20
def printFunc(parent,s,d):
    #print(d)
    last=d
    count=0 
    while last!=s:
        count+=1
        pygame.draw.rect(win,red,[last[0],last[1],blockSize,blockSize])
        pygame.display.update()
        #print(parent[last])
        last=parent[last]

visited=set()
def dfs(lis,s,d):
    if s==d:
        text=font.render('DONE!!!',True,green)
        win.blit(text,[150,300])
        pygame.display.update()
        sleep(3)
        quit()
    pygame.draw.rect(win,white,[s[0],s[1],blockSize,blockSize])
    pygame.display.update()
    visited.add(s)
    if type(lis[s])==list:
        for x in lis[s]:
            if x not in visited:
                dfs(lis,x,d)


def getSourceDest():
    sX=int(round(random.randrange(blockSize,width-blockSize-1)/blockSize)*blockSize)
    sY=int(round(random.randrange(blockSize,hight-blockSize-1)/blockSize)*blockSize)
    dX=int(round(random.randrange(blockSize,width-blockSize-1)/blockSize)*blockSize)
    dY=int(round(random.randrange(blockSize,hight-blockSize-1)/blockSize)*blockSize)

    pygame.draw.rect(win,red,[sX,sY,blockSize,blockSize])
    pygame.draw.rect(win,blue,[dX,dY,blockSize,blockSize])
    pygame.display.update()
    return ((sX,sY),(dX,dY))

def adjacencylist():
#adjacency list representation of pixels
    lis=defaultdict(lambda:0)
    for i in range(2*blockSize,hight-blockSize+1,blockSize):
        for j in range(2*blockSize,width-blockSize+1,blockSize):
            lis[(i,j)]=[(i-blockSize,j),(i+blockSize,j),(i,j+blockSize),(i,j-blockSize)]

    #first row
    i=blockSize
    lis[(0,0)]=[(0,blockSize),(blockSize,0)]
    for j in range(2*blockSize,width-blockSize+1,blockSize):
        lis[(i,j)]=[(i+blockSize,j),(i,j+blockSize),(i,j-blockSize)]

    #last row
    i=hight-blockSize
    lis[(i,0)]=[(i-blockSize,0),(i,blockSize)]
    for j in range(2*blockSize,width-blockSize+1,blockSize):
        lis[(i,j)]=[(i-blockSize,j),(i,j-blockSize),(i,j+blockSize)]

    #first col
    j=0
    for i in range(2*blockSize,hight-blockSize,blockSize):
        lis[(i,j)]=[(i+blockSize,j),(i,j+blockSize),(i-blockSize,j)]
    #last col
    lis[(0,width-blockSize)]=[(0,width-2*blockSize),(blockSize,width-blockSize)]
    lis[(hight-blockSize),(width-blockSize)]=[(hight-blockSize,width-2*blockSize),(hight-2*blockSize,width-blockSize)]
    j=width-blockSize
    for i in range(2*blockSize,hight-1,blockSize):
        lis[(i,j)]=[(i,j-blockSize),(i+blockSize,j),(i-blockSize,j)]
    return lis

def gameloop():
    lis=adjacencylist()
    (s,d)=getSourceDest()

    text=font.render('press any key to start DFS',True,white)
    win.blit(text,[100,300])
    pygame.display.update()
    #print(s,d)
    #print(lis)

    pygame.display.update()
    exit=False
    while not exit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                text=font.render('press any key to start DFS',True,black)
                win.blit(text,[100,300])
                dfs(lis,s,d)
                pygame.display.update()
        pygame.display.update()

        #clock.tick(FPS)

gameloop()
#start for event
'''
import pygame
import random
import sys
from time import sleep
sys.setrecursionlimit(1000000000)

from collections import defaultdict
pygame.init()
#colors
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)

width=600
hight=600
win=pygame.display.set_mode((width,hight))
pygame.display.set_caption("DFS")

blockSize=10
#pix=pygame.PixelArray(win)
#print(pix)
win.fill(black)
font=pygame.font.SysFont('comicsansms',50)
clock=pygame.time.Clock()
FPS=20
def printFunc(parent,s,d):
    #print(d)
    last=d
    count=0
    while last!=s:
        count+=1
        pygame.draw.rect(win,red,[last[0],last[1],blockSize,blockSize])
        pygame.display.update()
        #print(parent[last])
        last=parent[last]

visited=set()
def dfs(lis,s,d):
    if s==d:
        text=font.render('DONE!!!',True,green)
        win.blit(text,[150,300])
        pygame.display.update()
        sleep(3)
        quit()
    pygame.draw.rect(win,white,[s[0],s[1],blockSize,blockSize])
    pygame.display.update()
    visited.add(s)
    if type(lis[s])==list:
        for x in lis[s]:
            if x not in visited:
                dfs(lis,x,d)


def getSourceDest():
    sX=int(round(random.randrange(blockSize,width-blockSize-1)/blockSize)*blockSize)
    sY=int(round(random.randrange(blockSize,hight-blockSize-1)/blockSize)*blockSize)
    dX=int(round(random.randrange(blockSize,width-blockSize-1)/blockSize)*blockSize)
    dY=int(round(random.randrange(blockSize,hight-blockSize-1)/blockSize)*blockSize)

    pygame.draw.rect(win,red,[sX,sY,blockSize,blockSize])
    pygame.draw.rect(win,blue,[dX,dY,blockSize,blockSize])
    pygame.display.update()
    return ((sX,sY),(dX,dY))

def adjacencylist():
#adjacency list representation of pixels
    lis=defaultdict(lambda:0)
    for i in range(2*blockSize,hight-blockSize+1,blockSize):
        for j in range(2*blockSize,width-blockSize+1,blockSize):
            lis[(i,j)]=[(i-blockSize,j),(i+blockSize,j),(i,j+blockSize),(i,j-blockSize)]

    #first row
    i=blockSize
    lis[(0,0)]=[(0,blockSize),(blockSize,0)]
    for j in range(2*blockSize,width-blockSize+1,blockSize):
        lis[(i,j)]=[(i+blockSize,j),(i,j+blockSize),(i,j-blockSize)]

    #last row
    i=hight-blockSize
    lis[(i,0)]=[(i-blockSize,0),(i,blockSize)]
    for j in range(2*blockSize,width-blockSize+1,blockSize):
        lis[(i,j)]=[(i-blockSize,j),(i,j-blockSize),(i,j+blockSize)]

    #first col
    j=0
    for i in range(2*blockSize,hight-blockSize,blockSize):
        lis[(i,j)]=[(i+blockSize,j),(i,j+blockSize),(i-blockSize,j)]
    #last col
    lis[(0,width-blockSize)]=[(0,width-2*blockSize),(blockSize,width-blockSize)]
    lis[(hight-blockSize),(width-blockSize)]=[(hight-blockSize,width-2*blockSize),(hight-2*blockSize,width-blockSize)]
    j=width-blockSize
    for i in range(2*blockSize,hight-1,blockSize):
        lis[(i,j)]=[(i,j-blockSize),(i+blockSize,j),(i-blockSize,j)]
    return lis

def gameloop():
    lis=adjacencylist()
    (s,d)=getSourceDest()

    text=font.render('press any key to start DFS',True,white)
    win.blit(text,[100,300])
    pygame.display.update()
    #print(s,d)
    #print(lis)

    pygame.display.update()
    exit=False
    while not exit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                text=font.render('press any key to start DFS',True,black)
                win.blit(text,[100,300])
                dfs(lis,s,d)
                pygame.display.update()
        pygame.display.update()

        #clock.tick(FPS)

gameloop()
'''
