"""Slope chart before -> after for each student (paired data). Hans went down."""
import numpy as np
import matplotlib.pyplot as plt
from common import load, save, BLUE, ORANGE, INK, INK2

d = load()
b, a, nm = d["score_before"], d["score_after"], d["name"]
fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12, 5.5), gridspec_kw={"width_ratios": [1, 1.2]})
for i in range(len(nm)):
    down = a[i] < b[i]
    c = ORANGE if down else BLUE
    ax.plot([0, 1], [b[i], a[i]], color=c, lw=3 if down else 1.8, alpha=1 if down else 0.75)
    ax.scatter([0, 1], [b[i], a[i]], color=c, s=30, zorder=3)
    ax.text(1.04, a[i], f"{nm[i]} ({a[i]-b[i]:+g})", va="center", fontsize=8.5,
            color=INK if down else INK2, fontweight="bold" if down else "normal")
ax.set_xticks([0, 1], ["before", "after"])
ax.set_xlim(-0.15, 1.45)
ax.set_ylabel("score")
ax.set_title("Each line is one student: 11 up, 1 down")

diff = a - b
o = np.argsort(diff)
ax2.barh(range(len(o)), diff[o], color=[ORANGE if v < 0 else BLUE for v in diff[o]], height=0.65)
ax2.set_yticks(range(len(o)), nm[o])
ax2.axvline(0, color=INK2, lw=1)
ax2.axvline(diff.mean(), color=INK, ls="--", lw=1.5)
ax2.text(diff.mean() + 0.3, 11.45, f"mean d̄ = {diff.mean():g}", fontsize=9.5, color=INK)
ax2.set_xlabel("d = after − before")
ax2.set_title("Differences d: paired t = 4.07, p = 0.002")
fig.tight_layout()
save(fig, "11-paired-before-after.png")
