import pygame

import random
import time
from time import sleep

pygame.init()


#colors
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)

width=1200
hight=600
win=pygame.display.set_mode((width,hight))
pygame.display.set_caption("BubbleSort")

win.fill(black)
pygame.display.update()


font=pygame.font.SysFont('comicsansms',100)
font_small=pygame.font.SysFont('comicsansms',50)
def preview():

    text1=font.render("BUBBLE SORT",True,white)
    win.blit(text1,[300,100])

    text2=font.render("Time Complexity:O(n^2)",True,white)
    win.blit(text2,[200,300])

    text3=font.render("Space Complexity:O(1)",True,white)
    win.blit(text3,[200,450])

    text4=font_small.render('press any key to continue',True,white)
    win.blit(text4,[300,550])

    pygame.display.update()
    seen=False
    while not seen:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                win.fill(black)
                pygame.display.update()
                seen=True

#random numbers
poleH=[]
#we can cahnge this value to change the number of poles
#this will be inversely proportional.
poleW=50

for x in range(width//poleW):
    poleH.append(random.randint(1,599))

def display(h,w):
    x=0
    #global hight
    for hi in h:
        pygame.draw.rect(win,green,[x,hi,poleW,hight])
        pygame.display.update()
        x+=poleW

    text=font_small.render('press any key to start bubble sort',True,white)
    win.blit(text,[300,100])
    pygame.display.update()
    pressed=False
    while not pressed:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                pressed=True
def BubbleSort(h,w):
    l=width//poleW
    n=l
    for i in range(l):
        for j in range(1,n):
            sleep(0.1)
            if h[j-1]<h[j]:

                pygame.draw.rect(win,black,[(j-1)*poleW,0,poleW,hight])
                #time.sleep(3)
                pygame.draw.rect(win,black,[j*poleW,0,poleW,hight])
                pygame.draw.rect(win,green,[(j-1)*poleW,h[j],poleW,hight])
                pygame.draw.rect(win,green,[j*poleW,h[j-1],poleW,hight])
                pygame.display.update()
                h[j-1],h[j]=h[j],h[j-1]
                #clock.tick(10)
        n-=1
    #time.sleep(2)

def gameloop():
    #print(poleH)
    pygame.display.set_caption("BUBBLE SORT")
    preview()
    display(poleH,poleW)
    BubbleSort(poleH,poleW)
    text=font.render('DONE!!!',True,white)
    win.blit(text,[400,300])
    pygame.display.update()
    exit=False
    while not exit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                pygame.quit()
                quit()
    pygame.display.update()
    #clock.tick(FPS)




#gameloop()
#start for event

'''
import pygame

import random
import time

pygame.init()


#colors
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)

width=1200
hight=600
win=pygame.display.set_mode((width,hight))
pygame.display.set_caption("BubbleSort")

win.fill(black)
pygame.display.update()


font=pygame.font.SysFont('comicsansms',100)
font_small=pygame.font.SysFont('comicsansms',50)
def preview():

    text1=font.render("BUBBLE SORT",True,white)
    win.blit(text1,[300,100])

    text2=font.render("Time Complexity:O(n^2)",True,white)
    win.blit(text2,[200,300])

    text3=font.render("Space Complexity:O(1)",True,white)
    win.blit(text3,[200,450])

    text4=font_small.render('press any key to continue',True,white)
    win.blit(text4,[300,550])

    pygame.display.update()
    seen=False
    while not seen:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                win.fill(black)
                pygame.display.update()
                seen=True

#random numbers
poleH=[]
#we can cahnge this value to change the number of poles
#this will be inversely proportional.
poleW=10

for x in range(width//poleW):
    poleH.append(random.randint(1,599))

def display(h,w):
    x=0
    #global hight
    for hi in h:
        pygame.draw.rect(win,green,[x,hi,poleW,hight])
        pygame.display.update()
        x+=poleW

    text=font_small.render('press any key to start bubble sort',True,white)
    win.blit(text,[300,100])
    pygame.display.update()
    pressed=False
    while not pressed:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                pressed=True
def BubbleSort(h,w):
    l=width//poleW
    n=l
    for i in range(l):
        for j in range(1,n):
            if h[j-1]<h[j]:

                pygame.draw.rect(win,black,[(j-1)*poleW,0,poleW,hight])
                #time.sleep(3)
                pygame.draw.rect(win,black,[j*poleW,0,poleW,hight])
                pygame.draw.rect(win,green,[(j-1)*poleW,h[j],poleW,hight])
                pygame.draw.rect(win,green,[j*poleW,h[j-1],poleW,hight])
                pygame.display.update()
                h[j-1],h[j]=h[j],h[j-1]
                #clock.tick(10)
        n-=1
    #time.sleep(2)

def gameloop():
    #print(poleH)
    pygame.display.set_caption("BUBBLE SORT")
    preview()
    display(poleH,poleW)
    BubbleSort(poleH,poleW)
    text=font.render('DONE!!!',True,white)
    win.blit(text,[400,300])
    pygame.display.update()
    exit=False
    while not exit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                pygame.quit()
                quit()
    pygame.display.update()
    #clock.tick(FPS)




#gameloop()
'''
