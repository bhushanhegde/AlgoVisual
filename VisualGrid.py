import pygame
import random
import time
#import VisualDFS
#import VisualBFS
#import Visual4MoveDFS
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
pygame.display.set_caption("GRAPH ALGORITHMS")

firtPage.fill(black)

pygame.display.update()
#f=pygame.font.SysFont('comicsansms',50)

f=pygame.font.SysFont('comicsansms',50)
def rectMSG(msg,pos,color):
    text=f.render(msg,True,color)
    firtPage.blit(text,pos)
def buttons():
    pygame.draw.rect(firtPage,red,(50,30,300,100))
    rectMSG("1. BFS",[60,50],black)

    pygame.draw.rect(firtPage,blue,(400,30,300,100))
    rectMSG("2. DFS",[410,50],black)
    pygame.draw.rect(firtPage,yellow,(800,30,300,100))
    rectMSG("3. 4 Directional DFS",[810,50],black)


    rectMSG("Press the number of your choice i.e. 1",[200,400],white)
    pygame.display.update()

    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_1:
                firtPage.fill(black)
                pygame.display.update()
                #import VisualDFS
                import VisualBFS
                #import Visual4MoveDFS
                main()

            if event.key==pygame.K_2:
                firtPage.fill(black)
                pygame.display.update()
                import VisualDFS

                main()
            if event.key==pygame.K_3:
                firtPage.fill(black)
                pygame.display.update()
                #import VisualDFS
                #import VisualBFS
                import Visual4MoveDFS
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

'''
import pygame
import random
import time
#import VisualDFS
#import VisualBFS
#import Visual4MoveDFS
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
pygame.display.set_caption("GRAPH ALGORITHMS")

firtPage.fill(black)

pygame.display.update()
#f=pygame.font.SysFont('comicsansms',50)

f=pygame.font.SysFont('comicsansms',50)
def rectMSG(msg,pos,color):
    text=f.render(msg,True,color)
    firtPage.blit(text,pos)
def buttons():
    pygame.draw.rect(firtPage,red,(50,30,300,100))
    rectMSG("BFS",[60,50],black)

    pygame.draw.rect(firtPage,blue,(400,30,300,100))
    rectMSG("DFS",[410,50],black)
    pygame.draw.rect(firtPage,yellow,(800,30,300,100))
    rectMSG("4 Directional DFS",[810,50],black)


    rectMSG("PLEASE CHOOSE ONE OF THE  ALGORITHM",[200,400],white)
    pygame.display.update()


    cur=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if click[0]==1:
        if cur[0]>50 and cur[0]<350 and cur[1]>30 and cur[1]<130:
            firtPage.fill(black)
            pygame.display.update()
            #import VisualDFS
            import VisualBFS
            #import Visual4MoveDFS
            main()

        elif cur[0]>400 and cur[0]<700 and cur[1]>30 and cur[1]<130:
            firtPage.fill(black)
            pygame.display.update()
            import VisualDFS

            main()

        elif cur[0]>800 and cur[0]<1100 and cur[1]>30 and cur[1]<130:
            firtPage.fill(black)
            pygame.display.update()
            #import VisualDFS
            #import VisualBFS
            import Visual4MoveDFS
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
'''
