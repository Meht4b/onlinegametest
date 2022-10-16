import pygame
import math

class rectangle:
    def __init__(self,posx,posy,color,size):
        self.size=size
        self.posx=posx
        self.posy=posy
        self.colour=color
    def draw(self,win):
        pygame.draw.rect(win,self.colour,(self.posx,self.posy,self.size,self.size))
    def move(self,velx,vely):
        self.posx+=velx
        self.posy+=vely

class Player(rectangle):
    def __init__(self, posx, posy, color, size):
        super().__init__(posx, posy, color, size)
        self.lisTrail=[]

    def mouseMove(self,vel):
        mousex,mousey=pygame.mouse.get_pos()
        disx=mousex-self.posx
        disy=mousey-self.posy
        hyp=math.sqrt(disx**2+disy**2)
        if hyp:
            n=vel/hyp
        if hyp>5:
            self.move(n*disx,n*disy)

    def trail(self,trailLength):
        if len(self.lisTrail)>trailLength:
            self.lisTrail.pop()
            self.lisTrail.insert(0,rectangle(self.posx,self.posy,self.colour,7))
        else:
            self.lisTrail.insert(0,rectangle(self.posx,self.posy,self.colour,7))

    def collision(self,i):
        return pygame.Rect.colliderect(pygame.Rect(self.posx,self.posy,self.size,self.size),pygame.Rect(i.posx,i.posy,i.size,i.size))

            

    def drawPlayer(self,win):
        self.draw(win)
        for obj in self.lisTrail:
            obj.draw(win)