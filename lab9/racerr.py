import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

# Загрузка изображений машин
player_img = pygame.image.load("lab8/player.png")  # Машина игрока
enemy_img = pygame.image.load("lab8/enemy.png")  # Вражеская машина

# Масштабирование изображений
player_img = pygame.transform.scale(player_img, (50, 100))
enemy_img = pygame.transform.scale(enemy_img, (50, 100))

# Игрок
player = pygame.Rect(175, 500, 50, 100)
player_speed = 5

# Враг (препятствие)
obstacle = pygame.Rect(random.randint(50, 300), -100, 50, 100)
obstacle_speed = 5  # Начальная скорость врага

# Монеты
coins = []
coin_size = 20
coin_speed = 5
coins_collected = 0  # Счетчик монет

# Количество монет для увеличения скорости врага
N = 5  # После каждой N монет враг становится быстрее

# Шрифт
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
running = True

while running:
    screen.fill((0, 128, 0))  # Зеленый фон (дорога)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Движение игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 50:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < 300:
        player.x += player_speed

    # Движение врага
    obstacle.y += obstacle_speed
    if obstacle.y > HEIGHT:
        obstacle.y = -100
        obstacle.x = random.randint(50, 300)

    # Столкновение с врагом
    if player.colliderect(obstacle):
        print("Game Over!")
        running = False

    # Генерация монет с разными весами
    if random.randint(1, 100) < 5:
        coin_weight = random.randint(1, 3)  # Вес монеты (1-3)
        coins.append({"rect": pygame.Rect(random.randint(50, 300), -20, coin_size, coin_size),
                      "weight": coin_weight})

    # Движение монет
    for coin in coins[:]:
        coin["rect"].y += coin_speed
        if coin["rect"].colliderect(player):  # Если игрок собрал монету
            coins_collected += coin["weight"]
            coins.remove(coin)
            # Увеличение скорости врага каждые N монет
            if coins_collected % N == 0:
                obstacle_speed += 1
        elif coin["rect"].y > HEIGHT:
            coins.remove(coin)

    # Отрисовка машин
    screen.blit(player_img, (player.x, player.y))
    screen.blit(enemy_img, (obstacle.x, obstacle.y))

    # Отрисовка монет (разные цвета в зависимости от веса)
    for coin in coins:
        color = (255, 255, 0) if coin["weight"] == 1 else (255, 165, 0) if coin["weight"] == 2 else (255, 0, 0)
        pygame.draw.circle(screen, color, (coin["rect"].x + 10, coin["rect"].y + 10), 10)

    # Отображение счета
    text = font.render(f"Coins: {coins_collected}", True, (255, 255, 255))
    screen.blit(text, (WIDTH - 120, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()