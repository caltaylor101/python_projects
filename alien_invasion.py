import sys
import pygame
from pygame.sprite import Group
from alien import Alien


from settings import Settings
from ship import Ship

import game_functions as gf


def run_game():
    #Initialize game, settings, and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    
    pygame.display.set_caption("Alien Invasion")

    #Make a ship. A group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    #Make a group to store bullets
    bullets = Group()
    aliens = Group()

    #Create fleet of aliens.
    gf.create_fleet(ai_settings, screen, aliens)
    
    #Make an alien
    alien = Alien(ai_settings, screen)
    

    #Main loop for game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        
        
        #Watch for keyboard and mouse events.
        
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        
        

        
run_game()


