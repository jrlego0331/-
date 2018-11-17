import os
import sys
import random as r
import pygame as pg
from pygame import *

screenx = 600
screeny = 600
screenName = "The Snake Game"

bgCol = (0, 255, 102)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0 ,0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

pg.init()
screen = pg.display.set_mode((screenx, screeny))
pg.display.set_caption(screenName)

clock = pg.time.Clock()
fps = 20

gamePlate = []
snakePos = [(3,1), (2,1), (1,1)]
applePos = (0, 0)
appleCK = False
gamestatus = True

horizontalSize = 40
verticalSize = 40
marginSize = 1
horizontaldir = 1
verticaldir = 0
horizontalRow = []


def applePosSet():
    global appleCK
    global applePos

    if appleCK == False:
        applePos = (r.randint(1, horizontalSize - 2), r.randint(1, verticalSize - 2))
        gamePlate[applePos[1]][applePos[0]] = 7
        appleCK = True

        

for x in range(0, horizontalSize):
    for y in range(0, verticalSize):
        if x == 0 or x == horizontalSize - 1 or y == 0 or y == verticalSize - 1:
            horizontalRow.append(5)
        else:
            horizontalRow.append(0)

    gamePlate.append(horizontalRow)
    horizontalRow = []


def plateDisplay():
    for n in gamePlate:
        print(n)
    print()

        
def snakePosCal():
    global appleCK
    global applePos
    global gamestatus
    posx = snakePos[0][0]  
    posy = snakePos[0][1]

    posx += horizontaldir
    posy += verticaldir

    if posx < 1 or posy < 1 or posx > horizontalSize - 2 or posy > verticalSize - 2:
        gamestatus = False
    
    snakePos.insert(0, (posx, posy))
    snakePos.pop(-1)

    for x in range(horizontalSize):
        for y in range(verticalSize):
            for n in range(snakeLength):
                if x == snakePos[n][0] and y == snakePos[n][1]:
                    gamePlate[y][x] = 8

    if snakePos[0][0] == applePos[0] and snakePos[0][1] == applePos[1]:
        tailx = snakePos[-1][0]
        taily = snakePos[-1][1]
        snakePos.insert(-1, (tailx, taily))
        appleCK = False
    
    for n in range(snakeLength):
        
        if snakePos[0][0] == snakePos[n][0] and snakePos[0][1] == snakePos[n][1] and n != 0:
            gamestatus = False
            

def snakePosDisplay():
    for n in range(snakeLength):
        print(snakePos[n])
    print()

def gamePlateBorderDrawing():

    for x in range(0, horizontalSize):
        startPoint = (screenx / horizontalSize * x, 0)
        endPoint = (screenx / horizontalSize * x, screeny)

        pg.draw.line(screen, black, startPoint, endPoint, marginSize)
        pg.draw.line(screen, black, (screenx, 0), (screenx, screeny))

    for y in range(0, verticalSize):
        startPoint = (0, screeny / verticalSize * y)
        endPoint = (screenx, screeny / verticalSize * y)

        pg.draw.line(screen, black, startPoint, endPoint, marginSize)
        pg.draw.line(screen, black, (0, screeny), (screenx, screeny))

def screenUpdate():
    screen.fill(bgCol)
    for x in range(horizontalSize):
        for y in range(verticalSize):
            if y != verticalSize -1 and y != 0 and x != horizontalSize -1 and x != 0:
                if applePos[0] == x and applePos[1] == y:
                    break
                    break
                else:
                    gamePlate[y][x] = 0

    snakePosCal()
    applePosSet()
    


    for n in range(len(gamePlate)):                     #wall coloring
        for m in range(len(gamePlate[n])):
            if gamePlate[n][m] == 5:
                pg.draw.rect(screen, blue, (m * screenx / horizontalSize, n * screeny / verticalSize, screenx / horizontalSize, screeny / verticalSize), 0)
            if gamePlate[n][m] == 7:
                pg.draw.rect(screen, yellow, (m * screenx / horizontalSize, n * screeny / verticalSize, screenx / horizontalSize, screeny / verticalSize), 0)
            if gamePlate[n][m] == 8:
                pg.draw.rect(screen, red, (m * screenx / horizontalSize, n * screeny / verticalSize, screenx / horizontalSize, screeny / verticalSize), 0)

    
    gamePlateBorderDrawing()

while True:
    if gamestatus == False:
        pg.quit()
        sys.exit()

    fpsCount = 0
    snakeLength = len(snakePos)
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            keyPressed = event.key
            print(keyPressed , " Pressed")

            if keyPressed == ord('w'):
                if verticaldir != 1:
                    verticaldir = -1
                    horizontaldir = 0

            if keyPressed == ord('a'):
                if horizontaldir != 1:
                    horizontaldir = -1
                    verticaldir = 0

            if keyPressed == ord('s'):
                if verticaldir != -1:
                    verticaldir = 1
                    horizontaldir = 0

            if keyPressed == ord('d'):
                if horizontaldir != -1:
                    horizontaldir = 1
                    verticaldir = 0
            
            if keyPressed == K_ESCAPE:
                gamestatus = False

    screenUpdate()
    plateDisplay()
    snakePosDisplay()
    print(snakeLength)
    print("--------------------------------------------------")
    pg.display.update()
    fpsCount += 1
    clock.tick(fps)