import matplotlib.patches
import matplotlib.pyplot as plt
import numpy as np


def draw_circle_and_triangle(ax):
    """
    Deseneaza un cerc de raza 1 si triunghiul echilateral inscris in el, a carui varfuri sunt definite folosind coordonate polare.
    """
    circle = matplotlib.patches.Circle((0, 0), 1, color="white", fill=False)
    ax.add_patch(circle)

    plt.plot(
        [np.cos(-np.pi / 6), np.cos(np.pi / 2)],
        [np.sin(-np.pi / 6), np.sin(np.pi / 2)],
        color="green",
    )
    plt.plot(
        [np.cos(7 * np.pi / 6), np.cos(np.pi / 2)],
        [np.sin(7 * np.pi / 6), np.sin(np.pi / 2)],
        color="green",
    )
    plt.plot(
        [np.cos(-np.pi / 6), np.cos(7 * np.pi / 6)],
        [np.sin(-np.pi / 6), np.sin(7 * np.pi / 6)],
        color="green",
    )


def main():
    plt.style.use("dark_background")
    ax = plt.gca()
    ax.set_aspect("equal", "box")
    ax.set_xlim((-1, 1))
    ax.set_ylim((-1, 1))
    draw_circle_and_triangle(ax)

    plt.show()


if __name__ == "__main__":
    main()
