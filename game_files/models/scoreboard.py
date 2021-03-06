import pygame.font
from models.ship import Ship
from pygame.sprite import Group

class Scoreboard():

    def __init__(self, settings, screen, game_state):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.game_state = game_state

        # Text
        self.text_color = (255, 102, 0)
        self.font = pygame.font.SysFont(None, 48)

        # Initial score
        self.prep_score()
        self.prep_high_score()

        # Number of ships
        self.prep_ships()

    def prep_score(self):
        score_str = str(self.game_state.score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        # Score display location
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_high_score(self):
        high_score = self.game_state.high_score
        high_score_str = 'HIGH SCORE: {}'.format(high_score)

        self.high_score_image = self.font.render(high_score_str, True, self.text_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

        
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.ships.draw(self.screen)
        self.screen.blit(self.high_score_image, self.high_score_rect)
    
    def prep_ships(self):
        self.ships = Group()

        for ship_number in range(self.game_state.ships_left):
            ship = Ship(self.screen, self.settings)
            ship.rect.x = 20 + ship_number * ship.rect.width
            ship.rect.y = 20
            self.ships.add(ship)
