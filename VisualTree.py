import pygame
import random
import time
import VisualInorder
import VisualPostorder
import VisualPreorder


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
pygame.display.set_caption("BST ALGORITHMS")

firtPage.fill(black)

pygame.display.update()
f=pygame.font.SysFont('comicsansms',50)
def rectMSG(msg,pos,color):
    text=f.render(msg,True,color)
    firtPage.blit(text,pos)
def buttons():
    pygame.draw.rect(firtPage,red,(50,30,300,100))
    rectMSG("Inorder ",[60,50],black)

    pygame.draw.rect(firtPage,blue,(400,30,300,100))
    rectMSG("Postorder ",[410,50],black)
    pygame.draw.rect(firtPage,yellow,(800,30,300,100))
    rectMSG("Preorder",[810,50],black)

    rectMSG("PLEASE CHOOSE ONE OF THE TRAVERSAL ALGORITHM",[200,400],white)
    pygame.display.update()

    cur=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if click[0]==1:
        if cur[0]>50 and cur[0]<350 and cur[1]>30 and cur[1]<130:
            firtPage.fill(black)
            pygame.display.update()
            VisualInorder.gameloop()
            main()

        elif cur[0]>400 and cur[0]<700 and cur[1]>30 and cur[1]<130:
            firtPage.fill(black)
            pygame.display.update()
            VisualPostorder.gameloop()
            main()

        elif cur[0]>800 and cur[0]<1100 and cur[1]>30 and cur[1]<130:
            firtPage.fill(black)
            pygame.display.update()
            VisualPreorder.gameloop()
            main()



def main():
    exit=False
    firtPage.fill(black)
    pygame.display.update()
    while not exit:
        buttons()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=True
        pygame.display.update()

main()
