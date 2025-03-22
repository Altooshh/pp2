import pygame
pygame.init()

width, height = 800, 600
ball_radius = 25
color_red = (255, 0, 0)
color_background = (255, 255, 255)
movement = 20

screen = pygame.display.set_mode((width, height))
circle_x, circle_y = width // 2, height // 2
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP] and circle_y - movement - ball_radius >= 0:
        circle_y -= movement
    if pressed_keys[pygame.K_DOWN] and circle_y + movement + ball_radius <= height:
        circle_y += movement
    if pressed_keys[pygame.K_RIGHT] and circle_x + movement + ball_radius <= width:
        circle_x += movement
    if pressed_keys[pygame.K_LEFT] and circle_x - movement - ball_radius >= 0:
        circle_x -= movement



    screen.fill(color_background)
    pygame.draw.circle(screen, color_red, (circle_x, circle_y), ball_radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()