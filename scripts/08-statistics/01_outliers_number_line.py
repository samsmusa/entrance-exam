"""Outliers on a number line: where the 1.5*IQR fences are and why Max is outside.

Top panel:  score_after   (Q1=58, Q3=71.5, IQR=13.5, fences 37.75 and 91.75)
Bottom:     study_hours   (Q1=3,  Q3=6,    IQR=3,    fences -1.5 and 10.5)
"""
import numpy as np
import matplotlib.pyplot as plt
from common import load, quartiles, save, BLUE, ORANGE, INK, INK2, MUTED, BAND

d = load()


def panel(ax, x, names, label, unit):
    q1, q3 = quartiles(x)
    iqr = q3 - q1
    lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    med = np.median(x)
    # the "normal zone" between the fences
    ax.axvspan(lo, hi, color=BAND, alpha=0.45, lw=0)
    # the box (middle 50 %)
    ax.axvspan(q1, q3, ymin=0.3, ymax=0.7, color=BLUE, alpha=0.25, lw=0)
    ax.axvline(med, ymin=0.3, ymax=0.7, color=BLUE, lw=2.5)
    for f, t in [(lo, "lower fence"), (hi, "upper fence")]:
        ax.axvline(f, color=INK2, lw=1.5, ls="--")
        ax.text(f, 1.02, f"{t}\n{f:g}", ha="center", va="bottom", fontsize=9, color=INK2,
                transform=ax.get_xaxis_transform())
    # points (stack equal values)
    seen = {}
    for v, nm in zip(x, names):
        k = seen.get(v, 0)
        seen[v] = k + 1
        out = v < lo or v > hi
        ax.scatter(v, 0.5 + 0.12 * k - 0.06 * (np.sum(x == v) - 1), s=70, zorder=3,
                   color=ORANGE if out else BLUE, edgecolor="white", linewidth=1.5,
                   marker="D" if out else "o")
        if out:
            ax.annotate(f"{nm}: {v:g} {unit}\nOUTLIER (> {hi:g})", (v, 0.5), xytext=(0, -42),
                        textcoords="offset points", ha="center", fontsize=9, color=INK,
                        fontweight="bold", arrowprops=dict(arrowstyle="-", color=INK2),
                        bbox=dict(boxstyle="round,pad=0.25", fc="#fcfcfb", ec="none"))
    # brackets showing 1.5*IQR
    ax.annotate("", xy=(q3, 0.85), xytext=(hi, 0.85), arrowprops=dict(arrowstyle="<->", color=INK2))
    ax.text((q3 + hi) / 2, 0.88, f"1.5 × IQR = {1.5*iqr:g}", ha="center", fontsize=9, color=INK2)
    ax.annotate("", xy=(q1, 0.15), xytext=(q3, 0.15), arrowprops=dict(arrowstyle="<->", color=BLUE))
    ax.text((q1 + q3) / 2, 0.11, f"box = middle 50%\nIQR = {q3:g} − {q1:g} = {iqr:g}", ha="center",
            fontsize=9, color=BLUE, va="top")
    ax.set_ylim(-0.1, 1.0)
    ax.set_yticks([])
    ax.grid(axis="y", visible=False)
    ax.set_xlabel(label)
    ax.spines["left"].set_visible(False)


fig, axes = plt.subplots(2, 1, figsize=(10, 7.2))
panel(axes[0], d["score_after"], d["name"], "score_after (points)", "pts")
axes[0].set_xlim(30, 100)
panel(axes[1], d["study_hours"], d["name"], "study_hours (per week)", "h")
axes[1].set_xlim(-3, 14)
fig.suptitle("Outlier = a point outside the fences  [Q1 − 1.5·IQR,  Q3 + 1.5·IQR]",
             x=0.01, ha="left", fontsize=13, fontweight="bold", color=INK)
fig.text(0.01, 0.935, "Light blue = 'normal zone'. Dark band = the box (Q1 to Q3), line = median.",
         fontsize=9.5, color=INK2)
fig.tight_layout(rect=(0, 0, 1, 0.93), h_pad=3)
save(fig, "01-outliers-number-line.png")
