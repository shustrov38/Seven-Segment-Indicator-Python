import pygame


class Segment(pygame.sprite.Sprite):
    '''(pygame.sprite.Sprite) Segment base class.
    You can use it for create your own indicators.'''

    def __init__(self, position, filename='seg.png'):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((255, 255, 255))
        self.pos = position
        self.rect = self.image.get_rect(center=self.pos)

    def rotate(self, degrees):
        '''Rotate segment on :param:degees count'''
        self.image = pygame.transform.rotate(self.image, degrees)
        self.rect = self.image.get_rect(center=self.pos)

    def scale(self, n):
        '''Scale segment'''
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*n),
                                                         int(self.image.get_height()*n)))
        self.rect = self.image.get_rect(center=self.pos)

    def render(self, surface):
        '''Render image'''
        surface.blit(self.image, self.rect)

