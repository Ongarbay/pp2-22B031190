import pygame
import os

pygame.init()
screen_width, screen_height = 500, 100
screen = pygame.display.set_mode((screen_width, screen_height))

Musics = "C:\\Users\\lenovo\\OneDrive\\Desktop\\pp2-22B031190\\TSIS7\\Musics\\"
music_files = os.listdir(Musics)
current_music = 0
pygame.mixer.music.load(Musics + music_files[current_music])

font = pygame.font.SysFont(None, 24)

key_play = pygame.K_SPACE
key_stop = pygame.K_ESCAPE
key_next = pygame.K_RIGHT
key_prev = pygame.K_LEFT

labels = {
    key_play: "Play",
    key_stop: "Stop",
    key_next: "Next",
    key_prev: "Previous",
}

label_pos = {
    key_play: (50, screen_height - 50),
    key_stop: (150, screen_height - 50),
    key_next: (250, screen_height - 50),
    key_prev: (350, screen_height - 50),
}
for key in label_pos:
    label_text = labels[key]
    label_surface = font.render(label_text, True, (255, 255, 255,))
    label_rect = label_surface.get_rect(center=label_pos[key])
    screen.blit(label_surface, label_rect)

pygame.mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == key_play:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            elif event.key == key_stop:
                pygame.mixer.music.stop()

            elif event.key == key_next:
                current_music = (current_music + 1) % len(music_files)
                pygame.mixer.music.load(Musics + music_files[current_music])
                pygame.mixer.music.play()

            elif event.key == key_prev:
                current_music = (current_music - 1) % len(music_files)
                pygame.mixer.music.load(Musics + music_files[current_music])
                pygame.mixer.music.play()

    pygame.display.update()
