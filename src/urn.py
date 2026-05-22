import numpy as np


class PolyaUrn:

    def __init__(self, balls, reinforcements, rng=None):

        self.balls = balls
        self.reinforcements = reinforcements
        self.rng = rng if rng is not None else np.random.default_rng()

        self.history = [balls.copy()]

    def draw(self):

        colors = list(self.balls.keys())
        weights = np.array(list(self.balls.values()), dtype=float)
        probabilities = weights / weights.sum()

        drawn_color = self.rng.choice(
            colors,
            p=probabilities
        )

        self.balls[drawn_color] += \
            self.reinforcements[drawn_color]

        self.history.append(
            self.balls.copy()
        )

        return drawn_color
    
    def simulate(self, n_steps):

        for _ in range(n_steps):
            self.draw()

    def always_black_leading(self):

        for state in self.history:

            if state["black"] <= state["white"]:
                return False

        return True