import pygame
import pygame.gfxdraw
from pygame.locals import *

import sys, datetime

pygame.init()

FPS = 60
Timer = pygame.time.Clock()

WIDTH, HEIGHT = 600, 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (50, 50, 50)
RED = (237, 28, 36)

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("[DEMO] 7-Segment Indicator")

HEX_STATES = [0x7E, 0x30, 0x6D, 0x79, 0x33, 0x5B, 0x5F, 0x70, 0x7F, 0x7B]


class Segment(pygame.sprite.Sprite):
    '''(pygame.sprite.Sprite) Segment base class.
    You can use it for create your own indicators.'''
    def __init__(self, position, filename='seg.png'):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(WHITE)
        self.pos = position
        self.rect = self.image.get_rect(center=self.pos)

    def rotate(self, degrees):
        self.image = pygame.transform.rotate(self.image, degrees)
        self.rect = self.image.get_rect(center=self.pos)

    def scale(self, n):
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*n),
                                                         int(self.image.get_height()*n)))
        self.rect = self.image.get_rect(center=self.pos)


class Indicator:
    '''Base indicator (ABCDEFG).'''
    def __init__(self, position, scale=1):
        self.pos = position
        self.n = scale

        d150, d75 = int(150*self.n) + 4, int(75*self.n) + 2
        x, y = self.pos[0], self.pos[1]
        self.params = [
            (x,     y-d150, 0),
            (x+d75, y-d75,  90),
            (x+d75, y+d75,  90),
            (x,     y+d150, 0),
            (x-d75, y+d75,  90),
            (x-d75, y-d75,  90),
            (x,     y,      0)
        ]

        self.segments = []
        for i in range(7):
            seg = Segment(self.params[i][:2])
            seg.scale(self.n)
            seg.rotate(self.params[i][2])
            self.segments.append(seg)

    def render(self, num):
        val = list(bin(HEX_STATES[num])[2:])
        if len(val) < 7:
            val = ['0'] + val
        for i in range(7):
            if val[i] == '1':
                DISPLAYSURF.blit(self.segments[i].image, self.segments[i].rect)


def getTime():
    now = datetime.datetime.now()
    return now.hour, now.minute, now.second


class Clock:
    '''Clock, created by six indicators.'''
    def __init__(self, position):
        self.pos = position

        x, y = self.pos[0], self.pos[1]
        self.params = [
            (x-250, y),
            (x-175, y),
            (x-37, y),
            (x+37, y),
            (x+175, y),
            (x+250, y),
        ]

        self.indicators = []
        for i in range(6):
            self.indicators.append(
                Indicator(self.params[i], 0.3)
            )

    def render(self, time):
        h, m, s = str(time[0]), str(time[1]), str(time[2])
        if len(h) == 1:
            h = '0' + h
        if len(m) == 1:
            m = '0' + m
        if len(s) == 1:
            s = '0' + s
        nums = [int(h[0]), int(h[1]), int(m[0]), int(m[1]), int(s[0]), int(s[1])]
        for i in range(6):
            self.indicators[i].render(nums[i])


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
    clock.render(tm)

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
