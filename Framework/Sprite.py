import pygame
from constants import *

# anything that draws to the screen must be or inherit from this type
# path can either be a direct path to image or resource name (if a resource cache is supplied)
class Sprite (pygame.sprite.Sprite):
    def __init__(self, path = "", img = None, resources = None):
        super().__init__()

        # load the image from file if there isn't already an image parsed through the constructor
        if img is None:
            # use image from resource cache if possible
            if not resources is None:
                self.image = resources[path]
            else:
                self.image = pygame.image.load (path).convert_alpha()
        else:
            self.image = img

        self.rect = self.image.get_rect()

    # TODO
    def Rotate(self, angle):
        self.image = pygame.transform.rotozoom (self.image, angle, 300)

    # changes width and height
    def Scale (self, width, height):
        self.rect.width = width
        self.rect.height = height
        # perform the scaling move
        self.image = pygame.transform.scale(self.image, (int(width), int(height)))  

    # used by pygame group, called once per frame
    def update (self):
        pass

    # removes all instances of this object from all pygame groups
    def kill (self):
        super().kill()