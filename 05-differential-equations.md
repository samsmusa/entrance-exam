# 5. Differential Equations

> **Official topics (Placement Test guide):** separable, linear and Bernoulli equations; linear systems of ODEs; initial value problems, existence and uniqueness; dimension of solution spaces; classical PDEs and their classification; separation of variables and Fourier series.
>
> **Exam:** 7 questions on this topic, 5 options each, about 85 seconds per question. Typical: recognize an equation, pick the right solution (plug in and check!), state a theorem, count dimensions, classify a PDE.
>
> **How to study this file:** every section is 🟢 (all are on the official list). Do every worked example on paper. Time: about 2 study days + 1 hour for the MCQs.
>
> *Removed (not on the official list):* exact equations, principles of self-organization. Stability of equilibria, phase portraits and bifurcations are now in [10-mathematical-modelling.md](10-mathematical-modelling.md); here only a short stability table for $y'=Ay$ remains.

## Contents
1. [Basic words and the plug-in trick](#1-basic-words-and-the-plug-in-trick-) 🟢
2. [Separable equations](#2-separable-equations-) 🟢
3. [Linear first-order equations](#3-linear-first-order-equations-) 🟢
4. [Bernoulli equations](#4-bernoulli-equations-) 🟢
5. [Initial value problems: existence and uniqueness](#5-initial-value-problems-existence-and-uniqueness-) 🟢
6. [Linear ODEs of order $n$ and the dimension of solution spaces](#6-linear-odes-of-order-n-and-the-dimension-of-solution-spaces-) 🟢
7. [Linear systems $y'=Ay$ and the matrix exponential](#7-linear-systems-yay-and-the-matrix-exponential-) 🟢
8. [Classical PDEs and their classification](#8-classical-pdes-and-their-classification-) 🟢
9. [Separation of variables and Fourier series](#9-separation-of-variables-and-fourier-series-) 🟢
10. [Formula sheet](#formula-sheet)
11. [Practice MCQs](#practice-mcqs) (30 questions, 5 options)

---

## 1. Basic words and the plug-in trick 🟢

An **ODE** is an equation for an unknown function $y(t)$ with derivatives $y',y'',\dots$

| Word | Meaning | Example |
|---|---|---|
| **Order** | highest derivative | $y''+y=0$: order 2 |
| **Linear** | $y,y',\dots$ only to the power 1, not multiplied together; coefficients may depend on $t$ | $y''+t^2y=\cos t$ |
| **Nonlinear** | not linear | $y'=y^2$, $y'=\sin y$, $yy'=1$ |
| **Homogeneous** (linear) | no term without $y$ | $y''+y=0$ |
| **Inhomogeneous** | a term $g(t)\ne0$ without $y$ | $y''+y=t$ |
| **Autonomous** | $t$ does not appear explicitly | $y'=y(1-y)$ |
| **IVP** | ODE + initial values | $y'=y$, $y(0)=1$ |

**Key rule:** order $n$ ⇒ general solution with $n$ free constants ⇒ need $n$ initial conditions.

**Plug-in trick (fastest in an MCQ).**
1. Check the initial condition at $t=0$; cross out options that fail.
2. Differentiate the rest and put them into the ODE.

**Example.** $y'=y+t$, $y(0)=1$. Option $2e^t-t-1$: $y(0)=1$ ✓; $y'=2e^t-1$ and $y+t=2e^t-1$ ✓.

> **Trap:** check **both** the ODE and the initial condition; wrong options often satisfy only one.

---

## 2. Separable equations 🟢

**Form:** $y'=g(t)\,h(y)$.

**Recipe**
1. $\frac{dy}{h(y)}=g(t)\,dt$.
2. Integrate both sides, add $C$.
3. Solve for $y$, use the initial condition.
4. Every $y_0$ with $h(y_0)=0$ gives an extra **constant solution** $y\equiv y_0$.

**Example.** $y'=2ty$, $y(0)=3$: $\ln\lvert y\rvert=t^2+C$, $y=Ke^{t^2}$, $K=3$ ⇒ $y=3e^{t^2}$.

**Special cases**
- $y'=ky$ ⇒ $y=y(0)e^{kt}$ (growth $k>0$, decay $k<0$).
- $y'=y^2$, $y(0)=1$: $-\frac1y=t+C$ ⇒ $y=\frac1{1-t}$ (blows up at $t=1$).

> **Trap:** dividing by $h(y)$ loses the constant solutions ($y\equiv0$ for $y'=2ty$).

---

## 3. Linear first-order equations 🟢

**Form:** $y'+p(t)\,y=q(t)$.

**Recipe (integrating factor)**
1. Bring to the form $y'+py=q$ (watch the sign of $p$).
2. $\mu(t)=e^{\int p\,dt}$.
3. $(\mu y)'=\mu q$ ⇒ $\mu y=\int\mu q\,dt+C$.
4. Divide by $\mu$; use the initial condition.

**Example (official practice problem).** $y'=y+t$, $y(0)=1$.
1. $y'-y=t$, $p=-1$, $\mu=e^{-t}$.
2. $(ye^{-t})'=te^{-t}$ ⇒ $ye^{-t}=-te^{-t}-e^{-t}+C$.
3. $y=Ce^t-t-1$, $C=2$ ⇒ $y=2e^t-t-1$.

**Example 2.** $y'+\frac2ty=t$ ($t>0$): $\mu=t^2$, $(t^2y)'=t^3$ ⇒ $y=\frac{t^2}{4}+\frac C{t^2}$.

**Shortcut:** $y'=ay+b$ ($a\ne0$) ⇒ $y=Ce^{at}-\frac ba$.

**Structure:** $y=\underbrace{Ce^{-\int p}}_{y_h}+y_p$ — a one-parameter family (solution space of the homogeneous equation has dimension 1).

> **Trap:** $y'=y+t$ must become $y'-y=t$, so $\mu=e^{-t}$, not $e^t$.

---

## 4. Bernoulli equations 🟢

**Form:** $y'+p(t)y=q(t)y^n$, $n\ne0,1$.

**Recipe**
1. Substitute $v=y^{1-n}$.
2. Then $v'+(1-n)p\,v=(1-n)q$ is **linear** → Section 3.
3. Back: $y=v^{1/(1-n)}$.

**Example (logistic).** $y'=y-y^2$: $p=-1$, $q=-1$, $n=2$, $v=\frac1y$.
$v'+v=1$ ⇒ $v=1+Ce^{-t}$ ⇒ $y=\dfrac1{1+Ce^{-t}}$.

| $n$ | $2$ | $3$ | $\frac12$ |
|---|---|---|---|
| $v$ | $y^{-1}$ | $y^{-2}$ | $y^{1/2}$ |

> **Trap:** the exponent is $1-n$. For $y'+y=ty^3$: $v=y^{-2}$.

---

## 5. Initial value problems: existence and uniqueness 🟢

IVP: $y'=f(t,y)$, $y(t_0)=y_0$ (also for systems, $y\in\mathbb R^n$).

**Lipschitz in $y$:** $\lvert f(t,y)-f(t,z)\rvert\le L\lvert y-z\rvert$. Sufficient: $\partial f/\partial y$ continuous (locally Lipschitz).

> **Must-know facts**
> 1. **Picard–Lindelöf:** $f$ continuous and (locally) **Lipschitz in $y$** ⇒ there is a **unique** solution on some interval around $t_0$.
> 2. **Peano:** $f$ only continuous ⇒ a solution **exists**, but may not be unique.
> 3. Non-uniqueness example: $y'=\sqrt{y}$, $y(0)=0$ has $y\equiv0$ **and** $y=\frac{t^2}{4}$ ($\sqrt y$ is not Lipschitz at $0$). Also $y'=3y^{2/3}$, $y(0)=0$: $y\equiv0$ and $y=t^3$.
> 4. **Local only:** $y'=y^2$, $y(0)=1$ has $y=\frac1{1-t}$, which **blows up** at $t=1$, although $f=y^2$ is smooth. The solution exists on a **maximal interval** and leaves every compact set at its end.
> 5. **Global existence:** if $f$ is globally Lipschitz (e.g. **linear** ODEs $y'=A(t)y+g(t)$ with continuous coefficients), the solution exists on the whole interval.
> 6. **Picard iteration** (proof idea): $y_{k+1}(t)=y_0+\int_{t_0}^tf(s,y_k(s))\,ds$. For $y'=y$, $y(0)=1$ it gives $1,\ 1+t,\ 1+t+\frac{t^2}2,\dots\to e^t$.
> 7. **Uniqueness ⇒ solution curves never cross.** For an autonomous equation, a solution starting at an equilibrium stays there forever; a solution starting above an equilibrium can never pass it.
> 8. The solution depends **continuously** on the initial value (on finite time intervals).

**Worked example.** Is $y'=t\,y^{1/3}$, $y(0)=1$ uniquely solvable near $t=0$?
1. $\frac{\partial f}{\partial y}=\frac t3y^{-2/3}$ is continuous near $y=1$.
2. So $f$ is locally Lipschitz there ⇒ unique (Picard–Lindelöf). (At $y_0=0$ it would not be.)

> **Trap:** "$f$ is continuous" gives only **existence**. Uniqueness needs Lipschitz.

---

## 6. Linear ODEs of order $n$ and the dimension of solution spaces 🟢

**Form:** $y^{(n)}+a_{n-1}(t)y^{(n-1)}+\dots+a_0(t)y=g(t)$, coefficients continuous.

### Structure theorem (dimension of solution spaces)
> 1. The solutions of the **homogeneous** equation ($g=0$) form a **vector space of dimension exactly $n$** (superposition: sums and multiples of solutions are solutions).
> 2. A **basis** $y_1,\dots,y_n$ is called a **fundamental system**; the general solution is $y_h=C_1y_1+\dots+C_ny_n$.
> 3. The solutions of the **inhomogeneous** equation form an **affine** space $y_p+\{y_h\}$ of dimension $n$ — **not** a vector space ($0$ is not a solution).
> 4. Nonlinear equations: no superposition ($y'=y^2$: the sum of two solutions is not a solution).
> 5. For a **system** $y'=A(t)y$ with $y\in\mathbb R^n$: solution space also has dimension $n$.

**Wronskian** of $n$ solutions: $W(t)=\det\begin{pmatrix}y_1&\cdots&y_n\\y_1'&\cdots&y_n'\\\vdots&&\vdots\\y_1^{(n-1)}&\cdots&y_n^{(n-1)}\end{pmatrix}$.
For solutions: $W(t_0)\ne0$ at **one** point ⇔ $W(t)\ne0$ for all $t$ ⇔ independent (fundamental system).
Example: $W(e^t,e^{2t})=e^t\cdot2e^{2t}-e^t\cdot e^{2t}=e^{3t}\ne0$.
**Abel/Liouville:** $W(t)=W(t_0)\exp\left(-\int_{t_0}^ta_{n-1}(s)\,ds\right)$.

### Constant coefficients: characteristic equation
$a_ny^{(n)}+\dots+a_0y=0$: try $y=e^{rt}$ ⇒ $a_nr^n+\dots+a_0=0$.

| Roots | Contribution to the fundamental system |
|---|---|
| real simple $r$ | $e^{rt}$ |
| real $r$ of multiplicity $m$ | $e^{rt},\ te^{rt},\dots,t^{m-1}e^{rt}$ |
| complex pair $\alpha\pm i\beta$ | $e^{\alpha t}\cos\beta t,\ e^{\alpha t}\sin\beta t$ |

**Examples**
- $y''-5y'+6y=0$: $r=2,3$ ⇒ $C_1e^{2t}+C_2e^{3t}$. With $y(0)=1$, $y'(0)=0$: $y=3e^{2t}-2e^{3t}$.
- $y''-4y'+4y=0$: $r=2$ double ⇒ $(C_1+C_2t)e^{2t}$.
- $y''+2y'+5y=0$: $r=-1\pm2i$ ⇒ $e^{-t}(C_1\cos2t+C_2\sin2t)$.
- $y''+\omega^2y=0$ ⇒ $C_1\cos\omega t+C_2\sin\omega t$.
- $y'''-y'=0$: $r(r^2-1)=0$, $r=0,\pm1$ ⇒ basis $1,e^t,e^{-t}$ (dimension 3 ✓).

### Inhomogeneous: $y=y_h+y_p$
| $g(t)$ | Trial $y_p$ |
|---|---|
| constant / polynomial of degree $m$ | polynomial of degree $m$ |
| $ke^{at}$ | $Ae^{at}$ |
| $k\cos\omega t$ or $k\sin\omega t$ | $A\cos\omega t+B\sin\omega t$ (both!) |

**Resonance:** if the trial already solves the homogeneous equation, multiply by $t$ (by $t^m$ for a root of multiplicity $m$).
- $y''-3y'+2y=4$ ⇒ $y_p=2$.
- $y''+y=t$ ⇒ $y_p=t$, so $y=C_1\cos t+C_2\sin t+t$.
- $y''-3y'+2y=e^t$ (root $1$) ⇒ trial $Ate^t$, result $y_p=-te^t$.
- General method for any $g$: **variation of constants** (uses $W$).

> **Trap 1:** use the initial conditions on $y_h+y_p$, never on $y_h$ alone.
> **Trap 2:** a double root needs $te^{rt}$; $C_1e^{rt}+C_2e^{rt}$ has only one free constant.

---

## 7. Linear systems $y'=Ay$ and the matrix exponential 🟢

### The solution formula (official example 2)
For a constant $n\times n$ matrix $A$:
$$y'=Ay,\ y(0)=y_0\quad\Longrightarrow\quad y(t)=e^{At}y_0,\qquad e^{At}=\sum_{k=0}^\infty\frac{(At)^k}{k!}=I+At+\frac{A^2t^2}{2}+\dots$$
Why: $\frac{d}{dt}e^{At}=Ae^{At}$ and $e^{A\cdot0}=I$. Unique by Picard–Lindelöf.

### Computing $e^{At}$
| $A$ | $e^{At}$ |
|---|---|
| diagonal $\operatorname{diag}(\lambda_1,\dots,\lambda_n)$ | $\operatorname{diag}(e^{\lambda_1t},\dots,e^{\lambda_nt})$ |
| diagonalizable $A=PDP^{-1}$ | $Pe^{Dt}P^{-1}$ |
| nilpotent $N^2=0$ | $I+Nt$ |
| $\begin{pmatrix}\lambda&1\\0&\lambda\end{pmatrix}$ | $e^{\lambda t}\begin{pmatrix}1&t\\0&1\end{pmatrix}$ |
| $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ | $\begin{pmatrix}\cos t&\sin t\\-\sin t&\cos t\end{pmatrix}$ |

> **Must-know facts**
> 1. $\det e^{A}=e^{\operatorname{tr}A}$; $e^{At}$ is always invertible with inverse $e^{-At}$.
> 2. $e^{A+B}=e^Ae^B$ **only if** $AB=BA$.
> 3. Eigenvalue $\lambda$ of $A$ ⇒ eigenvalue $e^{\lambda t}$ of $e^{At}$.
> 4. A **fundamental matrix** $\Phi(t)$ has $n$ independent solutions as columns; $e^{At}$ is the one with $\Phi(0)=I$. The solution space has dimension $n$.
> 5. Inhomogeneous $y'=Ay+g(t)$: $y(t)=e^{At}y_0+\int_0^te^{A(t-s)}g(s)\,ds$ (variation of constants).

### Eigenvector method
If $Av_i=\lambda_iv_i$ with $n$ independent eigenvectors: $y(t)=C_1e^{\lambda_1t}v_1+\dots+C_ne^{\lambda_nt}v_n$.

**Example.** $A=\begin{pmatrix}1&2\\2&1\end{pmatrix}$, $y(0)=\binom20$.
1. $\operatorname{tr}A=2$, $\det A=-3$: $\lambda^2-2\lambda-3=0$ ⇒ $\lambda=3,-1$.
2. $v_1=\binom11$, $v_2=\binom1{-1}$.
3. $C_1+C_2=2$, $C_1-C_2=0$ ⇒ $C_1=C_2=1$: $y=e^{3t}\binom11+e^{-t}\binom1{-1}$.

Complex eigenvalues $\alpha\pm i\beta$ give real solutions $e^{\alpha t}(\cos\beta t,\ \sin\beta t)$-combinations.

### Order $n$ → system
$y''+py'+qy=0$ with $x_1=y$, $x_2=y'$: $x'=\begin{pmatrix}0&1\\-q&-p\end{pmatrix}x$. Eigenvalues = roots of $r^2+pr+q$.

### Stability of the origin (short)
| Eigenvalues of $A$ | Behaviour |
|---|---|
| all $\operatorname{Re}\lambda<0$ | asymptotically stable (all solutions $\to0$) |
| some $\operatorname{Re}\lambda>0$ | unstable |
| $2\times2$, $\det A<0$ | saddle (unstable) |
| $2\times2$, $\operatorname{tr}A=0$, $\det A>0$ | center (stable, not asymptotically) |

$2\times2$ shortcut: asymptotically stable ⇔ $\operatorname{tr}A<0$ and $\det A>0$. More → [10-mathematical-modelling.md](10-mathematical-modelling.md).

> **Trap:** $e^{At}$ is **not** the matrix of entries $e^{a_{ij}t}$ (only for diagonal $A$).

---

## 8. Classical PDEs and their classification 🟢

A **PDE** contains partial derivatives of $u(x,y)$ or $u(x,t)$: $u_x=\frac{\partial u}{\partial x}$, $u_{xx}$, $u_{xy}$, …

### The classical equations (official example 1)
| Name | Equation | Type | Describes | Data |
|---|---|---|---|---|
| **Laplace** | $\Delta u=u_{xx}+u_{yy}=0$ | elliptic | steady state | boundary values |
| **Poisson** | $\Delta u=f$ | elliptic | steady state with source | boundary values |
| **Heat / diffusion** | $u_t=k\,u_{xx}$ | parabolic | diffusion, smoothing | $u(x,0)$ + boundary |
| **Wave** | $u_{tt}=c^2u_{xx}$ | hyperbolic | vibrations, speed $c$ | $u(x,0)$ **and** $u_t(x,0)$ + boundary |
| **Transport** | $u_t+cu_x=0$ | first order | shift: $u=f(x-ct)$ | $u(x,0)$ |

Harmonic ($\Delta u=0$): $x^2-y^2$, $xy$, $e^x\sin y$, $\ln(x^2+y^2)$ (away from $0$). Not harmonic: $x^2+y^2$ ($\Delta=4$).

### Classification (second order, two variables)
$$Au_{xx}+Bu_{xy}+Cu_{yy}+(\text{lower-order terms})=G.$$
| $B^2-4AC$ | Type |
|---|---|
| $<0$ | elliptic |
| $=0$ | parabolic |
| $>0$ | hyperbolic |

**Recipe:** read $A$ ($u_{xx}$), $B$ ($u_{xy}$), $C$ ($u_{yy}$); ignore $u_x,u_y,u$.
- $u_{xx}+4u_{xy}+3u_{yy}=0$: $16-12>0$ → hyperbolic.
- $u_{xx}+2u_{xy}+u_{yy}=0$: $0$ → parabolic.
- $u_{xx}+u_{xy}+u_{yy}=0$: $-3$ → elliptic.
- Heat $u_t-u_{xx}=0$: no $u_{tt}$, no $u_{xt}$ → $0$ → parabolic.

> **Must-know facts**
> 1. With $x,y$-dependent coefficients the type can change from point to point. **Tricomi** $yu_{xx}+u_{yy}=0$: $B^2-4AC=-4y$ → elliptic for $y>0$, hyperbolic for $y<0$.
> 2. More variables: look at the symmetric coefficient matrix of the second-order terms — all eigenvalues same sign: elliptic; one zero eigenvalue: parabolic; one of opposite sign: hyperbolic.
> 3. **Maximum principle:** harmonic functions and heat-equation solutions take max/min on the boundary (wave: no maximum principle).
> 4. Heat spreads with infinite speed and smooths; waves travel with finite speed $c$ and do not smooth.
> 5. **d'Alembert** (wave on $\mathbb R$, $u(x,0)=f$, $u_t(x,0)=0$): $u=\frac{f(x+ct)+f(x-ct)}2$.

> **Trap:** first-order terms never change the type; heat has only $u_t$ (first order in $t$) ⇒ parabolic.

---

## 9. Separation of variables and Fourier series 🟢

**Idea.** Try $u(x,t)=X(x)T(t)$. The PDE splits into two ODEs linked by a constant $-\lambda$. The boundary conditions allow only special $\lambda_n$ (eigenvalues) with eigenfunctions $X_n$ (sines/cosines). Superpose them; the initial data fixes the coefficients through a **Fourier series**.

### Heat equation, ends held at $0$
$u_t=ku_{xx}$ on $0<x<L$, $u(0,t)=u(L,t)=0$, $u(x,0)=f(x)$.
1. $XT'=kX''T$ ⇒ $\frac{T'}{kT}=\frac{X''}{X}=-\lambda$.
2. $X''+\lambda X=0$, $X(0)=X(L)=0$ ⇒ $\lambda_n=\left(\frac{n\pi}L\right)^2$, $X_n=\sin\frac{n\pi x}L$, $n=1,2,\dots$
3. $T'=-k\lambda_nT$ ⇒ $T_n=e^{-k(n\pi/L)^2t}$.
4. Superpose:
$$u(x,t)=\sum_{n\ge1}b_n\,e^{-k(n\pi/L)^2t}\sin\frac{n\pi x}L,\qquad b_n=\frac2L\int_0^Lf(x)\sin\frac{n\pi x}L\,dx$$
($b_n$ = coefficients of the **Fourier sine series** of $f$).

**Worked example.** $L=\pi$, $k=1$, $u(x,0)=3\sin x-\sin4x$.
1. Already a sine series: $b_1=3$, $b_4=-1$.
2. $u(x,t)=3e^{-t}\sin x-e^{-16t}\sin4x$.
3. Higher modes die faster; $u\to0$ as $t\to\infty$.

### Variations
| Problem | Eigenfunctions | Time / $y$ part |
|---|---|---|
| Heat, insulated ends $u_x=0$ | $\cos\frac{n\pi x}L$, $n\ge0$ | $e^{-k(n\pi/L)^2t}$; $u\to$ mean of $f$ |
| Wave, fixed ends | $\sin\frac{n\pi x}L$ | $a_n\cos\frac{cn\pi t}L+b_n\sin\frac{cn\pi t}L$ (no decay) |
| Laplace on a rectangle $[0,a]\times[0,b]$, data on one side | $\sin\frac{n\pi x}a$ | $\sinh\frac{n\pi y}a$ |

**Wave example.** $u_{tt}=u_{xx}$ on $(0,\pi)$, fixed ends, $u(x,0)=\sin x$, $u_t(x,0)=0$ ⇒ $u=\cos t\,\sin x$.

> **Must-know facts**
> 1. Works for **linear homogeneous** PDEs with homogeneous boundary conditions on simple domains (intervals, rectangles, discs).
> 2. The eigenfunctions $\sin\frac{n\pi x}L$ are **orthogonal** on $[0,L]$; this is why the coefficients are Fourier coefficients.
> 3. Inhomogeneous boundary values (e.g. $u(0)=T_1$, $u(L)=T_2$): first subtract the steady state (linear function), then separate.

> **Trap:** heat modes decay like $e^{-n^2t}$ (no oscillation in time); wave modes oscillate like $\cos(nt)$ (no decay).

---

## Formula sheet

| Topic | Form | Result |
|---|---|---|
| Exponential | $y'=ky$ | $y=y(0)e^{kt}$ |
| Separable | $y'=g(t)h(y)$ | $\int\frac{dy}{h}=\int g\,dt$; plus $h(y_0)=0$ |
| Linear 1st order | $y'+py=q$ | $\mu=e^{\int p}$, $(\mu y)'=\mu q$ |
| Bernoulli | $y'+py=qy^n$ | $v=y^{1-n}$ ⇒ linear |
| Picard–Lindelöf | $f$ cont. + Lipschitz in $y$ | unique local solution |
| Peano | $f$ continuous | existence only |
| Solution space | linear homog. order $n$ / system in $\mathbb R^n$ | vector space, dim $n$ |
| Inhomogeneous | | affine: $y_p+y_h$ |
| Wronskian | $W\ne0$ at one point | fundamental system |
| Const. coeff. | char. polynomial | $e^{rt}$, $te^{rt}$, $e^{\alpha t}\cos\beta t$, $e^{\alpha t}\sin\beta t$ |
| Resonance | trial solves homog. eq. | multiply by $t$ |
| System | $y'=Ay$, $y(0)=y_0$ | $y=e^{At}y_0$; $=\sum C_ie^{\lambda_it}v_i$ |
| $e^{At}$ | | $Pe^{Dt}P^{-1}$; $\det e^A=e^{\operatorname{tr}A}$ |
| Stability | | all $\operatorname{Re}\lambda<0$; $2\times2$: $\operatorname{tr}<0$, $\det>0$ |
| PDE type | $B^2-4AC$ | $<0$ elliptic, $=0$ parabolic, $>0$ hyperbolic |
| Heat on $[0,L]$ | Dirichlet | $\sum b_ne^{-k(n\pi/L)^2t}\sin\frac{n\pi x}L$ |
| Sine coefficients | | $b_n=\frac2L\int_0^Lf\sin\frac{n\pi x}L$ |

---

## Practice MCQs

**Q1.** (official example 1) The Laplace equation is (subscripts denote partial derivatives)
A) $u_t=u_{xx}$  B) $u_{tt}=u_{xx}$  C) $u_{xx}+u_{yy}=0$  D) $u_{xx}+u_{yy}=f$  E) $u_t=u_x$

<details><summary>Answer</summary>

**C** — A is heat, B is wave, D is Poisson, E is transport.

</details>

**Q2.** (official example 2) $y'=Ay$ with constant $A$ and $y(0)=y_0$ has solutions of the form
A) $y(t)=tA$  B) $y(t)=At$  C) $y(t)=e^{At}y_0$  D) $y(t)=Ay_0$  E) $y(t)=ty_0$

<details><summary>Answer</summary>

**C** — $\frac d{dt}e^{At}y_0=Ae^{At}y_0$ and $e^{0}=I$.

</details>

**Q3.** The ODE $y''+3y'=t^2$ is
A) first order, linear  B) second order, linear  C) second order, nonlinear  D) third order, linear  E) second order, homogeneous

<details><summary>Answer</summary>

**B** — Highest derivative $y''$; $y',y''$ appear linearly. $t^2\ne0$, so it is inhomogeneous (E wrong).

</details>

**Q4.** Which function solves $y'=3y$, $y(0)=5$?
A) $3e^{5t}$  B) $5e^t$  C) $e^{3t}+4$  D) $5e^{3t}$  E) $15e^{3t}$

<details><summary>Answer</summary>

**D** — $y=y(0)e^{kt}$. C has the right initial value but $y'=3e^{3t}\ne3y$.

</details>

**Q5.** The solution of $y'=y+t$, $y(0)=1$ is
A) $2e^t-t-1$  B) $e^t+t$  C) $e^t-t$  D) $2e^t+t-1$  E) $e^{t}+t^2$

<details><summary>Answer</summary>

**A** — $y'=2e^t-1=y+t$ ✓ and $y(0)=1$ ✓.

</details>

**Q6.** The integrating factor for $y'+2y=e^t$ is
A) $e^{-2t}$  B) $e^{2t}$  C) $e^t$  D) $2t$  E) $e^{t^2}$

<details><summary>Answer</summary>

**B** — $p=2$, $\mu=e^{\int2\,dt}$.

</details>

**Q7.** The solution of $y'=2ty$, $y(0)=3$ is
A) $3e^{2t}$  B) $e^{t^2}+2$  C) $3e^{t^2}$  D) $3t^2$  E) $3e^{-t^2}$

<details><summary>Answer</summary>

**C** — Separable: $y=Ke^{t^2}$, $K=3$.

</details>

**Q8.** Which substitution turns $y'+y=t\,y^3$ into a linear equation?
A) $v=y^3$  B) $v=y^2$  C) $v=y^{-2}$  D) $v=y^{-3}$  E) $v=\ln y$

<details><summary>Answer</summary>

**C** — Bernoulli, $n=3$: $v=y^{1-n}=y^{-2}$.

</details>

**Q9.** For the IVP $y'=\sqrt y$, $y(0)=0$ ($y\ge0$):
A) $y\equiv0$ is the only solution  B) there is no solution  C) there is more than one solution  D) the solution blows up at $t=1$  E) the solution is $e^t$

<details><summary>Answer</summary>

**C** — $y\equiv0$ and $y=\frac{t^2}4$. $\sqrt y$ is not Lipschitz at $0$.

</details>

**Q10.** The Picard–Lindelöf theorem guarantees a unique local solution of $y'=f(t,y)$, $y(t_0)=y_0$ if
A) $f$ is continuous  B) $f$ is continuous and Lipschitz in $y$  C) $f$ is bounded  D) $f$ is linear in $t$  E) $f$ is a polynomial in $t$

<details><summary>Answer</summary>

**B** — Continuity alone (A) gives only existence (Peano).

</details>

**Q11.** The solution of $y'=y^2$, $y(0)=1$ exists
A) for all $t\in\mathbb R$  B) only for $t<1$ (it blows up at $t=1$)  C) only for $t>0$  D) nowhere  E) only for $\lvert t\rvert<\frac12$

<details><summary>Answer</summary>

**B** — $y=\frac1{1-t}$. Smooth $f$ ⇒ unique, but only local existence.

</details>

**Q12.** The dimension of the solution space of $y'''+y'=0$ is
A) $1$  B) $2$  C) $3$  D) $4$  E) infinite

<details><summary>Answer</summary>

**C** — Linear homogeneous of order 3. Basis: $1,\cos t,\sin t$ ($r^3+r=0$).

</details>

**Q13.** The set of all solutions of $y''+y=t$ is
A) a 2-dimensional vector space  B) a 2-dimensional affine space (not a vector space)  C) a single function  D) a 1-dimensional vector space  E) empty

<details><summary>Answer</summary>

**B** — $t+C_1\cos t+C_2\sin t$: a particular solution plus a 2-dim vector space. $0$ is not a solution.

</details>

**Q14.** The Wronskian of $e^t$ and $e^{2t}$ is
A) $0$  B) $e^{3t}$  C) $e^{2t}$  D) $-e^{3t}$  E) $3e^{3t}$

<details><summary>Answer</summary>

**B** — $e^t\cdot2e^{2t}-e^t\cdot e^{2t}=e^{3t}\ne0$ ⇒ independent.

</details>

**Q15.** The general solution of $y''-5y'+6y=0$ is
A) $C_1e^{2t}+C_2e^{3t}$  B) $C_1e^{-2t}+C_2e^{-3t}$  C) $C_1\cos2t+C_2\sin3t$  D) $(C_1+C_2t)e^{5t}$  E) $C_1e^{6t}+C_2e^{-t}$

<details><summary>Answer</summary>

**A** — $(r-2)(r-3)=0$.

</details>

**Q16.** The general solution of $y''+4y=0$ is
A) $C_1e^{2t}+C_2e^{-2t}$  B) $C_1\cos2t+C_2\sin2t$  C) $C_1\cos4t+C_2\sin4t$  D) $(C_1+C_2t)e^{2t}$  E) $C_1+C_2t$

<details><summary>Answer</summary>

**B** — $r=\pm2i$. Trap C: $\beta=\sqrt4=2$.

</details>

**Q17.** The general solution of $y''-4y'+4y=0$ is
A) $C_1e^{2t}+C_2e^{-2t}$  B) $C_1e^{4t}+C_2$  C) $e^{2t}(C_1\cos t+C_2\sin t)$  D) $(C_1+C_2t)e^{2t}$  E) $C_1e^{2t}$

<details><summary>Answer</summary>

**D** — Double root $r=2$. E has only one constant.

</details>

**Q18.** For $y''-3y'+2y=e^t$ the correct trial function for $y_p$ is
A) $Ae^t$  B) $Ate^t$  C) $At^2e^t$  D) $Ae^{2t}$  E) $A$

<details><summary>Answer</summary>

**B** — $r=1$ is a simple root: resonance, multiply by $t$.

</details>

**Q19.** For $A=\begin{pmatrix}1&0\\0&2\end{pmatrix}$, $e^{At}=$
A) $\begin{pmatrix}e^t&0\\0&e^{2t}\end{pmatrix}$  B) $\begin{pmatrix}e^t&1\\1&e^{2t}\end{pmatrix}$  C) $\begin{pmatrix}t&0\\0&2t\end{pmatrix}$  D) $e^{3t}I$  E) $\begin{pmatrix}1&0\\0&2\end{pmatrix}e^t$

<details><summary>Answer</summary>

**A** — Diagonal: exponentiate the diagonal. Off-diagonal zeros stay $0$ (B wrong: $e^{0\cdot t}$ appears only on the diagonal).

</details>

**Q20.** For $N=\begin{pmatrix}0&1\\0&0\end{pmatrix}$, $e^{Nt}=$
A) $\begin{pmatrix}1&e^t\\0&1\end{pmatrix}$  B) $\begin{pmatrix}1&t\\0&1\end{pmatrix}$  C) $\begin{pmatrix}0&t\\0&0\end{pmatrix}$  D) $\begin{pmatrix}1&1\\1&1\end{pmatrix}$  E) $\begin{pmatrix}e^t&t\\0&e^t\end{pmatrix}$

<details><summary>Answer</summary>

**B** — $N^2=0$, so the series stops: $I+Nt$.

</details>

**Q21.** If $\operatorname{tr}A=3$, then $\det e^{A}=$
A) $3$  B) $e^3$  C) $1$  D) $3e$  E) $e^{\det A}$

<details><summary>Answer</summary>

**B** — $\det e^A=e^{\operatorname{tr}A}$ (eigenvalues $e^{\lambda_i}$, product $e^{\sum\lambda_i}$).

</details>

**Q22.** The solution space of $y'=Ay$, $A\in\mathbb R^{3\times3}$, has dimension
A) $1$  B) $3$  C) $6$  D) $9$  E) depends on the eigenvalues

<details><summary>Answer</summary>

**B** — Always $n$, independent of the eigenvalues (columns of $e^{At}$).

</details>

**Q23.** The origin of $y'=\begin{pmatrix}1&2\\2&1\end{pmatrix}y$ is
A) a stable node  B) a saddle  C) an unstable spiral  D) a center  E) a stable spiral

<details><summary>Answer</summary>

**B** — $\det=-3<0$; eigenvalues $3,-1$.

</details>

**Q24.** The heat equation $u_t=u_{xx}$ is
A) elliptic  B) hyperbolic  C) parabolic  D) first order  E) nonlinear

<details><summary>Answer</summary>

**C** — $A=1$, $B=C=0$ ⇒ $B^2-4AC=0$.

</details>

**Q25.** The PDE $u_{xx}+4u_{xy}+3u_{yy}=0$ is
A) hyperbolic  B) parabolic  C) elliptic  D) elliptic only for $x>0$  E) not linear

<details><summary>Answer</summary>

**A** — $16-12=4>0$.

</details>

**Q26.** Which function is harmonic?
A) $x^2+y^2$  B) $x^2-y^2$  C) $x^3$  D) $e^x\cos x$  E) $x^2y$

<details><summary>Answer</summary>

**B** — $2+(-2)=0$. A: $4$; C: $6x$; E: $2y$.

</details>

**Q27.** Which equation needs two initial conditions $u(x,0)$ and $u_t(x,0)$?
A) Laplace  B) heat  C) Poisson  D) wave  E) transport

<details><summary>Answer</summary>

**D** — Second order in $t$.

</details>

**Q28.** Separation of variables for $u_t=u_{xx}$ on $(0,\pi)$ with $u(0,t)=u(\pi,t)=0$ gives the eigenfunctions
A) $\cos nx$, $n\ge0$  B) $\sin nx$, $n\ge1$  C) $e^{nx}$  D) $x^n$  E) $\sin\frac{nx}2$

<details><summary>Answer</summary>

**B** — $X''+\lambda X=0$, $X(0)=X(\pi)=0$ ⇒ $\lambda=n^2$, $X=\sin nx$. Cosines belong to insulated ends ($u_x=0$).

</details>

**Q29.** The solution of $u_t=u_{xx}$ on $(0,\pi)$, $u=0$ at the ends, $u(x,0)=\sin x$ is
A) $\cos t\sin x$  B) $e^t\sin x$  C) $e^{-t}\sin x$  D) $e^{-t^2}\sin x$  E) $\sin(x-t)$

<details><summary>Answer</summary>

**C** — $T'=-T$. A would solve the wave equation.

</details>

**Q30.** Same problem with $u(x,0)=3\sin x-\sin4x$. Then $u(x,t)=$
A) $3e^{-t}\sin x-e^{-4t}\sin4x$  B) $3e^{-t}\sin x-e^{-16t}\sin4x$  C) $e^{-t}(3\sin x-\sin4x)$  D) $3\cos t\sin x-\cos4t\sin4x$  E) $3e^{-t}\sin x+e^{-16t}\sin4x$

<details><summary>Answer</summary>

**B** — Mode $n$ decays like $e^{-n^2t}$; $n=4$ gives $e^{-16t}$.

</details>
