"""z-score of each student's score_after; |z| > 2 is 'unusual'."""
import numpy as np
import matplotlib.pyplot as plt
from common import load, save, BLUE, ORANGE, INK, INK2, BAND

d = load()
x = d["score_after"]
z = (x - x.mean()) / x.std(ddof=1)
order = np.argsort(z)
fig, ax = plt.subplots(figsize=(9, 5))
ax.axvspan(-2, 2, color=BAND, alpha=0.45, lw=0)
for i, j in enumerate(order):
    c = ORANGE if abs(z[j]) > 2 else BLUE
    ax.barh(i, z[j], color=c, height=0.65)
    ax.text(z[j] + (0.06 if z[j] >= 0 else -0.06), i, f"{z[j]:+.2f}  ({x[j]:g})",
            va="center", ha="left" if z[j] >= 0 else "right", fontsize=9, color=INK)
ax.set_yticks(range(len(x)), d["name"][order])
ax.axvline(0, color=INK2, lw=1)
for v in (-2, 2):
    ax.axvline(v, color=INK2, ls="--", lw=1.2)
ax.text(2.03, 11.45, "z = +2", fontsize=9, color=INK2)
ax.text(-2.03, 11.45, "z = −2", fontsize=9, color=INK2, ha="right")
ax.set_xlim(-2.8, 3.3)
ax.set_xlabel("z = (score − 66) / 11.86   →   'how many SDs from the mean'")
ax.set_title("z-scores: only Max is more than 2 SDs from the mean")
save(fig, "05-zscores.png")
