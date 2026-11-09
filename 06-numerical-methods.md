# 6. Numerical Methods

> **Official topics (Placement Test guide):** Gaussian elimination and condition numbers; matrix factorizations; pseudo-inverse and least squares; eigenvalues; root finding; floating-point arithmetic; interpolation and numerical integration; explicit and implicit methods.
>
> **Exam:** 7 questions on this topic, 5 options each, about 85 seconds per question. Typical: recognize a factorization or formula, do one iteration step, know an order of convergence or an error rate.
>
> **How to study this file:** every section is 🟢 (all are on the official list). Each has a small hand calculation (2×2 matrices, 1–2 steps). Time: about 5 hours + 1 hour for the MCQs.
>
> *Removed (not on the official list, or covered elsewhere):* Jacobi / Gauss–Seidel iterations, rank and structure of the solution space (→ [02-algebra.md](02-algebra.md), section 2). Numerical differentiation is now a small part of section 10.

## Contents
🟢 1. Gaussian elimination and pivoting · 2. Matrix factorizations: LU, Cholesky, QR, SVD · 3. Norms and condition number · 4. Least squares and the pseudo-inverse · 5. Eigenvalues · 6. Root finding · 7. Floating-point arithmetic · 8. Polynomial interpolation · 9. Numerical integration · 10. Explicit and implicit methods for ODEs
📋 Formula sheet · Practice MCQs (31 questions, 5 options)

---

## 1. Gaussian elimination and pivoting 🟢

**Idea.** Solve $Ax=b$ by row operations: make $A$ upper triangular, then solve from the bottom up (**back substitution**).

**Worked example.** $x+y=3$, $2x+3y=8$.
1. $\left(\begin{array}{cc|c}1&1&3\\2&3&8\end{array}\right)$, Row 2 − 2·Row 1: $\left(\begin{array}{cc|c}1&1&3\\0&1&2\end{array}\right)$.
2. Back substitution: $y=2$, $x=1$.

**Pivoting.** The pivot is the diagonal entry we divide by.
- A pivot $0$ ⇒ elimination breaks down: swap rows.
- A **tiny** pivot ⇒ huge multipliers ⇒ rounding errors blow up.
- **Partial pivoting:** before each step, swap in the row with the largest $\lvert a_{ik}\rvert$ in the current column. Then all multipliers satisfy $\lvert l_{ik}\rvert\le1$. This makes Gaussian elimination stable in practice.

**Example.** $\begin{pmatrix}10^{-20}&1\\1&1\end{pmatrix}x=\binom12$ in double precision: without pivoting you get $x_1=0$ (wrong; true $x_1\approx1$); with a row swap you get the correct answer.

**Cost** ($n\times n$, leading term):

| Task | Cost |
|---|---|
| Gaussian elimination / LU | $\frac23n^3$ |
| Cholesky | $\frac13n^3$ |
| forward / back substitution | $n^2$ |
| tridiagonal system | $O(n)$ |
| matrix × vector | $2n^2$ |

Never compute $A^{-1}$ to solve $Ax=b$ — it is more expensive and less accurate than LU.

> **Trap:** partial pivoting is about **stability** (rounding errors); it does not change the exact solution.

---

## 2. Matrix factorizations: LU, Cholesky, QR, SVD 🟢

### Overview (official example 1)
| Factorization | Form | Exists for | Used for |
|---|---|---|---|
| **LU** | $A=LU$ ($PA=LU$ with pivoting) | every invertible $A$ (with $P$) | linear systems, $\det A=\pm\prod u_{ii}$ |
| **Cholesky** | $A=LL^T$, $L$ lower triangular, positive diagonal | **symmetric positive definite** $A$ | SPD systems, half the cost |
| **QR** | $A=QR$, $Q$ orthogonal, $R$ upper triangular | **every** $A$ | least squares, QR algorithm |
| **SVD** | $A=U\Sigma V^T$, $U,V$ orthogonal, $\Sigma$ diagonal $\ge0$ | **every** $A$ (also non-square) | rank, pseudo-inverse, $\lVert A\rVert_2$, $\kappa_2$ |
| **Eigen-decomposition** | $A=PDP^{-1}$ | **diagonalizable** $A$ only | powers, $e^{At}$ |
| **Spectral** | $A=Q\Lambda Q^T$ | real symmetric $A$ | |

### LU
$L$ = lower triangular with $1$s on the diagonal and the **multipliers** below; $U$ = result of elimination. Solve $Ly=b$ (forward), then $Ux=y$ (backward).

**Example.** $A=\begin{pmatrix}2&1\\4&5\end{pmatrix}$: $l_{21}=2$, Row 2 − 2·Row 1 $=(0,3)$.
$L=\begin{pmatrix}1&0\\2&1\end{pmatrix}$, $U=\begin{pmatrix}2&1\\0&3\end{pmatrix}$, $\det A=6$.
$\begin{pmatrix}0&1\\1&0\end{pmatrix}$ is invertible but has no LU without a row swap.

### Cholesky
SPD = $A=A^T$ and $x^TAx>0$ for $x\ne0$ ⇔ all eigenvalues $>0$ ⇔ all leading minors $>0$ (Sylvester).
$2\times2$: $A=\begin{pmatrix}a&b\\b&c\end{pmatrix}$ ⇒ $l_{11}=\sqrt a$, $l_{21}=\frac b{l_{11}}$, $l_{22}=\sqrt{c-l_{21}^2}$.
**Example.** $\begin{pmatrix}4&2\\2&5\end{pmatrix}$: $L=\begin{pmatrix}2&0\\1&2\end{pmatrix}$.

### QR
$Q^TQ=I$ (orthonormal columns), $R$ upper triangular. Computed by Gram–Schmidt (columns of $Q$ = orthonormalized columns of $A$), Householder reflections or Givens rotations (both numerically stable).
**Example.** $A=\begin{pmatrix}3&1\\4&2\end{pmatrix}$: $q_1=\frac15(3,4)$, $r_{11}=5$; $r_{12}=q_1\cdot(1,2)=\frac{11}5$; $(1,2)-\frac{11}5q_1=\frac1{25}(-8,6)$, length $\frac25$ ⇒ $r_{22}=\frac25$, $q_2=\frac15(-4,3)$.

> **Trap:** symmetric is not enough for Cholesky: $\begin{pmatrix}1&2\\2&1\end{pmatrix}$ has $\det=-3<0$.

---

## 3. Norms and condition number 🟢

| Vector norm | Formula | $x=(3,-4)$ |
|---|---|---|
| $\lVert x\rVert_1$ | $\sum\lvert x_i\rvert$ | $7$ |
| $\lVert x\rVert_2$ | $\sqrt{\sum x_i^2}$ | $5$ |
| $\lVert x\rVert_\infty$ | $\max\lvert x_i\rvert$ | $4$ |

| Matrix norm | Compute |
|---|---|
| $\lVert A\rVert_1$ | largest **column** sum of $\lvert a_{ij}\rvert$ |
| $\lVert A\rVert_\infty$ | largest **row** sum |
| $\lVert A\rVert_2$ | $\sigma_{\max}=\sqrt{\lambda_{\max}(A^TA)}$; symmetric: $\max\lvert\lambda_i\rvert$ |

**Condition number** $\kappa(A)=\lVert A\rVert\,\lVert A^{-1}\rVert$:
$$\frac{\lVert\Delta x\rVert}{\lVert x\rVert}\le\kappa(A)\frac{\lVert\Delta b\rVert}{\lVert b\rVert}.$$
- $\kappa\ge1$, $\kappa(I)=1$, $\kappa(cA)=\kappa(A)$, orthogonal $Q$: $\kappa_2(Q)=1$.
- $\kappa_2=\frac{\sigma_{\max}}{\sigma_{\min}}$; symmetric: $\frac{\max\lvert\lambda\rvert}{\min\lvert\lambda\rvert}$; diagonal: $\frac{\max\lvert d_i\rvert}{\min\lvert d_i\rvert}$.
- You lose about $\log_{10}\kappa$ correct digits. Singular $A$: $\kappa=\infty$.
- Condition = property of the **problem**; stability = property of the **algorithm**.

**Example.** $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$: $\lVert A\rVert_\infty=7$, $A^{-1}=\begin{pmatrix}-2&1\\1.5&-0.5\end{pmatrix}$, $\lVert A^{-1}\rVert_\infty=3$, $\kappa_\infty=21$.

> **Trap:** small $\det$ ≠ ill-conditioned: $0.1\,I_{10}$ has $\det=10^{-10}$ but $\kappa=1$.

---

## 4. Least squares and the pseudo-inverse 🟢

**Problem.** $A$ is $m\times n$, $m>n$ (more equations than unknowns). Minimize $\lVert Ax-b\rVert_2$.

**Normal equations:** $A^TAx=A^Tb$. Unique solution ⇔ columns of $A$ independent. The residual $b-Ax$ is orthogonal to the column space of $A$.

**Example (line $y=c+mx$ through $(0,1),(1,3),(2,4)$).**
1. $A=\begin{pmatrix}1&0\\1&1\\1&2\end{pmatrix}$, $b=(1,3,4)^T$.
2. $A^TA=\begin{pmatrix}3&3\\3&5\end{pmatrix}$, $A^Tb=\binom8{11}$.
3. $2m=3$ ⇒ $m=\frac32$, $c=\frac76$.

Fitting a constant: $c$ = mean of the data.

**Three ways to solve**
| Method | How | Comment |
|---|---|---|
| Normal equations | Cholesky on $A^TA$ | fast, but $\kappa(A^TA)=\kappa(A)^2$ |
| QR | $A=QR$ ⇒ $Rx=Q^Tb$ | stable, standard |
| SVD | $x=A^+b$ | most robust, handles rank deficiency |

### SVD and pseudo-inverse
$A=U\Sigma V^T$, singular values $\sigma_1\ge\sigma_2\ge\dots\ge0$.

> **Must-know facts**
> 1. $\sigma_i=\sqrt{\lambda_i(A^TA)}$ (eigenvalues of $A^TA$, not of $A$). Symmetric $A$: $\sigma_i=\lvert\lambda_i\rvert$.
> 2. $\operatorname{rank}A$ = number of $\sigma_i>0$; $\lVert A\rVert_2=\sigma_1$; $\kappa_2=\sigma_1/\sigma_n$.
> 3. **Moore–Penrose pseudo-inverse:** $A^+=V\Sigma^+U^T$, $\Sigma^+$ has $\frac1{\sigma_i}$ for $\sigma_i>0$, else $0$ (transposed shape).
> 4. Independent columns: $A^+=(A^TA)^{-1}A^T$. Invertible: $A^+=A^{-1}$.
> 5. $x=A^+b$ is the least-squares solution with **minimal norm**.
> 6. Penrose conditions: $AA^+A=A$, $A^+AA^+=A^+$, $AA^+$ and $A^+A$ symmetric.
> 7. **Best rank-$k$ approximation** (Eckart–Young): keep the $k$ largest $\sigma_i$.

**Example.** $a=\binom11$: $a^+=\frac{a^T}{a^Ta}=\frac12(1\ \ 1)$.

> **Trap:** singular values are never negative.

---

## 5. Eigenvalues 🟢

Basics: $\sum\lambda_i=\operatorname{tr}A$, $\prod\lambda_i=\det A$; triangular ⇒ diagonal entries; $A^{-1}$: $\frac1\lambda$; $A-\mu I$: $\lambda-\mu$. Computing roots of the characteristic polynomial is **not** used numerically (unstable); iterative methods are.

### Gershgorin circles
Every eigenvalue lies in some disc $\lvert z-a_{ii}\rvert\le R_i=\sum_{j\ne i}\lvert a_{ij}\rvert$. A group of $k$ discs separated from the rest contains exactly $k$ eigenvalues.
**Example.** $\begin{pmatrix}5&1\\2&-3\end{pmatrix}$: discs $\lvert z-5\rvert\le1$, $\lvert z+3\rvert\le2$ — separate, one eigenvalue each; $0$ in no disc ⇒ invertible.

### Power method
$x_{k+1}=\frac{Ax_k}{\lVert Ax_k\rVert}$, eigenvalue estimate $\frac{x_k^TAx_k}{x_k^Tx_k}$ (Rayleigh quotient).
- Converges to the eigenvalue of **largest $\lvert\lambda\rvert$**, rate $\left\lvert\frac{\lambda_2}{\lambda_1}\right\rvert$ per step; needs $\lvert\lambda_1\rvert>\lvert\lambda_2\rvert$.
- **Example.** $\begin{pmatrix}2&1\\1&2\end{pmatrix}$ (eigenvalues $3,1$), $x_0=(1,0)$: $(2,1)$, $(5,4)$, $(14,13)$ → direction $(1,1)$, rate $\frac13$.

### Inverse iteration and the QR algorithm
> 1. **Inverse iteration** (power method with $A^{-1}$): smallest $\lvert\lambda\rvert$.
> 2. **Shifted** with $(A-\mu I)^{-1}$: eigenvalue **closest to $\mu$** (eigenvalues $1,4,7$, $\mu=5$ → $4$). Each step solves a linear system (LU once).
> 3. **QR algorithm:** $A_k=Q_kR_k$, $A_{k+1}=R_kQ_k=Q_k^TA_kQ_k$ — similar, same eigenvalues. $A_k$ → upper triangular (Schur form); **all** eigenvalues on the diagonal.
> 4. In practice: reduce to Hessenberg (tridiagonal if symmetric) form first, use shifts; cost $O(n^3)$.

> **Trap:** for the power-method rate use the two largest **absolute values**: eigenvalues $6,-3,2$ ⇒ rate $\frac36=\frac12$.

---

## 6. Root finding 🟢

Goal: $f(x^*)=0$.

### Bisection
$f(a)f(b)<0$ ⇒ root in $[a,b]$. Take the midpoint, keep the half with the sign change.
Length after $n$ steps: $\frac{b-a}{2^n}$. Always converges (continuous $f$), order 1.
$[0,1]$ to accuracy $10^{-3}$: $2^{10}=1024$ ⇒ $10$ steps.

### Fixed-point iteration
$x=g(x)$, $x_{k+1}=g(x_k)$. **Banach:** $g$ contraction ($\lvert g'\rvert\le q<1$ near $x^*$) ⇒ converges, error × $\lvert g'(x^*)\rvert$ per step.
The limit is a fixed point of $g$ — check that it is the root you want!

### Newton's method
$$x_{k+1}=x_k-\frac{f(x_k)}{f'(x_k)}\quad(\text{zero of the tangent line}).$$
**Official example 2:** $x^2=2$: $f=x^2-2$ ⇒ $x_{k+1}=x_k-\frac{x_k^2-2}{2x_k}=\frac{x_k}2+\frac1{x_k}$.
- $x_{k+1}=x_k+\frac{x_k^2-2}{2x_k}$ (wrong sign) moves **away** from $\sqrt2$.
- $x_{k+1}=\frac2{x_k}+\frac{x_k}2$ is a fixed-point iteration whose fixed point satisfies $\frac x2=\frac2x$, i.e. $x=2$ — it converges to $2$, not $\sqrt2$.

**Example.** $x_0=1$: $x_1=1.5$, $x_2=1.41\overline6$ (true $1.41421$). General: $\sqrt a$: $x_{k+1}=\frac12\left(x_k+\frac a{x_k}\right)$.

**Secant method:** replace $f'(x_k)$ by $\frac{f(x_k)-f(x_{k-1})}{x_k-x_{k-1}}$; no derivative needed.

### Order of convergence
$\lvert e_{k+1}\rvert\approx C\lvert e_k\rvert^p$.

| Method | Order |
|---|---|
| bisection, fixed point ($g'(x^*)\ne0$) | 1 (linear) |
| secant | $\frac{1+\sqrt5}2\approx1.618$ |
| Newton, simple root | 2 (correct digits double) |
| Newton, double root | 1 (error × $\frac12$) |

> **Trap:** Newton converges fast only near the root and fails if $f'(x_k)=0$; bisection is slow but safe.

---

## 7. Floating-point arithmetic 🟢

A float is $x=\pm(1.d_1d_2\dots d_t)_2\cdot2^e$ with $t$ stored mantissa bits and a bounded exponent.

- **Machine epsilon** $\varepsilon$: gap between $1$ and the next float, $\varepsilon=2^{-t}$.
- Rounding: $\mathrm{fl}(x)=x(1+\delta)$, $\lvert\delta\rvert\le u=\frac\varepsilon2$ (unit roundoff) — small **relative** error.
- Each operation: $\mathrm{fl}(a\circ b)=(a\circ b)(1+\delta)$.

| IEEE 754 | Bits | Mantissa bits | $\varepsilon$ | Digits |
|---|---|---|---|---|
| single | 32 | 23 | $2^{-23}\approx1.2\cdot10^{-7}$ | ~7 |
| double | 64 | 52 | $2^{-52}\approx2.2\cdot10^{-16}$ | ~16 |

**Typical problems**
- **Cancellation:** subtracting nearly equal numbers loses digits. Fix by rewriting: $\sqrt{x+1}-\sqrt x=\frac1{\sqrt{x+1}+\sqrt x}$; $1-\cos x=2\sin^2\frac x2$.
- **Absorption:** $1+10^{-17}=1$ in double.
- Addition is **not associative**; $0.1$ is not exact in binary.
- **Overflow / underflow:** too large / too close to $0$; special values $\pm\infty$, NaN.
- Floats are **not** equally spaced: the gap grows with $\lvert x\rvert$ (relative spacing is constant).

**Toy system.** Base 2, mantissa $1.d_1d_2$, $e\in\{-1,0,1\}$: $4$ mantissas × $3$ exponents × $2$ signs $+1$ (zero) $=25$ numbers; $\varepsilon=\frac14$; largest $1.11_2\cdot2=3.5$.

> **Trap:** some books call $u=2^{-53}$ the machine epsilon. Read the definition in the question.

---

## 8. Polynomial interpolation 🟢

**Problem.** Given $n+1$ points $(x_0,y_0),\dots,(x_n,y_n)$ with **distinct** $x_i$, find a polynomial $p$ with $p(x_i)=y_i$.

**Theorem.** There is **exactly one** such $p$ of degree $\le n$. (Vandermonde matrix is invertible for distinct nodes.)

### Lagrange form
$$p(x)=\sum_{i=0}^ny_iL_i(x),\qquad L_i(x)=\prod_{j\ne i}\frac{x-x_j}{x_i-x_j},\qquad L_i(x_j)=\delta_{ij}.$$

### Newton form (divided differences)
$f[x_i]=y_i$, $f[x_i,x_{i+1}]=\frac{y_{i+1}-y_i}{x_{i+1}-x_i}$, $f[x_0,x_1,x_2]=\frac{f[x_1,x_2]-f[x_0,x_1]}{x_2-x_0}$, …
$$p(x)=f[x_0]+f[x_0,x_1](x-x_0)+f[x_0,x_1,x_2](x-x_0)(x-x_1)+\dots$$
Adding a new point adds one new term (Lagrange would need all $L_i$ again).

**Worked example.** Points $(0,1),(1,3),(2,7)$.
1. $f[0,1]=2$, $f[1,2]=4$, $f[0,1,2]=\frac{4-2}{2}=1$.
2. $p(x)=1+2x+1\cdot x(x-1)=x^2+x+1$.
3. Check: $p(0)=1$, $p(1)=3$, $p(2)=7$ ✓.

### Error
$$f(x)-p(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^n(x-x_i).$$
- If $f$ is a polynomial of degree $\le n$, interpolation is **exact**.
- **Runge phenomenon:** high-degree interpolation at **equidistant** nodes can oscillate wildly near the ends (e.g. $f=\frac1{1+25x^2}$ on $[-1,1]$); more nodes make it worse.
- Remedies: **Chebyshev nodes** $x_i=\cos\frac{(2i+1)\pi}{2n+2}$ (clustered at the ends), or **splines**.

### Splines
**Cubic spline:** a cubic polynomial on each subinterval, glued so that $s$, $s'$, $s''$ are continuous ($C^2$). **Natural spline:** $s''=0$ at both ends. Low degree, no Runge oscillation; computing it needs a tridiagonal system ($O(n)$).

> **Trap:** $n+1$ points ⇒ degree **at most $n$** (not $n+1$). Through 3 points: a parabola (or lower if the points happen to be collinear).

---

## 9. Numerical integration 🟢

**Idea (Newton–Cotes).** Replace $f$ by an interpolation polynomial and integrate that exactly.

| Rule on $[a,b]$ | Formula | Interpolant | Exact up to degree | Composite error |
|---|---|---|---|---|
| Midpoint | $(b-a)f\!\left(\frac{a+b}2\right)$ | constant | 1 | $O(h^2)$ |
| Trapezoid | $\frac{b-a}2\big(f(a)+f(b)\big)$ | linear | 1 | $O(h^2)$ |
| Simpson | $\frac{b-a}6\Big(f(a)+4f\!\left(\frac{a+b}2\right)+f(b)\Big)$ | quadratic | **3** | $O(h^4)$ |
| Gauss ($n$ points) | optimal nodes and weights | | $2n-1$ | |

**Composite trapezoid** ($n$ pieces, $h=\frac{b-a}n$): $T=h\left[\frac{f_0}2+f_1+\dots+f_{n-1}+\frac{f_n}2\right]$.

**Worked example.** $\int_0^1x^2dx=\frac13$.
1. Trapezoid, 1 piece: $0.5$ (error $0.1\overline6$).
2. Trapezoid, 2 pieces: $0.5[0+0.25+0.5]=0.375$ (error 4× smaller).
3. Simpson: $\frac16(0+1+1)=\frac13$ exact.

**Halving $h$:** $O(h^2)$ → error ÷4; $O(h^4)$ → ÷16.
**Gauss–Legendre:** 2 points $\pm\frac1{\sqrt3}$ on $[-1,1]$, weights $1$, exact up to degree 3.

> **Trap:** Simpson is exact for cubics too, not only quadratics.

---

## 10. Explicit and implicit methods for ODEs 🟢

IVP $y'=f(t,y)$, $y(t_0)=y_0$; step $h$, $t_k=t_0+kh$, $y_k\approx y(t_k)$.

### Finite differences (from Taylor)
| Formula | Approximates | Error |
|---|---|---|
| $\frac{f(x+h)-f(x)}h$ (forward) | $f'(x)$ | $O(h)$ |
| $\frac{f(x+h)-f(x-h)}{2h}$ (central) | $f'(x)$ | $O(h^2)$ |
| $\frac{f(x+h)-2f(x)+f(x-h)}{h^2}$ | $f''(x)$ | $O(h^2)$ |

### The basic one-step methods
| Method | Formula | Type | Order |
|---|---|---|---|
| **Explicit (forward) Euler** | $y_{k+1}=y_k+hf(t_k,y_k)$ | explicit | 1 |
| **Implicit (backward) Euler** | $y_{k+1}=y_k+hf(t_{k+1},y_{k+1})$ | implicit | 1 |
| **Trapezoidal (Crank–Nicolson)** | $y_{k+1}=y_k+\frac h2\big(f(t_k,y_k)+f(t_{k+1},y_{k+1})\big)$ | implicit | 2 |
| **Heun** (improved Euler) | predictor Euler, then trapezoid with the predicted value | explicit | 2 |
| **Classical Runge–Kutta (RK4)** | 4 evaluations of $f$ per step | explicit | 4 |

- **Explicit:** $y_{k+1}$ is computed directly from known values — cheap per step.
- **Implicit:** $y_{k+1}$ appears on both sides — solve an equation each step (Newton / linear system). More work, but much better stability.
- Order $p$: global error $O(h^p)$, local (one-step) error $O(h^{p+1})$.
- Multistep: Adams–Bashforth (explicit), Adams–Moulton (implicit), BDF (implicit, for stiff problems).

**Worked example.** $y'=y$, $y(0)=1$, $h=0.1$ (exact $y(0.1)=1.10517$).
- Explicit Euler: $y_1=1+0.1\cdot1=1.1$.
- Implicit Euler: $y_1=1+0.1y_1$ ⇒ $y_1=\frac1{0.9}=1.111$.

### Stability: the test equation $y'=\lambda y$, $\lambda<0$
The exact solution decays. Does the numerical one?

| Method | One step | Stable for $\lambda<0$ when |
|---|---|---|
| Explicit Euler | $y_{k+1}=(1+h\lambda)y_k$ | $\lvert1+h\lambda\rvert\le1$ ⇔ $h\le\frac2{\lvert\lambda\rvert}$ |
| Implicit Euler | $y_{k+1}=\frac{1}{1-h\lambda}y_k$ | **every** $h>0$ (A-stable) |
| Trapezoidal | $y_{k+1}=\frac{1+h\lambda/2}{1-h\lambda/2}y_k$ | **every** $h>0$ (A-stable) |

**Stiff example.** $y'=-100y$, $h=0.1$:
- Explicit Euler: factor $1-10=-9$ ⇒ $\lvert y_k\rvert=9^k$ explodes.
- Implicit Euler: factor $\frac1{1+10}=\frac1{11}$ ⇒ decays, like the true solution.

**Stiff problem** = very different time scales (some large negative $\lambda$). Explicit methods need tiny steps; **use implicit methods**.

**Heat equation** $u_t=u_{xx}$ (space step $\Delta x$, time step $\Delta t$): explicit scheme stable only if $\frac{\Delta t}{\Delta x^2}\le\frac12$; Crank–Nicolson and implicit Euler are stable for all $\Delta t$.

> **Trap:** higher order does not mean stable. RK4 is explicit and also has a step-size limit for stiff problems.

---

## Formula sheet

| Topic | Formula / fact |
|---|---|
| Costs | LU $\frac23n^3$, Cholesky $\frac13n^3$, substitution $n^2$ |
| Pivoting | largest $\lvert a_{ik}\rvert$ in column; multipliers $\le1$ |
| LU / Cholesky / QR / SVD | $LU$ / $LL^T$ (SPD) / $QR$ (all $A$) / $U\Sigma V^T$ (all $A$) |
| Cholesky 2×2 | $l_{11}=\sqrt a$, $l_{21}=b/l_{11}$, $l_{22}=\sqrt{c-l_{21}^2}$ |
| Norms | $\lVert A\rVert_1$ max column sum, $\lVert A\rVert_\infty$ max row sum, $\lVert A\rVert_2=\sigma_1$ |
| Condition | $\kappa=\lVert A\rVert\lVert A^{-1}\rVert\ge1$; $\kappa_2=\sigma_1/\sigma_n$ |
| Least squares | $A^TAx=A^Tb$; QR: $Rx=Q^Tb$; $\kappa(A^TA)=\kappa(A)^2$ |
| Pseudo-inverse | $A^+=V\Sigma^+U^T$; full column rank: $(A^TA)^{-1}A^T$ |
| Gershgorin | $\lvert z-a_{ii}\rvert\le\sum_{j\ne i}\lvert a_{ij}\rvert$ |
| Power / inverse / shifted | largest $\lvert\lambda\rvert$ (rate $\lvert\lambda_2/\lambda_1\rvert$) / smallest / closest to $\mu$ |
| Bisection | length $(b-a)/2^n$ |
| Newton | $x_{k+1}=x_k-f(x_k)/f'(x_k)$; order 2 (double root: 1); secant 1.618 |
| Machine eps | double $2^{-52}$, single $2^{-23}$ |
| Interpolation | $n+1$ points ⇒ unique degree $\le n$; error $\frac{f^{(n+1)}(\xi)}{(n+1)!}\prod(x-x_i)$ |
| Quadrature | trapezoid $O(h^2)$, deg 1; Simpson $O(h^4)$, deg 3; Gauss $n$ points deg $2n-1$ |
| Euler explicit / implicit | $y_k+hf(t_k,y_k)$ / $y_k+hf(t_{k+1},y_{k+1})$, order 1 |
| Stability ($y'=\lambda y$) | explicit Euler $h\le2/\lvert\lambda\rvert$; implicit Euler, trapezoidal: all $h$ |

---

## Practice MCQs

**Q1.** (official example 1) The singular value decomposition of a matrix $A$ is
A) $A=LU$, $L$ lower and $U$ upper triangular  B) $A=QR$, $Q$ orthogonal, $R$ upper triangular  C) $A=U\Sigma V^T$, $U,V$ orthogonal, $\Sigma$ diagonal with non-negative entries  D) $A=PDP^{-1}$, $P$ invertible, $D$ diagonal  E) $A=LL^T$, $L$ lower triangular

<details><summary>Answer</summary>

**C** — The others are LU, QR, eigen-decomposition and Cholesky. The SVD exists for every matrix.

</details>

**Q2.** (official example 2) Which recurrence determines iteratively a solution of $x^2=2$?
A) $x_{n+1}=x_n+\frac{x_n^2-2}{2x_n}$  B) $x_{n+1}=x_n-\frac{x_n^2+5}{2x_n}$  C) $x_{n+1}=x_n-\frac{x_n^2-2}{2x_n}$  D) $x_{n+1}=\frac2{x_n}+\frac{x_n}2$  E) $x_{n+1}=\frac2{x_n}-\frac{5x_n}2$

<details><summary>Answer</summary>

**C** — Newton for $f=x^2-2$. A moves away from $\sqrt2$; D converges to $2$ (fixed point $\frac x2=\frac2x$).

</details>

**Q3.** Bisection on $[0,1]$: the interval length after 3 steps is
A) $\frac13$  B) $\frac16$  C) $\frac18$  D) $\frac1{16}$  E) $\frac14$

<details><summary>Answer</summary>

**C** — $2^{-3}$.

</details>

**Q4.** Newton for $f(x)=x^2-3$ with $x_0=2$ gives $x_1=$
A) $1.75$  B) $1.5$  C) $1.732$  D) $2.25$  E) $1.8$

<details><summary>Answer</summary>

**A** — $2-\frac{1}{4}$.

</details>

**Q5.** Order of convergence of Newton's method at a simple root:
A) $1$  B) $1.618$  C) $2$  D) $3$  E) $0.5$

<details><summary>Answer</summary>

**C** — Quadratic. $1.618$ is the secant method.

</details>

**Q6.** Newton for $f(x)=(x-1)^2$ converges
A) quadratically  B) linearly, error halves each step  C) not at all  D) in one step  E) cubically

<details><summary>Answer</summary>

**B** — $x_{k+1}-1=\frac12(x_k-1)$ at a double root.

</details>

**Q7.** For $A=\begin{pmatrix}1&-2\\3&4\end{pmatrix}$, $\lVert A\rVert_\infty=$
A) $4$  B) $6$  C) $10$  D) $7$  E) $5$

<details><summary>Answer</summary>

**D** — Row sums $3$ and $7$. ($6$ is $\lVert A\rVert_1$.)

</details>

**Q8.** $\kappa_\infty\begin{pmatrix}1&2\\3&4\end{pmatrix}=$
A) $7$  B) $10$  C) $21$  D) $14$  E) $3$

<details><summary>Answer</summary>

**C** — $7\cdot3$.

</details>

**Q9.** The condition number of $\operatorname{diag}(2,\ 0.01)$ is
A) $200$  B) $2$  C) $0.02$  D) $100$  E) $1$

<details><summary>Answer</summary>

**A** — $\frac{2}{0.01}$.

</details>

**Q10.** Why is partial pivoting used in Gaussian elimination?
A) to reduce the cost to $O(n^2)$  B) to keep multipliers $\le1$ and limit rounding errors  C) to make $A$ symmetric  D) to compute eigenvalues  E) it changes the exact solution to a better one

<details><summary>Answer</summary>

**B** — Stability. The cost stays $\frac23n^3$ and the exact solution is unchanged.

</details>

**Q11.** LU (no pivoting, unit $L$) of $\begin{pmatrix}2&1\\4&5\end{pmatrix}$:
A) $U=\begin{pmatrix}2&1\\0&5\end{pmatrix}$  B) $L=\begin{pmatrix}1&0\\4&1\end{pmatrix}$  C) $U=\begin{pmatrix}2&1\\0&1\end{pmatrix}$  D) $L=\begin{pmatrix}1&0\\2&1\end{pmatrix}$, $U=\begin{pmatrix}2&1\\0&3\end{pmatrix}$  E) $L=I$, $U=A$

<details><summary>Answer</summary>

**D** — Multiplier $2$, new row $(0,3)$.

</details>

**Q12.** The Cholesky factor of $\begin{pmatrix}9&3\\3&5\end{pmatrix}$ is
A) $\begin{pmatrix}3&0\\1&2\end{pmatrix}$  B) $\begin{pmatrix}3&0\\1&\sqrt5\end{pmatrix}$  C) $\begin{pmatrix}9&0\\3&2\end{pmatrix}$  D) $\begin{pmatrix}3&0\\3&2\end{pmatrix}$  E) $\begin{pmatrix}3&1\\0&2\end{pmatrix}$

<details><summary>Answer</summary>

**A** — $\sqrt9=3$, $\frac33=1$, $\sqrt{5-1}=2$. (E is $L^T$.)

</details>

**Q13.** Which factorization exists for **every** real matrix (also non-square)?
A) Cholesky  B) LU without pivoting  C) eigen-decomposition $PDP^{-1}$  D) SVD  E) $A=LL^T$

<details><summary>Answer</summary>

**D** — QR also exists for every matrix, but it is not offered. Cholesky needs SPD; $PDP^{-1}$ needs diagonalizable.

</details>

**Q14.** The normal equations for $\min\lVert Ax-b\rVert_2$ are
A) $Ax=b$  B) $AA^Tx=b$  C) $A^TAx=A^Tb$  D) $A^Tx=b$  E) $x=A^{-1}b$

<details><summary>Answer</summary>

**C** — The residual must be orthogonal to the columns of $A$.

</details>

**Q15.** The least-squares line $y=c+mx$ through $(0,1),(1,3),(2,4)$ has slope
A) $1$  B) $2$  C) $\frac76$  D) $\frac32$  E) $\frac53$

<details><summary>Answer</summary>

**D** — $3c+3m=8$, $3c+5m=11$.

</details>

**Q16.** The pseudo-inverse of $a=\binom11$ is
A) $(1\ \ 1)$  B) $\frac12(1\ \ 1)$  C) $\binom{1/2}{1/2}$  D) does not exist  E) $\frac1{\sqrt2}(1\ \ 1)$

<details><summary>Answer</summary>

**B** — $a^+=(a^Ta)^{-1}a^T$, a $1\times2$ row.

</details>

**Q17.** The singular values of $\begin{pmatrix}3&0\\0&-4\end{pmatrix}$ are
A) $3,-4$  B) $9,16$  C) $4,3$  D) $5,0$  E) $7,1$

<details><summary>Answer</summary>

**C** — $\sqrt{\lambda(A^TA)}=\sqrt{16},\sqrt9$.

</details>

**Q18.** The Gershgorin discs of $\begin{pmatrix}5&1\\2&-3\end{pmatrix}$ are
A) $\lvert z-5\rvert\le2$, $\lvert z+3\rvert\le1$  B) $\lvert z-5\rvert\le1$, $\lvert z+3\rvert\le2$  C) $\lvert z-5\rvert\le3$, $\lvert z+3\rvert\le3$  D) $\lvert z-1\rvert\le5$, $\lvert z-2\rvert\le3$  E) $\lvert z-5\rvert\le1$, $\lvert z-3\rvert\le2$

<details><summary>Answer</summary>

**B** — Centre $a_{ii}$, radius = off-diagonal row sum. Centre of row 2 is $-3$.

</details>

**Q19.** The power method on a matrix with eigenvalues $6,-3,2$ converges to
A) $6$, rate $\frac13$  B) $-3$, rate $\frac12$  C) $6$, rate $\frac12$  D) $2$, rate $\frac13$  E) $6$, rate $\frac23$

<details><summary>Answer</summary>

**C** — Rate $\frac{\lvert-3\rvert}{6}$.

</details>

**Q20.** Shifted inverse iteration with $\mu=5$, eigenvalues $1,4,7$, converges to
A) $1$  B) $4$  C) $7$  D) $5$  E) $\frac15$

<details><summary>Answer</summary>

**B** — Closest to the shift.

</details>

**Q21.** Machine epsilon in IEEE double precision is
A) $2^{-23}$  B) $2^{-52}$  C) $2^{-64}$  D) $10^{-8}$  E) $2^{-1022}$

<details><summary>Answer</summary>

**B** — 52 mantissa bits. $2^{-1022}$ is the smallest normal number, not epsilon.

</details>

**Q22.** For large $x$, which formula for $\sqrt{x+1}-\sqrt x$ avoids cancellation?
A) $\sqrt{x+1}-\sqrt x$  B) $\frac1{\sqrt{x+1}+\sqrt x}$  C) $\sqrt{(x+1)-x}$  D) $\frac{\sqrt{x+1}}{\sqrt x}$  E) $\sqrt{x+1}+\sqrt x$

<details><summary>Answer</summary>

**B** — Multiply by the conjugate: no subtraction of nearly equal numbers.

</details>

**Q23.** The interpolation polynomial through $(0,1),(1,3),(2,7)$ is
A) $2x+1$  B) $x^2+x+1$  C) $x^2+2x+1$  D) $3x^2-x+1$  E) $x^3+x+1$

<details><summary>Answer</summary>

**B** — Divided differences $2,4$, then $1$: $1+2x+x(x-1)$.

</details>

**Q24.** Through $n+1$ points with distinct $x_i$ there is exactly one interpolation polynomial of degree
A) exactly $n+1$  B) at most $n$  C) exactly $2n$  D) at most $n-1$  E) any degree

<details><summary>Answer</summary>

**B** — Vandermonde matrix is invertible.

</details>

**Q25.** The Lagrange basis polynomials satisfy
A) $L_i(x_j)=1$ for all $i,j$  B) $L_i(x_j)=\delta_{ij}$  C) $L_i(x_j)=x_j^i$  D) $\sum_iL_i(x)=0$  E) $L_i(x_j)=y_j$

<details><summary>Answer</summary>

**B** — $1$ at its own node, $0$ at the others. (Also $\sum_iL_i\equiv1$, so D is false.)

</details>

**Q26.** High-degree interpolation at equidistant nodes oscillates near the interval ends (Runge phenomenon). A standard remedy is
A) more equidistant nodes  B) Chebyshev nodes or splines  C) a higher degree  D) Newton form instead of Lagrange form  E) double precision

<details><summary>Answer</summary>

**B** — More nodes make it worse. Newton vs Lagrange give the same polynomial (D changes nothing).

</details>

**Q27.** Simpson's rule is exact for polynomials of degree up to
A) $1$  B) $2$  C) $3$  D) $4$  E) $5$

<details><summary>Answer</summary>

**C** — By symmetry it also integrates cubics exactly.

</details>

**Q28.** Composite trapezoid with 2 subintervals for $\int_0^1x^2dx$ gives
A) $0.375$  B) $0.5$  C) $0.25$  D) $\frac13$  E) $0.3$

<details><summary>Answer</summary>

**A** — $0.5(0+0.25+0.5)$.

</details>

**Q29.** One explicit Euler step for $y'=y$, $y(0)=1$, $h=0.1$ gives
A) $1.1$  B) $1.105$  C) $1.111$  D) $0.9$  E) $1.01$

<details><summary>Answer</summary>

**A** — $1+0.1\cdot1$. ($1.111$ is implicit Euler.)

</details>

**Q30.** For $y'=-50y$, explicit Euler is stable only if
A) $h\le0.5$  B) $h\le0.04$  C) $h\le0.02$  D) all $h>0$  E) $h\le2$

<details><summary>Answer</summary>

**B** — $\lvert1-50h\rvert\le1$ ⇔ $h\le\frac2{50}$.

</details>

**Q31.** Why are implicit methods (e.g. implicit Euler) preferred for stiff ODEs?
A) they need no equation solving  B) they are always of higher order  C) they are stable for large step sizes  D) they are exact  E) they use fewer function evaluations

<details><summary>Answer</summary>

**C** — A-stable: $\frac1{1-h\lambda}$ has modulus $<1$ for every $h>0$ when $\lambda<0$. The price is solving an equation each step (A false).

</details>
