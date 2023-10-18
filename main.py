import pygame
import sys
from chenni import MainCharacter

def start_game():
    pygame.init()
    screen = pygame.display.set_mode((500,900))
    pygame.display.set_caption("SpaceX by Gulamova")


    flag = True
    maincharacter = MainCharacter(screen)
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()
        maincharacter.output()


start_game()