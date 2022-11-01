import pygame, sys
from bullet import Bullet
from invaders import Invader
import time


def events(screen,spaceship, bullets):
    """Refactoring of events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #вправо_влево
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                spaceship.mright = True
            elif event.key == pygame.K_a:
                spaceship.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, spaceship)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                spaceship.mright = False
            elif event.key == pygame.K_a:
                spaceship.mleft = False

def start(bg, screen, sc, spaceship, invaders):
    "Screen update"
    screen.blit(bg, (0, 0))
    sc.show_score()
    spaceship.output()
    invaders.draw(screen)

def end(bg, screen, sc, spaceship, invaders):
    "Screen update"
    screen.blit(bg, (0, 0))
    sc.show_score_game_over()
    spaceship.output()
    invaders.draw(screen)

def draw_text(screen, text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def draw_counter(screen, text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
    pygame.display.update()

def update(bg, screen, sc, spaceship, invaders, bullets):
    "Screen update"
    screen.blit(bg, (0, 0))
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    spaceship.output()
    invaders.draw(screen)
    pygame.display.flip()


def update_bullets(screen, stats, sc, invaders, bullets):
    """Update bullets position"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, invaders, True, True)
    if collisions:
        for invaders in collisions.values():
            stats.score += 10 * len(invaders)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_spaceships()
    if len(invaders) == 0:
        bullets.empty()
        create_army(screen, invaders)

def spaceship_kill(stats, screen, sc, spaceship, invaders, bullets):
    """Collision of army and spaceship"""
    if stats.spaceship_left > 0:
        stats.spaceship_left -= 1
        sc.image_spaceships()
        invaders.empty()
        bullets.empty()
        create_army(screen, invaders)
        spaceship.create_spaceship()
        time.sleep(2)
    else:
        stats.run_game = False
        #sys.exit()

def invaders_check(stats, screen, sc, spaceship, invaders, bullets):
    """Invaders crossing checking"""
    screen_rect = screen.get_rect()
    for invader in invaders.sprites():
        if invader.rect.bottom >= screen_rect.bottom:
            spaceship_kill(stats, screen, sc, spaceship, invaders, bullets)
            break

def update_invaders(stats, screen, sc, spaceship, invaders, bullets):
    """Update invaders position"""
    invaders.update()
    if pygame.sprite.spritecollideany(spaceship, invaders):
        spaceship_kill(stats, screen, sc, spaceship, invaders, bullets)
    invaders_check(stats, screen, sc, spaceship, invaders, bullets)

def create_army(screen, invaders):
    """Creating invaders army"""
    invader = Invader(screen)
    invader_width = invader.rect.width
    number_invader_x = int((700 - 2 * invader_width)/invader_width)
    invader_height = invader.rect.height
    number_invader_y = int((800 - 100 - 2 * invader_height)/invader_height)

    for row_number in range(number_invader_y - 2):
        for invader_number in range(number_invader_x):
            invader = Invader(screen)
            invader.x = invader_width + invader_width * invader_number
            invader.y = invader_height + invader_height * row_number
            invader.rect.x = invader.x
            invader.rect.y = invader.rect.height + invader.rect.height * row_number
            invaders.add(invader)

def check_high_score(stats, sc):
    "Checking of the new record"
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open("high_score.txt", "w") as f:
            f.write(str(stats.high_score))