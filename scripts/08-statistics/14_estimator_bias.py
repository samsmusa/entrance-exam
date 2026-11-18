"""Simulation: dividing by n-1 is unbiased, dividing by n underestimates sigma^2.

Draw 20 000 samples of size 12 from N(66, 12^2) (true variance 144) and compare.
"""
import numpy as np
import matplotlib.pyplot as plt
from common import save, BLUE, ORANGE, INK, INK2

rng = np.random.default_rng(1)
smp = rng.normal(66, 12, size=(20000, 12))
s2 = smp.var(axis=1, ddof=1)
s2n = smp.var(axis=1, ddof=0)
fig, ax = plt.subplots(figsize=(9, 4.6))
bins = np.linspace(0, 400, 50)
ax.hist(s2, bins=bins, color=BLUE, histtype="step", lw=2, label="S² = Σ/(n−1)")
ax.hist(s2n, bins=bins, color=ORANGE, histtype="step", lw=2, label="Σ/n  (MLE)")
ax.axvline(144, color=INK, lw=2)
ax.axvline(s2.mean(), color=BLUE, lw=2, ls="--")
ax.axvline(s2n.mean(), color=ORANGE, lw=2, ls="--")
ax.set_ylim(0, ax.get_ylim()[1] * 1.15)
ax.text(146, ax.get_ylim()[1] * 0.95, "true σ² = 144", fontsize=9.5, color=INK)
ax.text(s2.mean() + 40, ax.get_ylim()[1] * 0.7, f"average S² = {s2.mean():.1f}\n(unbiased)",
        fontsize=9, color=INK)
ax.text(s2n.mean() - 45, ax.get_ylim()[1] * 0.88, f"average Σ/n = {s2n.mean():.1f}\n≈ (11/12)·144 = 132\n(biased low)",
        fontsize=9, color=INK, ha="right")
ax.set_xlabel("estimated variance from one sample of 12 students")
ax.set_ylabel("how often (20 000 samples)")
ax.legend(loc="center right")
ax.set_title("Why divide by n − 1: the estimates centre on the true value")
save(fig, "14-estimator-bias.png")
