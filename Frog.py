import pygame
from log import Log

class Frog(pygame.sprite.Sprite): # establish Frog class as a subclass of the pygame Sprite class

    # Establish values for starting position and starting size
    STARTING_POSITION = (300,490)
    SIZE = (20,10)
    MOVE_DIST = 20
    SCREEN_DIM = (600,500)


    # Add the Frog Image
    IMAGE = pygame.image.load('frog/New Piskel.png')
    IMAGE = pygame.transform.scale2x(IMAGE)

    # constructor
    def __init__(self):
        super().__init__()
        self.image = Frog.IMAGE
        self.rect = pygame.Rect((0,0), Frog.SIZE) # creates rectangle of the predetermined size
        self.rect.center = Frog.STARTING_POSITION # centers the rectangle at the predetermined position
        self.lives = 3

    def move_up(self):
        if self.rect.top >= 20:
            self.rect.centery -= self.MOVE_DIST

    def move_down(self):
        if self.rect.bottom < 490:
            self.rect.centery += self.MOVE_DIST

    def move_right(self):
        if self.rect.bottomright[0] < 600:
            self.rect.centerx += self.MOVE_DIST

    def move_left(self):
        if self.rect.bottomleft[0] > 0:
            self.rect.centerx -= self.MOVE_DIST

    def reset_position(self):
        self.rect.center = self.STARTING_POSITION
        self.lives -= 1

    def move_on_log(self, log: Log):
        # Log moving right
        if log.direction == 'Right':
            self.rect.centerx += Log.MOVE_DIST
            # Frog has moved off screen
            if self.rect.left >= Log.SCREEN_DIM[0]:
                diff = log.rect.right - self.rect.centerx
                self.rect.centerx = -diff
        # Log moving left
        else:
            self.rect.centerx -= Log.MOVE_DIST
            # Frog has moved off screen
            if self.rect.right <= 0:
                diff = abs(log.rect.left - self.rect.centerx)
                self.rect.centerx = Frog.SCREEN_DIM[0] + diff