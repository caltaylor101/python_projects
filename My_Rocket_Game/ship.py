import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('rocket.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        

        self.center = float(self.rect.centerx)
        self.upward = float(self.rect.centery)
        
        self.moving_left = False
        self.moving_right = False

        #ship can move up
        self.moving_up = False
        
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

        #move ship up and let it fall
        if self.moving_up and self.rect.top > self.screen_rect.top + 150:
            self.upward -= self.ai_settings.ship_speed_factor
        

        if self.moving_up == False and self.upward < 500:
            self.upward += self.ai_settings.ship_speed_factor
            
        self.rect.centery = self.upward
            
    def blitme(self):

        self.screen.blit(self.image, self.rect)
        
