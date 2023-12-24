import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("images/enemy.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
        self.score_value = 10
    def update(self):
        self.rect.y += self.speed
    def blitme(self):
        self.screen.blit(self.image, self.rect)