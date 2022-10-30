import pygame
import random
import time

pygame.init()
X = 1280
Y = 720

direction = 0
screen = pygame.display.set_mode((X,Y))
green = (0,255,0)
white = (255,255,255)
blue = (0, 0, 128)

red = (255,0,0)
clock = pygame.time.Clock()
snake_size = 60
snake_head = [30,30]
snakes = [[0,30]]
snakes.append(snake_head)
snake_speed = snake_size
food_x = random.randint(0,1280-50)//60*60
food_y = random.randint(0,720-50)//60*60
timepass = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Ngu', True, green, blue)
textRect = text.get_rect()
textRect.center = (X // 2, Y // 2)


def move_snake(event):
    global direction
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            if direction == 2:
                ...
            else:
                direction = 1
        if event.key == pygame.K_RIGHT:
            if direction == 1:
                ...
            else:
                direction = 2
        if event.key == pygame.K_DOWN:
            if direction == 4:
                ...
            else:
                direction = 3
        if event.key == pygame.K_UP:
            if direction == 3:
                ...
            else:
                direction = 4



while True:
    pygame.time.wait(200)
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        move_snake(event)
    screen.fill((0, 0, 0))

    for i in range(1280//snake_size):
        pygame.draw.line(screen, white, [snake_size*i,0], [snake_size*i,720])

    food = pygame.draw.rect(screen,green,(food_x,food_y, snake_size,snake_size))
    
    if direction == 1:
        snakes.insert(0,[(snakes[0][0]-snake_speed)//60*60,snakes[0][1]])
        snakes.pop()
    if direction == 2:
        snakes.insert(0,[(snakes[0][0]+snake_speed)//60*60,snakes[0][1]])
        snakes.pop()

    if direction == 3:
        snakes.insert(0,[snakes[0][0],(snakes[0][1]+snake_speed)//60*60])
        snakes.pop() 

    if direction == 4:
        snakes.insert(0,[snakes[0][0],(snakes[0][1]-snake_speed)//60*60])
        snakes.pop()   
    try:
        if [food_x, food_y] in snakes:
            snakes.insert(0,[food_x, food_y])
            x = pygame.draw.rect(screen, green, (snake[0], snake[1],snake_size,snake_size))
            food_x = random.randint(0,1280-50)//60*60
            food_y = random.randint(0,720-50)//60*60

    except:
        ...
    if len(snakes) > 4:
        if snakes[0] in snakes[2:]:
            direction = 0
            screen.blit(text, textRect)

    for i, snake in enumerate(snakes):
        if i == 0:
            x = pygame.draw.rect(screen, red, (snake[0], snake[1],snake_size,snake_size))
        else:
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
    clock.tick(60)         # wait until next frame (at 60 FPS)