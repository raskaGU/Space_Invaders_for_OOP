import pygame
class Hero:
  def __init__(self, screen):
    '''инициализация главного героя'''
    self.image = pygame.image.load("images/hero.png")
    self.rect = self.image.get_rect()
    self.screen = screen
    self.screen_rect = screen.get_rect()
    self.rect.bottom = self.screen_rect.bottom
    self.rect.centerx = self.screen_rect.centerx
    self.lives = 3
    self.score = 0
    self.font = pygame.font.Font(None, 36)  # добавьте эту строку    
  def output_hero(self):
    self.screen.blit(self.image, self.rect)
    

  def get_score(self):
    return self.score  # добавьте этот метод
  def draw_score(self):
      score_text = self.font.render("Score: " + str(self.score), True, (255, 255, 255))
      score_rect = score_text.get_rect()
      score_rect.topleft = (10, 60)  # измените координаты, чтобы счет был под надписью о количестве жизней
      self.screen.blit(score_text, score_rect)