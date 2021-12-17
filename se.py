class Setting:
    def __init__(self):
        self.wi = 1280
        self.he = 800
        self.bgc = (75, 0, 130)
        self.ship_limit = 2
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dinamic_setting()

    def initialize_dinamic_setting(self):
        self.alien_points = 10
        self.ship_speed_factor = 4.5
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 3
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.fleet_direction *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
