import pygame
from datetime import datetime
pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

image = pygame.image.load('clock.png')
im_min = pygame.image.load('min_hand.png')
im_sec = pygame.image.load('sec_hand.png')

rect_min = im_min.get_rect(center=(width // 2, height // 2))
rect_sec = im_sec.get_rect(center=(width // 2, height // 2))

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(image, (0, 0))

    x = datetime.now()
    minuten = x.minute 
    seconden = x.second

    angle_min = minuten * (-6) 
    angle_sec = seconden * (-6) 

    r_im_min = pygame.transform.rotate(im_min, angle_min)
    r_rect_min = r_im_min.get_rect(center=rect_min.center)

    r_im_sec = pygame.transform.rotate(im_sec, angle_sec)
    r_rect_sec = r_im_sec.get_rect(center=rect_sec.center)

    screen.blit(r_im_min, r_rect_min.topleft)
    screen.blit(r_im_sec, r_rect_sec.topleft)

    pygame.display.flip()
    clock.tick(1)

pygame.quit()