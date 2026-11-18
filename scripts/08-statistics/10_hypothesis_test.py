"""Two-sided z-test of H0: mu = 60 -> z = 1.73: rejection region vs p-value area."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from common import save, BLUE, ORANGE, INK, INK2, BAND

z_obs = (66 - 60) / (12 / np.sqrt(12))
z = np.linspace(-4, 4, 500)
y = stats.norm.pdf(z)
fig, ax = plt.subplots(figsize=(10, 4.6))
ax.plot(z, y, color=INK2, lw=2)
for m in (z <= -z_obs, z >= z_obs):
    ax.fill_between(z[m], y[m], color=BLUE, alpha=0.35, lw=0)
for lo, hi in ((-4, -1.96), (1.96, 4)):
    ax.plot([lo, hi], [-0.006, -0.006], color=ORANGE, lw=6, solid_capstyle="butt", clip_on=False)
for c in (-1.96, 1.96):
    ax.axvline(c, color=ORANGE, lw=1.5, ls="--")
ax.axvline(z_obs, color=BLUE, lw=2.5)
ax.text(z_obs - 0.08, 0.30, f"observed\nz = {z_obs:.2f}", ha="right", color=INK, fontsize=10)
ax.annotate("rejection region (orange bar)\n(α/2 = 0.025 each side)\n|z| > 1.96", (2.6, -0.006), xytext=(2.35, 0.16),
            fontsize=9.5, color=INK, arrowprops=dict(arrowstyle="->", color=INK2))
ax.annotate(f"p-value = blue area (both tails)\n= 2(1 − Φ(1.73)) = {2*(1-stats.norm.cdf(z_obs)):.3f}",
            (-2.0, 0.03), xytext=(-3.95, 0.2), fontsize=9.5, color=INK,
            arrowprops=dict(arrowstyle="->", color=INK2))
ax.text(0, 0.17, "do not reject H₀\n(1.73 < 1.96, p = 0.083 > 0.05)", ha="center", fontsize=10,
        color=INK, fontweight="bold")
ax.set_ylim(-0.012, 0.42)
ax.set_yticks([])
ax.grid(axis="y", visible=False)
ax.spines["left"].set_visible(False)
ax.set_xticks([-3, -1.96, -1, 0, 1, 1.96, 3])
ax.set_xlabel("z under H₀ (μ = 60)")
ax.set_title("Hypothesis test: is the class mean different from 60?")
save(fig, "10-hypothesis-test.png")
