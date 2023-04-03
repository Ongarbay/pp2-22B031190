import pygame
import os


pygame.init()

height, width = 600, 600
screen = pygame.display.set_mode((height, width))
exit = False

Musics = "C:\\Users\\lenovo\\OneDrive\\Desktop\\pp2-22B031190\\TSIS7\\Musics\\"
List_of_Musics = os.listdir(Musics)

Index, font = 0, pygame.font.SysFont(None, 24)
pygame.mixer.music.load(Musics+List_of_Musics[Index])

play = pygame.K_SPACE
next = pygame.K_RIGHT
previous = pygame.K_LEFT
stop = pygame.K_TAB

words = {
    play: "Play",
    next: "Next",
    previous: "Previous",
    stop: "Stop",
}
positions = {
    play: (50, height-100,),
    stop: (150, height-100,),
    next: (250, height-100,),
    previous: (350, height-100,),
}
for key in positions:
    text = words[key]
    surface = font.render(text, True, (255, 255, 255,))
    rectangle = surface.get_rect(center=positions[key])
    screen.blit(surface, rectangle)

pygame.mixer.music.play()

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
            pygame.quit()
        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == play:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == stop:
                pygame.mixer.music.stop()
            elif event.key == previous:
                Index = (Index+1) % len(List_of_Musics)
                pygame.mixer.music.load(Musics+List_of_Musics[Index])
                pygame.mixer.music.play()
            elif event.key == next:
                Index = (Index-1) % len(List_of_Musics)
                pygame.mixer.music.load(Musics+List_of_Musics[Index])
                pygame.mixer.music.play()
    pygame.display.update()