import pygame
import random

pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Змейка
snake = [(250, 250)]
snake_dir = (10, 0)
speed = 10

# Еда
def spawn_food():
    while True:
        pos = (random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10))
        if pos not in snake:
            return pos

food = spawn_food()

# Очки и уровни
score = 0
level = 1
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != (0, 10):
        snake_dir = (0, -10)
    if keys[pygame.K_DOWN] and snake_dir != (0, -10):
        snake_dir = (0, 10)
    if keys[pygame.K_LEFT] and snake_dir != (10, 0):
        snake_dir = (-10, 0)
    if keys[pygame.K_RIGHT] and snake_dir != (-10, 0):
        snake_dir = (10, 0)

    # Движение змейки
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    
    # Проверка на границы
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT or new_head in snake:
        running = False
    
    snake.insert(0, new_head)

    # Проверка еды
    if new_head == food:
        score += 1
        food = spawn_food()
        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    # Отрисовка
    pygame.draw.rect(screen, RED, (food[0], food[1], 10, 10))
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], 10, 10))
    
    text = font.render(f"Score: {score}  Level: {level}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()