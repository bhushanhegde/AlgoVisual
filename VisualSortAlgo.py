import pygame
import random
import time
import VisualBubbleSort
import VisualSelectionSort
import VisualInsertionSort
import VisualMergeSort
import VisualQuickSort
pygame.init()

#colors
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
yellow=(200,200,0)
purple=(0,200,200)
width=1200
hight=600
firtPage=pygame.display.set_mode((width,hight))
pygame.display.set_caption("SORTING ALGORITHMS")

firtPage.fill(black)

pygame.display.update()
f=pygame.font.SysFont('comicsansms',50)
def rectMSG(msg,pos,color):
    text=f.render(msg,True,color)
    firtPage.blit(text,pos)
def buttons():
    pygame.draw.rect(firtPage,red,(50,30,300,100))
    rectMSG("BubbleSort",[60,50],black)

    pygame.draw.rect(firtPage,blue,(400,30,300,100))
    rectMSG("SelectionSort",[410,50],black)
    pygame.draw.rect(firtPage,yellow,(800,30,300,100))
    rectMSG("MergeSort",[810,50],black)
    pygame.draw.rect(firtPage,purple,(150,150,300,100))
    rectMSG("InsertionSort",[160,170],black)
    pygame.draw.rect(firtPage,white,(600,150,300,100))
    rectMSG("QuickSort",[610,170],black)

    rectMSG("PLEASE CHOOSE ONE OF THE SORTING ALGORITHM",[200,400],white)
    pygame.display.update()

    cur=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if click[0]==1:
        if cur[0]>50 and cur[0]<350 and cur[1]>30 and cur[1]<130:
            firtPage.fill(black)
            pygame.display.update()
            VisualBubbleSort.gameloop()
            main()

        elif cur[0]>400 and cur[0]<700 and cur[1]>30 and cur[1]<130:
            firtPage.fill(black)
            pygame.display.update()
            VisualSelectionSort.gameloop()
            main()

        elif cur[0]>800 and cur[0]<1100 and cur[1]>30 and cur[1]<130:
            firtPage.fill(black)
            pygame.display.update()
            VisualMergeSort.gameloop()
            main()

        elif cur[0]>150 and cur[0]<450 and cur[1]>100 and cur[1]<230:
            firtPage.fill(black)
            pygame.display.update()
            VisualInsertionSort.gameloop()
            main()
        elif cur[0]>600 and cur[0]<900 and cur[1]>100 and cur[1]<230:
            firtPage.fill(black)
            pygame.display.update()
            VisualQuickSort.gameloop()
            main()

def main():
    exit=False
    while not exit:
        buttons()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=True
        pygame.display.update()

main()
