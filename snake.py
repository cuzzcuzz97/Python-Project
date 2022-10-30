import pygame
import random
import time

pygame.init()

direction = 0
screen = pygame.display.set_mode((1280,720))
green = (0,255,0)
white = (255,255,255)
red = (0,255,0)
clock = pygame.time.Clock()
snake_size = 60
snake_head = [30,30]
snakes = [[0,30]]
snakes.append(snake_head)
snake_speed = snake_size
food_x = random.randint(0,1280-50)
food_y = random.randint(0,720-50)
while True:

    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            direction = 1
            
        if event.key == pygame.K_RIGHT:
            direction = 2
        if event.key == pygame.K_DOWN:
            direction = 3
        if event.key == pygame.K_UP:
            direction = 4
    screen.fill((0, 0, 0))

    for i in range(1280//snake_size):
        pygame.draw.line(screen, white, [snake_size*i,0], [snake_size*i,720])

    food = pygame.draw.rect(screen,green,(food_x,food_y, snake_size,snake_size))
    try:
        if x.colliderect(food):
            snakes.insert(0,[food_x, food_y])
            food_x = random.randint(0,1280-50)//60*60
            food_y = random.randint(0,720-50)//60*60
    except:
        ...
    if direction == 1:
        snakes.insert(0,[snakes[0][0]-snake_speed,snakes[0][1]])
        snakes.pop()
    if direction == 2:
        snakes.insert(0,[snakes[0][0]+snake_speed,snakes[0][1]])
        snakes.pop()
    if direction == 3:
        snakes.insert(0,[snakes[0][0],snakes[0][1]+snake_speed])
        snakes.pop() 

    if direction == 4:
        snakes.insert(0,[snakes[0][0],snakes[0][1]-snake_speed])
        snakes.pop()   

    for snake in snakes:
        x = pygame.draw.rect(screen, green, (snake[0], snake[1],snake_size,snake_size))
        if snake[0] > 1280:
            snake[0] = 0
        if snake[0] < 0:
            snake[0] = 1280
        if snake[1] > 720:
            snake[1] = 0
        if snake[1] < 0:
            snake[1] = 720

    
    pygame.display.update()
    pygame.display.flip() 
    clock.tick(15)         # wait until next frame (at 60 FPS)