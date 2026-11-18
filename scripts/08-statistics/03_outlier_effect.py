"""What one outlier does: mean vs median vs SD with and without Max.

Each statistic gets its own zoomed panel so you can see how far it moves.
"""
import numpy as np
import matplotlib.pyplot as plt
from common import load, save, BLUE, ORANGE, INK, INK2

d = load()
x = d["score_after"]
x_wo = x[d["name"] != "Max"]
stats = [
    ("mean", x_wo.mean(), x.mean(), "sensitive"),
    ("median", np.median(x_wo), np.median(x), "robust"),
    ("SD  s", x_wo.std(ddof=1), x.std(ddof=1), "very sensitive"),
]
fig, axes = plt.subplots(3, 1, figsize=(9, 5.2))
for ax, (lab, wo, w, verdict) in zip(axes, stats):
    ax.annotate("", xy=(w, 0), xytext=(wo, 0), arrowprops=dict(arrowstyle="->", color=INK2, lw=1.5))
    ax.scatter(wo, 0, s=110, color=BLUE, edgecolor="white", lw=1.5, zorder=3)
    ax.scatter(w, 0, s=110, color=ORANGE, marker="D", edgecolor="white", lw=1.5, zorder=3)
    ax.text(wo, 0.45, f"without Max\n{wo:.2f}", ha="center", fontsize=9, color=INK)
    ax.text(w, 0.45, f"with Max\n{w:.2f}", ha="center", fontsize=9, color=INK)
    c = min(wo, w) - 0.5
    ax.set_xlim(c, c + 5)  # every panel shows the same 5-point window
    ax.set_ylim(-0.6, 1.3)
    ax.set_yticks([])
    ax.grid(axis="y", visible=False)
    ax.spines["left"].set_visible(False)
    ax.text(-0.02, 0.35, lab, transform=ax.transAxes, ha="right", fontsize=11, fontweight="bold", color=INK)
    ax.text(1.02, 0.35, f"moves {abs(w-wo):.2f}\n({verdict})", transform=ax.transAxes, fontsize=9.5, color=INK2)
axes[-1].set_xlabel("points (each panel is a 5-point-wide window, so distances are comparable)")
fig.suptitle("Adding ONE outlier (Max = 94): the median hardly moves", x=0.01, ha="left",
             fontsize=13, fontweight="bold", color=INK)
fig.tight_layout(rect=(0.04, 0, 0.9, 1))
save(fig, "03-outlier-effect.png")
