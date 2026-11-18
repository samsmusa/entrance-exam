"""Histogram of score_after with mean and median: right skew (skewness 0.86)."""
import numpy as np
import matplotlib.pyplot as plt
from common import load, save, BLUE, ORANGE, AQUA, INK, INK2

x = load()["score_after"]
fig, ax = plt.subplots(figsize=(9, 4.2))
bins = np.arange(45, 100, 5)
ax.hist(x, bins=bins, color=BLUE, edgecolor="white", linewidth=2)
ax.axvline(np.median(x), color=AQUA, lw=2.5)
ax.axvline(x.mean(), color=ORANGE, lw=2.5, ls="--")
ax.text(np.median(x) - 0.6, 3.6, f"median {np.median(x):g}", ha="right", color=INK, fontsize=10)
ax.text(x.mean() + 0.6, 3.6, f"mean {x.mean():g}", ha="left", color=INK, fontsize=10)
ax.annotate("long right tail (Max, 94)\npulls the mean to the right", (94, 1), xytext=(80, 2.4),
            fontsize=9.5, color=INK2, arrowprops=dict(arrowstyle="->", color=INK2))
ax.set_xticks(bins)
ax.set_yticks(range(5))
ax.set_ylim(0, 4.2)
ax.set_xlabel("score_after (bins of 5 points)")
ax.set_ylabel("number of students")
ax.set_title("Right-skewed: mean > median, skewness = 0.86")
save(fig, "04-histogram-skew.png")
