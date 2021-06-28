import pygame
import time
from time import sleep
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

radius=20
edgelen=50



firtPage=pygame.display.set_mode((width,hight))
pygame.display.set_caption("INORDER TRAVERSAL")

firtPage.fill(black)

pygame.display.update()
f=pygame.font.SysFont('comicsansms',50)
fM=pygame.font.SysFont("comicsansms",8)
nodeFONT=pygame.font.SysFont("comicsansms",15)
def intro():
    text=f.render('Enter the BST details in the terminal',True,white)
    firtPage.blit(text,[200,300])
    pygame.display.update()
    sleep(1)
    firtPage.fill(black)


def rectMSG(msg,pos,color):
    text=f.render(msg,True,color)
    firtPage.blit(text,pos)

def nodeMSG(msg,pos,color):
    text=nodeFONT.render(msg,True,color)
    firtPage.blit(text,pos)

class node:
    def __init__(self,val=None):
        self.val=val
        self.pos=None
        self.parent=None
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
    def insert(self,val):
        if self.root==None:
            self.root=node(val)
            pygame.draw.circle(firtPage,white,[width//2,radius],radius)
            self.root.pos=[width//2,radius]
            pygame.draw.line(firtPage,white,(width//2,radius),(width//2-100,radius+100),3)
            pygame.draw.line(firtPage,white,(width//2,radius),(width//2+100,radius+100),3)
            nodeMSG(str(val),[width//2,radius],black)
            pygame.display.update()
            self.parent=None
        else:

            self._insert(val,self.root,self.root.pos)
    def _insert(self,val,root,pos):
        if val<root.val:
            if root.left==None:
                root.left=node(val)



                root.left.parent=root
                pos=root.left.parent.pos
                root.left.pos=[pos[0]-100,pos[1]+100]
                pygame.draw.circle(firtPage,white,root.left.pos,radius)
                pygame.draw.line(firtPage,white,root.left.pos,(root.left.pos[0]-100,root.left.pos[1]+100),3)
                pygame.draw.line(firtPage,white,root.left.pos,(root.left.pos[0]+100,root.left.pos[1]+100),3)
                nodeMSG(str(val),root.left.pos,black)
                pygame.display.update()

            else:
                if root.left:
                    self._insert(val,root.left,root.left.pos)
                else:
                    self._insert(val,root.left,None)
        elif val>root.val:
            if root.right==None:
                root.right=node(val)

                root.right.parent=root
                pos=root.right.parent.pos
                root.right.pos=[pos[0]+100,pos[1]+100]

                pygame.draw.circle(firtPage,white,root.right.pos,radius)
                pygame.draw.line(firtPage,white,root.right.pos,(root.right.pos[0]-100,root.right.pos[1]+100),3)
                pygame.draw.line(firtPage,white,root.right.pos,(root.right.pos[0]+100,root.right.pos[1]+100),3)

                nodeMSG(str(val),root.right.pos,black)
                pygame.display.update()
            else:
                #pos=[(pos[0][0]-100,pos[0][1]+100),(pos[1][0]+100,pos[1][1]+100)]
                if root.right:
                    self._insert(val,root.right,root.right.pos)
                else:
                    self._insert(val,root.right,None)
        else:
            print("the value already exists",val)
    def inorder(self):
        if self.root!=None:
            #pos=[(width//2,radius),(width//2,radius)]
            self._inorder(self.root)
        pygame.quit()
        
    def _inorder(self,cur_val):
        if cur_val!=None:

            self._inorder(cur_val.left)
            print(cur_val.val)

            pygame.draw.circle(firtPage,blue,cur_val.pos,radius)

            #pygame.draw.line(firtPage,white,(pos[0][0],pos[0][1]),(pos[0][0]-100,pos[0][1]+100),3)
            #pygame.draw.line(firtPage,white,(pos[0][0],pos[0][1]),(pos[0][0]+100,pos[0][1]+100),3)

            nodeMSG(str(cur_val.val),cur_val.pos,black)
            pygame.display.update()
            time.sleep(1)
            #pos=[pos[0],(pos[1][0]+100,pos[1][1]+100)]
            #first=False
            self._inorder(cur_val.right)


    def preorder(self):
        if self.root!=None:
            self._preorder(self.root)
    def _preorder(self,cur_val):
        if cur_val!=None:
            print(cur_val.val)
            self._preorder(cur_val.left)
            self._preorder(cur_val.right)

    def postorder(self):
        if self.root!=None:
            self._postorder(self.root)
    def _postorder(self,cur_val):
        if cur_val!=None:
            self._postorder(cur_val.left)
            self._postorder(cur_val.right)
            print(cur_val.val)


def gameloop():

    tree=BST()
    intro()
    inp=list(input("enter the list of values in BST: "))

    for i in inp:
        tree.insert(i)
    time.sleep(2)


    text=f.render('press any key to continue',True,white)
    firtPage.blit(text,[200,300])
    pygame.display.update()
    exit=False
    while not exit:
        #buttons()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=True
            if event.type==pygame.KEYDOWN:
                text=f.render('press any key to continue',True,black)
                firtPage.blit(text,[200,300])
                pygame.display.update()

                tree.inorder()

        pygame.display.update()

#gameloop()

'''
import pygame
import time
from time import sleep
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

radius=20
edgelen=50



firtPage=pygame.display.set_mode((width,hight))
pygame.display.set_caption("INORDER TRAVERSAL")

firtPage.fill(black)

pygame.display.update()
f=pygame.font.SysFont('comicsansms',50)
fM=pygame.font.SysFont("comicsansms",8)
nodeFONT=pygame.font.SysFont("comicsansms",15)
def intro():
    text=f.render('Enter the BST details in the terminal',True,white)
    firtPage.blit(text,[200,300])
    pygame.display.update()
    sleep(1)
    firtPage.fill(black)


def rectMSG(msg,pos,color):
    text=f.render(msg,True,color)
    firtPage.blit(text,pos)

def nodeMSG(msg,pos,color):
    text=nodeFONT.render(msg,True,color)
    firtPage.blit(text,pos)

class node:
    def __init__(self,val=None):
        self.val=val
        self.pos=None
        self.parent=None
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
    def insert(self,val):
        if self.root==None:
            self.root=node(val)
            pygame.draw.circle(firtPage,white,[width//2,radius],radius)
            self.root.pos=[width//2,radius]
            pygame.draw.line(firtPage,white,(width//2,radius),(width//2-100,radius+100),3)
            pygame.draw.line(firtPage,white,(width//2,radius),(width//2+100,radius+100),3)
            nodeMSG(str(val),[width//2,radius],black)
            pygame.display.update()
            self.parent=None
        else:

            self._insert(val,self.root,self.root.pos)
    def _insert(self,val,root,pos):
        if val<root.val:
            if root.left==None:
                root.left=node(val)



                root.left.parent=root
                pos=root.left.parent.pos
                root.left.pos=[pos[0]-100,pos[1]+100]
                pygame.draw.circle(firtPage,white,root.left.pos,radius)
                pygame.draw.line(firtPage,white,root.left.pos,(root.left.pos[0]-100,root.left.pos[1]+100),3)
                pygame.draw.line(firtPage,white,root.left.pos,(root.left.pos[0]+100,root.left.pos[1]+100),3)
                nodeMSG(str(val),root.left.pos,black)
                pygame.display.update()

            else:
                if root.left:
                    self._insert(val,root.left,root.left.pos)
                else:
                    self._insert(val,root.left,None)
        elif val>root.val:
            if root.right==None:
                root.right=node(val)

                root.right.parent=root
                pos=root.right.parent.pos
                root.right.pos=[pos[0]+100,pos[1]+100]

                pygame.draw.circle(firtPage,white,root.right.pos,radius)
                pygame.draw.line(firtPage,white,root.right.pos,(root.right.pos[0]-100,root.right.pos[1]+100),3)
                pygame.draw.line(firtPage,white,root.right.pos,(root.right.pos[0]+100,root.right.pos[1]+100),3)

                nodeMSG(str(val),root.right.pos,black)
                pygame.display.update()
            else:
                #pos=[(pos[0][0]-100,pos[0][1]+100),(pos[1][0]+100,pos[1][1]+100)]
                if root.right:
                    self._insert(val,root.right,root.right.pos)
                else:
                    self._insert(val,root.right,None)
        else:
            print("the value already exists",val)
    def inorder(self):
        if self.root!=None:
            #pos=[(width//2,radius),(width//2,radius)]
            self._inorder(self.root)
        pygame.quit()
        
    def _inorder(self,cur_val):
        if cur_val!=None:

            self._inorder(cur_val.left)
            print(cur_val.val)

            pygame.draw.circle(firtPage,blue,cur_val.pos,radius)

            #pygame.draw.line(firtPage,white,(pos[0][0],pos[0][1]),(pos[0][0]-100,pos[0][1]+100),3)
            #pygame.draw.line(firtPage,white,(pos[0][0],pos[0][1]),(pos[0][0]+100,pos[0][1]+100),3)

            nodeMSG(str(cur_val.val),cur_val.pos,black)
            pygame.display.update()
            time.sleep(1)
            #pos=[pos[0],(pos[1][0]+100,pos[1][1]+100)]
            #first=False
            self._inorder(cur_val.right)


    def preorder(self):
        if self.root!=None:
            self._preorder(self.root)
    def _preorder(self,cur_val):
        if cur_val!=None:
            print(cur_val.val)
            self._preorder(cur_val.left)
            self._preorder(cur_val.right)

    def postorder(self):
        if self.root!=None:
            self._postorder(self.root)
    def _postorder(self,cur_val):
        if cur_val!=None:
            self._postorder(cur_val.left)
            self._postorder(cur_val.right)
            print(cur_val.val)


def gameloop():

    tree=BST()
    intro()
    inp=list(input("enter the list of values in BST: "))

    for i in inp:
        tree.insert(i)
    time.sleep(2)


    text=f.render('press any key to continue',True,white)
    firtPage.blit(text,[200,300])
    pygame.display.update()
    exit=False
    while not exit:
        #buttons()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=True
            if event.type==pygame.KEYDOWN:
                text=f.render('press any key to continue',True,black)
                firtPage.blit(text,[200,300])
                pygame.display.update()

                tree.inorder()

        pygame.display.update()

#gameloop()
'''
