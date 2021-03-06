class Settings():

    def __init__(self):

        # Screen settings
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (46, 55, 71)

        # Ship settings
        self.ship_limit = 2

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

        # Score settings
        self.score_scale = 1.5

    # Settings need to be changed here too
    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3

        self.alien_points = 10
        self.alien_speed = 1
        self.fleet_direction = 1
    
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

