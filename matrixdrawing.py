import os
import sys
import pygame as pg
from pygame import *

screenx = 800
screeny = 800
screenName = "The Snake Game"

bgCol = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0 ,0)
green = (0, 255, 0)
blue = (0, 0, 255)

pg.init()
screen = pg.display.set_mode((screenx, screeny))
pg.display.set_caption(screenName)

clock = pg.time.Clock()
fps = 0.5

gamePlate = []

horizontalSize = 2
verticalSize = 2
marginSize = 1
horizontalRow = []

def plateDisplay():
    for n in gamePlate:
        print(n)
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

    for n in range(len(gamePlate)):                     #wall coloring
        for m in range(len(gamePlate[n])):
            if gamePlate[n][m] == 5:
                pg.draw.rect(screen, blue, (m * screenx / horizontalSize, n * screeny / verticalSize, screenx / horizontalSize, screeny / verticalSize), 0)
            
    gamePlateBorderDrawing()

while True:
    
    fpsCount = 0
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()

    screenUpdate()
    plateDisplay()
    pg.display.update()
    fpsCount += 1
    horizontalSize += 1
    verticalSize += 1