import pygame as pg
import time
import random

snake_speed = 15
window_x = 760
window_y = 420
black = pg.Color(0, 0, 0)
white = pg.Color(255, 255, 255)
red = pg.Color(255, 0, 0)
green = pg.Color(0, 255, 0)
blue = pg.Color(0, 0, 255)

pg.init()
pg.display.set_caption("Snake Game")
game_window = pg.display.set_mode((window_x, window_y))

fps = pg.time.Clock()
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

fruit_pos = [
    random.randrange(1, (window_x // 10)) * 10,
    random.randrange(1, (window_y // 10)) * 10,
]

fruit_spawn = True
direction = "RIGHT"
change_to = direction
score = 0

def show_score(color, font, size):
    score_font = pg.font.SysFont(font, size)
    score_surface = score_font.render("Score : " + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

def game_over():
    my_font = pg.font.SysFont("times new roman", 50)
    game_over_surface = my_font.render("YOU DIED", True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop(window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pg.display.flip()
    time.sleep(2)
    pg.quit()
    quit()

while True:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                change_to = "UP"

            if event.key == pg.K_DOWN:
                change_to = "DOWN"

            if event.key == pg.K_LEFT:
                change_to = "LEFT"

            if event.key == pg.K_RIGHT:
                change_to = "RIGHT"

    if change_to == "UP" and direction != "DOWN":
        direction = "UP"

    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"

    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"

    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"
        
    if direction == "UP":
        snake_pos[1] -= 10

    if direction == "DOWN":
        snake_pos[1] += 10

    if direction == "LEFT":
        snake_pos[0] -= 10

    if direction == "RIGHT":
        snake_pos[0] += 10


    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_pos = [
            random.randrange(1, (window_x // 10)) * 10,
            random.randrange(1, (window_y // 10)) * 10,
        ]
    fruit_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        pg.draw.rect(game_window, green, pg.Rect(pos[0], pos[1], 10, 10))

    pg.draw.rect(game_window, white, pg.Rect(fruit_pos[0], fruit_pos[1], 10, 10))

    if snake_pos[0] < 0 or snake_pos[0] > window_x - 10:
        game_over()
        
    if snake_pos[1] < 0 or snake_pos[1] > window_y - 10:
        game_over()
        
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()
            
    show_score(white, "times new roman", 20)
    pg.display.update()
    fps.tick(snake_speed)
