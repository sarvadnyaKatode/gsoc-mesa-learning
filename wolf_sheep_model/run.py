from model import WolfSheepModel
import matplotlib.pyplot as plt

# Create model
model = WolfSheepModel(10, 10, 20, 5)

# Run simulation
steps = 200
for i in range(steps):
    model.step()

# Get data
data = model.datacollector.get_model_vars_dataframe()

print(data)

# Plot graph
data.plot()
plt.title("Wolf-Sheep Population Dynamics")
plt.xlabel("Time Step")
plt.ylabel("Population")
plt.grid()

plt.show()