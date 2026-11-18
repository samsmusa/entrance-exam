"""Empirical CDF vs fitted normal CDF; the KS statistic D is the largest vertical gap."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from common import load, save, BLUE, ORANGE, INK, INK2

x = np.sort(load()["score_after"])
n, mu, sg = len(x), x.mean(), x.std(ddof=1)
grid = np.linspace(40, 100, 400)
fig, ax = plt.subplots(figsize=(9, 4.8))
ax.plot(grid, stats.norm.cdf(grid, mu, sg), color=INK2, lw=2, label="normal CDF  N(66, 11.86²)")
ax.step(np.r_[40, x, 100], np.r_[0, np.arange(1, n + 1) / n, 1], where="post", color=BLUE, lw=2,
        label="empirical CDF  Fₙ(x)")
xv = 70
fn, f0 = (x <= xv).mean(), stats.norm.cdf(xv, mu, sg)
ax.plot([xv, xv], [f0, fn], color=ORANGE, lw=3)
ax.annotate(f"largest gap D = {fn:.2f} − {f0:.3f} = {fn-f0:.3f}\n(critical ≈ 1.36/√12 = 0.39 ⇒ fits)",
            (xv, (fn + f0) / 2), xytext=(74, 0.35), fontsize=9.5, color=INK,
            arrowprops=dict(arrowstyle="->", color=INK2))
ax.set_xlabel("score_after")
ax.set_ylabel("P(X ≤ x)")
ax.legend(loc="upper left")
ax.set_title("Kolmogorov–Smirnov: compare the staircase with the smooth curve")
save(fig, "13-ecdf-ks.png")
