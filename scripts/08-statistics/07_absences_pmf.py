"""Probability distribution of absences with E[X] and ±1 SD."""
import numpy as np
import matplotlib.pyplot as plt
from common import load, save, BLUE, ORANGE, INK, INK2, BAND

a = load()["absences"].astype(int)
k = np.arange(5)
p = np.array([(a == v).sum() for v in k]) / len(a)
mu = (k * p).sum()
sd = np.sqrt((k**2 * p).sum() - mu**2)
fig, ax = plt.subplots(figsize=(8, 4.2))
ax.axvspan(mu - sd, mu + sd, color=BAND, alpha=0.45, lw=0)
ax.bar(k, p, color=BLUE, width=0.6)
for kk, pp in zip(k, p):
    ax.text(kk, pp + 0.01, f"{int(round(pp*12))}/12", ha="center", fontsize=9.5, color=INK)
ax.axvline(mu, color=ORANGE, lw=2.5, ls="--")
ax.text(mu + 0.06, 0.37, f"E[X] = {mu:.2f}", color=INK, fontsize=10)
ax.text(mu + sd + 0.05, 0.25, f"μ ± σ  (σ = {sd:.2f})", color=INK2, fontsize=9)
ax.set_xticks(k)
ax.set_ylim(0, 0.42)
ax.set_xlabel("number of absences k")
ax.set_ylabel("P(X = k)")
ax.set_title("E[X] is the balance point of the distribution")
save(fig, "07-absences-distribution.png")
