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
pygame.display.set_caption("QuickSort")

win.fill(black)
pygame.display.update()

#clock=pygame.time.Clock()

font=pygame.font.SysFont('comicsansms',100)
font_small=pygame.font.SysFont('comicsansms',50)
def preview():
    seen=False
    text1=font.render("QUICK SORT",True,white)
    win.blit(text1,[300,100])

    text2=font.render("Time Complexity:O(n log n)",True,white)
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

    text=font_small.render('press any key to start quick sort',True,white)
    win.blit(text,[300,550])
    pygame.display.update()
    pressed=False
    while not pressed:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                pressed=True
    text=font_small.render('press any key to start quick sort',True,green)
    win.blit(text,[300,550])
    pygame.display.update()


def swap(arr, i, j):
    pygame.draw.rect(win,black,[i*poleW,0,poleW,hight])
    pygame.draw.rect(win,black,[j*poleW,0,poleW,hight])
    pygame.draw.rect(win,green,[i*poleW,arr[j],poleW,hight])
    pygame.draw.rect(win,green,[j*poleW,arr[i],poleW,hight])
    pygame.display.update()
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def partition(array, start, end):
    """ quicksort partitioning, using end """
    pivot = array[end]
    L = start
    R = end
    while L < R:
        while array[L] > pivot:
            L += 1
        while array[R] < pivot:
            R -= 1
        swap(array, L, R)
        # avoid hanging on the same numbers
        if ( array[L] == array[R] ):
            L += 1
    return R

def _quicksort(array, start, end):
    """ Recursive quicksort function """
    if start < end:
        split = partition(array, start, end)
        _quicksort(array, start, split-1)
        _quicksort(array, split+1, end)

def quicksort(array):
    _quicksort(array, 0, len(array)-1)

    #time.sleep(2)


def gameloop():
    #print(poleH)
    pygame.display.set_caption("QUICK SORT")
    preview()
    display(poleH,poleW)
    quicksort(poleH)
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
