import pygame

class Trash(pygame.sprite.Sprite):
    def __init__(self, image, typeof, squareLoc, screen):
        super().__init__()
        self.typeof = typeof
        self.squareLoc = squareLoc
        self.screen = screen
        
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (128, 128))
        self.rect = self.image.get_rect()
        
        self.x = 0
        self.y = 0
        
    def update(self):
        self.screen.blit(self.image, (self.x ,self.y))

        
    def setSquare(self):
        if self.squareLoc == 1:
            self.x = 1080*0.25
            self.y = 720*0.25
        elif self.squareLoc == 2:
            self.x = 1080*0.75
            self.y = 720*0.25
        elif self.squareLoc == 3:
            self.x = 1080*0.25
            self.y = 720*0.75
        elif self.squareLoc == 4:
            self.x = 1080*0.75
            self.y = 720*0.75
        elif self.squareLoc > 4 or self.squareLoc < 1:
            print("setSquare takes only 1, 2, 3, 4 as arguments")
            pygame.quit()

        self.rect.center = (self.x, self.y)
        self.update()
            
    