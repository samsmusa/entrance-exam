# 10. Mathematical Modelling

> **Official topics (Placement Test guide):** dynamical systems; equilibria and their stability; linearization; exponential and logistic growth; predator-prey and epidemic models; units and dimensions of model parameters; bifurcations and phase transitions.
>
> **Exam:** 7 questions on this topic, 5 options each, about 85 seconds per question. Typical: find an equilibrium and decide stability, read a parameter's unit, recognize a bifurcation, know a model's long-term behaviour.
>
> **How to study this file:** every section is 🟢 (all are on the official list). The ODE skills come from [05-differential-equations.md](05-differential-equations.md). Time: about 1 study day + 1 hour for the MCQs.
>
> *Removed (not on the official list):* Fokker–Planck formalism, synergetics (slaving principle). The modelling cycle is reduced to a few lines.

## Contents
1. [Dynamical systems](#1-dynamical-systems-) 🟢
2. [Equilibria and their stability](#2-equilibria-and-their-stability-) 🟢
3. [Linearization](#3-linearization-) 🟢
4. [Exponential growth and decay](#4-exponential-growth-and-decay-) 🟢
5. [Logistic growth](#5-logistic-growth-) 🟢
6. [Predator–prey and competition models](#6-predatorprey-and-competition-models-) 🟢
7. [Epidemic models](#7-epidemic-models-) 🟢
8. [Units and dimensions of model parameters](#8-units-and-dimensions-of-model-parameters-) 🟢
9. [Bifurcations](#9-bifurcations-) 🟢
10. [Phase transitions](#10-phase-transitions-) 🟢
11. [Formula sheet](#formula-sheet)
12. [Practice MCQs](#practice-mcqs) (33 questions, 5 options)

---

## 1. Dynamical systems 🟢

A **dynamical system** is a rule that says how a state $x$ changes in time.

| Type | Form | Example |
|---|---|---|
| continuous time (flow) | $\dot x=f(x)$, $x\in\mathbb R^n$ | $\dot N=rN(1-N/K)$ |
| discrete time (map) | $x_{n+1}=F(x_n)$ | $x_{n+1}=rx_n(1-x_n)$ |

**Words**
- **State / phase space:** the set of all possible states $x$ (e.g. $\mathbb R^2$ for two populations).
- **Autonomous:** $f$ does not depend on $t$.
- **Orbit / trajectory:** the curve $t\mapsto x(t)$ of one solution. By uniqueness, orbits never cross.
- **Phase portrait:** picture of many orbits plus equilibria and arrows.
- **Equilibrium (fixed point):** $f(x^*)=0$ (flow) or $F(x^*)=x^*$ (map).
- **Periodic orbit:** $x(t+T)=x(t)$; a **limit cycle** is an isolated periodic orbit that attracts or repels its neighbours (e.g. van der Pol oscillator).
- **Attractor:** a set that nearby orbits approach (stable equilibrium, stable limit cycle, strange attractor).

> **Must-know facts**
> 1. **1D flows** ($\dot x=f(x)$): every solution is monotone; it goes to an equilibrium or to $\pm\infty$. No oscillations.
> 2. **Poincaré–Bendixson:** a bounded orbit of a 2D autonomous flow approaches an equilibrium or a periodic orbit — **no chaos in 2D**.
> 3. Chaos needs $\ge3$ dimensions for flows (Lorenz system), but already **1** dimension for maps (logistic map, $r\approx3.57$–$4$).
> 4. **Chaos** = deterministic, bounded, and sensitive to initial conditions (positive Lyapunov exponent).

**Model types:** deterministic vs stochastic (noise), continuous vs discrete time, linear vs nonlinear, ODE (no space) vs PDE (space + time). **Modelling cycle:** assumptions → model → solve → interpret → **validate** against data (verification = checking the model is solved correctly).

---

## 2. Equilibria and their stability 🟢

### Definitions (official example 1)
Let $x^*$ be an equilibrium.
| Word | Meaning |
|---|---|
| **(Lyapunov) stable** | solutions that start close to $x^*$ **remain close** to $x^*$ for all later times (small perturbations stay small) |
| **attracting** | solutions that start close converge to $x^*$ |
| **asymptotically stable** | stable **and** attracting |
| **unstable** | not stable: some solutions starting arbitrarily close move away |

Formal: stable ⇔ for every $\varepsilon>0$ there is $\delta>0$ with $\lvert x(0)-x^*\rvert<\delta\Rightarrow\lvert x(t)-x^*\rvert<\varepsilon$ for all $t\ge0$.

### 1D test for $\dot x=f(x)$
| $f'(x^*)$ | Result |
|---|---|
| $<0$ | asymptotically stable |
| $>0$ | unstable |
| $=0$ | no decision — look at the sign of $f$ around $x^*$ |

**Graphical method:** where $f>0$ arrows point right, where $f<0$ left; arrows pointing **towards** $x^*$ = stable.

**Example.** $\dot x=x^2-4$: $x^*=\pm2$, $f'=2x$: $-2$ stable, $+2$ unstable.
**Example (test fails).** $\dot x=-x^3$: $f'(0)=0$, but $f>0$ for $x<0$ and $f<0$ for $x>0$ ⇒ asymptotically stable. $\dot x=x^3$: unstable. $\dot x=x^2$: **semi-stable** (attracts from the left, repels to the right).

### Lyapunov functions (no linearization needed)
If $V(x)$ has a strict minimum at $x^*$ and $\dot V=\nabla V\cdot f\le0$ nearby, then $x^*$ is stable; if $\dot V<0$ for $x\ne x^*$, asymptotically stable.
Example: $\dot x=-x^3$, $V=x^2$: $\dot V=-2x^4<0$ ⇒ asymptotically stable.

> **Trap:** stability is about **small** perturbations near $x^*$; it says nothing about noise, linearity or periodicity.

---

## 3. Linearization 🟢

**Idea.** Near an equilibrium, replace $f$ by its first-order Taylor polynomial. With $u=x-x^*$:
$$\dot u\approx Df(x^*)\,u\qquad(\text{1D: }\dot u\approx f'(x^*)\,u).$$
$Df(x^*)$ is the **Jacobian matrix** at the equilibrium.

### Recipe (2D, $\dot x=f(x,y)$, $\dot y=g(x,y)$)
1. Solve $f=0$, $g=0$ → equilibria.
2. $J=\begin{pmatrix}f_x&f_y\\g_x&g_y\end{pmatrix}$ at the equilibrium.
3. $\tau=\operatorname{tr}J$, $\Delta=\det J$; eigenvalues from $\lambda^2-\tau\lambda+\Delta=0$.
4. Classify:

| Condition | Type of the linearization |
|---|---|
| $\Delta<0$ | saddle (unstable) |
| $\Delta>0$, $\tau<0$ | stable node ($\tau^2>4\Delta$) or stable spiral ($\tau^2<4\Delta$) |
| $\Delta>0$, $\tau>0$ | unstable node / spiral |
| $\Delta>0$, $\tau=0$ | center (linear) — **nonlinear system undecided** |
| $\Delta=0$ | zero eigenvalue — undecided |

**General rule:** all eigenvalues with $\operatorname{Re}\lambda<0$ ⇒ asymptotically stable; one with $\operatorname{Re}\lambda>0$ ⇒ unstable.

### When can we trust the linearization?
> 1. **Hartman–Grobman:** if the equilibrium is **hyperbolic** (no eigenvalue with $\operatorname{Re}\lambda=0$), the nonlinear system looks locally like its linearization (same stability and type of node/saddle/spiral).
> 2. Non-hyperbolic ($\operatorname{Re}\lambda=0$, e.g. center, $f'(x^*)=0$): linearization does not decide; the nonlinear terms do (use a Lyapunov function, conserved quantity, or sign arguments).

**Worked example.** $\dot x=\sin x$.
1. Equilibria $x^*=k\pi$.
2. $f'(x)=\cos x$: $f'(0)=1$ ⇒ unstable; $f'(\pi)=-1$ ⇒ stable.

**Worked example (2D).** $\dot x=x-y$, $\dot y=x^2-4$ at $(2,2)$:
1. $J=\begin{pmatrix}1&-1\\2x&0\end{pmatrix}=\begin{pmatrix}1&-1\\4&0\end{pmatrix}$.
2. $\tau=1$, $\Delta=4>0$, $\tau^2-4\Delta<0$ ⇒ unstable spiral.

### Discrete maps $x_{n+1}=F(x_n)$
Linearization: $u_{n+1}\approx F'(x^*)u_n$.
| Test | Result |
|---|---|
| $\lvert F'(x^*)\rvert<1$ | stable |
| $\lvert F'(x^*)\rvert>1$ | unstable |
| $F'(x^*)<0$ | values alternate around $x^*$ |
In $n$ dimensions: all eigenvalues of $DF(x^*)$ with $\lvert\lambda\rvert<1$.

**Example.** $x_{n+1}=0.5x_n+3$: $x^*=6$, $F'=0.5$ ⇒ stable. Logistic map $r=2.5$: $x^*=1-\frac1r=0.6$, $F'(0.6)=2.5(1-1.2)=-0.5$ ⇒ stable, alternating.

> **Trap:** flows: sign of $\operatorname{Re}\lambda$; maps: size of $\lvert\lambda\rvert$. $F'(x^*)=-1.5$ is unstable for a map, but $f'(x^*)=-1.5$ is stable for a flow.

---

## 4. Exponential growth and decay 🟢

$\dot N=rN$, $N(0)=N_0$ ⇒ $N(t)=N_0e^{rt}$.
| Quantity | Formula |
|---|---|
| doubling time ($r>0$) | $T_2=\frac{\ln2}r$ |
| half-life ($r=-k<0$) | $T_{1/2}=\frac{\ln2}k$ |

**Example.** $\dot N=0.1N$ (per hour): $T_2=6.93$ h.
**Newton's law of cooling:** $\dot T=-k(T-T_{\text{env}})$ ⇒ $T=T_{\text{env}}+(T_0-T_{\text{env}})e^{-kt}$. Coffee $90°$, room $20°$, $k=0.1$: $T=20+70e^{-0.1t}$.
**Discrete version:** $N_{n+1}=\lambda N_n$ ⇒ $N_n=\lambda^nN_0$; growth if $\lambda>1$.

> **Trap:** exponential growth never stops — realistic only for small populations with unlimited resources.

---

## 5. Logistic growth 🟢

$$\dot N=rN\left(1-\frac NK\right),\qquad N(t)=\frac{K}{1+\frac{K-N_0}{N_0}e^{-rt}}.$$
$r$ = intrinsic growth rate, $K$ = carrying capacity.

**Equilibria (official example 2).** $f(N)=rN(1-\frac NK)$, $f'(N)=r(1-\frac{2N}K)$.
- $N=0$: $f'(0)=r>0$ ⇒ **unstable**.
- $N=K$: $f'(K)=-r<0$ ⇒ **stable**.

| Fact | Value |
|---|---|
| long-term ($N_0>0$) | $N\to K$ |
| fastest growth | at $N=\frac K2$, rate $\frac{rK}4$ |
| shape | S-curve (sigmoid), inflection at $\frac K2$ |

**Example.** $\dot N=0.5N(1-\frac N{100})$, $N_0=10$: $N=\frac{100}{1+9e^{-0.5t}}\to100$; fastest at $N=50$ with rate $12.5$.

**With harvesting:** $\dot N=rN(1-\frac NK)-h$. Equilibria exist only for $h\le\frac{rK}4$; at $h=\frac{rK}4$ they merge (saddle-node, section 9) — overharvesting causes collapse.

> **Trap:** fastest growth is at $\frac K2$, not at $K$ (where growth is $0$).

---

## 6. Predator–prey and competition models 🟢

### Lotka–Volterra
$$\dot x=\alpha x-\beta xy,\qquad\dot y=\delta xy-\gamma y\qquad(x\text{ prey},\ y\text{ predators}).$$
- $\alpha$: prey growth, $\beta$: predation rate, $\delta$: predator gain from eating, $\gamma$: predator death rate.
- Equilibria: $(0,0)$ — saddle ($J=\operatorname{diag}(\alpha,-\gamma)$); $\left(\frac\gamma\delta,\frac\alpha\beta\right)$ — linearization is a **center** ($\tau=0$, $\Delta=\alpha\gamma>0$).
- The system has a **conserved quantity** $V=\delta x-\gamma\ln x+\beta y-\alpha\ln y$, so the nonlinear equilibrium really is a center: closed orbits, **periodic oscillations**, stable but not asymptotically stable.
- Predator peaks lag behind prey peaks. Average populations over a cycle = the equilibrium values.

**Example.** $\dot x=x(3-y)$, $\dot y=y(x-2)$: equilibrium $(2,3)$, $J=\begin{pmatrix}0&-2\\3&0\end{pmatrix}$, eigenvalues $\pm i\sqrt6$ → center.

**Variant with logistic prey:** $\dot x=\alpha x(1-\frac xK)-\beta xy$: the inner equilibrium becomes a stable spiral — damped oscillations.

### Competition
$\dot x=x(1-x-ay)$, $\dot y=y(1-y-bx)$, $a,b>0$.
- $a<1$, $b<1$ (weak competition): stable **coexistence**.
- $a>1$, $b>1$: coexistence point is a saddle; one species wins depending on the start (bistability).
- Otherwise: one species always wins (**competitive exclusion**).

> **Trap:** the Lotka–Volterra inner equilibrium is a center, not a stable spiral: the populations keep cycling.

---

## 7. Epidemic models 🟢

### SIR
$$\dot S=-\beta\frac{SI}N,\qquad\dot I=\beta\frac{SI}N-\gamma I,\qquad\dot R=\gamma I,\qquad S+I+R=N.$$
$\beta$ = transmission rate, $\gamma$ = recovery rate, $\frac1\gamma$ = mean infectious period.

| Quantity | Formula |
|---|---|
| basic reproduction number | $R_0=\frac\beta\gamma$ (dimensionless) |
| outbreak | $R_0>1$ (with $S\approx N$); dies out if $R_0<1$ |
| peak of $I$ | when $S=\frac N{R_0}$ ($\dot I=0$) |
| herd-immunity threshold | $1-\frac1{R_0}$ |

**Example.** $\beta=0.3$/day, $\gamma=0.1$/day: $R_0=3$, sick for 10 days, herd immunity $67\%$.
Table: $R_0=2\to50\%$, $2.5\to60\%$, $4\to75\%$, $5\to80\%$.

**Why $R_0>1$?** $\dot I=I\gamma\left(R_0\frac SN-1\right)$; at the start $S\approx N$, so $I$ grows ⇔ $R_0>1$. (This is the linearization at the disease-free equilibrium.)

### SIS (no immunity)
$\dot I=\beta\frac{(N-I)I}N-\gamma I$ — a logistic equation. Equilibria $I=0$ and $I^*=N\left(1-\frac1{R_0}\right)$ (**endemic**). For $R_0>1$: $I^*$ stable, $0$ unstable; at $R_0=1$ they exchange stability (transcritical bifurcation).

> **Trap:** $R_0=\beta/\gamma$, not $\gamma/\beta$; herd immunity is $1-1/R_0$.

---

## 8. Units and dimensions of model parameters 🟢

**Rule 1:** every term in an equation has the **same unit**. **Rule 2:** arguments of $e^x$, $\ln x$, $\sin x$ are **dimensionless**.

**Reading units from a model** (time in days, populations in individuals = ind):
| Model | Parameter | Unit |
|---|---|---|
| $\dot N=rN$ | $r$ | $\frac1{\text{day}}$ (so $rt$ in $e^{rt}$ is dimensionless) |
| logistic | $K$ | ind (same as $N$) |
| Lotka–Volterra | $\alpha,\gamma$ | $\frac1{\text{day}}$ |
| Lotka–Volterra | $\beta$ | $\frac1{\text{ind}\cdot\text{day}}$ (since $\beta xy$ must be ind/day) |
| SIR with $\frac{SI}N$ | $\beta,\gamma$ | $\frac1{\text{day}}$ |
| SIR | $R_0=\frac\beta\gamma$ | dimensionless |
| cooling | $k$ | $\frac1{\text{time}}$ |
| diffusion $u_t=Du_{xx}$ | $D$ | $\frac{\text{length}^2}{\text{time}}$ |

**Buckingham $\Pi$ theorem:** $n$ variables with $k$ independent base units (M, L, T, …) form $n-k$ independent dimensionless groups.
Example: pendulum period $T$ from $L$, $m$, $g$: $n=4$, $k=3$ ⇒ one group $\frac{T^2g}L$ ⇒ $T\propto\sqrt{L/g}$ (mass drops out).

**Nondimensionalization** removes parameters:
- Logistic: $u=\frac NK$, $s=rt$ ⇒ $\frac{du}{ds}=u(1-u)$ — no parameters left.
- Lotka–Volterra: 4 parameters reduce to 1 ($\frac\gamma\alpha$).
Characteristic time scale of $\dot N=rN$: $\frac1r$.

> **Trap:** a rate multiplied by a product of two populations ($\beta xy$) needs units "per individual per time".

---

## 9. Bifurcations 🟢

A **bifurcation** occurs at a parameter value $r_c$ where the **number or stability** of equilibria (or periodic orbits) changes. At a bifurcation point of an equilibrium, the linearization has an eigenvalue with $\operatorname{Re}\lambda=0$ (non-hyperbolic).

| Type | Normal form | What happens at $r=0$ |
|---|---|---|
| **saddle-node** (fold) | $\dot x=r+x^2$ | $r<0$: two equilibria $\pm\sqrt{-r}$ (one stable, one unstable); they collide and **vanish** for $r>0$ |
| **transcritical** | $\dot x=rx-x^2$ | equilibria $0$ and $r$ **exchange stability** |
| **pitchfork** (supercritical) | $\dot x=rx-x^3$ | $r<0$: only $0$, stable; $r>0$: $0$ unstable, $\pm\sqrt r$ stable (**symmetry breaking**) |
| subcritical pitchfork | $\dot x=rx+x^3$ | unstable branches; jumps and **hysteresis** |
| **Hopf** | complex pair $\alpha(r)\pm i\omega$ crosses $\operatorname{Re}\lambda=0$ | a **limit cycle** (oscillation) is born |
| **period doubling** (maps) | $F'(x^*)$ crosses $-1$ | 2-cycle appears; logistic map at $r=3$ |

**Worked example (pitchfork).** $\dot x=rx-x^3$, $r>0$.
1. $x(r-x^2)=0$ ⇒ $x=0,\pm\sqrt r$.
2. $f'(x)=r-3x^2$: $f'(0)=r>0$ unstable; $f'(\pm\sqrt r)=-2r<0$ stable.

**Worked example (harvesting).** $\dot x=x(1-x)-h$.
1. $x^2-x+h=0$ ⇒ $x=\frac{1\pm\sqrt{1-4h}}2$.
2. Two equilibria for $h<\frac14$, one at $h=\frac14$, none for $h>\frac14$ ⇒ saddle-node at $h_c=\frac14$.

**Logistic map** $x_{n+1}=rx_n(1-x_n)$: $0<r<1$: $x_n\to0$; $1<r<3$: $x_n\to1-\frac1r$ (transcritical at $r=1$); $r=3$: period doubling; $r\approx3.57$: chaos begins; $r=4$: fully chaotic.

**Bifurcation diagram:** plot equilibria (solid = stable, dashed = unstable) against the parameter.

> **Trap:** at a saddle-node the equilibria do not change stability — they disappear. At a transcritical bifurcation they swap stability.

---

## 10. Phase transitions 🟢

A **phase transition** is a sudden change of the macroscopic state of a system when a control parameter (often temperature $T$) crosses a critical value $T_c$. In dynamical-systems language it corresponds to a bifurcation.

> **Must-know facts**
> 1. **Order parameter** $m$: $0$ in the disordered phase, $\ne0$ in the ordered phase (magnetization, density difference, laser amplitude).
> 2. **First-order** transition: $m$ **jumps**; latent heat, coexistence of phases, **hysteresis** (melting, boiling) — like a subcritical / saddle-node bifurcation.
> 3. **Second-order (continuous)** transition: $m$ grows continuously from $0$ (ferromagnet at the Curie point) — like a **supercritical pitchfork**.
> 4. **Landau theory:** $F(m)=a(T-T_c)m^2+bm^4$ ($a,b>0$). For $T>T_c$ the minimum is $m=0$; for $T<T_c$: $m=\pm\sqrt{\frac{a(T_c-T)}{2b}}\propto(T_c-T)^{1/2}$ (critical exponent $\frac12$).
> 5. **Symmetry breaking:** the equations are symmetric ($m\to-m$), but the system picks one of $\pm m$.
> 6. **Critical slowing down:** for $\dot x=ax-x^3$, the return rate to $0$ is $\lvert a\rvert$; as $a\to0$ the relaxation time $\frac1{\lvert a\rvert}\to\infty$. Fluctuations and the correlation length also grow near $T_c$.
> 7. Ising model: no phase transition in 1D at $T>0$; there is one in 2D.

> **Trap:** "order parameter jumps" = first order; "continuous with $(T_c-T)^{1/2}$" = second order.

---

## Formula sheet

| Topic | Formula / rule |
|---|---|
| Stability | stable: start close ⇒ stay close; asymptotically: + converge |
| 1D flow | $f(x^*)=0$; $f'(x^*)<0$ stable, $>0$ unstable, $=0$ undecided |
| 1D map | $F(x^*)=x^*$; $\lvert F'(x^*)\rvert<1$ stable |
| Linearization | $\dot u=Df(x^*)u$; trust it if hyperbolic (Hartman–Grobman) |
| 2D | $\Delta<0$ saddle; $\Delta>0,\tau<0$ stable; $\tau^2<4\Delta$ spiral; $\tau=0$ center (undecided) |
| Exponential | $N_0e^{rt}$; $T_2=\ln2/r$ |
| Cooling | $T_{\text{env}}+(T_0-T_{\text{env}})e^{-kt}$ |
| Logistic | $0$ unstable, $K$ stable; fastest at $K/2$, rate $rK/4$ |
| Lotka–Volterra | equilibrium $(\gamma/\delta,\alpha/\beta)$, center, periodic orbits |
| SIR | $R_0=\beta/\gamma$; outbreak iff $R_0>1$; peak at $S=N/R_0$; herd immunity $1-1/R_0$ |
| SIS | endemic $I^*=N(1-1/R_0)$ |
| Units | all terms same unit; $[r]=1/\text{time}$; LV $[\beta]=1/(\text{ind}\cdot\text{time})$ |
| Π theorem | $n-k$ dimensionless groups |
| Bifurcations | $r+x^2$ saddle-node; $rx-x^2$ transcritical; $rx-x^3$ pitchfork; Hopf: limit cycle |
| Harvesting | $\dot x=rx(1-x/K)-h$: collapse at $h=rK/4$ |
| Phase transitions | 1st: jump, latent heat; 2nd: continuous, $m\propto(T_c-T)^{1/2}$ |

---

## Practice MCQs

**Q1.** (official example 1) Stability of an equilibrium means
A) solutions diverge from the equilibrium  B) solutions remain close to the equilibrium under small perturbations  C) the system has no noise  D) the system is linear  E) the system is periodic

<details><summary>Answer</summary>

**B** — Lyapunov stability.

</details>

**Q2.** (official example 2) For $\dot x=rx\left(1-\frac xK\right)$ with $r,K>0$:
A) the only equilibrium is $x=K$, stable  B) $x=0$ and $x=K$ are both stable  C) $x=0$ stable, $x=K$ unstable  D) $x=0$ unstable, $x=K$ stable  E) both unstable

<details><summary>Answer</summary>

**D** — $f'(0)=r>0$, $f'(K)=-r<0$.

</details>

**Q3.** An equilibrium is asymptotically stable if it is
A) stable and nearby solutions converge to it  B) attracting only  C) unstable but bounded  D) a center  E) periodic

<details><summary>Answer</summary>

**A** — A center (D) is stable but not asymptotically stable.

</details>

**Q4.** The equilibria of $\dot x=x^2-4$ are
A) $-2$ stable, $2$ unstable  B) $-2$ unstable, $2$ stable  C) both stable  D) both unstable  E) only $x=0$

<details><summary>Answer</summary>

**A** — $f'=2x$.

</details>

**Q5.** For $\dot x=-x^3$, the equilibrium $x=0$ is
A) unstable because $f'(0)=0$  B) asymptotically stable, although linearization gives $f'(0)=0$  C) a saddle  D) semi-stable  E) not an equilibrium

<details><summary>Answer</summary>

**B** — Linearization is inconclusive; the sign of $f$ (or $V=x^2$) shows stability.

</details>

**Q6.** For $\dot x=\sin x$, the equilibrium $x=\pi$ is
A) unstable  B) stable  C) semi-stable  D) not an equilibrium  E) a center

<details><summary>Answer</summary>

**B** — $f'(\pi)=\cos\pi=-1<0$.

</details>

**Q7.** The Hartman–Grobman theorem guarantees that the linearization decides stability when
A) the system is 1D  B) no eigenvalue of the Jacobian has zero real part  C) all eigenvalues are real  D) the Jacobian is symmetric  E) the equilibrium is a center

<details><summary>Answer</summary>

**B** — Hyperbolic equilibrium.

</details>

**Q8.** At an equilibrium $J=\begin{pmatrix}-1&2\\-2&-1\end{pmatrix}$. The equilibrium is
A) a saddle  B) an unstable node  C) a center  D) a stable spiral  E) a stable node

<details><summary>Answer</summary>

**D** — $\tau=-2$, $\Delta=5$, $\tau^2-4\Delta<0$: $-1\pm2i$.

</details>

**Q9.** The fixed point of $x_{n+1}=0.5x_n+3$ is
A) $3$, unstable  B) $0$, stable  C) $6$, stable  D) $6$, unstable  E) $2$, stable

<details><summary>Answer</summary>

**C** — $x^*=6$, $\lvert F'\rvert=0.5<1$.

</details>

**Q10.** A map has $F'(x^*)=-1.5$, a flow has $f'(x^*)=-1.5$. Then
A) both stable  B) map unstable, flow stable  C) both unstable  D) map stable, flow unstable  E) both undecided

<details><summary>Answer</summary>

**B** — Map: $\lvert F'\rvert>1$. Flow: $f'<0$.

</details>

**Q11.** For the logistic map $x_{n+1}=2.5x_n(1-x_n)$, the nonzero fixed point is
A) $0.4$, unstable  B) $0.6$, unstable  C) $0.6$, stable  D) $0.4$, stable  E) $1$, stable

<details><summary>Answer</summary>

**C** — $1-\frac1{2.5}$, $F'=-0.5$.

</details>

**Q12.** $\dot N=0.1N$ (time in years). Doubling time:
A) $0.69$  B) $6.93$  C) $10$  D) $20$  E) $0.1$

<details><summary>Answer</summary>

**B** — $\ln2/0.1$.

</details>

**Q13.** $\dot T=-0.1(T-20)$, $T(0)=90$. Then $T(t)=$
A) $90e^{-0.1t}$  B) $20+70e^{-0.1t}$  C) $20+90e^{-0.1t}$  D) $70+20e^{-0.1t}$  E) $90-7t$

<details><summary>Answer</summary>

**B** — $T_{\text{env}}+(T_0-T_{\text{env}})e^{-kt}$; check $T(0)=90$, $T\to20$.

</details>

**Q14.** $\dot N=0.5N(1-\frac N{100})$, $N(0)=10$. As $t\to\infty$:
A) $N\to0$  B) $N\to50$  C) $N\to100$  D) $N\to\infty$  E) $N$ oscillates

<details><summary>Answer</summary>

**C** — 1D flows do not oscillate (E).

</details>

**Q15.** In the logistic model, growth is fastest at
A) $N=K$  B) $N=0$  C) $N=K/4$  D) $N=K/2$  E) $N=2K$

<details><summary>Answer</summary>

**D** — $f(N)=rN-\frac rKN^2$ peaks where $f'(N)=0$.

</details>

**Q16.** The coexistence equilibrium of $\dot x=\alpha x-\beta xy$, $\dot y=\delta xy-\gamma y$ is
A) $(\alpha/\beta,\gamma/\delta)$, a saddle  B) $(\gamma/\delta,\alpha/\beta)$, a center with periodic orbits  C) $(\gamma/\delta,\alpha/\beta)$, a stable spiral  D) $(0,0)$  E) $(\beta/\alpha,\delta/\gamma)$

<details><summary>Answer</summary>

**B** — $\dot y=0\Rightarrow x=\gamma/\delta$; $\dot x=0\Rightarrow y=\alpha/\beta$.

</details>

**Q17.** The inner equilibrium of $\dot x=x(3-y)$, $\dot y=y(x-2)$ is
A) $(3,2)$, saddle  B) $(2,3)$, center  C) $(2,3)$, stable node  D) $(3,2)$, center  E) $(2,3)$, unstable spiral

<details><summary>Answer</summary>

**B** — $\tau=0$, $\Delta=6$.

</details>

**Q18.** SIR with $\beta=0.3$/day, $\gamma=0.1$/day. $R_0=$
A) $0.33$  B) $0.03$  C) $0.4$  D) $3$  E) $30$

<details><summary>Answer</summary>

**D** — $\beta/\gamma=0.3/0.1$.

</details>

**Q19.** A disease has $R_0=4$. Herd-immunity threshold:
A) $25\%$  B) $50\%$  C) $75\%$  D) $80\%$  E) $100\%$

<details><summary>Answer</summary>

**C** — $1-\frac14$.

</details>

**Q20.** In SIR, $I$ is largest when
A) $S=N/R_0$  B) $S=0$  C) $I=N/2$  D) $R=N/R_0$  E) $S=N$

<details><summary>Answer</summary>

**A** — $\dot I=0$.

</details>

**Q21.** SIS model with $R_0>1$: the endemic equilibrium is
A) $I^*=N/R_0$  B) $I^*=N(1-1/R_0)$  C) $I^*=0$  D) $I^*=N$  E) $I^*=R_0N$

<details><summary>Answer</summary>

**B** — Like a logistic equation with capacity $N(1-1/R_0)$.

</details>

**Q22.** In $\dot N=rN$ with $t$ in days, the unit of $r$ is
A) days  B) individuals per day  C) $1/\text{day}$  D) dimensionless  E) individuals

<details><summary>Answer</summary>

**C** — $rN$ must have the unit of $\dot N$ (ind/day); also $rt$ in $e^{rt}$ must be dimensionless.

</details>

**Q23.** In $\dot x=\alpha x-\beta xy$ ($x,y$ in individuals, $t$ in days), $\beta$ has unit
A) $1/\text{day}$  B) $1/(\text{individual}\cdot\text{day})$  C) individuals/day  D) dimensionless  E) day/individual

<details><summary>Answer</summary>

**B** — $\beta xy$ must be ind/day.

</details>

**Q24.** The basic reproduction number $R_0=\beta/\gamma$ is
A) measured in days  B) measured in $1/\text{day}$  C) dimensionless  D) measured in individuals  E) a probability

<details><summary>Answer</summary>

**C** — Ratio of two rates.

</details>

**Q25.** 5 variables with 3 base units (M, L, T). Number of dimensionless groups:
A) 8  B) 5  C) 3  D) 2  E) 15

<details><summary>Answer</summary>

**D** — $n-k$.

</details>

**Q26.** With $u=N/K$ and $s=rt$, the logistic equation becomes
A) $\frac{du}{ds}=ru(1-u)$  B) $\frac{du}{ds}=u(1-u)$  C) $\frac{du}{ds}=u(K-u)$  D) $\frac{du}{ds}=u$  E) $\frac{du}{ds}=Ku(1-u/K)$

<details><summary>Answer</summary>

**B** — All parameters scale out.

</details>

**Q27.** For $\dot x=rx-x^3$ with $r>0$, the stable equilibria are
A) $0$ only  B) $\pm\sqrt r$  C) $\pm r$  D) none  E) $0$ and $\pm\sqrt r$

<details><summary>Answer</summary>

**B** — Supercritical pitchfork.

</details>

**Q28.** For $\dot x=r+x^2$, as $r$ increases through $0$:
A) two equilibria collide and disappear  B) two equilibria exchange stability  C) a limit cycle is born  D) one equilibrium splits into three  E) nothing changes

<details><summary>Answer</summary>

**A** — Saddle-node. B is transcritical, C Hopf, D pitchfork.

</details>

**Q29.** A Hopf bifurcation occurs when
A) a real eigenvalue crosses $0$  B) a pair of complex-conjugate eigenvalues crosses the imaginary axis, creating a limit cycle  C) the Jacobian is symmetric  D) two equilibria collide  E) the system becomes 1D

<details><summary>Answer</summary>

**B** — The real part of the eigenvalues changes sign while they stay complex.

</details>

**Q30.** $\dot x=x(1-x)-h$ (logistic growth with constant harvesting). Equilibria disappear for
A) $h>1$  B) $h>\frac14$  C) $h>\frac12$  D) $h<0$  E) never

<details><summary>Answer</summary>

**B** — $x^2-x+h=0$ needs $1-4h\ge0$. Saddle-node at $h=\frac14=\frac{rK}4$.

</details>

**Q31.** Which property belongs to a first-order phase transition?
A) latent heat and a jump of the order parameter  B) continuous order parameter  C) no hysteresis  D) $m\propto(T_c-T)^{1/2}$  E) no symmetry

<details><summary>Answer</summary>

**A** — B and D are second order.

</details>

**Q32.** "Critical slowing down" means
A) the order parameter jumps  B) fluctuations disappear  C) the system becomes chaotic  D) the return time to equilibrium becomes very long near the critical point  E) the temperature drops

<details><summary>Answer</summary>

**D** — Relaxation time $1/\lvert a\rvert\to\infty$.

</details>

**Q33.** Which statement is true for autonomous ODE systems?
A) chaos is possible in 1D  B) chaos is possible in 2D  C) chaos needs at least 3 dimensions  D) chaos is impossible in any dimension  E) chaos needs a linear system

<details><summary>Answer</summary>

**C** — Poincaré–Bendixson rules out chaos in 2D flows; 1D flows are monotone. (Maps can be chaotic already in 1D.)

</details>
