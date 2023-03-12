import pygame
import random

class Dishies(pygame.sprite.Sprite):
    def __init__(self, img, win):
        super().__init__()
        self.img = pygame.image.load(img)
        self.win = win

        self.velocity = 2
        self.x = random.randint(25, 720-21)
        print(self.x)
        self.y = 50
        self.rect = pygame.Rect(100, 100, 50, 50)

    def draw(self):
        self.win.blit(self.img, [self.x, self.y])

    def update(self):
        self.y += self.velocity
        self.draw()