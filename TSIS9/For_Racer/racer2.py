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
platinum = "Platinum-Coin.png"
gold = "Golden-Coin.png"
silver = "Silver-Coin.png"
bronze = "Bronze-Coin.png"

# Points

minutes = seconds = 0
speed = 5
counter = 0
check = 6

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
                self.rect.move_ip(-5, 0)
        if self.rect.right < width:
            if pressed[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)
        if self.rect.bottom < height:
            if pressed[pygame.K_DOWN]:
                self.rect.move_ip(0, 5)
        if self.rect.top > 0:
            if pressed[pygame.K_UP]:
                self.rect.move_ip(0, -5)


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
        self.rect.move_ip(0, speed)
        if self.rect.top > height:
            self.rect.top = 0
            self.rect.center = (random.randint(35, width-35), 0)

# Bronze Coin


class Bronze_Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(bronze)
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(35, width-35), 0)

    def calling_of_bronze(self):
        self.rect.top = 0
        self.rect.center = (random.randint(35, width-35), 0)

    def movement(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > height:
            self.calling_of_bronze()


# Silver Coin


class Silver_Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(silver)
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(35, width-35), 0)

    def calling_of_silver(self):
        self.rect.top = 0
        self.rect.center = (random.randint(35, width-35), 0)

    def movement(self):
        self.rect.move_ip(0, 4)
        if self.rect.top > height:
            self.calling_of_silver()

# Gold Coin


class Golden_Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(gold)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, width-30), 0)

    def calling_of_golden(self):
        self.rect.top = 0
        self.rect.center = (random.randint(30, width-30), 0)

    def movement(self):
        self.rect.move_ip(0, 3)
        if self.rect.top > height:
            self.calling_of_golden()

# Platinum Coin


class Platinum_Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(platinum)
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(25, width-25), 0)

    def calling_of_platinum(self):
        self.rect.top = 0
        self.rect.center = (random.randint(25, width-25), 0)

    def movement(self):
        self.rect.move_ip(0, 2)
        if self.rect.top > height:
            self.calling_of_platinum()

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

racer1 = Player_car()
enemy1 = Enemy()
enemy2 = Enemy()
enemy3 = Enemy()
enemy4 = Enemy()
cheap1 = Bronze_Coin()
cheap2 = Bronze_Coin()
average1 = Silver_Coin()
expensive1 = Golden_Coin()
extravagant1 = Platinum_Coin()

# Create Groups

Sprites = pygame.sprite.Group()
Players = pygame.sprite.Group()
Enemies = pygame.sprite.Group()
Bronzes = pygame.sprite.Group()
Silvers = pygame.sprite.Group()
Golds = pygame.sprite.Group()
Platinums = pygame.sprite.Group()

# adding into groups

Sprites.add(racer1)
Sprites.add(enemy1)
Sprites.add(cheap1)
Sprites.add(average1)
Players.add(racer1)
Enemies.add(enemy1)
Bronzes.add(cheap1)
Silvers.add(average1)

# main loop

exit = True
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False

    # Difficulty

    if counter >= 10 and counter <= 13:
        speed += 0.005
        Sprites.add(cheap2)
        Bronzes.add(cheap2)

    if counter >= 20 and counter <= 23:
        speed += 0.005
        Sprites.add(enemy2)
        Enemies.add(enemy2)
        Golds.add(expensive1)
        Sprites.add(expensive1)

    if counter >= 40 and counter <= 43:
        speed += 0.010
        Sprites.add(enemy3)
        Enemies.add(enemy3)
        Platinums.add(extravagant1)
        Sprites.add(extravagant1)

    if check*10 < counter:
        speed += 0.005
        check += 2

    if counter >= 120 and counter <= 130:
        Sprites.add(enemy4)
        Enemies.add(enemy4)
    
    # Conditions for crushing

    if pygame.sprite.spritecollideany(racer1, Enemies):
        game_over()
        exit = False

    # Conditions for coins

    if pygame.sprite.spritecollideany(cheap1, Players):
        counter += 1
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(collection))
        cheap1.calling_of_bronze()

    if pygame.sprite.spritecollideany(cheap2, Players):
        counter += 1
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(collection))
        cheap2.calling_of_bronze()

    if pygame.sprite.spritecollideany(average1, Players):
        counter += 2
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(collection))
        average1.calling_of_silver()

    if pygame.sprite.spritecollideany(expensive1, Players):
        counter += 4
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(collection))
        expensive1.calling_of_golden()

    if pygame.sprite.spritecollideany(extravagant1, Players):
        counter += 7
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(collection))
        extravagant1.calling_of_platinum()

    # Blitting

    screen.blit(street, (0, 0))
    scores = small.render("Timer: "+str(minutes)+":"+str(round(seconds)), True, black)
    screen.blit(scores, (10, 10))

    for sprite in Sprites:
        screen.blit(sprite.image, sprite.rect)
        sprite.movement()

    text = small.render("Coins:"+str(counter), True, black)
    screen.blit(text, (300, 10))
    seconds += 0.01
    if (seconds == 60):
        seconds = 0
        minutes += 1

    # updating

    pygame.display.update()
    clock.tick(fps)
