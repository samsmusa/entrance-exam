"""What Phi((x - mu)/sigma) means.

(a) X ~ N(66, 12^2): P(X <= 78) is the area left of 78.
(b) Z ~ N(0, 1):     the SAME area lies left of z = (78 - 66)/12 = 1  -> Phi(1) = 0.8413.
(c) Symmetry:        Phi(-0.5) = 1 - Phi(0.5)  (left tail = right tail).
(d) Phi as a curve:  read Phi(z) off the cumulative curve (this is what the table lists).
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from common import save, BLUE, ORANGE, INK, INK2, BAND

mu, sg, xv = 66, 12, 78
zv = (xv - mu) / sg
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
(a, b), (c, d) = axes


def bell(ax, x, y, m, color, label, lx, ly, xlabel):
    ax.plot(x, y, color=INK2, lw=2)
    ax.fill_between(x[m], y[m], color=color, alpha=0.6, lw=0)
    ax.text(lx, ly, label, ha="center", fontsize=10.5, color=INK, fontweight="bold")
    ax.set_yticks([])
    ax.grid(axis="y", visible=False)
    ax.spines["left"].set_visible(False)
    ax.set_xlabel(xlabel)


x = np.linspace(mu - 4 * sg, mu + 4 * sg, 400)
bell(a, x, stats.norm.pdf(x, mu, sg), x <= xv, BAND, "area = P(X ≤ 78)\n= 0.8413", 64, 0.01,
     "score X   (μ = 66, σ = 12)")
a.axvline(xv, color=BLUE, lw=2)
a.set_xticks([30, 42, 54, 66, 78, 90, 102])
a.set_title("(a) Real scale: X ~ N(66, 12²)")

z = np.linspace(-4, 4, 400)
bell(b, z, stats.norm.pdf(z), z <= zv, BAND, "same area\n= Φ(1) = 0.8413", -0.15, 0.12,
     "z   (mean 0, SD 1)")
b.axvline(zv, color=BLUE, lw=2)
b.set_xticks(range(-3, 4))
b.set_title("(b) Standard scale: z = (78 − 66)/12 = 1")

pdf = stats.norm.pdf(z)
c.plot(z, pdf, color=INK2, lw=2)
c.fill_between(z[z <= -0.5], pdf[z <= -0.5], color=ORANGE, alpha=0.6, lw=0)
c.fill_between(z[z >= 0.5], pdf[z >= 0.5], color=BLUE, alpha=0.35, lw=0)
c.text(-2.3, 0.2, "Φ(−0.5)\n= 0.3085", ha="center", fontsize=10.5, color=INK, fontweight="bold")
c.text(2.3, 0.2, "1 − Φ(0.5)\n= 1 − 0.6915\n= 0.3085", ha="center", fontsize=10.5, color=INK,
       fontweight="bold")
c.set_yticks([])
c.grid(axis="y", visible=False)
c.spines["left"].set_visible(False)
c.set_xticks([-3, -2, -1, -0.5, 0.5, 1, 2, 3], ["−3", "−2", "−1", "−0.5", "0.5", "1", "2", "3"])
c.set_xlabel("z")
c.set_title("(c) Symmetry: Φ(−z) = 1 − Φ(z)  (tables list only z ≥ 0)")

cdf = stats.norm.cdf(z)
d.plot(z, cdf, color=BLUE, lw=2.5)
for zz in (-0.5, 0, 1, 2):
    p = stats.norm.cdf(zz)
    d.plot([zz, zz], [0, p], color=INK2, ls=":", lw=1.2)
    d.plot([-4, zz], [p, p], color=INK2, ls=":", lw=1.2)
    d.scatter(zz, p, color=ORANGE, s=45, zorder=3)
    d.text(zz + 0.12, p - 0.06, f"Φ({zz:g}) = {p:.4f}", fontsize=9.5, color=INK)
d.set_xlim(-4, 4)
d.set_ylim(0, 1.05)
d.set_xlabel("z")
d.set_ylabel("Φ(z) = P(Z ≤ z)")
d.set_title("(d) Φ is the cumulative curve: go up from z, read across")

fig.tight_layout(h_pad=2.5)
save(fig, "15-phi-standardization.png")
