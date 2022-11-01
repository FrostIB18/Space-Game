import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, spaceship):
        "Create a bullet in a current position"
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 195, 195, 195
        self.speed = 15
        self.rect.centerx = spaceship.rect.centerx
        self.rect.top = spaceship.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """Moving bullet up"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Drawing a bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
