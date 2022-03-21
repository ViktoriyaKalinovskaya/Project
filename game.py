import pygame
from random import randrange

Field = 800
Size = 30
x, y = randrange(0, Field, Size), randrange(0, Field, Size)
food = randrange(0, Field, Size),randrange(0, Field, Size)
dirs = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': True}
snake_lenght = 1
snake = [(x, y)]
score = 0
rx, ry = 0, 0
speed = 4

pygame.init()
window = pygame.display.set_mode([Field, Field])
reg_time = pygame.time.Clock()
font_score = pygame.font.SysFont('Calibri', 20, bold=True)
font_end = pygame.font.SysFont('Calibri', 62, bold=True)

while True:
    window.fill(pygame.Color('white'))
    [(pygame.draw.rect(window, pygame.Color('black'), (i, j, Size, Size))) for i, j in snake]
    pygame.draw.rect(window, pygame.Color('yellow'), (*food, Size, Size))
    r_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('blue'))
    window.blit(r_score, (5, 5))
    x += rx * Size
    y += ry * Size
    snake.append((x, y))
    snake = snake[-snake_lenght:]

    if snake[-1] == food:
        food = randrange(0, Field, Size), randrange(0, Field, Size)
        snake_lenght += 1
        score += 1
        speed += 1

    if x < 0 or x > Field - Size or y < 0 or y > Field - Size:
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('blue'))
            window.blit(render_end, (Field // 2 - 150, Field // 2))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
    elif len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('blue'))
            window.blit(render_end, (Field // 2 - 200, Field // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    pygame.display.flip()
    reg_time.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and dirs['UP']:
        rx, ry = 0, -1
        dirs = {'UP': True, 'DOWN': False, 'LEFT': True, 'RIGHT': True}
    elif key[pygame.K_DOWN] and dirs['DOWN']:
        rx, ry = 0, 1
        dirs = {'UP': False, 'DOWN': True, 'LEFT': True, 'RIGHT': True}
    elif key[pygame.K_LEFT] and dirs['LEFT']:
        rx, ry = -1, 0
        dirs = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': False}
    elif key[pygame.K_RIGHT] and dirs['RIGHT']:
        rx, ry = 1, 0
        dirs = {'UP': True, 'DOWN': True, 'LEFT': False, 'RIGHT': True}