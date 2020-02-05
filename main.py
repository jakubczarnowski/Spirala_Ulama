import pygame
import random
import math
import threading
from time import sleep

width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
bgX = 0
bgX2 = screen.get_width()
screen.fill((255, 255, 255))
currentNr = 1
x = int(screen.get_width()/2)
y = int(screen.get_height()/2)
turnX = 1
turnY = 1
primesList = []
isPossible = True
primesNumberNumber = 1
scrolling = False


def lookForNewMousePos():
    pygame.event.get()
    myx, myy = pygame.mouse.get_pos()
    return myx, myy


def changePos(new_x, new_y):
    global isPossible
    global x
    global y
    isPossible = False
    sleep(1)
    screen.fill((255, 255, 255))
    for i in range(0,len(primesList)):
        primesList[i].y += new_y
        primesList[i].x += new_x
        screen.set_at((primesList[i].x, primesList[i].y), (0, 0, 0))
    y += new_y
    x += new_x
    isPossible = True
    pygame.display.update()


class PrimeDot:
    def __init__(self):
        self.x = 1
        self.y = 1

    def setCords(self, x, y):
        self.x = x
        self.y = y


while running:

    def isPrime(number):
        for iterator in range(2, int(math.sqrt(number))):
            if number % iterator == 0:
                return False
            else:
                continue
        return True

    def nextNr():
        global primesNumberNumber

        if isPrime(currentNr):
            screen.set_at((x, y), (0, 0, 0))
            string1 = 'obiekt' + str(currentNr) + " = PrimeDot()"
            exec(string1)
            exec("obiekt" + str(currentNr) + ".x = x")
            exec("obiekt" + str(currentNr) + ".y = y")
            exec("primesList.append(obiekt" + str(currentNr) + ")")
            primesNumberNumber += 1


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if not scrolling:
                    mouse_x, mouse_y = event.pos
                scrolling = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                scrolling = False

        elif event.type == pygame.MOUSEMOTION:
            if scrolling:
                sleep(0.2)
                new_mouse_x, new_mouse_y = lookForNewMousePos()
                print(mouse_x, " ", mouse_y)
                print(new_mouse_x, " ", new_mouse_y)
                changePos(new_mouse_x - mouse_x, new_mouse_y - mouse_y)
                mouse_x = new_mouse_x
                mouse_y = new_mouse_y

    if isPossible:
        for i in range(0, turnX):
            nextNr()
            currentNr += 1
            x += 1
        turnX += 1
        for i in range(0, turnY):
            nextNr()
            currentNr += 1
            y += 1
        turnY += 1
        for i in range(0, turnX):
            nextNr()
            currentNr += 1
            x -= 1
        turnX += 1

        for i in range(0, turnY):
            nextNr()
            currentNr += 1
            y -= 1
        turnY += 1
    pygame.display.update()  # updates the screen
