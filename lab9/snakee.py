import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Настройки змейки
snake = [(200, 200)]
snake_dir = (20, 0)
speed = 10
score = 0

# Еда
food = []
food_timer = {}

# Шрифт
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Движение змейки
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: snake_dir = (-20, 0)
    if keys[pygame.K_RIGHT]: snake_dir = (20, 0)
    if keys[pygame.K_UP]: snake_dir = (0, -20)
    if keys[pygame.K_DOWN]: snake_dir = (0, 20)

    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake.insert(0, new_head)

    # Генерация еды с таймером
    if random.randint(1, 100) < 5:
        weight = random.randint(1, 3)
        x, y = random.randint(0, WIDTH // 20 - 1) * 20, random.randint(0, HEIGHT // 20 - 1) * 20
        food.append({"pos": (x, y), "weight": weight})
        food_timer[(x, y)] = pygame.time.get_ticks()

    # Проверка съеденной еды
    for f in food[:]:
        if f["pos"] == new_head:
            score += f["weight"]
            food.remove(f)
            food_timer.pop(f["pos"])
        else:
            # Удаление еды через 5 секунд
            if pygame.time.get_ticks() - food_timer[f["pos"]] > 5000:
                food.remove(f)
                food_timer.pop(f["pos"])

    # Отрисовка змейки
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], 20, 20))

    # Отрисовка еды (разные цвета)
    for f in food:
        color = (255, 255, 0) if f["weight"] == 1 else (255, 165, 0) if f["weight"] == 2 else (255, 0, 0)
        pygame.draw.rect(screen, color, (f["pos"][0], f["pos"][1], 20, 20))

    # Отображение счета
    text = font.render(f"Score: {score}", True, RED)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()