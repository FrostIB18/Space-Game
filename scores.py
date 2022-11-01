import pygame.font
from spaceship import Spaceship_live
from pygame.sprite import Group

class Scores():
    "Output of game information"
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (195, 195, 195)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_high_score()
        self.image_spaceships()

    def image_score(self):
        "Makes a text display as a picture"
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.score_rect.right + 640
        self.score_rect.top = 20

    def image_high_score(self):
        "Transform record into the graphical image"
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (0,0,0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def image_spaceships(self):
        "Quantity of lives"
        self.spaceships = Group()
        for spaceship_number in range(self.stats.spaceship_left + 1):
            spaceship = Spaceship_live(self.screen)
            spaceship.rect.x = 15 + spaceship_number * spaceship.rect.width/2
            spaceship.rect.y = 20
            self.spaceships.add(spaceship)

    def show_score(self):
        "Output score on display"
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.spaceships.draw(self.screen)

    def show_score_game_over(self):
        "Output score on display"
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
