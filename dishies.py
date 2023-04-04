import pygame
from random import *
from trash import *

class Dishie(pygame.sprite.Sprite):
    def __init__(self, image, typeof, screen):
        super().__init__()
        self.typeof = typeof
        self.screen = screen
        
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (96, 96))
        self.rect = self.image.get_rect()
        
        self.x = 0
        self.y = 0

        self.generate()

    def update(self):
        self.screen.blit(self.image, (self.x ,self.y))
        
    def generate(self):
        self.x += randint(1080*1/3, 1080*2/3)
        self.y += randint(720*1/3, 720*2/3)
        self.rect.center = (self.x, self.y)
    
    def mouseInterraction(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)