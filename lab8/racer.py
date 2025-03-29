import pygame
import random

pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Игрок
player = pygame.Rect(175, 500, 50, 100)
player_speed = 5

# Препятствия
obstacle = pygame.Rect(random.randint(50, 300), -100, 50, 100)
obstacle_speed = 5

# Монеты
coins = []
coin_size = 20
coin_speed = 5
coins_collected = 0

font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)
    
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

    # Движение препятствия
    obstacle.y += obstacle_speed
    if obstacle.y > HEIGHT:
        obstacle.y = -100
        obstacle.x = random.randint(50, 300)

    # Генерация монет
    if random.randint(1, 100) < 3:
        coins.append(pygame.Rect(random.randint(50, 300), -20, coin_size, coin_size))

    # Движение монет
    for coin in coins[:]:
        coin.y += coin_speed
        if coin.colliderect(player):
            coins.remove(coin)
            coins_collected += 1
        elif coin.y > HEIGHT:
            coins.remove(coin)

    # Отрисовка объектов
    pygame.draw.rect(screen, RED, player)
    pygame.draw.rect(screen, (0, 0, 0), obstacle)
    for coin in coins:
        pygame.draw.circle(screen, YELLOW, (coin.x + 10, coin.y + 10), 10)
    
    # Отображение счета
    text = font.render(f"Coins: {coins_collected}", True, (0, 0, 0))
    screen.blit(text, (WIDTH - 100, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()