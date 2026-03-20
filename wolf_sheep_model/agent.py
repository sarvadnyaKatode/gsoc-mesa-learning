from mesa import Agent
import random

class Sheep(Agent):
    def __init__(self, model):
        super().__init__(model)
        self.energy = 5

    def step(self):
        self.move()
        self.energy -= 1

        # Reproduce
        if self.energy > 8:
            self.energy /= 2
            lamb = Sheep(self.model)
            self.model.grid.place_agent(lamb, self.pos)

    # Die
        
        if self.energy <= 0:
            self.model.grid.remove_agent(self)
            self.model.agents.remove(self)
            return  

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

class Wolf(Agent):
    def __init__(self, model):
        super().__init__(model)
        self.energy = 10

    def step(self):
        self.move()
        self.energy -= 1

        # Check for sheep in same cell
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        sheep = [agent for agent in cellmates if isinstance(agent, Sheep)]

        if sheep:
            victim = self.random.choice(sheep)
            self.model.grid.remove_agent(victim)
            self.model.agents.remove(victim)
            self.energy += 5

    # Reproduce
        if self.energy > 15:
            self.energy /= 2
            pup = Wolf(self.model)
            self.model.grid.place_agent(pup, self.pos)

    # Die
        if self.energy <= 0:
            self.model.grid.remove_agent(self)
            self.model.agents.remove(self)
            return  # 🔥 important

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)