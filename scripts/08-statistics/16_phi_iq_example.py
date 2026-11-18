"""Phi((x - mu)/sigma) on the IQ example: mu = 100, sigma = 15, x = 130.

(a) One bell, two axes: the IQ axis and the z axis label the SAME curve.
    Standardizing only re-labels the axis (100 -> 0, 115 -> 1, 130 -> 2),
    so the shaded area P(X <= 130) is the same as P(Z <= 2) = Phi(2) = 0.9772.
    Arrows show the two 15-point steps: 130 is 2 SDs above the mean.
(b) Phi as the cumulative curve: go up from z = 2 (IQ 130), read 0.9772 across.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from common import save, BLUE, ORANGE, INK, INK2, BAND

mu, sg, xv = 100, 15, 130
zv = (xv - mu) / sg
p = stats.norm.cdf(zv)
fig, (a, b) = plt.subplots(1, 2, figsize=(13, 5.2), gridspec_kw={"width_ratios": [1.25, 1]})

# (a) bell with dual axis
x = np.linspace(mu - 4 * sg, mu + 4 * sg, 500)
y = stats.norm.pdf(x, mu, sg)
a.plot(x, y, color=INK2, lw=2)
a.fill_between(x[x <= xv], y[x <= xv], color=BAND, alpha=0.9, lw=0)
a.fill_between(x[x >= xv], y[x >= xv], color=ORANGE, alpha=0.6, lw=0)
a.axvline(xv, color=BLUE, lw=2)
a.text(98, 0.0095, f"P(X ≤ 130) = Φ(2)\n= {p:.4f}\n(97.72% below)", ha="center", fontsize=11,
       color=INK, fontweight="bold")
a.annotate(f"P(X > 130)\n= 1 − Φ(2) = {1-p:.4f}", xy=(136, 0.0006), xytext=(147, 0.009),
           fontsize=10, color=INK, ha="center",
           arrowprops=dict(arrowstyle="-", color=INK2))
# the two SD steps
top = stats.norm.pdf(mu, mu, sg) * 1.07
for s0, lab in [(100, "+15 = 1σ"), (115, "+15 = 1σ")]:
    a.annotate("", xy=(s0 + 15, top), xytext=(s0, top),
               arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.8))
    a.text(s0 + 7.5, top * 1.02, lab, ha="center", va="bottom", fontsize=9.5, color=BLUE)
a.text(xv + 1.5, top * 0.93, "130 is 2 SDs\nabove the mean → z = 2", fontsize=9.5, color=BLUE,
       va="top")
a.set_ylim(0, top * 1.12)
ticks = [mu + k * sg for k in range(-3, 4)]
a.set_xticks(ticks, [f"{t:g}" for t in ticks])
a.set_xlabel("IQ score  x   (μ = 100, σ = 15)")
a.set_yticks([])
a.grid(axis="y", visible=False)
a.spines["left"].set_visible(False)
# second axis: z = (x - 100)/15, the same tick positions re-labelled
zax = a.secondary_xaxis(-0.2, functions=(lambda v: (v - mu) / sg, lambda z: mu + sg * z))
zax.set_xticks(range(-3, 4), ["−3", "−2", "−1", "0", "1", "2", "3"])
zax.set_xlabel("z = (x − 100) / 15   — same curve, axis only re-labelled", color=BLUE)
zax.tick_params(colors=BLUE)
zax.spines["bottom"].set_color(BLUE)
a.set_title("(a) Standardizing re-labels the axis; the area stays 0.9772")

# (b) CDF
z = np.linspace(-4, 4, 400)
b.plot(z, stats.norm.cdf(z), color=BLUE, lw=2.5)
b.plot([zv, zv], [0, p], color=INK2, ls=":", lw=1.4)
b.plot([-4, zv], [p, p], color=INK2, ls=":", lw=1.4)
b.scatter(zv, p, color=ORANGE, s=60, zorder=3)
b.annotate(f"Φ(2) = {p:.4f}", (zv, p), xytext=(-2.3, 0.80), fontsize=11, fontweight="bold",
           color=INK, arrowprops=dict(arrowstyle="->", color=INK2))
b.text(zv + 0.1, 0.04, "z = 2\n(IQ 130)", fontsize=9.5, color=INK2)
b.annotate("", xy=(zv, 0.5), xytext=(zv, 0.15), arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.5))
b.annotate("", xy=(-3.3, p), xytext=(zv - 0.4, p), arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.5))
b.text(-3.9, 0.5, "① go up from z\n② read across", fontsize=9.5, color=ORANGE)
b.set_xlim(-4, 4)
b.set_ylim(0, 1.05)
b.set_xlabel("z")
b.set_ylabel("Φ(z) = P(Z ≤ z)")
b.set_title("(b) Φ = CDF of N(0,1): the table value")

fig.tight_layout(w_pad=3)
save(fig, "16-phi-iq-example.png")
