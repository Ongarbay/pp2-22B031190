# libraries

import pygame
import random
import time


# including pygame

pygame.init()

# colors

White, black, grey, red, blue, green = (
    255, 255, 255), (0, 0, 0), (60, 60, 60), (255, 0, 0), (0, 0, 255), (0, 255, 0)

# Setting

height, width = 600, 400
screen = pygame.display.set_mode((width, height))
street = pygame.image.load("Street.png")
screen.blit(street, (0, 0))

pygame.display.set_caption("Car Racing")
pygame.display.set_icon(pygame.image.load("Racing Icon.png"))

Oshiheteo = pygame.mixer.Channel(0).play(pygame.mixer.Sound("ОШИХЕТЕО.mp3"))
clock = pygame.time.Clock()
fps = 60
small = pygame.font.SysFont("", 30)
collection = "collection.mp3"

# Sprites

Player = "White lamba.png"
Opposite = "Yellow lamba.png"
coin = "Coin.png"
speed, counter, score = 5, 0, 0

# Player car


class Player_car(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(Player)
        self.image = pygame.transform.scale(self.image, (30, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    # movement of player

    def movement(self):
        pressed = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed[pygame.K_LEFT]:
                self.rect.move_ip(-7.5, 0)
        if self.rect.right < width:
            if pressed[pygame.K_RIGHT]:
                self.rect.move_ip(7.5, 0)

        if self.rect.bottom < height:
            if pressed[pygame.K_DOWN]:
                self.rect.move_ip(0, 7.5)
        if self.rect.top > 0:
            if pressed[pygame.K_UP]:
                self.rect.move_ip(0, -7.5)


# Enemies

class Enemy(pygame.sprite.Sprite):
    # setting enemy car

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(Opposite)
        self.image = pygame.transform.scale(self.image, (35, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(35, width-35), 0)

    # movement

    def movement(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.top > height:
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(35, width-35), 0)

# Coin


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(coin)
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(35, width-35), 0)
    # movement of coin

    def calling(self):
        self.rect.top = 0
        self.rect.center = (random.randint(35, width-35), 0)

    def movement(self):
        self.rect.move_ip(0, 4)
        if self.rect.top > height:
            self.calling()

# After crush


def game_over():

    # setting end game surfacse

    boom = pygame.image.load("boom.png")
    gameover = pygame.Surface(screen.get_size())
    gameover.fill(red)
    font = pygame.font.SysFont("", 80)
    text = font.render("GAME OVER", False, black)
    crash_sound = pygame.mixer.Sound("crash.wav")

    # blit surfaces

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    gameover.blit(text, (25, 200))
    screen.blit(boom, (25, 150))
    pygame.display.update()
    time.sleep(2)
    screen.blit(gameover, (0, 0))
    pygame.display.update()
    time.sleep(1)


# Create sprites

racer = Player_car()
enemy1 = Enemy()
enemy2 = Enemy()
enemy3 = Enemy()
tenge1 = Coin()
tenge2 = Coin()

# Create Groups

sprites = pygame.sprite.Group()
vehicle = pygame.sprite.Group()
coins = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# adding into groups

vehicle.add(racer)
enemies.add(enemy1)
sprites.add(racer)
sprites.add(enemy1)
sprites.add(tenge1)
coins.add(tenge1)

# main loop

exit = True
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False

    # Conditions

    if score % 5 == 0 and score > 0:
        speed += 0.005

    if score >= 15:
        enemies.add(enemy2)
        sprites.add(enemy2)

    if score >= 40:
        enemies.add(enemy3)
        sprites.add(enemy3)
        coins.add(tenge2)
        sprites.add(tenge2)

    # Blitting

    screen.blit(street, (0, 0))
    scores = small.render("Score:"+str(score), True, black)
    screen.blit(scores, (10, 10))

    for sprite in sprites:
        screen.blit(sprite.image, sprite.rect)
        sprite.movement()

    # Condition for crash

    if pygame.sprite.spritecollideany(racer, enemies):
        game_over()
        exit = False

    # Condition for coins

    if pygame.sprite.spritecollideany(tenge1, vehicle):
        counter += 1
        tenge1.calling()
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(collection))

    if pygame.sprite.spritecollideany(tenge2, vehicle):
        counter += 1
        pygame.mixer.Channel(2).play(pygame.mixer.Sound(collection))
        tenge2.calling()

    if (counter > 9):
        speed -= 0.005
        pygame.mixer.Channel(3).play(pygame.mixer.Sound("manycoins.mp3"))
        counter -= 10

    text = small.render("Coins:"+str(counter), True, black)
    screen.blit(text, (315, 10))

    # updating

    pygame.display.update()
    clock.tick(fps)
