import pygame

pygame.init()

height, width = 800, 800
screen = pygame.display.set_mode((height, width), pygame.RESIZABLE)
pygame.display.set_caption("LOL")
pygame.display.set_icon(pygame.image.load("mushroom.png"))

exit = True
clock = pygame.time.Clock()
FPS = 60

WHITE, BLACK, GREEN, BLUE, RED = (
    255, 255, 255), (0, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 0)
control, end = (0, 0), (0, 0)
x, y = height//4, width//4
speed = 5
draw = False
surface = pygame.Surface((400, 400))
surface.fill(RED)
screen.fill(BLUE)
surface.set_alpha(255)
pygame.draw.circle(surface, GREEN, (200, 200), 100, 50)
screen.blit(surface, (x, y))
pygame.display.update()
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
    clock.tick(FPS)
