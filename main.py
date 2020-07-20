import sys, datetime

import pygame
import pygame.gfxdraw
from pygame.locals import *

from clock import *

__author__ = "Dmitry Shustrov"

pygame.init()

FPS = 60
Timer = pygame.time.Clock()

WIDTH, HEIGHT = 600, 600

BLACK = (0, 0, 0)
RED = (237, 28, 36)

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("[DEMO] 7-Segment Indicator")


def getTime():
    now = datetime.datetime.now()
    return now.hour, now.minute, now.second

def square(pos, s=8):
    x, y = pos[0], pos[1]
    points = [
        (x-s, y-s),
        (x+s, y-s),
        (x+s, y+s),
        (x-s, y+s),
    ]
    pygame.gfxdraw.filled_polygon(DISPLAYSURF, points, RED)


clock = Clock((300, 300))
prev = getTime()[2]
state = -1

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(BLACK)

    tm = getTime()
    clock.render(DISPLAYSURF, tm)

    if prev != tm[2]:
        state *= -1
        prev = tm[2]

    # blinking squares
    if state == -1:
        # left side
        square((200, 280))
        square((200, 320))

        # right side
        square((410, 280))
        square((410, 320))

    pygame.display.update()
    Timer.tick(FPS)
