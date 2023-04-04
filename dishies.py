import pygame
from random import *
from trash import *

class Dishie(pygame.sprite.Sprite):
    def __init__(self, image, typeof, screen):
        super().__init__()
        self.typeof = typeof
        self.screen = screen
        
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        
        self.x = 1080/2
        self.y = 720/2

    def update(self):
        self.screen.blit(self.image, (self.x ,self.y))
        
    def generate(self):
        pass
    
    def mouseInterraction(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
                