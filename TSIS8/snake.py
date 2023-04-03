# libraries

import pygame
import random
import time

# initialization

pygame.init()

# setting

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_icon(pygame.image.load("Snake_icon.png"))
pygame.display.set_caption("Legenda")

# additional parametrization

pygame.mixer.Channel(0).play(pygame.mixer.Sound("killbill.mp3"), -1)
clock = pygame.time.Clock()
fps = 60
my_font = pygame.font.SysFont("", 40)

# colors

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
color_of_fruit = (200, 0, 0)
green = (0, 255, 0)
blue = (0, 100, 230)
yellow = (255, 255, 0)
# snake

position_of_snake = [100, 50]
body_of_snake = [[100, 50], [90, 50], [80, 50], [70, 50],]
speed_of_snake = 10
# direction of snake

direction = 'RIGHT'
change_to = direction

# score and level

counter = 0
global level
level = 1
# fruit

position_of_fruit = [random.randrange(
    1, (width//2)*2,), random.randrange(1, (height//2)*2)]
spawn_of_fruit = True

# Blit score


def score():
    text1 = my_font.render("Score: "+str(counter), True, yellow)
    screen.blit(text1, (10, 10))
    text2 = my_font.render("Level: "+str(level), True, yellow)
    screen.blit(text2, (10, 50))

# gameover


def game_over():
    # texts

    font1 = pygame.font.SysFont("", 80)
    font2 = pygame.font.SysFont("", 30)
    text1 = font1.render("GAME OVER", True, red)
    text2 = font2.render("Your score is: "+str(counter), True, red)
    text3 = font2.render("Your level is: "+str(level), True, red)

    # endgame

    endgame = pygame.Surface((screen.get_size()))
    endgame.fill(black)
    endgame.set_alpha(128)

    # Blitting

    screen.blit(endgame, (0, 0))
    screen.blit(text1, (130, 200))
    screen.blit(text2, (230, 300))
    screen.blit(text3, (230, 350))
    pygame.display.update()
    time.sleep(1.5)

# level up


def levelup(speed, level):
    if counter > 0 and counter % 50 == 0:
        level += 1
        speed += 10


# main loop

exit = True
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False

    # movement of snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'

    # direction of snake

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # moving snake on screen

    if direction == 'UP':
        position_of_snake[1] -= 5
    if direction == 'DOWN':
        position_of_snake[1] += 5
    if direction == 'RIGHT':
        position_of_snake[0] += 5
    if direction == 'LEFT':
        position_of_snake[0] -= 5

    # inserting fruit to snake

    body_of_snake.insert(0, (position_of_snake))
    if position_of_snake[0] == position_of_fruit[0] and position_of_fruit[1] == position_of_snake[1]:
        score += 10
        levelup(speed_of_snake, level)
        spawn_of_fruit = False
    else:
        body_of_snake.pop()

    # fruit spawn

    if not spawn_of_fruit:
        position_of_fruit = [random.randrange(
            1, (width//10)*10), random.randrange(1, (height//10)*10)]
    spawn_of_fruit = True

    # draw

    screen.fill(black)
    for position in body_of_snake:
        pygame.draw.rect(screen, blue, pygame.Rect(
            position[0], position[1], 10, 10))
    pygame.draw.rect(screen, color_of_fruit, pygame.Rect(
        position_of_fruit[0], position_of_fruit[1], 10, 10))

    # Conditions for snake

    if position_of_snake[0] < 0 or position_of_snake[0] > width-10:
        exit = False
    if position_of_snake[1] < 0 or position_of_snake[1] > height-10:
        exit = False

    # last details

    score()
    pygame.display.update()
    clock.tick(fps)

# ending game

game_over()
