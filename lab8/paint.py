import pygame

pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen.fill(WHITE)
color = BLACK
drawing = False
mode = "pencil"

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
        
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            if mode == "rectangle":
                pygame.draw.rect(screen, color, (*start_pos, event.pos[0] - start_pos[0], event.pos[1] - start_pos[1]), 2)
            elif mode == "circle":
                radius = int(((event.pos[0] - start_pos[0])**2 + (event.pos[1] - start_pos[1])**2)**0.5)
                pygame.draw.circle(screen, color, start_pos, radius, 2)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rectangle"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_e:
                mode = "eraser"
                color = WHITE
            elif event.key == pygame.K_p:
                mode = "pencil"
                color = BLACK
            elif event.key == pygame.K_b:
                color = BLUE
            elif event.key == pygame.K_k:
                color = BLACK

    if drawing and mode == "pencil":
        pygame.draw.circle(screen, color, pygame.mouse.get_pos(), 3)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()