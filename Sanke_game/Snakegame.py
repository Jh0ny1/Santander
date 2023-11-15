import pygame
import sys
import time
import random

# Inicialização do Pygame
pygame.init()

# Definição de variáveis
width, height = 600, 400
snake_size = 20
snake_speed = 15

# Cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Criação da janela
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Função para desenhar a cobra
def draw_snake(snake_list):
    for segment in snake_list:
        pygame.draw.rect(screen, white, 
[segment
[0], segment
[1], snake_size, snake_size])

# Função principal do jogo
def game():
    game_over = False
    game_close = False

    # Posição inicial da cobra
    x = width / 2
    y = height / 2

    # Inicialização da velocidade da cobra
    x_speed = 0
    y_speed = 0

    # Lista para armazenar os segmentos da cobra
    snake_list = 
[]
    length_of_snake = 1

    # Posição inicial da maçã
    apple_x = round(random.randrange(0, width - snake_size) / snake_size) * snake_size
    apple_y = round(random.randrange(0, height - snake_size) / snake_size) * snake_size

    while not game_over:

        while game_close:
            screen.fill(black)
            font = pygame.font.SysFont(None, 50)
            text = font.render("Você perdeu! Pressione Q para sair ou C para jogar novamente.", True, red)
            screen.blit(text, (width / 6, height / 3))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                elif event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                elif event.key == pygame.K_UP:
                    y_speed = -snake_size
                    x_speed = 0
                elif event.key == pygame.K_DOWN:
                    y_speed = snake_size
                    x_speed = 0

        if x >= width or x 
< 0 or y >= height or y 
< 0:
            game_close = True
        x += x_speed
        y += y_speed
        screen.fill(black)
        pygame.draw.rect(screen, red, 
[apple_x, apple_y, snake_size, snake_size])
        snake_head = 
[]
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list
[0]

        for segment in snake_list
[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_list)

        pygame.display.update()

        if x == apple_x and y == apple_y:
            apple_x = round(random.randrange(0, width - snake_size) / snake_size) * snake_size
            apple_y = round(random.randrange(0, height - snake_size) / snake_size) * snake_size
            length_of_snake += 1

        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    sys.exit()

# Iniciar o jogo
game()
