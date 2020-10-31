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
pygame.display.set_caption("SelectionSort")

win.fill(black)
pygame.display.update()

#clock=pygame.time.Clock()

font_small=pygame.font.SysFont('comicsansms',50)
font=pygame.font.SysFont('comicsansms',100)
def preview():
    seen=False
    text1=font.render("SELECTION SORT",True,white)
    win.blit(text1,[300,100])

    text2=font.render("Time Complexity:O(n^2)",True,white)
    win.blit(text2,[200,300])

    text3=font.render("Space Complexity:O(1)",True,white)
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
poleW=10

#FPS=20
for x in range(width//poleW):
    poleH.append(random.randint(1,599))

def display(h,w):
    x=0
    for hi in h:
        pygame.draw.rect(win,green,[x,hi,poleW,hight])
        pygame.display.update()
        x+=poleW

    text=font_small.render('press any key to start selection sort',True,white)
    win.blit(text,[300,550])
    pygame.display.update()
    pressed=False
    while not pressed:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                pressed=True
    text=font_small.render('press any key to start selection sort',True,green)
    win.blit(text,[300,550])
    pygame.display.update()

def SelectionSort(arr,w):
    l=len(arr)
    for i in range(l):
        max_pos=i
        for j in range(i+1,l):
            if arr[j]>arr[max_pos]:
                max_pos=j

        arr[i],arr[max_pos]=arr[max_pos],arr[i]
        pygame.draw.rect(win,black,[i*poleW,0,poleW,hight])
        pygame.draw.rect(win,black,[max_pos*poleW,0,poleW,hight])
        pygame.draw.rect(win,green,[i*poleW,arr[i],poleW,hight])
        pygame.draw.rect(win,green,[max_pos*poleW,arr[max_pos],poleW,hight])
        pygame.display.update()
        #in selection sort the number of swaps will be less
        #therefore im adding sleep time for graphics
        time.sleep(0.05)
        #clock.tick(10)

    #display(arr,w)
    #time.sleep(2)


def gameloop():
    #print(poleH)
    pygame.display.set_caption("SELECTION SORT")
    preview()
    display(poleH,poleW)
    SelectionSort(poleH,poleW)

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
