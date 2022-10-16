import socket
import threading
import pickle
from gameclasses import *
import random

host = 'localhost'
port = 9090

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))

playerDic={}

server.listen()
print('listening')

def handleclient(conn,playernumber):
    print('connected',playernumber)

    global playerDic

    conn.send(pickle.dumps(Player(random.randint(0,1000),random.randint(0,800),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),10)))
    while True:
        try:
            playerObj=pickle.loads(conn.recv(6000))

            playerDic[playernumber]=playerObj
            dataList=[]

            for key in playerDic:
                if key!=playernumber:
                    dataList.append(playerDic[key])
            print(dataList,playerDic)
            conn.send(pickle.dumps(dataList))
        except:
            del playerDic[playernumber]
            break


def main():
    playerNumber = 0

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handleclient,args=(conn,playerNumber))
        thread.start()
        playerNumber+=1

main()