from mesa import Model
from mesa.space import MultiGrid
from agent import Sheep, Wolf
from mesa.datacollection import DataCollector

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

        self.datacollector = DataCollector(
            model_reporters={
                "Sheep": lambda m: sum(isinstance(a, Sheep) for a in m.agents),
                "Wolves": lambda m: sum(isinstance(a, Wolf) for a in m.agents),
            }
        )

    def step(self):
        self.datacollector.collect(self)
        self.agents.do("step")