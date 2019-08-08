import sys, pygame
from ship import *
from pygame.locals import *

pygame.init()
screen_info = pygame.display.Info()

# set the width and height to the size of the screen
size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 0, 0)
screen.fill(color)

# define variables
player = Ship((20, height // 2))
numlevels = 5
level = 1
asteroidCount = 3


def main():
    global level

    # game loop
    while level <= numlevels:
        clock.tick(60)

        # event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    player.speed[0] = 5
                if event.key == K_LEFT:
                    player.speed[1] = -5
                if event.key == K_UP:
                    player.speed[1] = -5
                if event.key == K_DOWN:
                    player.speed[0] = 5
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    player.speed[0] = 0
                if event.key == K_LEFT:
                    player.speed[1] = 0
                if event.key == K_UP:
                    player.speed[1] = 0
                if event.key == K_DOWN:
                    player.speed[0] = 0


        # update screen
        screen.fill(color)
        player.update()
        screen.blit(player.image, player.rect)
        pygame.display.flip()


if __name__ == '__main__':
    main()