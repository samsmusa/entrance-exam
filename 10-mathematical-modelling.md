# 10. Mathematical Modelling

> **Syllabus:**
> - Dynamical systems
> - Fokker–Planck formalism
> - Synergetics
> - Phase transitions
> - Stability

> **How to study this file:** Sections 1–7 are 🟢 core. They use only the ODE skills from file 05 (solve $y'=ky$, find equilibria, check $f'(x^*)$ or eigenvalues). Sections 8–11 are 🟡: learn only the facts in the "Must-know facts" boxes.
> Time: about 1 study day for the 🟢 parts, plus 1–2 hours for the 🟡 parts and the MCQs.
> Most MCQs here are: "find the equilibrium", "is it stable?", "what is the long-term value?", or "which word matches which idea?".

## Contents
1. [What is a mathematical model?](#1-what-is-a-mathematical-model-) 🟢
2. [Exponential growth and decay](#2-exponential-growth-and-decay-) 🟢
3. [Logistic growth](#3-logistic-growth-) 🟢
4. [Equilibria and stability in 1D](#4-equilibria-and-stability-in-1d-) 🟢
5. [Discrete models $x_{n+1}=F(x_n)$](#5-discrete-models-) 🟢
6. [Two-species models and stability in 2D](#6-two-species-models-and-stability-in-2d-) 🟢
7. [Epidemic model SIR](#7-epidemic-model-sir-) 🟢
8. [Dimensional analysis and bifurcations](#8-dimensional-analysis-and-bifurcations-) 🟡
9. [Fokker–Planck formalism](#9-fokkerplanck-formalism-) 🟡
10. [Synergetics](#10-synergetics-) 🟡
11. [Phase transitions](#11-phase-transitions-) 🟡
12. [Formula sheet](#formula-sheet)
13. [Practice MCQs](#practice-mcqs)

---

## 1. What is a mathematical model? 🟢

**Plain words:** a model describes a real situation with mathematics (variables, parameters, equations). Then we solve or simulate the model and compare the result with reality.

**The modelling cycle**
1. Real problem.
2. Make **assumptions** and simplify.
3. Build the mathematical model (choose variables, parameters, equations).
4. Solve or simulate it.
5. **Interpret** the result in the real world.
6. **Validate**: compare with real data. If it does not fit, go back to step 2.

**Types of models**

| Question | Choices |
|---|---|
| How does time run? | **continuous** (ODE, PDE) or **discrete** (steps $n=0,1,2,\dots$; difference equations) |
| Is there randomness? | **deterministic** (no chance) or **stochastic** (random, e.g. noise, Markov chains) |
| Shape of the equations? | **linear** or **nonlinear** |
| Space included? | ODE (no space) or PDE (space + time) |

- **Variable** = a quantity that changes (population $N(t)$).
- **Parameter** = a fixed number in the model (growth rate $r$).

**Trap:** *validation* = compare the model with real data. *Verification* = check that the computer/maths solves the model correctly. Different things.

---

## 2. Exponential growth and decay 🟢

**Plain words:** the change is proportional to the current amount. Many people → many births.

**Model:** $N'(t)=rN(t)$, with start value $N(0)=N_0$.
- $N(t)$ = amount at time $t$, $r$ = growth rate (a constant).

**Solution:** $N(t)=N_0e^{rt}$ (separable ODE, see file 05).

| Quantity | Formula |
|---|---|
| growth ($r>0$): doubling time | $T_2=\dfrac{\ln2}{r}$ |
| decay ($r=-k<0$): half-life | $T_{1/2}=\dfrac{\ln2}{k}$ |

**Example.** Bacteria: $N'=0.1N$, $N(0)=500$.
- $N(t)=500e^{0.1t}$.
- Doubling time $\ln2/0.1\approx6.93$ hours.
- After $T_2$: $N=1000$ ✓.

**Related model – Newton's law of cooling:** $T'=-k(T-T_{\text{env}})$.
- $T$ = temperature of the object, $T_{\text{env}}$ = room temperature, $k>0$.
- Solution: $T(t)=T_{\text{env}}+(T_0-T_{\text{env}})e^{-kt}$. For $t\to\infty$, $T\to T_{\text{env}}$.
- Example: coffee $T_0=90$, room $20$, $k=0.1$: $T(t)=20+70e^{-0.1t}$.

**Trap:** the exponential model grows forever. It is only realistic for small populations with unlimited resources. That is why we need the logistic model.

---

## 3. Logistic growth 🟢

**Plain words:** growth is fast when the population is small, and stops when it reaches the **carrying capacity** $K$ (the maximum the environment can support).

**Model (Verhulst):**
$$N'=rN\Big(1-\frac NK\Big)$$
- $r>0$ = growth rate for small $N$, $K>0$ = carrying capacity.

**Solution:**
$$N(t)=\frac{K}{1+\frac{K-N_0}{N_0}\,e^{-rt}}$$

**Key facts**

| Fact | Value |
|---|---|
| Equilibria | $N=0$ (unstable), $N=K$ (stable) |
| Long-term value (if $N_0>0$) | $N(t)\to K$ |
| Fastest growth | at $N=K/2$; the maximum rate is $rK/4$ |
| Shape of $N(t)$ | S-shaped curve ("sigmoid"); inflection point at $N=K/2$ |

**Example.** $N'=0.5N\big(1-\frac{N}{100}\big)$, $N(0)=10$.
- $K=100$, $r=0.5$.
- Solution: $N(t)=\dfrac{100}{1+9e^{-0.5t}}$ (since $\frac{100-10}{10}=9$).
- Check $t=0$: $100/(1+9)=10$ ✓. For $t\to\infty$: $N\to100$.
- Fastest growth at $N=50$, rate $=0.5\cdot100/4=12.5$.

**Why $K/2$?** The growth rate is $f(N)=rN-\frac{r}{K}N^2$, a downward parabola. Its top is where $f'(N)=r-\frac{2r}{K}N=0$, i.e. $N=K/2$.

**Trap:** the population **grows fastest** at $K/2$, not at $K$. At $K$ the growth is zero.

---

## 4. Equilibria and stability in 1D 🟢

**Plain words:** an **equilibrium** is a state that does not change. It is **stable** if small pushes die out (the system comes back). It is **unstable** if small pushes grow.

**Model:** $x'=f(x)$ (the right side does not depend on $t$: "autonomous").

**Recipe**
- Step 1: Solve $f(x^*)=0$. The solutions $x^*$ are the equilibria.
- Step 2: Compute $f'(x)$.
- Step 3: $f'(x^*)<0$ ⇒ **stable**. $f'(x^*)>0$ ⇒ **unstable**. $f'(x^*)=0$ ⇒ test fails, look at the sign of $f$.

**Graphical method:** draw $f(x)$. Where $f>0$, $x$ increases (arrow →). Where $f<0$, $x$ decreases (arrow ←). Arrows pointing **towards** a point = stable.

**Example 1.** $x'=x^2-4$.
- Equilibria: $x^*=-2$ and $x^*=2$.
- $f'(x)=2x$. $f'(-2)=-4<0$ → stable. $f'(2)=4>0$ → unstable.

**Example 2.** Logistic $N'=rN(1-N/K)$: $f'(N)=r-\frac{2rN}{K}$. $f'(0)=r>0$ unstable; $f'(K)=-r<0$ stable.

**Example 3 (test fails).** $x'=-x^3$: $f'(0)=0$. But $f>0$ for $x<0$ and $f<0$ for $x>0$, so all arrows point to $0$: stable.

**Words for stability**

| Word | Meaning |
|---|---|
| (Lyapunov) **stable** | start close ⇒ stay close |
| **asymptotically stable** | stable **and** the solution goes back to $x^*$ |
| **unstable** | some solutions starting close move away |

**Fact:** in 1D ($x'=f(x)$) solutions are always monotone. There are no oscillations in 1D.

**Trap:** for continuous models the test is the **sign** of $f'(x^*)$. Do not mix it with the discrete test $|F'(x^*)|<1$ (next section).

---

## 5. Discrete models $x_{n+1}=F(x_n)$ 🟢

**Plain words:** time moves in steps (years, generations). The next value is computed from the current value.

**Fixed point:** $x^*$ with $F(x^*)=x^*$. (Not $=0$!)

**Recipe**
- Step 1: Solve $F(x^*)=x^*$.
- Step 2: Compute $F'(x^*)$.
- Step 3: $|F'(x^*)|<1$ ⇒ **stable**. $|F'(x^*)|>1$ ⇒ **unstable**.
- Extra: $F'(x^*)<0$ means the values jump from one side to the other (alternating approach).

**Example 1 (linear map).** $x_{n+1}=0.5x_n+3$.
- $x^*=0.5x^*+3$ ⇒ $x^*=6$.
- $F'=0.5$, $|0.5|<1$ → stable. From $x_0=0$: $3,\ 4.5,\ 5.25,\dots\to6$.

**Example 2 (logistic map).** $x_{n+1}=rx_n(1-x_n)$, $0\le x\le1$.
- Fixed points: $x^*=0$ and $x^*=1-\frac1r$.
- $F'(x)=r(1-2x)$, so $F'(0)=r$ and $F'(1-\frac1r)=2-r$.
- With $r=2.5$: $x^*=1-0.4=0.6$, $F'(0.6)=-0.5$. $|{-0.5}|<1$ → stable, with alternating approach.

**Logistic map facts (🟡, just remember)**

| $r$ | Behaviour |
|---|---|
| $0<r<1$ | $x_n\to0$ |
| $1<r<3$ | $x_n\to1-\frac1r$ |
| $r=3$ | period doubling starts (2-cycle) |
| $r\approx3.57$ | chaos begins |
| $r=4$ | fully chaotic |

- **Chaos** = deterministic, bounded, but very sensitive to the start value (positive Lyapunov exponent).
- The continuous logistic ODE is never chaotic. The discrete logistic map can be chaotic.

**Trap:** discrete stability is $|F'(x^*)|<1$, **not** $F'(x^*)<0$. Example: $F'(x^*)=-1.5$ is unstable for a map.

---

## 6. Two-species models and stability in 2D 🟢

**Plain words:** two populations $x(t)$, $y(t)$ influence each other. To check stability of an equilibrium we use the **Jacobian matrix** $J$ (all first partial derivatives) and its eigenvalues.

**Recipe (stability of a 2D equilibrium)**
- Step 1: Solve $x'=0$ and $y'=0$ together → equilibria.
- Step 2: Jacobian $J=\begin{pmatrix}\partial f/\partial x&\partial f/\partial y\\ \partial g/\partial x&\partial g/\partial y\end{pmatrix}$ for $x'=f(x,y)$, $y'=g(x,y)$.
- Step 3: Put in the equilibrium. Compute $\tau=\operatorname{tr}J$ (sum of diagonal) and $\Delta=\det J$.
- Step 4: Use the table.

| Condition | Type |
|---|---|
| $\Delta<0$ | saddle (unstable) |
| $\Delta>0$, $\tau<0$ | **stable** (node if $\tau^2>4\Delta$, spiral if $\tau^2<4\Delta$) |
| $\Delta>0$, $\tau>0$ | unstable (node or spiral) |
| $\Delta>0$, $\tau=0$ | center (closed orbits) in the linearization |

**Same rule in eigenvalue words:** continuous system stable ⇔ all eigenvalues have **negative real part**. Discrete system stable ⇔ all eigenvalues have **absolute value $<1$**.

### 6.1 Predator–prey (Lotka–Volterra)
$$x'=\alpha x-\beta xy,\qquad y'=\delta xy-\gamma y$$
- $x$ = prey (rabbits), $y$ = predators (foxes). All parameters $>0$.
- $\alpha x$: prey grows without predators. $-\beta xy$: prey is eaten. $\delta xy$: predators grow by eating. $-\gamma y$: predators die without food.

**Facts**
- Equilibria: $(0,0)$ (saddle) and $\big(\frac\gamma\delta,\frac\alpha\beta\big)$.
- The inner equilibrium is a **center**: populations **oscillate** in closed cycles. Stable, but not asymptotically stable.
- The predator peak comes after the prey peak.

**Example.** $x'=x(3-y)$, $y'=y(x-2)$.
- Inner equilibrium: $3-y=0$ and $x-2=0$ ⇒ $(2,3)$.
- $J=\begin{pmatrix}3-y&-x\\y&x-2\end{pmatrix}$. At $(2,3)$: $J=\begin{pmatrix}0&-2\\3&0\end{pmatrix}$.
- $\tau=0$, $\Delta=0-(-6)=6>0$ → center, eigenvalues $\pm i\sqrt6$.

### 6.2 Competition
Two species compete for the same food: $x'=x(1-x-a y)$, $y'=y(1-y-b x)$ (with $a,b>0$).
- If $a<1$ and $b<1$ (weak competition): both species **coexist** at a stable equilibrium.
- If competition is strong: usually one species wins ("competitive exclusion").

**Trap:** the inner equilibrium of Lotka–Volterra is a **center**, not a stable spiral. The populations never settle down; they keep cycling.

---

## 7. Epidemic model SIR 🟢

**Plain words:** the population is split into three groups:
- $S$ = **susceptible** (can get sick), $I$ = **infected**, $R$ = **recovered** (immune).
- $N=S+I+R$ = total population (constant).

**Model**
$$S'=-\beta\frac{SI}{N},\qquad I'=\beta\frac{SI}{N}-\gamma I,\qquad R'=\gamma I$$
- $\beta$ = infection (contact) rate, $\gamma$ = recovery rate, $1/\gamma$ = average time a person is sick.

**Key numbers**

| Quantity | Formula | Meaning |
|---|---|---|
| Basic reproduction number | $R_0=\dfrac{\beta}{\gamma}$ | number of new infections caused by one sick person in a fully susceptible population |
| Epidemic? | $R_0>1$ (with $S\approx N$) | yes, $I$ grows at first; if $R_0<1$ it dies out |
| Herd-immunity threshold | $p_c=1-\dfrac{1}{R_0}$ | fraction that must be immune to stop spread |
| Peak of $I$ | when $S=\dfrac{N}{R_0}$ | then $I'=0$ |

**Example.** $\beta=0.3$ per day, $\gamma=0.1$ per day.
- $R_0=0.3/0.1=3$. People are sick for $1/0.1=10$ days on average.
- Herd immunity: $1-\frac13\approx67\%$.
- The number of infected is largest when $S=N/3$.

**Quick table:** $R_0=2\to50\%$, $R_0=2.5\to60\%$, $R_0=4\to75\%$, $R_0=5\to80\%$.

**Why $I'=0$ at $S=N/R_0$:** $I'=I\big(\beta\frac SN-\gamma\big)=0$ ⇔ $\frac SN=\frac\gamma\beta=\frac1{R_0}$.

**Trap:** $R_0=\beta/\gamma$, not $\gamma/\beta$. And herd immunity is $1-1/R_0$, not $1/R_0$.

---

## 8. Dimensional analysis and bifurcations 🟡

> **Must-know facts: dimensions**
> - Every term in a correct equation has the **same unit**. Arguments of $e^x$, $\ln x$, $\sin x$ must have **no unit**.
> - **Buckingham $\Pi$ theorem:** $n$ variables with $k$ independent basic units (e.g. mass M, length L, time T) can be combined into $n-k$ dimensionless groups.
> - Example: pendulum period $T$ depends on length $L$, mass $m$, gravity $g$: $n=4$, $k=3$ → 1 group, so $T\propto\sqrt{L/g}$ (mass does not matter).
> - **Nondimensionalization** (scaling variables) reduces the number of parameters. Logistic: with $u=N/K$, $s=rt$ you get $\frac{du}{ds}=u(1-u)$, no parameters left.

> **Must-know facts: bifurcations**
> - A **bifurcation** = at a critical parameter value the number or stability of equilibria changes.
> - **Saddle-node:** $x'=r+x^2$. For $r<0$ two equilibria $\pm\sqrt{-r}$; at $r=0$ they meet; for $r>0$ none.
> - **Transcritical:** $x'=rx-x^2$. Equilibria $0$ and $r$ exchange stability at $r=0$.
> - **Pitchfork:** $x'=rx-x^3$. For $r<0$ only $0$ (stable); for $r>0$, $0$ is unstable and $\pm\sqrt r$ are stable (symmetry breaking).
> - **Hopf:** a pair of complex eigenvalues crosses the imaginary axis → an oscillation (limit cycle) starts.

---

## 9. Fokker–Planck formalism 🟡

**Plain words:** a system with random noise. One random path is described by a **Langevin equation** / stochastic differential equation (SDE). The **Fokker–Planck equation** describes how the **probability density** $p(x,t)$ of all paths changes in time.

> **Must-know facts**
> - SDE: $dX=A(X)\,dt+\sigma\,dW$. Here $A$ = **drift** (the deterministic push), $\sigma$ = noise strength, $W$ = Wiener process.
> - **Fokker–Planck equation:** $\displaystyle\frac{\partial p}{\partial t}=-\frac{\partial}{\partial x}\big[A(x)p\big]+\frac12\frac{\partial^2}{\partial x^2}\big[B(x)p\big]$ with **diffusion** coefficient $B=\sigma^2$. So: drift term + diffusion term.
> - **Wiener process / Brownian motion** $W_t$: starts at $0$, independent increments, $W_t\sim\mathcal N(0,t)$ (mean $0$, variance $t$), continuous paths that are nowhere differentiable.
> - Pure diffusion $\partial_tp=D\,\partial_x^2p$ starting at one point: $p$ is a Gaussian with variance $2Dt$ (it spreads and never stops).
> - **Ornstein–Uhlenbeck** process $dX=-\gamma X\,dt+\sigma\,dW$: noise + pull back to $0$. Stationary distribution is Gaussian $\mathcal N\big(0,\frac{\sigma^2}{2\gamma}\big)$.
> - For drift $A=-U'(x)$ (a potential $U$) the stationary density is $p_s\propto e^{-2U(x)/\sigma^2}$: most probable states are at the **minima** of $U$.

**Mini example.** $dX=-2X\,dt+3\,dW$: drift $A(x)=-2x$, diffusion $B=3^2=9$.

**Trap:** the diffusion coefficient is the **square** of the noise amplitude ($\sigma\,dW$ ⇒ $B=\sigma^2$).

---

## 10. Synergetics 🟡

**Plain words:** synergetics (Hermann Haken, 1970s) studies how many parts **work together** and produce order by themselves (self-organization). Examples: laser light, convection rolls in heated fluid, chemical oscillations.

> **Must-know facts**
> - Self-organization happens in **open** systems **far from equilibrium** (energy flows in and out).
> - **Control parameter:** set from outside (pump power of a laser, heating of a fluid). When it crosses a critical value, the old state becomes **unstable**.
> - **Order parameter:** a few **slow** variables that describe the new macroscopic order (e.g. laser light amplitude, roll amplitude).
> - **Slaving principle:** the many **fast** variables follow ("are enslaved by") the few slow order parameters. Technically: *adiabatic elimination* — set the derivative of the fast variable to $0$.
> - **Circular causality:** the parts create the order parameter, and the order parameter controls the parts.
> - **Laser:** below the threshold pump power → normal lamp light (disordered); above → coherent laser light. This is like a second-order phase transition.

**Mini example (adiabatic elimination).** $\dot u=\varepsilon u-us$, $\dot s=-\gamma s+u^2$, with $s$ fast ($\gamma$ large). Set $\dot s=0$: $s=u^2/\gamma$. Then $\dot u=\varepsilon u-u^3/\gamma$ (a pitchfork).

---

## 11. Phase transitions 🟡

**Plain words:** a **phase transition** is a sudden change of the macroscopic state when a parameter (often temperature $T$) crosses a critical value. Examples: water → ice, a magnet losing its magnetization when heated.

> **Must-know facts**
> - **Order parameter** $m$: $0$ in the disordered phase, $\ne0$ in the ordered phase (e.g. magnetization).
> - **First-order** transition: the order parameter **jumps**; there is **latent heat**, coexistence of phases and hysteresis (example: boiling, melting).
> - **Second-order (continuous)** transition: the order parameter changes **continuously** from $0$; fluctuations and correlation length become very large near $T_c$ (example: ferromagnet at the Curie temperature).
> - **Landau theory:** free energy $F(m)=a(T-T_c)m^2+bm^4$. For $T<T_c$: $m=\pm\sqrt{\frac{a(T_c-T)}{2b}}$, so $m\propto(T_c-T)^{1/2}$ (mean-field exponent $\beta=\tfrac12$).
> - **Symmetry breaking:** the equations are symmetric ($m\to-m$), but the system chooses one state ($+m$ or $-m$).
> - **Critical slowing down:** near the critical point the system returns to equilibrium very slowly (relaxation time → ∞).
> - Ising model: in 1D there is **no** phase transition at $T>0$; in 2D there is one.

**Link to stability:** the pitchfork $x'=ax-x^3$ is the "dynamic version" of a second-order transition. For $a<0$ the state $0$ is stable; at $a=0$ it loses stability (relaxation time $1/|a|\to\infty$ = critical slowing down); for $a>0$ two new states $\pm\sqrt a$ appear.

---

## Formula sheet

| Topic | Formula / rule |
|---|---|
| Exponential | $N'=rN$ ⇒ $N=N_0e^{rt}$; doubling time $\ln2/r$ |
| Cooling | $T'=-k(T-T_{\text{env}})$ ⇒ $T=T_{\text{env}}+(T_0-T_{\text{env}})e^{-kt}$ |
| Logistic | $N'=rN(1-N/K)$; $N=\dfrac{K}{1+\frac{K-N_0}{N_0}e^{-rt}}$ |
| Logistic facts | $0$ unstable, $K$ stable; fastest growth at $K/2$, rate $rK/4$ |
| 1D continuous stability | $f(x^*)=0$; $f'(x^*)<0$ stable, $>0$ unstable |
| 1D discrete stability | $F(x^*)=x^*$; $|F'(x^*)|<1$ stable, $>1$ unstable |
| Logistic map | $x^*=1-1/r$, $F'(x^*)=2-r$, stable for $1<r<3$ |
| 2D stability | $J$ at equilibrium; stable ⇔ $\operatorname{tr}J<0$ and $\det J>0$; $\det J<0$ saddle |
| Eigenvalue rule | flow: all $\mathrm{Re}\,\lambda<0$; map: all $|\lambda|<1$ |
| Lotka–Volterra | $x'=\alpha x-\beta xy$, $y'=\delta xy-\gamma y$; equilibrium $(\gamma/\delta,\ \alpha/\beta)$, center |
| SIR | $R_0=\beta/\gamma$; epidemic iff $R_0>1$; herd immunity $1-1/R_0$; peak at $S=N/R_0$ |
| Π theorem | $n-k$ dimensionless groups |
| Bifurcations | saddle-node $r+x^2$; transcritical $rx-x^2$; pitchfork $rx-x^3$; Hopf: complex pair crosses $i\mathbb R$ |
| Fokker–Planck | $p_t=-(Ap)_x+\frac12(Bp)_{xx}$; drift $A$, diffusion $B=\sigma^2$ |
| Wiener | $W_t\sim\mathcal N(0,t)$ |
| Synergetics | control parameter → instability → order parameter (slow); slaving of fast modes |
| Phase transitions | 1st order: jump + latent heat; 2nd order: continuous; Landau $m\propto(T_c-T)^{1/2}$ |

---

## Practice MCQs

**Q1.** A population follows $N'=0.1N$ (time in years). Its doubling time is about
A) 0.69 years  B) 6.93 years  C) 10 years  D) 20 years

<details><summary>Answer</summary>

**B** — $T_2=\ln2/r=0.693/0.1\approx6.93$.

</details>

**Q2.** The solution of $N'=2N$, $N(0)=5$ is
A) $5e^{2t}$  B) $2e^{5t}$  C) $5+2t$  D) $10e^{t}$

<details><summary>Answer</summary>

**A** — $N=N_0e^{rt}$ with $N_0=5$, $r=2$. Check: $N'=10e^{2t}=2N$ ✓.

</details>

**Q3.** For $N'=0.5N\big(1-\frac{N}{100}\big)$ with $N(0)=10$, what happens as $t\to\infty$?
A) $N\to0$  B) $N\to50$  C) $N\to100$  D) $N\to\infty$

<details><summary>Answer</summary>

**C** — Logistic model with carrying capacity $K=100$. $K$ is the stable equilibrium, so $N\to100$ for every $N_0>0$.

</details>

**Q4.** In the logistic model $N'=rN(1-N/K)$, the population grows fastest when
A) $N=K$  B) $N=0$  C) $N=K/4$  D) $N=K/2$

<details><summary>Answer</summary>

**D** — $f(N)=rN-\frac rKN^2$ is a parabola with top at $f'(N)=r-\frac{2r}KN=0$, i.e. $N=K/2$.

</details>

**Q5.** The equilibria of $x'=x^2-4$ are
A) $x=-2$ stable, $x=2$ unstable  B) $x=-2$ unstable, $x=2$ stable  C) both stable  D) both unstable

<details><summary>Answer</summary>

**A** — $x^2-4=0$ at $x=\pm2$. $f'(x)=2x$: $f'(-2)=-4<0$ stable, $f'(2)=4>0$ unstable.

</details>

**Q6.** The fixed point of $x_{n+1}=0.5x_n+3$ is
A) $3$, unstable  B) $0$, stable  C) $6$, stable  D) $6$, unstable

<details><summary>Answer</summary>

**C** — $x^*=0.5x^*+3$ ⇒ $0.5x^*=3$ ⇒ $x^*=6$. $|F'|=0.5<1$ ⇒ stable.

</details>

**Q7.** In the modelling cycle, "validation" means
A) checking the computer code for errors  B) comparing model results with real data  C) choosing the variables  D) simplifying the problem

<details><summary>Answer</summary>

**B** — Validation compares the model with reality. Checking that the model is solved correctly is called verification.

</details>

**Q8.** In an SIR model, $\beta=0.3$ per day and $\gamma=0.1$ per day. Then $R_0$ equals
A) $0.33$  B) $0.03$  C) $0.4$  D) $3$

<details><summary>Answer</summary>

**D** — $R_0=\beta/\gamma=0.3/0.1=3$. Since $R_0>1$, an epidemic starts.

</details>

**Q9.** A disease has $R_0=4$. The herd-immunity threshold is
A) $25\%$  B) $50\%$  C) $75\%$  D) $80\%$

<details><summary>Answer</summary>

**C** — $1-1/R_0=1-0.25=0.75$.

</details>

**Q10.** A model that contains random noise is called
A) stochastic  B) deterministic  C) linear  D) discrete

<details><summary>Answer</summary>

**A** — Stochastic = includes chance. Deterministic = the same start always gives the same result.

</details>

**Q11.** A cup of coffee cools by $T'=-0.1(T-20)$ with $T(0)=90$. Which formula gives $T(t)$?
A) $90e^{-0.1t}$  B) $20+70e^{-0.1t}$  C) $20+90e^{-0.1t}$  D) $70+20e^{-0.1t}$

<details><summary>Answer</summary>

**B** — $T=T_{\text{env}}+(T_0-T_{\text{env}})e^{-kt}=20+70e^{-0.1t}$. Check: $T(0)=90$ ✓, $T\to20$ ✓.

</details>

**Q12.** For the logistic map $x_{n+1}=2.5\,x_n(1-x_n)$, the nonzero fixed point and its stability are
A) $0.4$, unstable  B) $0.6$, unstable  C) $0.6$, stable  D) $0.4$, stable

<details><summary>Answer</summary>

**C** — $x^*=1-1/r=1-0.4=0.6$. $F'(x)=r(1-2x)$, $F'(0.6)=2.5\cdot(-0.2)=-0.5$. $|{-0.5}|<1$ → stable (alternating approach).

</details>

**Q13.** The inner equilibrium of $x'=x(3-y)$, $y'=y(x-2)$ is
A) $(3,2)$, a saddle  B) $(2,3)$, a center  C) $(2,3)$, a stable node  D) $(3,2)$, a center

<details><summary>Answer</summary>

**B** — $3-y=0$, $x-2=0$ ⇒ $(2,3)$. $J=\begin{pmatrix}0&-2\\3&0\end{pmatrix}$: $\operatorname{tr}=0$, $\det=6>0$ → center (Lotka–Volterra cycles).

</details>

**Q14.** The Jacobian at an equilibrium is $J=\begin{pmatrix}-1&2\\-2&-1\end{pmatrix}$. The equilibrium is
A) a saddle  B) an unstable node  C) a center  D) a stable spiral

<details><summary>Answer</summary>

**D** — $\tau=-2<0$, $\Delta=1+4=5>0$, $\tau^2-4\Delta=-16<0$ → complex eigenvalues $-1\pm2i$ with negative real part.

</details>

**Q15.** A fixed point of a **discrete** map has $F'(x^*)=-1.5$. A fixed point of a **continuous** model $x'=f(x)$ has $f'(x^*)=-1.5$. Which is true?
A) both are stable  B) the map's point is unstable, the ODE's point is stable  C) both are unstable  D) the map's point is stable, the ODE's point is unstable

<details><summary>Answer</summary>

**B** — Map: $|-1.5|>1$ → unstable. ODE: $-1.5<0$ → stable.

</details>

**Q16.** In an SIR model, the number of infected people $I$ is largest when
A) $S=N/R_0$  B) $S=0$  C) $I=N/2$  D) $R=N/R_0$

<details><summary>Answer</summary>

**A** — $I'=I\big(\beta\frac SN-\gamma\big)=0$ ⇔ $\frac SN=\frac\gamma\beta=\frac1{R_0}$.

</details>

**Q17.** A law involves 5 physical variables built from the 3 basic units M, L, T. How many dimensionless groups does the Buckingham $\Pi$ theorem give?
A) 8  B) 5  C) 3  D) 2

<details><summary>Answer</summary>

**D** — $n-k=5-3=2$.

</details>

**Q18.** For $x'=rx-x^3$ with $r>0$, the stable equilibria are
A) $x=0$ only  B) $x=\pm\sqrt r$  C) $x=\pm r$  D) there are none

<details><summary>Answer</summary>

**B** — $x(r-x^2)=0$ ⇒ $x=0,\pm\sqrt r$. $f'(x)=r-3x^2$: $f'(0)=r>0$ unstable; $f'(\pm\sqrt r)=-2r<0$ stable. (Pitchfork bifurcation.)

</details>

**Q19.** The Fokker–Planck equation describes
A) the path of one single particle  B) the time evolution of a probability density  C) a discrete map  D) the equilibrium of a Lotka–Volterra model

<details><summary>Answer</summary>

**B** — It is a PDE for the density $p(x,t)$ with a drift term and a diffusion term. A single random path is described by a Langevin equation (SDE).

</details>

**Q20.** For the SDE $dX=-2X\,dt+3\,dW$, the drift $A(x)$ and diffusion coefficient $B$ in the Fokker–Planck equation are
A) $A=-2x$, $B=9$  B) $A=3$, $B=-2x$  C) $A=-2x$, $B=3$  D) $A=2x$, $B=9$

<details><summary>Answer</summary>

**A** — Drift = coefficient of $dt$: $-2x$. Diffusion = (noise amplitude)$^2=3^2=9$.

</details>

**Q21.** For a standard Wiener process $W_t$, the variance of $W_4$ is
A) $2$  B) $16$  C) $4$  D) $1$

<details><summary>Answer</summary>

**C** — $W_t\sim\mathcal N(0,t)$, so $\mathrm{Var}(W_4)=4$. (The standard deviation is $2$.)

</details>

**Q22.** In synergetics, the slaving principle says that
A) the order parameters are the fastest variables  B) the control parameter fixes the pattern in detail  C) the many fast variables follow the few slow order parameters  D) it works only in thermal equilibrium

<details><summary>Answer</summary>

**C** — Fast, stable variables adapt to the slow order parameters. This reduces many variables to a few.

</details>

**Q23.** Which property belongs to a **first-order** phase transition?
A) latent heat and a jump of the order parameter  B) the order parameter changes continuously  C) no hysteresis  D) $m\propto(T_c-T)^{1/2}$

<details><summary>Answer</summary>

**A** — First order: jump, latent heat, coexistence, hysteresis. B and D describe a second-order (continuous) transition.

</details>

**Q24.** "Critical slowing down" near a critical point means
A) the order parameter jumps  B) fluctuations disappear  C) the system becomes chaotic  D) the time to return to equilibrium becomes very long

<details><summary>Answer</summary>

**D** — For $x'=ax-x^3$ near $x=0$ the return rate is $|a|$; as $a\to0$ the relaxation time $1/|a|\to\infty$.

</details>

**Q25.** The equilibrium $x=0$ of the oscillator $x''+x=0$ (system $x'=y$, $y'=-x$) is
A) asymptotically stable  B) unstable  C) stable but not asymptotically stable  D) a saddle

<details><summary>Answer</summary>

**C** — $J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, eigenvalues $\pm i$: a center. Solutions move on circles: they stay close but do not return to $0$.

</details>
