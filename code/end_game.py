import pygame
from settings import *

class End_Game:
  def __init__(self):
    
    #general setup
    self.display_surface = pygame.display.get_surface()
    self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
    self.height = self.display_surface.get_size()[1] * 0.8
    self.width = self.display_surface.get_size()[0] * 0.8
    self.top = (self.display_surface.get_size()[1] - self.height) // 2
    self.left = (self.display_surface.get_size()[0] - self.width) // 2

  def display(self):
    
    # display box
    self.rect = pygame.Rect(self.left, self.top, self.width, self.height)
    pygame.draw.rect(self.display_surface, UI_BG_COLOR, self.rect)
    pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, self.rect, 4)

    # display text
    message = 'Game Over'
    message_surf = self.font.render(message, False, TEXT_COLOR)
    message_rect = message_surf.get_rect(center = self.rect.center)

    # restart text
    # restart = 'Restart? Press \'r\''
    # restart_surf = self.font.render(restart, False, TEXT_COLOR)
    # restart_rect = restart_surf.get_rect(center = self.rect.center - pygame.math.Vector2(0, -32))

    # draw
    self.display_surface.blit(message_surf, message_rect)
    # self.display_surface.blit(restart_surf, restart_rect)
