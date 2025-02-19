import pygame

class Player:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.velocity = pygame.Vector2(3, 0) # Изачальная скорость
        self.acceleration = 0.1 # Ускорение
        self.jumping = False # Был ли уже прыжок

    def update(self, keys):
        # Проверка нажатия пробела
        if self.jumping and keys[pygame.K_SPACE] == False:
            self.jumping = False # Сброс прыжка

        # Управление движением
        if keys[pygame.K_SPACE] and not self.jumping:
            self.velocity.y = -3  # Применение силы прыжка
            self.jumping = True # Запрет прыжка

        # Обновление позиции
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        # Применение ускорения по оси Y (гравитация)
        self.velocity.y += self.acceleration

        # Проверка на выход за границы по Y
        if self.rect.bottom > 600 or self.rect.top < 0:
            self.rect.y = 250
            self.rect.x = 100
            self.velocity.y = 0
            self.velocity.x = 3

        # Проверка на выход за границы по X
        if self.rect.right > 800:
            self.velocity.x = -3
        if self.rect.left < 0:
            self.velocity.x = 3

    def draw(self, display):
        pygame.draw.rect(display, (100, 100, 200), self.rect)

class Enemy:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def spawm(self, display):
        pygame.draw.rect(display, (200, 100, 200), self.rect)


# Инициализация
pygame.init()
display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Basic Game')
clock = pygame.time.Clock()

player = Player(100, 250, 50, 50)
enemy = Enemy(500, 500, 25, 25)

running = True
while running:
    keys = pygame.key.get_pressed()
    display.fill((100, 200, 100))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:  # Реагируем на нажатие клавиши
            if event.key == pygame.K_SPACE:
                player.update(keys)

    player.update(keys)
    player.draw(display)

    enemy.spawm(display)

    pygame.display.update()
    clock.tick(100)