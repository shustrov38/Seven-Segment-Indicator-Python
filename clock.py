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
        h, m, s = time
        nums = [
            h[0], h[1],
            m[0], m[1],
            s[0], s[1]
        ]
        for i in range(6):
            self.indicators[i].render(surface, int(nums[i]))
