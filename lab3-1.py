import numpy as np

SAMPLE = 50000
P_BUGGY = 0.75
P_ACCEPT_BUGGY = 0.05
P_ACCEPT_NOT_BUGGY = 0.98

bugs = (np.random.random(size=SAMPLE) <= P_BUGGY).sum()
not_bug = SAMPLE - bugs

buggy_accepted = (np.random.random(size=bugs) <= P_ACCEPT_BUGGY).sum()
buggy_rejected = bugs - buggy_accepted
not_buggy_accepted = (np.random.random(size=not_bug) <= P_ACCEPT_NOT_BUGGY).sum()
not_buggy_rejected = not_bug - not_buggy_accepted

accepted = buggy_accepted + not_buggy_accepted
rejected = buggy_rejected + not_buggy_rejected

print(f"P has bugs when accepted: {buggy_accepted / accepted:.3f}")
print(f"P is correct when accepted: {not_buggy_accepted / accepted:.3f}")
print(f"P has bugs when rejected: {buggy_rejected / rejected:.3f}")
print(f"P is correct when rejected: {not_buggy_rejected / rejected:.3f}")
