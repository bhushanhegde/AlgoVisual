import pygame
pygame.init()
import random
import time
#colors
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)

width=1200
hight=600
win=pygame.display.set_mode((width,hight))
pygame.display.set_caption("MergeSort")

win.fill(black)
pygame.display.update()

#clock=pygame.time.Clock()

font=pygame.font.SysFont('comicsansms',100)
font_small=pygame.font.SysFont('comicsansms',50)
def preview():
    seen=False
    text1=font.render("MERGE SORT",True,white)
    win.blit(text1,[300,100])

    text2=font.render("Time Complexity:O(n log n)",True,white)
    win.blit(text2,[200,300])

    text3=font.render("Space Complexity:O(n)",True,white)
    win.blit(text3,[200,450])

    text4=font_small.render('press any key to continue',True,white)
    win.blit(text4,[300,550])
    pygame.display.update()

    while not seen:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                win.fill(black)
                pygame.display.update()
                seen=True


poleH=[]
poleW=5

#FPS=20
for x in range(width//poleW):
    poleH.append(random.randint(1,599))

def display(h,w):
    x=0
    for hi in h:
        pygame.draw.rect(win,green,[x,hi,poleW,hight])
        pygame.display.update()
        x+=poleW
    text=font_small.render('press any key to start merge sort',True,white)
    win.blit(text,[300,550])
    pygame.display.update()
    pressed=False
    while not pressed:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                pressed=True
    text=font_small.render('press any key to start merge sort',True,green)
    win.blit(text,[300,550])
    pygame.display.update()
def MergeSort(arr):

    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        MergeSort(L)
        MergeSort(R)

        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]>R[j]:
                pygame.draw.rect(win,black,[k*poleW,0,poleW,hight])
                pygame.draw.rect(win,green,[k*poleW,L[i],poleW,hight])
                pygame.display.update()
                arr[k]=L[i]

                i+=1
                k+=1
            else:
                pygame.draw.rect(win,black,[k*poleW,0,poleW,hight])
                pygame.draw.rect(win,green,[k*poleW,R[j],poleW,hight])
                pygame.display.update()
                arr[k]=R[j]
                j+=1
                k+=1
        while i<len(L):
            pygame.draw.rect(win,black,[k*poleW,0,poleW,hight])
            pygame.draw.rect(win,green,[k*poleW,L[i],poleW,hight])
            pygame.display.update()
            arr[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            pygame.draw.rect(win,black,[k*poleW,0,poleW,hight])
            pygame.draw.rect(win,green,[k*poleW,R[j],poleW,hight])
            pygame.display.update()
            arr[k]=R[j]
            j+=1
            k+=1



def gameloop():
    #print(poleH)
    pygame.display.set_caption("MERGE SORT")
    preview()
    display(poleH,poleW)
    MergeSort(poleH)
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
