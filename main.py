#To run the program

#command- python3 -u main.py


import pygame

#initialize pygame
pygame.init()

#colors
#COLOR=(RED,GREEN,BLUE)
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
yellow=(200,200,0)
purple=(0,200,200)

#width and hight of the window
width=1200
hight=600


firstPage=pygame.display.set_mode((width,hight))
pygame.display.set_caption("ALGORITHMS VISUALIZATION")

firstPage.fill(black)

pygame.display.update()

#font used
f=pygame.font.SysFont('comicsansms',50)
def rectMSG(msg,pos,color):
    text=f.render(msg,True,color)
    firstPage.blit(text,pos)

#buttons on the display window
def buttons():
    pygame.draw.rect(firstPage,red,(50,30,300,100))
    rectMSG("SORTING",[60,50],black)

    pygame.draw.rect(firstPage,blue,(400,30,300,100))
    rectMSG("Graph Traversal",[410,50],black)

    pygame.draw.rect(firstPage,yellow,(800,30,300,100))
    rectMSG("Graph",[810,50],black)

    pygame.draw.rect(firstPage,purple,(150,150,300,100))
    rectMSG("TREE Traversal",[160,170],black)

    rectMSG("PLEASE CHOOSE ONE OF THE ABOVE",[200,400],white)
    pygame.display.update()


    cur=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if click[0]==1:
        if cur[0]>50 and cur[0]<350 and cur[1]>30 and cur[1]<130:
            firstPage.fill(black)
            pygame.display.update()
            import VisualSortAlgo
            main()

        elif cur[0]>400 and cur[0]<700 and cur[1]>30 and cur[1]<130:
            firstPage.fill(black)
            pygame.display.update()
            import VisualGrid
            main()

        elif cur[0]>800 and cur[0]<1100 and cur[1]>30 and cur[1]<130:
            firstPage.fill(black)
            pygame.display.update()
            import VisualGraphDijkstra
            main()

        elif cur[0]>150 and cur[0]<450 and cur[1]>100 and cur[1]<230:
            firstPage.fill(black)
            pygame.display.update()
            import VisualTree
            main()






def main():
    exit=False
    while not exit:
        buttons()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=True
        pygame.display.update()

#driver program
main()

'''
#To run the program

#command- python3 -u main.py


import pygame

#initialize pygame
pygame.init()

#colors
#COLOR=(RED,GREEN,BLUE)
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
yellow=(200,200,0)
purple=(0,200,200)

#width and hight of the window
width=1200
hight=600


firstPage=pygame.display.set_mode((width,hight))
pygame.display.set_caption("ALGORITHMS VISUALIZATION")

firstPage.fill(black)

pygame.display.update()

#font used
f=pygame.font.SysFont('comicsansms',50)
def rectMSG(msg,pos,color):
    text=f.render(msg,True,color)
    firstPage.blit(text,pos)

#buttons on the display window
def buttons():
    pygame.draw.rect(firstPage,red,(50,30,300,100))
    rectMSG("SORTING",[60,50],black)

    pygame.draw.rect(firstPage,blue,(400,30,300,100))
    rectMSG("Graph Traversal",[410,50],black)

    pygame.draw.rect(firstPage,yellow,(800,30,300,100))
    rectMSG("Graph",[810,50],black)

    pygame.draw.rect(firstPage,purple,(150,150,300,100))
    rectMSG("TREE Traversal",[160,170],black)

    rectMSG("PLEASE CHOOSE ONE OF THE ABOVE",[200,400],white)
    pygame.display.update()


    cur=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if click[0]==1:
        if cur[0]>50 and cur[0]<350 and cur[1]>30 and cur[1]<130:
            firstPage.fill(black)
            pygame.display.update()
            import VisualSortAlgo
            main()

        elif cur[0]>400 and cur[0]<700 and cur[1]>30 and cur[1]<130:
            firstPage.fill(black)
            pygame.display.update()
            import VisualGrid
            main()

        elif cur[0]>800 and cur[0]<1100 and cur[1]>30 and cur[1]<130:
            firstPage.fill(black)
            pygame.display.update()
            import VisualGraphDijkstra
            main()

        elif cur[0]>150 and cur[0]<450 and cur[1]>100 and cur[1]<230:
            firstPage.fill(black)
            pygame.display.update()
            import VisualTree
            main()






def main():
    exit=False
    while not exit:
        buttons()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=True
        pygame.display.update()

#driver program
main()
'''
