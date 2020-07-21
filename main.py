import sys, datetime

import pygame.gfxdraw
from pygame.locals import *

from src.clock import *


__author__ = "Dmitry Shustrov"


pygame.init()

FPS = 60
Timer = pygame.time.Clock()

BLACK = (0, 0, 0)
RED = (237, 28, 36)

WIDTH, HEIGHT = 600, 300
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("[DEMO] 7-Segment Indicator")


def getTime():
    now = datetime.datetime.now()
    return now

def getTimeStr():
    time = getTime().time()
    return str(time).split(':')

def square(pos, s=8):
    x, y = pos
    points = [
        (x-s, y-s),
        (x+s, y-s),
        (x+s, y+s),
        (x-s, y+s),
    ]
    pygame.gfxdraw.filled_polygon(DISPLAYSURF, points, RED)


clock = Clock((300, 150))
t1 = getTime()
state = -1

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(BLACK)

    clock.render(DISPLAYSURF, getTimeStr())

    # check time and change blink state every 500mcs
    t2 = getTime()
    if (t2 - t1).microseconds > 500000:
        state *= -1
        t1 = t2

    # blinking squares
    if state == -1:
        # left side
        square((200, 130))
        square((200, 170))

        # right side
        square((410, 130))
        square((410, 170))

    pygame.display.update()
    Timer.tick(FPS)
