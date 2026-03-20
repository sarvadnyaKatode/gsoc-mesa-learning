from model import WolfSheepModel

model = WolfSheepModel(10, 10, 20, 5)

for i in range(10):
    model.step()
    print(f"Step {i} done")