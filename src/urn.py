import random


class PolyaUrn:

    def __init__(self, balls, reinforcements):

        self.balls = balls
        self.reinforcements = reinforcements

        self.history = [balls.copy()]

    def draw(self):

        colors = list(self.balls.keys())
        weights = list(self.balls.values())

        drawn_color = random.choices(
            colors,
            weights=weights
        )[0]

        self.balls[drawn_color] += \
            self.reinforcements[drawn_color]

        self.history.append(
            self.balls.copy()
        )

        return drawn_color