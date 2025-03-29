import pygame

pygame.init()

# Настройки
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Белый фон

    # Квадрат
    pygame.draw.rect(screen, (0, 0, 255), (50, 50, 100, 100))

    # Равносторонний треугольник
    pygame.draw.polygon(screen, (255, 0, 0), [(250, 150), (200, 250), (300, 250)])

    # Ромб
    pygame.draw.polygon(screen, (0, 255, 0), [(450, 150), (500, 200), (450, 250), (400, 200)])

    pygame.display.flip()

pygame.quit()