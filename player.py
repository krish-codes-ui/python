import pygame
import random

pygame.init()
collision = False
window_size = (800, 400)  # (width, height)
screen = pygame.display.set_mode(window_size)  # init window
bg = pygame.Surface(window_size)
bg.fill("white")  # create window

clock = pygame.time.Clock()

x = 200
y = 100

food_pos = [random.randint(0, 750), random.randint(0, 350)]  # random start
enemy_pos = [random.randint(0, 750), random.randint(0, 350)]  # random start





hero = pygame.Surface((50, 50))
hero.fill("red")
food = pygame.Surface((50, 50))
food.fill('green')
enemy = pygame.Surface((50, 50))
enemy.fill('black')

score = 0
game_status = 'start'
score_label = pygame.font.Font(None, 36)

speed = 10


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_status == "start" and event.key == pygame.K_SPACE:
                game_status = 'playing'
            elif game_status == 'end' and event.key == pygame.K_r:
                game_status = 'playing'
                score = 0
                x,y = 200,100

    enemy_speed=(score/2)+1
    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    x=max(0,min(x,750))
    y=max(0,min(y,350))
    

    if x>=enemy_pos[0]: 
        enemy_pos[0]+= enemy_speed
    else:
        enemy_pos[0]-=enemy_speed
    if y>=enemy_pos[1]: 
        enemy_pos[1]+=enemy_speed
    else:
        enemy_pos[1]-=enemy_speed
    

        

    hero_rect = pygame.Rect(x, y, 50, 50)
    enemy_rect = pygame.Rect(enemy_pos[0], enemy_pos[1], 50, 50)
    food_rect = pygame.Rect(food_pos[0], food_pos[1], 50, 50)

    # Collision detection and food respawn
    if hero_rect.colliderect(food_rect):
        score += 1
        food_pos = [random.randint(0, 750), random.randint(0, 350)]  # respawn at random location
    if enemy_rect.colliderect(hero_rect):
        game_status='end'
    
        

    # Draw everything
    score_text = score_label.render(f'Score: {score}, the speed is {enemy_speed}', True, "black")
    screen.blit(bg, (0, 0))
    if game_status == 'start':
        # font = pygame.font.Font(None, 36)  # Create a font object (size 36)
        status_text = score_label.render("Press Spacebar to start game", True, 'red')
        screen.blit(status_text,(100,50))
    elif game_status == 'playing':
        screen.blit(score_text, (320, 50))

        screen.blit(food, (food_pos[0], food_pos[1]))
        screen.blit(enemy,(enemy_pos))


        screen.blit(hero, (x, y))

    elif game_status == 'end':
        # font = pygame.font.Font(None, 36)  # Create a font object (size 36)
        status_text = score_label.render(f"Game Over!! Score:{score}",True,'red')
        status_text2 = score_label.render("Press Enter to restart", True, 'red')
        screen.blit(status_text, (320, 50))  
        screen.blit(status_text2, (320, 100))  



    pygame.display.update()
    clock.tick(30)

pygame.quit()