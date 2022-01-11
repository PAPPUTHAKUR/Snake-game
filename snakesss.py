import pygame
import random
import os
pygame.mixer.init()




pygame.init()
screen_width = 900
screen_height = 600

# crearing window
gamewindow = pygame.display.set_mode((screen_width, screen_height))

#backgroung image
bimage = pygame.image.load('a1.jpg')
bimage = pygame.transform.scale(bimage,(screen_width,screen_height)).convert_alpha()

pygame.display.set_caption("Snake and Grow")
pygame.display.update()
# clock
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    scree_test = font.render(text, True, color)
    gamewindow.blit(scree_test, [x, y])


def plot_snake(gamewindow, black, snake_list, snake_size):
    # print(snake_list)
    for x, y in snake_list:
        pygame.draw.rect(gamewindow, black, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    game_over = False
    # colorss
    # it is rgb valuess of color learn in css and html
    white = (255, 255, 255)
    red = (255, 0, 0)
    black = (0, 0, 0)
    fps = 20
    exit_game = False
    while not exit_game:
        gamewindow.fill(white)
        text_screen("welcome to Game",black,200,300)
        text_screen("Press spacebar to play", black, 200, 340)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('Jiya Ho Bihar Ke Lala-Manoj Tiwari -VlcMusic.CoM.mp3')
                    pygame.mixer.music.play()
                    game_loop()
        pygame.display.update()
        clock.tick(fps)




# game loop
def game_loop():
    # game specific variable
    exit_game = False
    game_over = False
    # colorss
    # it is rgb valuess of color learn in css and html
    white = (255, 255, 255)
    red = (255, 0, 0)
    black = (0, 0, 0)

    snake_x = 55
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snake_size = 11

    snake_length = 1
    snake_list = []
    with open("highscore.txt", 'r') as f:
        hihscore = f.read()

    fps = 20
    food_x = random.randint(0, screen_width)
    food_y = random.randint(0, screen_height)
    score = 0

    while not exit_game:
        if game_over:
            with open("highscore.txt", 'w') as f:
                f.write(str(hihscore))
            gamewindow.fill(white)
            text_screen("GAMEOVER!", red, 200, 300)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 10
                        velocity_y = 0
                        # snake_x = snake_x + 5

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        velocity_x = -10
                        velocity_y = 0
                        # snake_x = snake_x - 5

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        velocity_x = 0
                        velocity_y = -10
                        # snake_y = snake_y - 5

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = 10
                        # snake_y = snake_y + 5

                if  event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        score = score + 5

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score = score + 10
                # print("score", score * 10)

                food_x = random.randint(0, screen_width)
                food_y = random.randint(0, screen_height)
                snake_length = snake_length + 2
                if score > int(hihscore):
                    hihscore = score

            gamewindow.fill(white)
            gamewindow.blit(bimage,(0,0))
            text_screen("score :" + str(score) + "Highscore: " + str(hihscore), red, 5, 5)
            pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load('samir_fuddi_oh_yeah.mp3')
                pygame.mixer.music.play()
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                pygame.mixer.music.load('samir_fuddi_oh_yeah.mp3')
                pygame.mixer.music.play()
                game_over = True
                # print("game over")
            # pygame.draw.rect(gamewindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gamewindow, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


#game_loop()
welcome()
