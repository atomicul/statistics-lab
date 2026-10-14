import itertools

import matplotlib.pyplot as plt
import numpy as np

NUM_SIMULATIONS = 200
count = np.arange(1, NUM_SIMULATIONS + 1)

dice = [
    (2, 2, 2, 5, 5, 5),
    (3, 3, 3, 3, 3, 6),
    (1, 4, 4, 4, 4, 4),
]
colors = ["red", "green", "black"]

sequences = {
    c: np.random.choice(d, size=NUM_SIMULATIONS)
    for c, d in zip(colors, dice, strict=True)
}

plt.style.use("dark_background")

fig, plots = plt.subplots(2, 2, figsize=(10, 4))

for i, (l, r) in enumerate(itertools.combinations(colors, 2)):
    p = plots[i // 2][i % 2]

    p.set_ylim((0, 1))
    p.set_xlim((0, NUM_SIMULATIONS))
    p.set_title(f"{l} against {r}")

    y = np.cumsum(sequences[l] > sequences[r]) / count

    p.plot([0, NUM_SIMULATIONS], [1 / 2, 1 / 2], linestyle=":", color="gray")
    p.plot(count, y)

p = plots[1][1]
p.set_title("three way")

red_wins = (
    np.cumsum(sequences["red"] > np.maximum(sequences["green"], sequences["black"]))
    / count
)
green_wins = (
    np.cumsum(sequences["green"] > np.maximum(sequences["red"], sequences["black"]))
    / count
)
black_wins = (
    np.cumsum(sequences["black"] > np.maximum(sequences["green"], sequences["red"]))
    / count
)

p.plot(count, red_wins, color="red")
p.plot(count, green_wins, color="green")
p.plot(count, black_wins, color="white")

plt.tight_layout()
plt.show()
