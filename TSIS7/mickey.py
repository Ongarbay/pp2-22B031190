import pygame
import time
pygame.init()

window_size = (829, 836)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Mickey Mouse Clock")
clock = pygame.time.Clock()
mickey = pygame.image.load("C:\\Users\\lenovo\\OneDrive\\Desktop\\pp2-22B031190\\TSIS7\\main-clock.png")
minute_hand = pygame.image.load("C:\\Users\\lenovo\\OneDrive\\Desktop\\pp2-22B031190\\TSIS7\\righthand.png")
second_hand = pygame.image.load("C:\\Users\\lenovo\\OneDrive\\Desktop\\pp2-22B031190\\TSIS7\\lefthand.png")

minute_hand_pos = (window_size[0] // 2, window_size[1] // 2)
second_hand_pos = (window_size[0] // 2, window_size[1] // 2)

exit = False
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    minute_angle = (minutes / 60) * 360
    second_angle = (seconds / 60) * 360

    minute_hand_rotated = pygame.transform.rotate(minute_hand, 90-minute_angle)
    second_hand_rotated = pygame.transform.rotate(second_hand, 90-second_angle)

    minute_hand_pos = (window_size[0] // 2 - minute_hand_rotated.get_width() // 2,
                       window_size[1] // 2 - minute_hand_rotated.get_height() // 2)
    second_hand_pos = (window_size[0] // 2 - second_hand_rotated.get_width() // 2,
                       window_size[1] // 2 - second_hand_rotated.get_height() // 2)

    window.fill((255, 255, 255))

    window.blit(mickey, (0, 0))
    window.blit(minute_hand_rotated, minute_hand_pos)
    window.blit(second_hand_rotated, second_hand_pos)

    pygame.display.flip()
    pygame.time.delay(1000)
