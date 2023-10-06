import pygame

class Bus(pygame.sprite.Sprite):

    LEFT_IMAGE = pygame.image.load('resources/bus_left.png')
    RIGHT_IMAGE = pygame.image.load('resources/bus_right.png')

    SCREEN_DIM = (600,500)
    SIZE = (60,30)
    MOVE_DIST = 2
    STARTING_POSITION = (300,250)

    def __init__(self, starting_position: tuple, direction: str):
        super().__init__()
        self.image = Bus.LEFT_IMAGE if direction == 'Left' else Bus.RIGHT_IMAGE
        self.rect = pygame.Rect((0, 0), Bus.SIZE)
        self.rect.center = starting_position[0], starting_position[1]
        self.direction = direction

    def move(self):
        if self.direction == 'Left':
            self.rect.centerx -= self.MOVE_DIST
            if self.rect.right <= 0:
                self.rect.centerx = self.SCREEN_DIM[0] + self.SIZE[0]/2
        else:
            self.rect.centerx += self.MOVE_DIST
            if self.rect.left >= 600:
                self.rect.centerx = 0 - self.SIZE[0]/2

