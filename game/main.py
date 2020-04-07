import pygame
RED = 255, 0, 0
BLACK = 0, 0, 0
pygame.init()
win = pygame.display.set_mode((320, 240))
win.fill(BLACK)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            print(pygame.event.event_name(event.scancode))
    pygame.display.flip()
