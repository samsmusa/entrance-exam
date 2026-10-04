# 6. Numerical Methods

> Syllabus:
> - Linear systems of equations (Gaussian elimination, LU, Cholesky, condition number, iterative methods Jacobi / Gauss–Seidel, rank and structure of the solution space)
> - Eigenvalue methods (power method, inverse iteration, QR algorithm, Gershgorin)
> - Pseudo-inverses (Moore–Penrose, SVD, least squares, normal equations)
> - Taylor series in numerics (error terms, Newton's method and convergence order, bisection, numerical differentiation / integration errors)
> - Floating-point arithmetic basics
>
> How to study this file: sections 1–9 are 🟢 core. Each has a small hand calculation (2×2 matrices, 1–3 iteration steps). Section 10 and the 🟡 boxes in section 8 are facts only. Time: about 4–5 hours for 🟢, 30 minutes for 🟡, 1 hour for the MCQs.

## Contents
🟢 1. Gaussian elimination and the solution space · 2. LU and Cholesky · 3. Norms and condition number · 4. Jacobi and Gauss–Seidel · 5. Root finding (bisection, Newton) · 6. Numerical differentiation and integration · 7. Floating-point numbers · 8. Eigenvalues: Gershgorin and power method · 9. Least squares and normal equations
🟡 8b. Inverse iteration and QR algorithm · 10. Pseudo-inverse and SVD
📋 Formula sheet · Practice MCQs (24 questions)

---

## 1. Gaussian elimination and the solution space 🟢

**Idea.** Solve $Ax=b$ by row operations. Make the matrix upper triangular, then solve from the bottom up (**back substitution**).

**Allowed row operations:** swap two rows; multiply a row by a number $\ne0$; add a multiple of one row to another.

**Worked example.** $x+y=3$, $2x+3y=8$.
1. Augmented matrix $\left(\begin{array}{cc|c}1&1&3\\2&3&8\end{array}\right)$.
2. Row 2 − 2·Row 1: $\left(\begin{array}{cc|c}1&1&3\\0&1&2\end{array}\right)$.
3. Back substitution: $y=2$, then $x=3-2=1$.

**Rank** = number of pivots (non-zero rows after elimination).

**How many solutions?** $A$ is $m\times n$ ($m$ equations, $n$ unknowns). Let $r=\operatorname{rank}A$.

| Situation | Solutions |
|---|---|
| $\operatorname{rank}A<\operatorname{rank}(A\mid b)$ | none |
| $\operatorname{rank}A=\operatorname{rank}(A\mid b)=n$ | exactly one |
| $\operatorname{rank}A=\operatorname{rank}(A\mid b)<n$ | infinitely many, with $n-r$ free parameters |

- **Rank–nullity:** $\dim\ker A=n-\operatorname{rank}A$. ($\ker A$ = all $x$ with $Ax=0$.)
- Solution set = one particular solution $x_p$ + $\ker A$. This is an **affine** subspace of dimension $n-r$.
- Square $A$: unique solution for every $b$ ⇔ $\det A\ne0$ ⇔ $\operatorname{rank}A=n$.
- Homogeneous system $Ax=0$ with more unknowns than equations always has a non-zero solution.

**Worked example (official problem 12 style).** $A$ is $4\times6$ with rank $3$, and the system is solvable.
Free parameters $=6-3=3$. The solutions form a 3-dimensional affine subspace of $\mathbb R^6$.

**Worked example 2.** $x+y+z=1$, $2x+2y+2z=3$.
Row 2 − 2·Row 1 gives $0=1$. So $\operatorname{rank}A=1<\operatorname{rank}(A\mid b)=2$: **no solution**.

> **Trap:** if $b\ne0$, the solution set is **not** a subspace (it does not contain $0$). It is an affine subspace.

---

## 2. LU and Cholesky 🟢

**LU idea.** Gaussian elimination = writing $A=LU$.
- $U$ = the upper triangular matrix at the end of elimination.
- $L$ = lower triangular, $1$ on the diagonal, the **multipliers** below the diagonal.
Then $Ax=b$ is solved in two easy steps: $Ly=b$ (forward), $Ux=y$ (backward).

**Worked example.** $A=\begin{pmatrix}2&1\\4&5\end{pmatrix}$.
1. Multiplier $l_{21}=\frac42=2$.
2. Row 2 − 2·Row 1: $(4,5)-(4,2)=(0,3)$.
3. $L=\begin{pmatrix}1&0\\2&1\end{pmatrix}$, $U=\begin{pmatrix}2&1\\0&3\end{pmatrix}$. Check: $LU=A$ ✓. Also $\det A=2\cdot3=6$.

**Pivoting.** If a pivot is $0$ (or very small), swap rows first. This gives $PA=LU$ ($P$ = permutation matrix). With **partial pivoting** (take the largest $\lvert a_{ik}\rvert$ in the column) it works for every invertible $A$.
Example: $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ is invertible but has no LU without swapping.

**Cholesky.** If $A$ is **symmetric positive definite** (SPD: $A=A^T$ and all eigenvalues $>0$), then $A=LL^T$ with $L$ lower triangular, positive diagonal.

**Formulas for 2×2:** $A=\begin{pmatrix}a&b\\b&c\end{pmatrix}$ gives $l_{11}=\sqrt a$, $l_{21}=\frac{b}{l_{11}}$, $l_{22}=\sqrt{c-l_{21}^2}$.

**Worked example.** $A=\begin{pmatrix}4&2\\2&5\end{pmatrix}$.
1. $l_{11}=\sqrt4=2$.
2. $l_{21}=\frac22=1$.
3. $l_{22}=\sqrt{5-1}=2$. So $L=\begin{pmatrix}2&0\\1&2\end{pmatrix}$. Check: $LL^T=\begin{pmatrix}4&2\\2&5\end{pmatrix}$ ✓.

**SPD test (Sylvester):** all leading minors $>0$. For 2×2: $a>0$ and $\det A>0$.

**Cost** (number of operations for $n\times n$, leading term):

| Task | Cost |
|---|---|
| LU / Gaussian elimination | $\frac23n^3$ |
| Cholesky | $\frac13n^3$ (half of LU) |
| Forward or back substitution | $n^2$ |
| Matrix × vector | $2n^2$ |
| Matrix × matrix | $2n^3$ |
| Tridiagonal system | $O(n)$ |

> **Trap:** symmetric is not enough for Cholesky. $\begin{pmatrix}1&2\\2&1\end{pmatrix}$ is symmetric but $\det=-3<0$, so not positive definite.

---

## 3. Norms and condition number 🟢

**Vector norms** (ways to measure length):

| Norm | Formula | $x=(3,-4)$ |
|---|---|---|
| $\lVert x\rVert_1$ | $\sum\lvert x_i\rvert$ | $7$ |
| $\lVert x\rVert_2$ | $\sqrt{\sum x_i^2}$ | $5$ |
| $\lVert x\rVert_\infty$ | $\max\lvert x_i\rvert$ | $4$ |

**Matrix norms**

| Norm | How to compute |
|---|---|
| $\lVert A\rVert_1$ | largest **column** sum of $\lvert a_{ij}\rvert$ |
| $\lVert A\rVert_\infty$ | largest **row** sum of $\lvert a_{ij}\rvert$ |
| $\lVert A\rVert_2$ | $\sqrt{\lambda_{\max}(A^TA)}$; for symmetric $A$: $\max\lvert\lambda_i\rvert$ |

Memory help: "$1$ is a standing line → columns; $\infty$ lies flat → rows".

**Condition number.** $\kappa(A)=\lVert A\rVert\cdot\lVert A^{-1}\rVert$.
- It says how much errors in the data can grow in the solution:
$$\frac{\lVert\Delta x\rVert}{\lVert x\rVert}\le\kappa(A)\,\frac{\lVert\Delta b\rVert}{\lVert b\rVert}.$$
- Always $\kappa(A)\ge1$. $\kappa(I)=1$. $\kappa(cA)=\kappa(A)$.
- Large $\kappa$ = **ill-conditioned**. Rule of thumb: you lose about $\log_{10}\kappa$ correct digits.
- Diagonal matrix: $\kappa=\frac{\max\lvert d_i\rvert}{\min\lvert d_i\rvert}$. Symmetric: $\kappa_2=\frac{\max\lvert\lambda\rvert}{\min\lvert\lambda\rvert}$.

**2×2 inverse:** $\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1}=\dfrac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$.

**Worked example.** $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$, find $\kappa_\infty$.
1. Row sums of $A$: $3$ and $7$, so $\lVert A\rVert_\infty=7$.
2. $\det A=4-6=-2$, $A^{-1}=\begin{pmatrix}-2&1\\1.5&-0.5\end{pmatrix}$.
3. Row sums of $A^{-1}$: $3$ and $2$, so $\lVert A^{-1}\rVert_\infty=3$.
4. $\kappa_\infty=7\cdot3=21$.

> **Trap:** a small determinant does **not** mean ill-conditioned. $0.1\cdot I$ (size $10$) has $\det=10^{-10}$ but $\kappa=1$.

---

## 4. Jacobi and Gauss–Seidel 🟢

**Idea.** For big systems, guess a solution and improve it again and again. Solve equation $i$ for $x_i$.

| Method | Which values on the right side? |
|---|---|
| Jacobi | only **old** values from the last step |
| Gauss–Seidel | the **newest** values, as soon as they are computed |

**Worked example.** $4x+y=6$, $2x+5y=12$ (exact solution $x=1,y=2$). Start $(0,0)$.
Rewrite: $x=\frac{6-y}{4}$, $y=\frac{12-2x}{5}$.
- **Jacobi step 1:** $x=\frac{6-0}{4}=1.5$, $y=\frac{12-0}{5}=2.4$.
- **Jacobi step 2:** $x=\frac{6-2.4}{4}=0.9$, $y=\frac{12-3}{5}=1.8$.
- **Gauss–Seidel step 1:** $x=1.5$, then use it: $y=\frac{12-2\cdot1.5}{5}=1.8$.
- **Gauss–Seidel step 2:** $x=\frac{6-1.8}{4}=1.05$, $y=\frac{12-2.1}{5}=1.98$. (Closer to $(1,2)$.)

**When do they converge?**
- Write the method as $x^{(k+1)}=Tx^{(k)}+c$. It converges for every start ⇔ $\rho(T)<1$. ($\rho$ = **spectral radius** = largest $\lvert\lambda\rvert$ of $T$.)
- **Strictly diagonally dominant** ($\lvert a_{ii}\rvert>$ sum of the other $\lvert a_{ij}\rvert$ in row $i$) ⇒ Jacobi and Gauss–Seidel converge.
- SPD matrix ⇒ Gauss–Seidel converges.
- Jacobi matrix: $T_J=-D^{-1}(L+U)$, where $A=D+L+U$ (diagonal, lower, upper part).
- Often Gauss–Seidel is about twice as fast (e.g. tridiagonal: $\rho(T_{GS})=\rho(T_J)^2$).

**Check the example:** $\lvert4\rvert>1$ and $\lvert5\rvert>2$ ⇒ diagonally dominant ⇒ both converge.

> **Trap:** the condition is $\rho(T)<1$ for the **iteration matrix** $T$, not $\rho(A)<1$. Diagonal dominance is sufficient, not necessary.

---

## 5. Root finding: bisection, fixed point, Newton 🟢

Goal: find $x^*$ with $f(x^*)=0$.

### Bisection
**Idea.** If $f(a)$ and $f(b)$ have opposite signs, there is a root between them. Take the midpoint $m$ and keep the half where the sign changes.
- After $n$ steps the interval has length $\frac{b-a}{2^n}$.
- Always converges (for continuous $f$), but slowly: error is halved each step.

**Worked example.** $f(x)=x^2-2$ on $[1,2]$.
1. $m=1.5$: $f=0.25>0$, $f(1)<0$ ⇒ new interval $[1,1.5]$.
2. $m=1.25$: $f=-0.4375<0$ ⇒ new interval $[1.25,1.5]$.

**How many steps for length $<\varepsilon$?** Need $\frac{b-a}{2^n}<\varepsilon$. For $[0,1]$ and $\varepsilon=10^{-3}$: $2^{10}=1024$, so $n=10$.

### Fixed-point iteration
Write the problem as $x=g(x)$ and iterate $x_{k+1}=g(x_k)$.
- Converges near $x^*$ if $\lvert g'(x^*)\rvert<1$. Error shrinks by about $\lvert g'(x^*)\rvert$ each step.
- Example: $x_{k+1}=\frac12x_k+1$ from $x_0=0$: $1,\ 1.5,\ 1.75,\dots\to2$ (here $g'=\frac12$).

### Newton's method
**Idea.** Replace $f$ by its tangent line (Taylor of order 1) and take the zero of the tangent.
$$x_{k+1}=x_k-\frac{f(x_k)}{f'(x_k)}.$$

**Worked example.** $\sqrt2$: $f(x)=x^2-2$, $f'(x)=2x$, $x_0=1$.
1. $x_1=1-\frac{1-2}{2}=1.5$.
2. $x_2=1.5-\frac{2.25-2}{3}=1.5-0.0833=1.41\overline{6}$ (true: $1.41421$).

For $\sqrt a$ Newton becomes $x_{k+1}=\frac12\left(x_k+\frac{a}{x_k}\right)$.

### Order of convergence
Order $p$ means: new error $\approx C\cdot(\text{old error})^p$.

| Method | Order | In words |
|---|---|---|
| Bisection | 1 | error halves each step |
| Fixed point | 1 (if $g'(x^*)\ne0$) | error × $\lvert g'(x^*)\rvert$ |
| Secant | $\approx1.618$ | no derivative needed |
| Newton (simple root) | 2 | correct digits roughly **double** each step |
| Newton (double root) | 1 | slows down: error × $\frac12$ |

> **Trap:** Newton is fast only **near** the root, and fails if $f'(x_k)=0$. Bisection is slow but always works.

---

## 6. Numerical differentiation and integration 🟢

### Differences (from Taylor series)
$h$ = small step size.

| Formula | Approximates | Error |
|---|---|---|
| $\frac{f(x+h)-f(x)}{h}$ (forward) | $f'(x)$ | $O(h)$ |
| $\frac{f(x+h)-f(x-h)}{2h}$ (central) | $f'(x)$ | $O(h^2)$ |
| $\frac{f(x+h)-2f(x)+f(x-h)}{h^2}$ | $f''(x)$ | $O(h^2)$ |

Why: $f(x+h)=f(x)+hf'(x)+\frac{h^2}{2}f''(x)+\dots$ So the forward difference $=f'(x)+\frac h2f''(x)+\dots$

**Worked example.** $f=e^x$ at $x=0$, $h=0.1$ (true value $f'(0)=1$).
- Forward: $\frac{e^{0.1}-1}{0.1}\approx1.0517$. Error $\approx0.05\approx\frac h2$.
- Central: $\frac{e^{0.1}-e^{-0.1}}{0.2}\approx1.0017$. Error $\approx0.0017\approx\frac{h^2}{6}$.

### Integration rules (quadrature)

| Rule | Formula on $[a,b]$ | Exact for polynomials of degree | Error (composite, step $h$) |
|---|---|---|---|
| Midpoint | $(b-a)\,f\!\left(\frac{a+b}2\right)$ | $\le1$ | $O(h^2)$ |
| Trapezoid | $\frac{b-a}{2}\big(f(a)+f(b)\big)$ | $\le1$ | $O(h^2)$ |
| Simpson | $\frac{b-a}{6}\Big(f(a)+4f\!\left(\frac{a+b}2\right)+f(b)\Big)$ | $\le3$ | $O(h^4)$ |

**Composite trapezoid** with $n$ pieces, $h=\frac{b-a}{n}$: $T=h\left[\frac{f_0}{2}+f_1+\dots+f_{n-1}+\frac{f_n}{2}\right]$.

**Worked example.** $\int_0^1x^2\,dx=\frac13$.
1. Trapezoid, 1 piece: $\frac12(0+1)=0.5$. Error $0.1\overline{6}$.
2. Trapezoid, 2 pieces ($h=0.5$): $0.5\left[0+0.25+\frac12\right]=0.375$. Error $0.041\overline{6}$ (4 times smaller).
3. Simpson: $\frac16(0+4\cdot0.25+1)=\frac13$. **Exact**.

**Halving $h$:** error $O(h)$ → ÷2; $O(h^2)$ → ÷4; $O(h^4)$ → ÷16.

> **Trap:** Simpson is exact for cubics too (degree 3), not only for quadratics.

---

## 7. Floating-point numbers 🟢

**Idea.** A computer stores $x=\pm(1.d_1d_2\dots)_2\cdot2^e$ with a fixed number of digits. So most numbers are rounded.

- **Machine epsilon** $\varepsilon$: the gap between $1$ and the next larger float.
- Rounding: $\mathrm{fl}(x)=x(1+\delta)$ with $\lvert\delta\rvert\le u=\frac{\varepsilon}{2}$ (unit roundoff). The **relative** error is small.

| IEEE type | Bits | $\varepsilon$ | Decimal digits |
|---|---|---|---|
| single | 32 | $2^{-23}\approx1.2\cdot10^{-7}$ | about 7 |
| double | 64 | $2^{-52}\approx2.2\cdot10^{-16}$ | about 16 |

**Typical problems**
- **Cancellation:** subtracting two almost equal numbers loses many digits.
  Fix: rewrite, e.g. $\sqrt{x+1}-\sqrt x=\frac{1}{\sqrt{x+1}+\sqrt x}$.
- Addition is **not associative**: $(a+b)+c$ can differ from $a+(b+c)$.
- $0.1$ is not exact in binary.
- Overflow (too big) and underflow (too close to $0$) are range problems.

**Worked example (toy system).** Base $2$, 3 digits $1.d_1d_2$, exponent $e\in\{-1,0,1\}$.
1. Mantissas: $1.00,1.01,1.10,1.11$ → 4.
2. $4\cdot3$ exponents $\cdot2$ signs $=24$, plus zero $=25$ numbers.
3. $\varepsilon=0.01_2=\frac14$. Largest: $1.11_2\cdot2=3.5$.

> **Trap:** some books define $\varepsilon=2^{-53}$ (the unit roundoff $u$) instead of $2^{-52}$. Read the definition in the question.

---

## 8. Eigenvalues: Gershgorin and power method 🟢

**Basic facts first.** $\operatorname{tr}A=\sum\lambda_i$, $\det A=\prod\lambda_i$. Triangular matrix: eigenvalues = diagonal. $A^{-1}$ has eigenvalues $\frac1{\lambda_i}$, $A-\mu I$ has $\lambda_i-\mu$.

### Gershgorin circles
**Idea.** Each eigenvalue lies near some diagonal entry.
For row $i$: centre $a_{ii}$, radius $R_i=\sum_{j\ne i}\lvert a_{ij}\rvert$. Every eigenvalue lies in the union of these discs.
- If some discs are separated from the others, a group of $k$ discs contains exactly $k$ eigenvalues.
- Symmetric matrix: eigenvalues are real, so the discs become intervals.

**Worked example.** $A=\begin{pmatrix}5&1\\2&-3\end{pmatrix}$.
1. Row 1: centre $5$, radius $1$ → $[4,6]$ (on the real line).
2. Row 2: centre $-3$, radius $2$ → $[-5,-1]$.
3. Discs are separate ⇒ one eigenvalue in each. (Exact: $1\pm\sqrt{18}\approx5.24,\ -3.24$ ✓.)
4. $0$ is in no disc ⇒ $A$ is invertible.

### Power method
**Idea.** Multiply a start vector by $A$ again and again. The part along the eigenvector of the **largest** $\lvert\lambda\rvert$ wins.
$$x_{k+1}=\frac{Ax_k}{\lVert Ax_k\rVert},\qquad\lambda\approx\frac{x_k^TAx_k}{x_k^Tx_k}\ \text{(Rayleigh quotient)}.$$
- Speed: error shrinks like $\left\lvert\frac{\lambda_2}{\lambda_1}\right\rvert^k$ ($\lambda_1$ = largest, $\lambda_2$ = second largest in absolute value).
- Needs $\lvert\lambda_1\rvert>\lvert\lambda_2\rvert$.

**Worked example.** $A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$ (eigenvalues $3$ and $1$), $x_0=(1,0)$.
1. $Ax_0=(2,1)$. 2. $A(2,1)=(5,4)$. 3. $A(5,4)=(14,13)$.
4. Direction → $(1,1)$. Ratio $\frac{14}{5}=2.8\to3$. Rate $\frac13$.

> **Trap:** for the rate use the two largest **absolute values**. Eigenvalues $6,-3,2$: rate $\frac{3}{6}=\frac12$.

### 🟡 Inverse iteration and QR algorithm

> **Must-know facts**
> 1. **Inverse iteration** = power method with $A^{-1}$ → finds the eigenvalue with the **smallest** $\lvert\lambda\rvert$.
> 2. **With shift $\mu$** (use $(A-\mu I)^{-1}$) → finds the eigenvalue **closest to $\mu$**. Eigenvalues $1,4,7$, $\mu=5$ → finds $4$.
> 3. **QR algorithm:** $A_k=Q_kR_k$, then $A_{k+1}=R_kQ_k$. All $A_k$ have the **same eigenvalues** (they are similar).
> 4. $A_k$ tends to upper triangular form; the eigenvalues appear on the diagonal. It finds **all** eigenvalues.
> 5. In practice: first reduce to Hessenberg form, use shifts. Cost about $O(n^3)$.

---

## 9. Least squares and normal equations 🟢

**Idea.** Too many equations ($m>n$), usually no exact solution. Find $x$ that makes the error $\lVert Ax-b\rVert_2$ as small as possible.

**Formula (normal equations):**
$$A^TA\,x=A^Tb.$$
- Unique solution if the columns of $A$ are independent.
- The residual $r=b-Ax$ is orthogonal to all columns of $A$.

**Worked example (fit a line $y=c+mx$).** Points $(0,1),(1,3),(2,4)$.
1. $A=\begin{pmatrix}1&0\\1&1\\1&2\end{pmatrix}$, $b=\begin{pmatrix}1\\3\\4\end{pmatrix}$.
2. $A^TA=\begin{pmatrix}3&3\\3&5\end{pmatrix}$, $A^Tb=\begin{pmatrix}8\\11\end{pmatrix}$.
3. Solve $3c+3m=8$, $3c+5m=11$: subtract → $2m=3$, $m=\frac32$, $c=\frac76$.
4. Line: $y=\frac76+\frac32x$.

**Shortcut:** fitting a constant $y\approx c$ gives $c$ = **mean** of the data.

> **Trap:** the normal equations square the condition number ($\kappa(A^TA)=\kappa(A)^2$). For bad cases, QR or SVD is better.

---

## 10. Pseudo-inverse and SVD 🟡

**SVD:** $A=U\Sigma V^T$ with $U,V$ orthogonal and $\Sigma$ diagonal with **singular values** $\sigma_1\ge\sigma_2\ge\dots\ge0$.

> **Must-know facts**
> 1. $\sigma_i=\sqrt{\lambda_i(A^TA)}$ — square roots of the eigenvalues of $A^TA$ (not of $A$).
> 2. $\operatorname{rank}A$ = number of $\sigma_i>0$. $\lVert A\rVert_2=\sigma_1$, $\kappa_2(A)=\frac{\sigma_{\max}}{\sigma_{\min}}$.
> 3. **Pseudo-inverse** $A^+=V\Sigma^+U^T$, where $\Sigma^+$ has $\frac1{\sigma_i}$ for $\sigma_i>0$ (and $0$ otherwise).
> 4. Independent columns: $A^+=(A^TA)^{-1}A^T$. Invertible $A$: $A^+=A^{-1}$.
> 5. $x=A^+b$ is the least-squares solution with the **smallest norm**.
> 6. Example: $a=\begin{pmatrix}1\\1\end{pmatrix}$ gives $a^+=\frac{a^T}{a^Ta}=\frac12(1\ \ 1)$.

> **Trap:** singular values are always $\ge0$. They equal $\lvert\lambda_i\rvert$ only for symmetric matrices.

---

## Formula sheet

| Topic | Formula / fact |
|---|---|
| Solvability | solvable ⇔ $\operatorname{rank}A=\operatorname{rank}(A\mid b)$; free parameters $=n-\operatorname{rank}A$ |
| LU | $L$ = multipliers (1 on diagonal), $U$ = result of elimination; $\det A=\prod u_{ii}$ |
| Cholesky (2×2) | $l_{11}=\sqrt a$, $l_{21}=b/l_{11}$, $l_{22}=\sqrt{c-l_{21}^2}$; needs SPD |
| Costs | LU $\frac23n^3$, Cholesky $\frac13n^3$, substitution $n^2$ |
| Norms | $\lVert A\rVert_1$ max column sum, $\lVert A\rVert_\infty$ max row sum |
| Condition | $\kappa=\lVert A\rVert\lVert A^{-1}\rVert\ge1$; rel. error $\le\kappa\cdot$ rel. data error |
| Jacobi / GS | converge ⇔ $\rho(T)<1$; strictly diagonally dominant ⇒ both converge |
| Bisection | length $\frac{b-a}{2^n}$ after $n$ steps |
| Newton | $x_{k+1}=x_k-f(x_k)/f'(x_k)$, order 2 |
| Orders | bisection 1, fixed point 1, secant 1.618, Newton 2 (double root: 1) |
| Differences | forward $O(h)$, central $O(h^2)$ |
| Quadrature | trapezoid/midpoint $O(h^2)$, exact degree 1; Simpson $O(h^4)$, exact degree 3 |
| Simpson | $\frac{b-a}{6}\big(f(a)+4f(m)+f(b)\big)$ |
| Machine eps | double $2^{-52}\approx2.2\cdot10^{-16}$, single $2^{-23}\approx1.2\cdot10^{-7}$ |
| Gershgorin | discs $\lvert z-a_{ii}\rvert\le\sum_{j\ne i}\lvert a_{ij}\rvert$ |
| Power method | largest $\lvert\lambda\rvert$, rate $\lvert\lambda_2/\lambda_1\rvert$ |
| Shifted inverse iteration | eigenvalue closest to $\mu$ |
| Least squares | $A^TAx=A^Tb$ |
| SVD | $\sigma_i=\sqrt{\lambda_i(A^TA)}$; $A^+=V\Sigma^+U^T$ |

---

## Practice MCQs

**Q1.** Bisection starts on $[0,1]$. After 3 steps, the length of the interval is
A) $\frac13$  B) $\frac16$  C) $\frac18$  D) $\frac1{16}$

<details><summary>Answer</summary>

**C** — Each step halves the length: $\frac{1}{2^3}=\frac18$.

</details>

**Q2.** Newton's method for $f(x)=x^2-3$ with $x_0=2$ gives $x_1=$
A) $1.75$  B) $1.5$  C) $1.732$  D) $2.25$

<details><summary>Answer</summary>

**A** — $x_1=2-\frac{f(2)}{f'(2)}=2-\frac{4-3}{4}=1.75$.

</details>

**Q3.** For $A=\begin{pmatrix}1&-2\\3&4\end{pmatrix}$, $\lVert A\rVert_\infty=$
A) $4$  B) $6$  C) $10$  D) $7$

<details><summary>Answer</summary>

**D** — Row sums of absolute values: $1+2=3$ and $3+4=7$. Maximum $7$. (The column sums give $\lVert A\rVert_1=6$.)

</details>

**Q4.** The trapezoid rule with one interval for $\int_0^2x^2\,dx$ gives
A) $\frac83$  B) $4$  C) $2$  D) $8$

<details><summary>Answer</summary>

**B** — $\frac{2-0}{2}\big(f(0)+f(2)\big)=1\cdot(0+4)=4$. The exact value is $\frac83$.

</details>

**Q5.** Simpson's rule for $\int_0^2x^2\,dx$ gives
A) $\frac83$  B) $4$  C) $3$  D) $\frac73$

<details><summary>Answer</summary>

**A** — $\frac26\big(0+4\cdot1+4\big)=\frac13\cdot8=\frac83$. Exact, because Simpson is exact up to degree 3.

</details>

**Q6.** What is the order of convergence of Newton's method at a simple root?
A) $1$  B) $1.618$  C) $2$  D) $3$

<details><summary>Answer</summary>

**C** — Quadratic: the number of correct digits roughly doubles each step. $1.618$ is the secant method.

</details>

**Q7.** Machine epsilon (gap between $1$ and the next number) in IEEE double precision is
A) $2^{-23}$  B) $2^{-52}$  C) $2^{-64}$  D) $10^{-8}$

<details><summary>Answer</summary>

**B** — Double has 52 stored mantissa bits, so $\varepsilon=2^{-52}\approx2.2\cdot10^{-16}$. $2^{-23}$ is single precision.

</details>

**Q8.** A system has 3 equations, 5 unknowns, $\operatorname{rank}A=\operatorname{rank}(A\mid b)=3$. The number of free parameters is
A) $0$  B) $3$  C) $5$  D) $2$

<details><summary>Answer</summary>

**D** — The system is solvable. Free parameters $=n-r=5-3=2$.

</details>

**Q9.** The Cholesky factor $L$ of $A=\begin{pmatrix}9&3\\3&5\end{pmatrix}$ is
A) $\begin{pmatrix}3&0\\1&2\end{pmatrix}$  B) $\begin{pmatrix}3&0\\1&\sqrt5\end{pmatrix}$  C) $\begin{pmatrix}9&0\\3&2\end{pmatrix}$  D) $\begin{pmatrix}3&0\\3&2\end{pmatrix}$

<details><summary>Answer</summary>

**A** — $l_{11}=\sqrt9=3$, $l_{21}=\frac33=1$, $l_{22}=\sqrt{5-1}=2$. Check: $LL^T=\begin{pmatrix}9&3\\3&5\end{pmatrix}$.

</details>

**Q10.** The Gershgorin discs of $A=\begin{pmatrix}5&1\\2&-3\end{pmatrix}$ are
A) $\lvert z-5\rvert\le2$, $\lvert z+3\rvert\le1$  B) $\lvert z-5\rvert\le1$, $\lvert z+3\rvert\le2$  C) $\lvert z-5\rvert\le3$, $\lvert z+3\rvert\le3$  D) $\lvert z-1\rvert\le5$, $\lvert z-2\rvert\le3$

<details><summary>Answer</summary>

**B** — Centre = diagonal entry, radius = sum of the other $\lvert a_{ij}\rvert$ in that row: row 1 gives radius $1$, row 2 gives radius $2$.

</details>

**Q11.** For $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$, the condition number $\kappa_\infty(A)$ is
A) $7$  B) $10$  C) $21$  D) $14$

<details><summary>Answer</summary>

**C** — $\lVert A\rVert_\infty=7$. $A^{-1}=\begin{pmatrix}-2&1\\1.5&-0.5\end{pmatrix}$, so $\lVert A^{-1}\rVert_\infty=3$. Product $21$.

</details>

**Q12.** The condition number (any $p$-norm) of $\operatorname{diag}(2,\ 0.01)$ is
A) $200$  B) $2$  C) $0.02$  D) $100$

<details><summary>Answer</summary>

**A** — For a diagonal matrix $\kappa=\frac{\max\lvert d_i\rvert}{\min\lvert d_i\rvert}=\frac{2}{0.01}=200$.

</details>

**Q13.** Jacobi for $4x+y=6$, $2x+5y=12$, starting at $(0,0)$. After one step:
A) $(1.5,\ 1.8)$  B) $(1,\ 2)$  C) $(6,\ 12)$  D) $(1.5,\ 2.4)$

<details><summary>Answer</summary>

**D** — Jacobi uses only old values: $x=\frac{6-0}{4}=1.5$, $y=\frac{12-0}{5}=2.4$. Answer A is Gauss–Seidel.

</details>

**Q14.** Same system, Gauss–Seidel from $(0,0)$. After one step:
A) $(1.5,\ 2.4)$  B) $(1.5,\ 1.8)$  C) $(1.05,\ 1.98)$  D) $(1,\ 2)$

<details><summary>Answer</summary>

**B** — $x=\frac{6-0}{4}=1.5$, then use the new $x$: $y=\frac{12-2\cdot1.5}{5}=1.8$.

</details>

**Q15.** Which property guarantees that Jacobi and Gauss–Seidel converge for every start vector?
A) $A$ is symmetric  B) $\det A\ne0$  C) $A$ is strictly diagonally dominant  D) all entries of $A$ are positive

<details><summary>Answer</summary>

**C** — Strict diagonal dominance is a standard sufficient condition. Symmetry or invertibility alone is not enough.

</details>

**Q16.** How many bisection steps on $[0,1]$ are needed to make the interval shorter than $10^{-3}$?
A) $10$  B) $3$  C) $100$  D) $1000$

<details><summary>Answer</summary>

**A** — Need $2^{-n}<10^{-3}$, i.e. $2^n>1000$. $2^9=512$ is too small, $2^{10}=1024$ works.

</details>

**Q17.** The LU decomposition (no pivoting, $L$ with ones on the diagonal) of $A=\begin{pmatrix}2&1\\4&5\end{pmatrix}$ has
A) $U=\begin{pmatrix}2&1\\0&5\end{pmatrix}$  B) $L=\begin{pmatrix}1&0\\4&1\end{pmatrix}$  C) $U=\begin{pmatrix}2&1\\0&1\end{pmatrix}$  D) $L=\begin{pmatrix}1&0\\2&1\end{pmatrix}$, $U=\begin{pmatrix}2&1\\0&3\end{pmatrix}$

<details><summary>Answer</summary>

**D** — Multiplier $l_{21}=4/2=2$. Row 2 − 2·Row 1 $=(0,3)$. Check $LU=A$.

</details>

**Q18.** The power method is applied to a matrix with eigenvalues $6,\,-3,\,2$. It converges to
A) $6$ with rate $\frac13$  B) $-3$ with rate $\frac12$  C) $6$ with rate $\frac12$  D) $2$ with rate $\frac13$

<details><summary>Answer</summary>

**C** — It finds the largest $\lvert\lambda\rvert=6$. Rate $=\frac{\lvert\lambda_2\rvert}{\lvert\lambda_1\rvert}=\frac36=\frac12$ (second largest in absolute value is $-3$).

</details>

**Q19.** Shifted inverse iteration with $\mu=5$ on a matrix with eigenvalues $1,4,7$ converges to
A) $1$  B) $4$  C) $7$  D) $5$

<details><summary>Answer</summary>

**B** — It finds the eigenvalue closest to the shift. Distances: $4$, $1$, $2$. Closest is $4$.

</details>

**Q20.** The least-squares line $y=c+mx$ through $(0,1),(1,3),(2,4)$ has slope
A) $1$  B) $2$  C) $\frac76$  D) $\frac32$

<details><summary>Answer</summary>

**D** — Normal equations: $3c+3m=8$, $3c+5m=11$. Subtract: $2m=3$, so $m=\frac32$ (and $c=\frac76$).

</details>

**Q21.** The composite trapezoid rule with 2 subintervals for $\int_0^1x^2\,dx$ gives
A) $0.375$  B) $0.5$  C) $0.25$  D) $\frac13$

<details><summary>Answer</summary>

**A** — $h=0.5$: $h\left[\frac{f(0)}2+f(0.5)+\frac{f(1)}2\right]=0.5(0+0.25+0.5)=0.375$.

</details>

**Q22.** The error of the central difference $\frac{f(x+h)-f(x-h)}{2h}$ is $O(h^2)$. If $h$ is halved, the error becomes about
A) the same  B) $\frac12$ as large  C) $\frac14$ as large  D) $\frac1{16}$ as large

<details><summary>Answer</summary>

**C** — $O(h^2)$: $\left(\frac h2\right)^2=\frac{h^2}{4}$, so the error is divided by $4$.

</details>

**Q23.** Newton's method for $f(x)=(x-1)^2$ (a double root) converges
A) quadratically  B) linearly, error halves each step  C) not at all  D) in one step

<details><summary>Answer</summary>

**B** — $x_{k+1}=x_k-\frac{(x_k-1)^2}{2(x_k-1)}=x_k-\frac{x_k-1}{2}$. So $x_{k+1}-1=\frac12(x_k-1)$: linear with factor $\frac12$.

</details>

**Q24.** The singular values of $A=\begin{pmatrix}3&0\\0&-4\end{pmatrix}$ are
A) $3$ and $-4$  B) $9$ and $16$  C) $4$ and $3$  D) $5$ and $0$

<details><summary>Answer</summary>

**C** — $A^TA=\operatorname{diag}(9,16)$; $\sigma_i=\sqrt{\lambda_i}=4,3$. Singular values are never negative.

</details>
