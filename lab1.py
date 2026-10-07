import dataclasses
import functools

import matplotlib.patches
import matplotlib.pyplot as plt
import numpy as np


@dataclasses.dataclass(frozen=True)
class Point:
    th: float

    @classmethod
    def random(cls):
        return cls(th=np.random.random() * 2 * np.pi)

    @property
    def x(self):
        return np.cos(self.th)

    @property
    def y(self):
        return np.sin(self.th)

    def distance(self, other: Point):
        return np.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


@dataclasses.dataclass(frozen=True)
class Chord:
    p1: Point
    p2: Point

    @property
    def length(self):
        return self.p1.distance(self.p2)

    @property
    def plot(self):
        return functools.partial(
            plt.plot,
            [self.p1.x, self.p2.x],
            [self.p1.y, self.p2.y],
        )

    @classmethod
    def random(cls):
        return cls(Point.random(), Point.random())


def main():
    plt.style.use("dark_background")
    ax = plt.gca()
    ax.set_aspect("equal", "box")
    ax.set_xlim((-1, 1))
    ax.set_ylim((-1, 1))
    draw_circle_and_triangle(ax)

    probability = simulate(100)

    print(f"probability={probability}")

    plt.show()


def simulate(num_chords: int):
    chords = [Chord.random() for _ in range(num_chords)]

    TRESHOLD = np.sqrt(3)

    probability = sum(1 for chord in chords if chord.length > TRESHOLD) / num_chords

    for chord in chords:
        if chord.length > TRESHOLD:
            chord.plot(color="g")
        else:
            chord.plot(color="r")

    return probability


def draw_circle_and_triangle(ax):
    """
    Deseneaza un cerc de raza 1 si triunghiul echilateral inscris in el, a carui varfuri sunt definite folosind coordonate polare.
    """
    circle = matplotlib.patches.Circle((0, 0), 1, color="white", fill=False)
    ax.add_patch(circle)

    plt.plot(
        [np.cos(-np.pi / 6), np.cos(np.pi / 2)],
        [np.sin(-np.pi / 6), np.sin(np.pi / 2)],
    )
    plt.plot(
        [np.cos(7 * np.pi / 6), np.cos(np.pi / 2)],
        [np.sin(7 * np.pi / 6), np.sin(np.pi / 2)],
    )
    plt.plot(
        [np.cos(-np.pi / 6), np.cos(7 * np.pi / 6)],
        [np.sin(-np.pi / 6), np.sin(7 * np.pi / 6)],
    )


if __name__ == "__main__":
    main()
