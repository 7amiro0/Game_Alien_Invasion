with open("score.txt", "r") as fl:
    score_file = fl.read()


class Gamestats():
    def __init__(self, ai_set):
        self.ai_set = ai_set
        self.reset_stats()
        self.game_active = False
        self.high_score = int(score_file)

    def reset_stats(self):
        self.ship_left = self.ai_set.ship_limit
        self.score = 0

        self.level = 1
