"""Hours vs score with the least-squares line, fitted with and without Max.

Lesson: Max is an outlier on each axis alone, but he follows the trend,
so he is NOT a mistake and does not distort the line much.
"""
import numpy as np
import matplotlib.pyplot as plt
from common import load, save, BLUE, ORANGE, INK, INK2, MUTED

d = load()
h, s, nm = d["study_hours"], d["score_after"], d["name"]
b, a = np.polyfit(h, s, 1)
keep = nm != "Max"
b2, a2 = np.polyfit(h[keep], s[keep], 1)
r = np.corrcoef(h, s)[0, 1]
r2 = np.corrcoef(h[keep], s[keep])[0, 1]

fig, ax = plt.subplots(figsize=(9, 5.5))
xs = np.linspace(0, 13, 50)
ax.plot(xs, a + b * xs, color=BLUE, lw=2, label=f"all 12:  ŷ = {a:.2f} + {b:.2f}x,  r = {r:.3f}")
ax.plot(xs, a2 + b2 * xs, color=MUTED, lw=2, ls="--",
        label=f"without Max:  ŷ = {a2:.2f} + {b2:.2f}x,  r = {r2:.3f}")
ax.scatter(h[keep], s[keep], s=60, color=BLUE, edgecolor="white", lw=1.5, zorder=3)
ax.scatter(h[~keep], s[~keep], s=90, marker="D", color=ORANGE, edgecolor="white", lw=1.5, zorder=3)
ax.annotate("Max (12 h, 94): outlier on BOTH axes,\nbut close to the trend → a real,\nextreme student, not a data error.\nHe is a high-leverage point:\nremoving him changes the slope\nfrom 4.10 to 4.51.", (12, 94), xytext=(8.6, 47),
            fontsize=9.5, color=INK, ha="left", arrowprops=dict(arrowstyle="->", color=INK2))
ax.scatter([h.mean()], [s.mean()], marker="+", s=200, color=INK, zorder=4)
ax.annotate("(x̄, ȳ) = (4.75, 66)\nthe line always passes here", (h.mean(), s.mean()),
            xytext=(0.4, 78), fontsize=9, color=INK2, arrowprops=dict(arrowstyle="->", color=INK2))
for i in np.where(keep)[0]:
    ax.text(h[i] + 0.15, s[i] - 1.8, nm[i], fontsize=8, color=INK2)
ax.set_xlim(0, 13)
ax.set_ylim(40, 100)
ax.set_xlabel("study_hours per week (x)")
ax.set_ylabel("score_after (y)")
ax.legend(loc="upper left")
ax.set_title("Correlation & regression: more hours, higher score")
save(fig, "06-scatter-regression.png")
