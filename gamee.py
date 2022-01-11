import pygame
x = pygame.init()
#print(x)
#crearing window
gamewindow = pygame.display.set_mode((1200,500))
pygame.display.set_caption("My First Game")


#game specific variable
exit_game = False
game_over = False
#creating a game loop
#it control all actions in game
while not exit_game: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("right arrow key pressed")

pygame.quit()
quit()
#This is actually Shloka told by Jambavant ji  to Hanuman ji , while jumping into Sea...
#"Dhivara prasara Shaurya bhara
#Uthsara sthira gambhira......"
