import pygame

from trash import *
from dishies import *

pygame.init()

WIDTH, HEIGHT = 1080, 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dishies Game")

greenTrash = Trash("img/greentrash.png", 1, 1, screen)
greenTrash.setSquare()

redTrash = Trash("img/redtrash.png", 2, 2, screen)
redTrash.setSquare()

purpleTrash = Trash("img/purpletrash.png", 3, 3, screen)
purpleTrash.setSquare()

yellowTrash = Trash("img/yellowtrash.png", 4, 4, screen)
yellowTrash.setSquare()

trashGroup = pygame.sprite.Group(greenTrash, redTrash, purpleTrash, yellowTrash)

firstDishie = Dishie("img/greendishie.png", 1, screen)
secondDishie = Dishie("img/seconddishie.png", 1, screen)
thirdDishie = Dishie("img/thirddishie.png", 1, screen)
fourthDishie = Dishie("img/fourthdishie.png", 1, screen)

spawnZone = pygame.Rect(int(WIDTH*1/3), int(HEIGHT*1/3), int(WIDTH*1/3), int(HEIGHT*1/3))

run = True

while run == True:
    
    screen.fill((255, 255, 255))
    
    trashGroup.draw(screen)
    firstDishie.update()

    pygame.draw.rect(screen, (255, 0, 0), greenTrash, 2)
    pygame.draw.rect(screen, (255, 0, 0), redTrash, 2)
    pygame.draw.rect(screen, (255, 0, 0), purpleTrash, 2)
    pygame.draw.rect(screen, (255, 0, 0), yellowTrash, 2)

    pygame.draw.rect(screen, (255, 0, 0), spawnZone, 2)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        firstDishie.mouseInterraction(event)
            
    pygame.display.flip()
    pygame.display.update()

pygame.quit()