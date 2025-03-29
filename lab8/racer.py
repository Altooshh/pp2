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

# Игрок (его координаты и размер)
player = pygame.Rect(175, 500, 50, 100)
player_speed = 5  # Скорость передвижения игрока

# Вражеская машина (препятствие)
obstacle = pygame.Rect(random.randint(50, 300), -100, 50, 100)
obstacle_speed = 5  # Скорость движения врага

# Монеты
coins = []  # Список для хранения монет
coin_size = 20  # Размер монеты
coin_speed = 5  # Скорость падения монет
coins_collected = 0  # Количество собранных монет

# Шрифт для отображения счета
font = pygame.font.Font(None, 36)

# Создание игрового цикла
clock = pygame.time.Clock()
running = True

while running:
    screen.fill((0, 128, 0))  # Фон (зелёная дорога)

    # Обработка событий (выход из игры)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление машиной игрока (влево/вправо)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 50:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < 300:
        player.x += player_speed

    # Движение вражеской машины
    obstacle.y += obstacle_speed
    if obstacle.y > HEIGHT:
        obstacle.y = -100
        obstacle.x = random.randint(50, 300)

    # Проверка столкновения игрока с вражеской машиной
    if player.colliderect(obstacle):
        print("Game Over!")  # Вывод в консоль (можно заменить на экранный текст)
        running = False  # Остановка игрового цикла

    # Генерация монет (вероятность появления 3% за каждый кадр)
    if random.randint(1, 100) < 3:
        coins.append(pygame.Rect(random.randint(50, 300), -20, coin_size, coin_size))

    # Движение монет
    for coin in coins[:]:
        coin.y += coin_speed  # Монета падает вниз
        if coin.colliderect(player):  # Если игрок собрал монету
            coins.remove(coin)
            coins_collected += 1  # Увеличиваем счётчик монет
        elif coin.y > HEIGHT:  # Если монета выходит за границу экрана
            coins.remove(coin)

    # Отрисовка машин
    screen.blit(player_img, (player.x, player.y))
    screen.blit(enemy_img, (obstacle.x, obstacle.y))

    # Отрисовка монет (жёлтые круги)
    for coin in coins:
        pygame.draw.circle(screen, (255, 255, 0), (coin.x + 10, coin.y + 10), 10)

    # Отображение количества собранных монет
    text = font.render(f"Coins: {coins_collected}", True, (255, 255, 255))
    screen.blit(text, (WIDTH - 120, 10))  # Располагаем в правом верхнем углу

    pygame.display.flip()
    clock.tick(30)  # Ограничение FPS

# Завершение игры
pygame.quit()