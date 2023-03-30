import  pygame

# Инициализация Pygame
pygame.init()

# Установка размера окна
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Установка цвета фона
background_color = (255, 255, 255)

# Установка цвета квадрата
square_color = (255, 0, 0)

# Установка размеров и положения квадрата
square_width = 50
square_height = 50
square_x = screen_width // 2 - square_width // 2
square_y = screen_height // 2 - square_height // 2

# Основной игровой цикл
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Заливка фона цветом
    screen.fill(background_color)

    # Рисование квадрата
    pygame.draw.rect(screen, square_color, (square_x, square_y, square_width, square_height))

    # Обновление экрана
    pygame.display.update()
