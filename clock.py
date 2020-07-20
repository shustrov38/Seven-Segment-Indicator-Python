import pygame
from indicator import *


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

    def render(self, surface, time):
        '''Render image'''
        h, m, s = str(time[0]), str(time[1]), str(time[2])
        if len(h) == 1:
            h = '0' + h
        if len(m) == 1:
            m = '0' + m
        if len(s) == 1:
            s = '0' + s
        nums = [int(h[0]), int(h[1]), int(m[0]), int(m[1]), int(s[0]), int(s[1])]
        for i in range(6):
            self.indicators[i].render(surface, nums[i])