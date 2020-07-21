from src.segment import *

HEX_STATES = [0x7E, 0x30, 0x6D, 0x79, 0x33, 0x5B, 0x5F, 0x70, 0x7F, 0x7B]


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

    def render(self, surface, num):
        '''Render choosen :param:num number'''
        val = list(bin(HEX_STATES[num])[2:])
        if len(val) < 7:
            val = ['0'] + val
        for i in range(7):
            if val[i] == '1':
                self.segments[i].render(surface)
