import matplotlib.pyplot as plt
import numpy as np

NUM_SIMULATIONS = 200
count = np.arange(1, NUM_SIMULATIONS + 1)
coin_flips = np.random.random_integers(0, 1, NUM_SIMULATIONS)
coin_flips_cummulative = np.cumsum(coin_flips)
coin_flips_average = coin_flips_cummulative / count

plt.style.use("dark_background")

fig, plots = plt.subplots(1, 2, figsize=(10, 4))

plots[0].set_ylim((0, 1))
plots[0].set_xlim((0, NUM_SIMULATIONS))
plots[0].plot([0, NUM_SIMULATIONS], [1 / 2, 1 / 2], linestyle=":", color="gray")
plots[0].plot(count, coin_flips_average)

plots[1].plot(count, coin_flips_cummulative - count / 2)

plt.tight_layout()
plt.show()
