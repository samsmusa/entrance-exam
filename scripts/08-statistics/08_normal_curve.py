"""Normal model N(66, 12^2): shaded P(54<X<78) and P(X>90), plus the z-axis."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from common import save, BLUE, ORANGE, INK, INK2, BAND

mu, sg = 66, 12
x = np.linspace(mu - 4 * sg, mu + 4 * sg, 400)
y = stats.norm.pdf(x, mu, sg)
fig, ax = plt.subplots(figsize=(10, 4.6))
ax.plot(x, y, color=INK2, lw=2)
m = (x > 54) & (x < 78)
ax.fill_between(x[m], y[m], color=BAND)
m2 = x > 90
ax.fill_between(x[m2], y[m2], color=ORANGE, alpha=0.7)
ax.text(66, 0.012, "P(54 < X < 78)\n= 2Φ(1) − 1 = 0.6826", ha="center", fontsize=10, color=INK)
ax.annotate("P(X > 90) = 1 − Φ(2)\n= 0.0228", (93, 0.0012), xytext=(98, 0.012), fontsize=10,
            color=INK, arrowprops=dict(arrowstyle="->", color=INK2))
ticks = [mu + k * sg for k in range(-3, 4)]
ax.set_xticks(ticks, [f"{t}\nz={k:+d}" if k else f"{t}\nz=0" for t, k in zip(ticks, range(-3, 4))])
ax.set_ylim(0, 0.037)
ax.set_yticks([])
ax.grid(axis="y", visible=False)
ax.spines["left"].set_visible(False)
ax.set_xlabel("score   (top: X,  bottom: z = (X − 66)/12)")
ax.set_title("Standardization: X ~ N(66, 12²)  →  Z = (X − 66)/12 ~ N(0, 1)")
save(fig, "08-normal-curve.png")
