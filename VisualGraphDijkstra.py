import pygame
from time import sleep
from collections import defaultdict
pygame.init()

#colors
white=(255,255,255)
blue=(0,0,255)
green=(0,255,0)
red=(255,0,0)
black=(0,0,0)
yellow=(200,200,0)




width=1000
hight=600
win=pygame.display.set_mode((width,hight))
pygame.display.set_caption("GRAPH")
win.fill(black)
blocksize=20


fontBIG=pygame.font.SysFont("comicsansms",80)
fontSmall=pygame.font.SysFont("comicsansms",20)
fontM=pygame.font.SysFont("comicsansms",30)
fontMedium=pygame.font.SysFont("comicsansms",50)


text=fontMedium.render('enter graph details in the terminal',True,white)
win.blit(text,[200,300])
pygame.display.update()

sleep(2)
win.fill(black)
pygame.display.update()
nodeNum=int(input("enter the number of nodes:"))
edgeNum=int(input("enter the number of edges:"))


def msg(m,c,pos):

    text=fontSmall.render(m,True,c)
    win.blit(text,pos)

def mediumMSG(m,c,pos):
    text=fontM.render(m,True,c)
    win.blit(text,pos)
def draw_grid():
    for i in range(0,width,width//blocksize):

        pygame.draw.line(win,white,(i,0),(i,hight),1)
    for i in range(0,hight,hight//blocksize):
        pygame.draw.line(win,white,(0,i),(width,i),1)
    pygame.display.update()

    count=1
    for i in range(0,width,width//blocksize):
        for j in range(0,hight,hight//blocksize):

            msg(str(count),white,[i,j])
            count+=1

pygame.display.update()
clock=pygame.time.Clock()



def text_objects(text,color,font):
    textSur=font.render(text,True,color)
    return textSur,textSur.get_rect()


def msgToScreen(msg,color,font):
    textSur,textRect=text_objects(msg,color,font)
    textRect.center=(width//2),(hight//2)
    win.blit(textSur,textRect)

dic=dict()
graph=dict()
nodes=dict()
#edges=dict()
def takeInput():
    edge=0
    node=0
    while node<nodeNum:
        N=int(input("enter the node position on the graph:"))

        node+=1
        dic[node]=N
        xPos=(N//20)*(1000//20)+(1000//40)
        yPos=(N%20)*(600//20)-(600//40)
        nodes[N]=[xPos,yPos]
        pygame.draw.circle(win,red,(xPos,yPos),blocksize//2)
        msg(str(node),black,[xPos-5,yPos-5])
        pygame.display.update()

    while edge<edgeNum:
        edge+=1
        start=int(input("enter the starting vertex: "))
        end=int(input("enter the ending vertex: "))
        weight=int(input("enter the weight:"))
        x=nodes[dic[start]]
        y=nodes[dic[end]]
        if start in graph:
            graph[start].append((end,weight))
        else:
            graph[start]=[(end,weight)]
        if end in graph:
            graph[end].append((start,weight))
        else:
            graph[end]=[(start,weight)]
        pygame.draw.line(win,green,(x),(y),5)
        msg(str(weight),blue,[(x[0]+y[0])//2,(x[1]+y[1])//2])
        pygame.display.update()


    Dijkstra()
    pygame.display.update()

def printDist(distance,V):
    mediumMSG("the distance are",red,[750,400])
    pygame.display.update()
    d=20
    for i in range(1,V):
        if distance[i]!=float('inf'):
            mediumMSG(str(i)+'-'+str(distance[i]),red,[750,400+d])
            pygame.display.update()
            print(str(i)+'-'+str(distance[i]))
        else:
            mediumMSG(str(i)+'-'+'INFINITY',red,[750,400+d])
            print(str(i)+'-'+'INFINITY')
            pygame.display.update()
        d+=20
    text=fontMedium.render('DONE!!!',True,green)
    win.blit(text,[300,300])
    pygame.display.update()
    sleep(3)
def min_distance(V,visited,distance):
    min_val=float('inf')
    minInd=-1
    for i in range(1,V):
        if not visited[i] and distance[i]<min_val:
            min_val=distance[i]
            minInd=i
    return minInd
def dijkstra(graph,s,V):
    visited=[False]*(V+1)
    distance=[float('inf')]*(V+1)
    distance[s]=0
    pygame.draw.circle(win,blue,(nodes[dic[s]]),blocksize//2)
    msg(str(s),black,[nodes[dic[s]][0]-5,nodes[dic[s]][1]-5])
    pygame.display.update()
    sleep(1)
    for i in range(1,V):
        u=min_distance(V+1,visited,distance)
        visited[u]=True
        pygame.draw.circle(win,blue,(nodes[dic[u]]),blocksize//2)
        msg(str(u),black,[nodes[dic[u]][0]-5,nodes[dic[u]][1]-5])
        pygame.display.update()
        sleep(1)
        #recomputation of the updated distance
        for v in range(1,V+1):
            if not visited[v] and graph[u][v]!=float('inf')and distance[u]+graph[u][v]<distance[v]:
                distance[v]=distance[u]+graph[u][v]
    return printDist(distance,V+1)

def Dijkstra():
    g=[[float('inf')for _ in range(nodeNum+1)]for _ in range(nodeNum+1)]
    for i in graph:
        for j in graph[i]:
            g[i][j[0]]=j[1]

    s=int(input("enter the source vertex: "))
    return dijkstra(g,s,nodeNum)


def mainloop():
    exit=False

    draw_grid()
    pygame.display.update()
    takeInput()

    while not exit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=True
            if event.type==pygame.KEYDOWN:
                if event.type==pygame.K_d:
                    pass
                elif event.type==pygame.K_q:
                    pygame.quit()
                    quit()


    pygame.quit()
    quit()


mainloop()
