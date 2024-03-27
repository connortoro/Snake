import pygame
import random
import sys

#init
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((600, 600))
font = pygame.font.Font(None, 46)
pygame.display.set_caption("My Snake Game!")

#global
eat_sound = pygame.mixer.Sound("ESM_Game_Notification_81_Coin_Blip_Select_Tap_Button.wav")
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 12, 12)
green = (0, 255, 0)
size = 20
dir = 1
score = 0

#players
snake = [pygame.Rect(300, 300, size, size), pygame.Rect(280, 300, size, size)]
fruit = pygame.Rect(400, 460, size, size)

def read_input():
    global dir
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT] and dir != 1:
        dir = 0
    elif pressed[pygame.K_RIGHT] and dir != 0:
        dir = 1
    elif pressed[pygame.K_DOWN] and dir != 3:
        dir = 2
    elif pressed[pygame.K_UP] and dir != 2:
        dir = 3

def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, white, segment)

def move_snake():
    global dir
    global snake
    new_head = snake[0].copy()
    if dir == 0:
        new_head.x -= size
    elif dir == 1:
        new_head.x += size
    elif dir == 2:
        new_head.y += size
    else:
        new_head.y -= size

    snake.insert(0, new_head)
    snake.pop()

def move_snake_coll():
    global dir
    global snake
    new_head = snake[0].copy()
    if dir == 0:
        new_head.x -= size
    elif dir == 1:
        new_head.x += size
    elif dir == 2:
        new_head.y += size
    else:
        new_head.y -= size

    snake.insert(0, new_head)

def new_fruit():
    global fruit
    randx = random.randrange(30)
    randy = random.randrange(30)
    fruit = pygame.Rect(randx*size, randy*size, size, size)

def death():
    screen.fill(black)
    game_over_text = font.render("GAME OVER :(", True, red)
    game_over_text_rect = game_over_text.get_rect()
    game_over_text_rect.center = (300, 300)

    exit_text = font.render("EXIT", True, red)
    exit_text_rect = exit_text.get_rect()
    exit_text_rect.center = (300, 450)

    score_str = "Score: " + str(score)
    score_text = font.render(score_str, True, white)
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (300, 180)

    outline = pygame.Rect(exit_text_rect.left-5, exit_text_rect.top-5, exit_text_rect.width+10, exit_text_rect.height+10)
    inline = pygame.Rect(outline.x+2, outline.y+2, outline.width-4, outline.height-4)
    pygame.draw.rect(screen, red, outline)
    pygame.draw.rect(screen, black, inline)


    screen.blit(score_text, score_text_rect)
    screen.blit(exit_text, exit_text_rect)
    screen.blit(game_over_text, game_over_text_rect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if exit_text_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.quit()
        pygame.time.Clock().tick(60)

#main
while True:

    #exit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    #game play
    read_input()
    if snake[0].colliderect(fruit):
        eat_sound.play()
        move_snake_coll()
        new_fruit()
        score += 1
    else:
        move_snake()

    if (snake[0].x >= 600) or (snake[0].x < 0) or (snake[0].y >= 600) or (snake[0].y < 0):
        death()

    for segment in snake[1:]:
        if snake[0].colliderect(segment):
            death()

    #draw
    screen.fill(black)
    draw_snake()
    pygame.draw.rect(screen, red, fruit)
    pygame.display.flip()

    pygame.time.Clock().tick(15)




