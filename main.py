import pygame
from player import *
from fallingDishies import *

pygame.init()

WIDHT, HEIGHT = 1080, 720

MAXFPS = 144
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption("Fish game you know what")


dishie1 = Dishies("trash.png", screen)
player1 = Player("playerIMG.png", WIDHT/2, HEIGHT-100, screen)

clock = pygame.time.Clock()
run = True

while run == True:

    clock.tick(MAXFPS)
    screen.fill(WHITE)

    player1.handleInput()
    dishie1.update()

    if player1.rect.colliderect(dishie1):      

        print("collide")
        

    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            quit()

    pygame.display.update()