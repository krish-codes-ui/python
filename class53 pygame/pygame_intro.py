import pygame 
import sys

pygame.init()
width = 400
height =  800
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("MyGame -- PY Game")
# pygame.display.set_icon("image")
clock = pygame.time.Clock()

# test_Surface = pygame.Surface((300,700))
test_Surface = pygame.image.load('image_tony_stark.png')
# test_Surface.fill("Red")

while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()

    screen.blit(test_Surface,(220,150))
    pygame.display.update()
    clock.tick(60)