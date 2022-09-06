import pygame
import random
import os

pygame.mixer.init()

pygame.init()


# colors
white = (255, 255, 255)
red = (255, 0, 0)
l_blue = (173, 216, 230)
blue = (0, 0, 255)
black = (0, 0, 0)


# game window
screen_width = 900
screen_height = 500
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# music_images

bgImage=pygame.image.load("background.jpg")
bgImage=pygame.transform.scale(bgImage, (screen_width, screen_height)).convert_alpha()
wcImage= pygame.image.load("welcome.jpg")
wcImage=pygame.transform.scale(wcImage, (screen_width, screen_height)).convert_alpha()
overImage= pygame.image.load("gameOver.jpg")
overImage=pygame.transform.scale(overImage, (screen_width, screen_height)).convert_alpha()



# game title
pygame.display.set_caption("snake-beng")

gameOver = False
gameQuit = False


fps = 50
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 51)


def texting_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def snake_make(gamewindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gamewindow, black, [x, y, snake_size, snake_size])

def welcome():
    
    game_quit1=False
    
    pygame.mixer.music.load('welcome.mp3')
    pygame.mixer.music.play()

    while not game_quit1:

        gameWindow.fill(black)
        gameWindow.blit(wcImage,(0,0))
        texting_screen("Welcome to snake-beng Game", white, 60, 70)
        texting_screen("press space-bar to play", l_blue, 60, 380)

        

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                game_quit1 = True
                

            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_SPACE:
                    game_Loop()
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    game_quit1 = True

        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()



def game_Loop():

    # game specific variables
    gameOver = False
    gameQuit = False

    pygame.mixer.music.load('bgMusic.mp3')
    pygame.mixer.music.play()


    snake_x = 30
    snake_y = 80
    snake_size = 22
    food_size = 22
    velocity_x = 0
    velocity_y = 0

    food_x = random.randint(10, screen_width-160)
    food_y = random.randint(10, screen_height-160)

    snake_list = []
    snake_length = 5

    if(not os.path.exists("highScore.txt")):
        with open("highScore.txt", "w") as f:
            f.write("0")

    with open("highScore.txt", "r") as f:
        high_Score = f.read()

    gameOverText1 = "Game Over! press enter to continue"
    gameOverText2 = "press esc to quit"

    score = 0
    init_velo = 3

    # game loop
    while not gameQuit:
        
        if gameOver:

            with open("highScore.txt", "w") as f:
                f.write(str(high_Score))

            gameWindow.fill(white)
            gameWindow.blit(overImage,(0,0))
            texting_screen(gameOverText1, red, 120, 160)
            texting_screen(gameOverText2, red, 120, 220)


            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    gameQuit = True

                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_RETURN:
                        welcome()
                
                    if events.key == pygame.K_ESCAPE:
                        gameQuit = True

        else:

            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    gameQuit = True

                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_LEFT:
                        velocity_x = -init_velo
                        velocity_y = 0

                    elif events.key == pygame.K_RIGHT:
                        velocity_x = init_velo
                        velocity_y = 0

                    elif events.key == pygame.K_UP:
                        velocity_y = -init_velo
                        velocity_x = 0

                    elif events.key == pygame.K_DOWN:
                        velocity_y = init_velo
                        velocity_x = 0

                    if events.key == pygame.K_ESCAPE:
                        gameQuit = True

                    if events.key == pygame.K_q:
                        score=score+10 

                    

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if (snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height):
                gameOver = True
                pygame.mixer.music.load('w_f.mp3')
                pygame.mixer.music.play()

            gameWindow.fill(l_blue)
            gameWindow.blit(bgImage,(0,0))
            
            # texting_screen("score:"+str(score*10), blue, 5, 5)
            texting_screen("score:"+str(score)+"  \t high_Score: "+str(high_Score), blue, 5, 5)

            # pygame.draw.circle(gameWindow,red,[food_x,food_y],food_size)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, food_size, food_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if abs(snake_x - food_x) < 12 and abs(snake_y - food_y) < 12:
                score += 10
                food_x = random.randint(10, screen_width-60)
                food_y = random.randint(10, screen_height-60)
                snake_length += 7
                # pygame.mixer.music.load('pubg_supplies_.mp3')
                # pygame.mixer.music.play()
                if score > int(high_Score):
                    high_Score = score

            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            snake_make(gameWindow, black, snake_list, snake_size)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-5]:
                gameOver = True
                pygame.mixer.music.load('w_f.mp3')
                pygame.mixer.music.play()

        

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome()
