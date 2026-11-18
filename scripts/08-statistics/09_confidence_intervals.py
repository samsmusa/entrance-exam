"""Left: our z / t intervals for the mean.  Right: what '95 %' means (simulation)."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from common import load, save, BLUE, ORANGE, AQUA, INK, INK2

x = load()["score_after"]
n, xb, s = len(x), x.mean(), x.std(ddof=1)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 5), gridspec_kw={"width_ratios": [1, 1.3]})

rows = [
    ("90% z (σ=12)", xb, 1.645 * 12 / np.sqrt(n), BLUE),
    ("95% z (σ=12)", xb, 1.96 * 12 / np.sqrt(n), BLUE),
    ("99% z (σ=12)", xb, 2.576 * 12 / np.sqrt(n), BLUE),
    ("95% t (s=11.86)", xb, stats.t.ppf(0.975, n - 1) * s / np.sqrt(n), AQUA),
]
for i, (lab, c, m, col) in enumerate(rows[::-1]):
    a1.plot([c - m, c + m], [i, i], color=col, lw=4, solid_capstyle="round")
    a1.scatter(c, i, color=INK, s=30, zorder=3)
    a1.text(c, i + 0.22, f"[{c-m:.2f}, {c+m:.2f}]", ha="center", fontsize=9, color=INK)
a1.axvline(60, color=ORANGE, ls="--", lw=1.5)
a1.text(60.2, 3.55, "μ₀ = 60\n(inside 95% CI ⇒\nnot rejected)", fontsize=8.5, color=INK2)
a1.set_yticks(range(4), [r[0] for r in rows[::-1]])
a1.set_ylim(-0.6, 4.1)
a1.set_xlabel("score")
a1.set_title("Higher confidence ⇒ wider interval")

rng = np.random.default_rng(8)
mu_true, sg = 66, 12
miss = 0
for i in range(40):
    smp = rng.normal(mu_true, sg, n)
    m = 1.96 * sg / np.sqrt(n)
    lo, hi = smp.mean() - m, smp.mean() + m
    ok = lo <= mu_true <= hi
    miss += not ok
    a2.plot([lo, hi], [i, i], color=BLUE if ok else ORANGE, lw=2.5 if ok else 3.5,
            solid_capstyle="round")
a2.axvline(mu_true, color=INK, lw=1.5)
a2.text(mu_true + 0.3, 40.3, "true μ = 66", fontsize=9, color=INK)
a2.set_yticks([])
a2.set_ylim(-1, 42)
a2.set_xlabel("score")
a2.set_title(f"40 repeated samples: {40-miss} CIs hit μ, {miss} miss (orange)")
fig.tight_layout()
save(fig, "09-confidence-intervals.png")
