import pygame

class Ship:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = (self.screen_rect.w / 2, self.screen_rect.h / 2)
        
    def blitme(self):
        self.screen.blit(self.image, self.screen)