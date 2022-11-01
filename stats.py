class Stats():
    """Tracking statistics"""

    def __init__(self):
        """Stats initiolization"""
        self.reset_stats()
        self.run_game = True
        with open("high_score.txt", "r") as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """Statistics changing during the game"""
        self.spaceship_left = 2
        self.score = 0
