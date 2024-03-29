import sys, pygame, random
from ship import *
from asteroid import *
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
asteroids = pygame.sprite.Group()
numlevels = 5
level = 1
asteroidCount = 6

# game functions


def start_level():
    global asteroidCount, asteroids
    player.reset((20, height // 2))
    asteroids.empty()
    asteroidCount += 6
    for i in range(asteroidCount):
        asteroids.add(Asteroid((random.randint(40, width - 40), random.randint(40, height - 40)), (random.randint(15, 60))))


def win():
    font = pygame.font.SysFont(None, 70)
    text = font.render("You Survived Saturn's Deadly Rings", True, (255, 0, 0))
    text_rect = text.get.rect()
    text_rect.center = (width/2, height/2)
    while True:
        screen.fill(color)
        screen.blit(text, text_rect)
        pygame.display.flip()
        if event.type == QUIT:
            sys.exit()


def main():
    global level
    start_level()
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
                    player.speed[0] = -5
                if event.key == K_UP:
                    player.speed[1] = -5
                if event.key == K_DOWN:
                    player.speed[1] = 5
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    player.speed[0] = 0
                if event.key == K_LEFT:
                    player.speed[0] = 0
                if event.key == K_UP:
                    player.speed[1] = 0
                if event.key == K_DOWN:
                    player.speed[1] = 0



        # update screen
        screen.fill(color)
        player.update()
        screen.blit(player.image, player.rect)
        asteroids.update()
        gets_hit = pygame.sprite.spritecollide(player, asteroids, False)
        asteroids.draw(screen)
        pygame.display.flip()

        if player.checkReset(width):
            if level == numlevels:
                win()
            else:
                level += 1
                start_level()
        elif gets_hit:
            player.reset((20, height // 2))

if __name__ == '__main__':
    main()