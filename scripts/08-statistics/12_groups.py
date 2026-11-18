"""Group comparisons: method (ANOVA / Kruskal-Wallis) and gender (t / Mann-Whitney)."""
import numpy as np
import matplotlib.pyplot as plt
from common import load, save, BLUE, ORANGE, AQUA, VIOLET, INK, INK2, MUTED

d = load()
s = d["score_after"]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 5), gridspec_kw={"width_ratios": [1.4, 1]})


def dots(ax, groups, labels, colors, title):
    for i, (g, c) in enumerate(zip(groups, colors)):
        vals = s[g]
        jitter = np.linspace(-0.12, 0.12, len(vals))
        ax.scatter(i + jitter, vals, s=60, color=c, edgecolor="white", lw=1.5, zorder=3)
        m = vals.mean()
        ax.plot([i - 0.28, i + 0.28], [m, m], color=INK, lw=2.5)
        ax.text(i + 0.31, m, f"mean {m:.2f}", va="center", fontsize=9, color=INK)
        for xv, v, nm in zip(i + jitter, vals, d["name"][g]):
            if nm == "Max":
                ax.text(xv - 0.06, v, "Max", ha="right", va="center", fontsize=8.5, color=INK2)
    ax.axhline(s.mean(), color=MUTED, ls="--", lw=1.2)
    ax.text(-0.48, s.mean() + 0.8, "grand mean 66", fontsize=8.5, color=INK2, ha="left")
    ax.set_xticks(range(len(groups)), labels)
    ax.set_xlim(-0.5, len(groups) - 0.2)
    ax.set_ylabel("score_after")
    ax.set_title(title)


meth = ["Lecture", "Video", "Group"]
dots(a1, [d["method"] == m for m in meth], meth, [BLUE, ORANGE, AQUA],
     "By method: means differ\nANOVA F = 7.14 (p = 0.014), Kruskal–Wallis H = 8.12 (p = 0.017)")
dots(a2, [d["gender"] == g for g in "FM"], ["F", "M"], [BLUE, VIOLET],
     "By gender: no difference\nt = −0.14 (p = 0.89), Mann–Whitney U = 17 (p = 0.94)")
fig.tight_layout()
save(fig, "12-groups.png")
