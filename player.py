import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, img, x , y, win):
        super().__init__()
        self.x = x
        self.y = y
        self.win = win
        self.img = pygame.image.load(img)

        self.velocity = 4
        self.x_vel = 0
        self.rect = pygame.Rect(200, 200, 50, 50)

    def draw(self):
        self.win.blit(self.img, [self.x, self.y])

    def handleInput(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_d]:
            self.x += self.velocity
        if pressed[pygame.K_a]:
            self.x -= self.velocity

        self.draw()