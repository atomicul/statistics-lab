import sys
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

SAMPLE = 5000000
COIN_SKEW = 0.5

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} WINDOW_SIZE")
    sys.exit(1)

substring_length = int(sys.argv[1])
coinflips = np.random.random(size=SAMPLE) <= COIN_SKEW
windows = sliding_window_view(coinflips, substring_length)
all_head_substrings = windows.all(axis=1).sum()

print(f"All head sequences {all_head_substrings/windows.shape[0]:.3f}")
