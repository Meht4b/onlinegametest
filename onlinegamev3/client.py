from http import client
import pickle
import pygame
from gameclasses import *
import socket

import sys

width=1280
height=720

window = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
fps = 60

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('localhost',9090))
clientPlayer = pickle.loads(sock.recv(1048))

run = True
click = False

boosttime = 0

while run:
    window.fill((0,0,0))
    for events in pygame.event.get():
        #quit 
        if events.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        if events.type==pygame.MOUSEBUTTONDOWN:
            click=True

        if click:
            if boosttime<120:
                clientPlayer.trail(70)
                clientPlayer.mouseMove(16)

                boosttime+=1

            elif boosttime<180:
                clientPlayer.trail(50)
                clientPlayer.mouseMove(17)
                
                boosttime+=1

            else:
                click=False
                boosttime=0
        else:
            clientPlayer.mouseMove(10)
            clientPlayer.trail(50)


    sock.send(pickle.dumps(clientPlayer))
    enemyList = pickle.loads(sock.recv(5120))


    for play in enemyList:
        play.drawPlayer(window)
        for i in play.lisTrail:
            if clientPlayer.collision(i):

                run = False

    for obj in clientPlayer.lisTrail[3::]:
        if clientPlayer.collision(obj):
            pass
            run = False
    
    

    clientPlayer.drawPlayer(window)



    pygame.display.update()
    clock.tick(fps)