import sys
import pygame
from pygame.locals import *
from ship import Ship

pygame.init()
# Resolution is ignored on Android
surface = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
touched = False
rect = Ship(surface)
while True:
    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit()
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(ev.pos):
                touched = True
                # This is the starting point
                pygame.mouse.get_rel()
        elif ev.type == pygame.MOUSEBUTTONUP:
            touched = False
    clock.tick(60)
    surface.fill((0, 0, 0))
    if touched:
        rect.move_ip(pygame.mouse.get_rel())
        rect.clamp_ip(surfrect)
    surface.fill((255, 255, 255), rect)
    pygame.display.flip()
