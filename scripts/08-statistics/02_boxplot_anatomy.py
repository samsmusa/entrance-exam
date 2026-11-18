"""Boxplot of score_after with every part labelled (five-number summary + fences)."""
import numpy as np
import matplotlib.pyplot as plt
from common import load, quartiles, save, BLUE, ORANGE, INK, INK2

x = load()["score_after"]
q1, q3 = quartiles(x)
iqr = q3 - q1
lo_f, hi_f = q1 - 1.5 * iqr, q3 + 1.5 * iqr
med = np.median(x)
inside = x[(x >= lo_f) & (x <= hi_f)]
w_lo, w_hi = inside.min(), inside.max()

fig, ax = plt.subplots(figsize=(10, 3.8))
y = 0
ax.add_patch(plt.Rectangle((q1, y - 0.25), iqr, 0.5, facecolor=BLUE, alpha=0.25, edgecolor=BLUE, lw=2))
ax.plot([med, med], [y - 0.25, y + 0.25], color=BLUE, lw=3)
ax.plot([w_lo, q1], [y, y], color=BLUE, lw=2)
ax.plot([q3, w_hi], [y, y], color=BLUE, lw=2)
for w in (w_lo, w_hi):
    ax.plot([w, w], [y - 0.12, y + 0.12], color=BLUE, lw=2)
ax.scatter([94], [y], s=90, marker="D", color=ORANGE, edgecolor="white", lw=1.5, zorder=3)
for f in (lo_f, hi_f):
    ax.axvline(f, color=INK2, ls="--", lw=1.2)
ax.scatter(x, np.full_like(x, -0.55), s=25, color=INK2, alpha=0.7)
ax.text(30.5, -0.55, "raw data", va="center", fontsize=8.5, color=INK2)

labels = [
    (w_lo, f"min (whisker)\n{w_lo:g}", 0.45),
    (q1, f"Q1\n{q1:g}", 0.45),
    (med, f"median\n{med:g}", 0.62),
    (q3, f"Q3\n{q3:g}", 0.45),
    (w_hi, f"whisker end = largest value\ninside the fence: {w_hi:g}", 0.95),
    (94, "Max: 94\noutlier\n(drawn as a dot)", 0.45),
    (lo_f, f"lower fence\n{lo_f:g}", -0.95),
    (hi_f, f"upper fence\n{hi_f:g}", -0.95),
]
for xv, t, yy in labels:
    ax.annotate(t, (xv, 0.25 if yy > 0 else -0.25), xytext=(xv, yy), ha="center",
                va="bottom" if yy > 0 else "top", fontsize=9, color=INK,
                bbox=dict(boxstyle="round,pad=0.2", fc="#fcfcfb", ec="none"),
                arrowprops=dict(arrowstyle="-", color=INK2, lw=0.8))
ax.set_ylim(-1.45, 1.6)
ax.set_xlim(30, 100)
ax.set_yticks([])
ax.grid(axis="y", visible=False)
ax.spines["left"].set_visible(False)
ax.set_xlabel("score_after (points)")
ax.set_title("Boxplot anatomy: whiskers stop at the last point inside the fences")
save(fig, "02-boxplot-anatomy.png")
