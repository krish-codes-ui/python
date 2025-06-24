import pygame

pygame.init()

window_size = (800, 400)  # (width, height)
screen = pygame.display.set_mode(window_size)  # init window
bg = pygame.Surface(window_size)
bg.fill("white")  # create window

# Load image and set initial position
# hero = pygame.image.load(r'C:\Krish\Every single python program\python classes\class54\dragon.webp')
clock = pygame.time.Clock()

x = 200
y = 100

food = pygame.Surface(50,50)
food = pygame.Surface(50,50)
hero_rect.fill("red")

speed = 5
moveleft = False
movetop = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for held-down keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # if (x>=600):
    #     moveleft = True
    # if (x<=10):
    #     moveleft = False

    # if (y>=500):
    #     movetop = True
    # if (y<=100):
    #     movetop = False

    # if movetop:
    #     y-=5    
    # else:
    #     y+=5

    # if moveleft:
    #     x-=5      
    # else:
    #     x+=5
    # Update screen
    screen.blit(bg, (0, 0))
    screen.blit(hero, (x, y))
    pygame.display.update()
    clock.tick(30)
pygame.quit()