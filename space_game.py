import pygame, controls
from spaceship import Spaceship
from pygame.sprite import Group
from stats import Stats
from scores import Scores

#define variables
pygame.init()
clock = pygame.time.Clock()
fps = 60
screen_width = 700
screen_height = 800

#define fonts
font30 = pygame.font.SysFont('Constantia', 30)
font40 = pygame.font.SysFont('Constantia', 40)

#define colors
white = (255,255,255)

def run():

    #clock.tick(fps)
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Space Defender")
    bg = pygame.image.load("images/bg.png")
    spaceship = Spaceship(screen)
    bullets = Group()
    invaders = Group()
    controls.create_army(screen, invaders)
    stats = Stats()
    sc = Scores(screen, stats)

    countdown = 3
    last_count = pygame.time.get_ticks()
    i = 0
    while i == 0:
        controls.events(screen, spaceship, bullets)
        if stats.run_game:
            if countdown == 0:
                spaceship.update()
                controls.update(bg, screen, sc, spaceship, invaders, bullets)
                controls.update_bullets(screen, stats, sc, invaders, bullets)
                controls.update_invaders(stats, screen, sc, spaceship, invaders, bullets)
            if countdown > 0:
                controls.start(bg, screen, sc, spaceship, invaders)
                controls.draw_text(screen, 'GET READY!', font40, white, int(screen_width / 2 - 110), int(screen_height / 2 + 200))
                controls.draw_counter(screen, str(countdown), font40, white,int(screen_width / 2 - 8), int(screen_height / 2 + 250))
                count_timer = pygame.time.get_ticks()
                if count_timer - last_count > 1000:
                    countdown -= 1
                    last_count = count_timer

        elif stats.run_game == False:
            controls.end(bg, screen, sc, spaceship, invaders)
            controls.draw_counter(screen, 'GAME OVER!', font40, white, int(screen_width / 2 - 120),
                               int(screen_height / 2 - 250))

run()