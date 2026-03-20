from mesa import Model
from mesa.space import MultiGrid
from agent import Sheep, Wolf

class WolfSheepModel(Model):
    def __init__(self, width, height, initial_sheep, initial_wolves):
        super().__init__()

        self.grid = MultiGrid(width, height, torus=True)

        # Create sheep
        for _ in range(initial_sheep):
            sheep = Sheep(self)
            self.grid.place_agent(
                sheep,
                (self.random.randrange(width), self.random.randrange(height))
            )

        # Create wolves (optional for now)
        for _ in range(initial_wolves):
            wolf = Wolf(self)
            self.grid.place_agent(
                wolf,
                (self.random.randrange(width), self.random.randrange(height))
            )

    def step(self):
        self.agents.do("step")