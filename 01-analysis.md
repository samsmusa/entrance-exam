# 1. Analysis

> Syllabus:
> - Convergence of sequences and series in $\mathbb{R}^n$
> - Theory of (Riemann) integration and differentiation (in several variables)
> - Taylor / Fourier series, transformations (Fourier / Laplace)
> - Topological basics (open, closed, compact sets)
> - Hilbert- / Banach-spaces
>
> How to study this file: sections 1–9 are 🟢 core. Learn them well and do the worked examples on paper. Sections 10–12 are 🟡: read the "Must-know facts" boxes only. Time: about 5–6 hours for 🟢, 1 hour for 🟡, 1 hour for the MCQs.

## Contents
🟢 1. Inequalities and standard limits · 2. Sequences, accumulation points, limsup / liminf · 3. Series and convergence tests · 4. Power series and radius of convergence · 5. Taylor series · 6. Derivatives in several variables · 7. Integration in one variable · 8. Multiple integrals · 9. Open, closed and compact sets
🟡 10. Fourier series · 11. Fourier and Laplace transforms · 12. Banach and Hilbert spaces
📋 Formula sheet · Practice MCQs (22 questions)

---

## 1. Inequalities and standard limits 🟢

**Idea.** Many questions ask for a minimum or a limit that you should "just know".

**The key inequality (official problem 1).** For $x>0$:
$$x+\frac1x\ge 2,\qquad\text{equality only for }x=1.$$
Why: $x+\frac1x-2=\frac{(x-1)^2}{x}\ge0$.

**AM–GM (arithmetic mean ≥ geometric mean).** For $a,b\ge0$: $\dfrac{a+b}{2}\ge\sqrt{ab}$.
So for $a,b>0$ and $x>0$: $\min\left(ax+\dfrac bx\right)=2\sqrt{ab}$, reached at $x=\sqrt{b/a}$.

**Worked example.** Minimum of $x+\frac9x$ for $x>0$?
1. Here $a=1$, $b=9$.
2. Minimum $=2\sqrt{9}=6$, at $x=3$. Check: $3+3=6$ ✓.

**Other useful inequalities:** triangle $\lvert a+b\rvert\le\lvert a\rvert+\lvert b\rvert$; Bernoulli $(1+x)^n\ge1+nx$ ($x\ge-1$); $e^x\ge1+x$.

**Standard limits** ($n\to\infty$):

| Sequence | Limit |
|---|---|
| $\frac1n$, $q^n$ with $\lvert q\rvert<1$ | $0$ |
| $\sqrt[n]{n}$, $\sqrt[n]{a}$ ($a>0$) | $1$ |
| $\left(1+\frac1n\right)^n$ | $e\approx2.718$ |
| $\left(1+\frac xn\right)^n$ | $e^x$ |
| $\left(1-\frac1n\right)^n$ | $\frac1e$ |
| $\frac{n^k}{a^n}$ ($a>1$), $\frac{a^n}{n!}$, $\frac{\ln n}{n}$ | $0$ |
| $\frac{\sin x}{x}$ as $x\to0$ | $1$ |

**Growth order** (slow → fast): $\ln n \ll n \ll n^2 \ll 2^n \ll n! \ll n^n$.

**Rational sequences.** Divide by the highest power of $n$:
$\dfrac{3n^2+1}{5n^2-n}=\dfrac{3+1/n^2}{5-1/n}\to\dfrac35$.

> **Trap:** $(1+\frac1n)^n\to e$, **not** $1$. "$1^\infty$" is not $1$.

---

## 2. Sequences, accumulation points, limsup / liminf 🟢

**Idea.** A sequence $(a_n)$ **converges** to $a$ if the terms get as close to $a$ as we want and stay there.
Formally: for every $\varepsilon>0$ there is an $N$ with $\lvert a_n-a\rvert<\varepsilon$ for all $n\ge N$.

**Important facts**
- Convergent ⇒ bounded. (Bounded does **not** imply convergent: $(-1)^n$.) Monotone **and** bounded ⇒ convergent.
- **Bolzano–Weierstrass:** every bounded sequence has a convergent subsequence.
- In $\mathbb{R}^n$: a sequence of vectors converges ⇔ **each component** converges.

**Accumulation point** (cluster point) of a sequence: the limit of some subsequence.
- $\limsup a_n$ = the **largest** accumulation point.
- $\liminf a_n$ = the **smallest** accumulation point.
- $a_n$ converges ⇔ $\limsup=\liminf$ (then this is the limit).

**Method.** Split the sequence into simple parts (even $n$ / odd $n$, or $n \bmod k$). Find the limit of each part.

**Worked example (official problem 19).** $x_n=\left(-1-\frac1n\right)^n$.
1. Write $x_n=(-1)^n\left(1+\frac1n\right)^n$.
2. $\left(1+\frac1n\right)^n\to e$.
3. Even $n$: $x_n\to e$. Odd $n$: $x_n\to-e$.
4. Accumulation points $\{e,-e\}$, $\limsup=e$, $\liminf=-e$.

**Worked example 2.** $a_n=(-1)^n+\frac1n$.
- Even $n$: $a_n\to1$. Odd $n$: $a_n\to-1$. So $\limsup=1$, $\liminf=-1$.
- But $\sup a_n=a_2=1.5$. The sup is **not** the limsup.

> **Trap:** $\sup$ can be changed by one single term. $\limsup$ never changes if you change finitely many terms.

**Countable sets:** $\mathbb N,\mathbb Z,\mathbb Q$, $\mathbb N\times\mathbb N$, countable unions of countable sets. **Uncountable:** $\mathbb R$, any interval $(a,b)$, the irrationals, $\mathcal P(\mathbb N)$.

---

## 3. Series and convergence tests 🟢

**Idea.** A series $\sum_{n=1}^\infty a_n$ converges if the partial sums $s_N=a_1+\dots+a_N$ converge.

**Step 0 — always first: term test.** If $a_n\not\to0$, the series **diverges**.
(If $a_n\to0$, you know nothing yet: $\sum\frac1n$ diverges.)

**The tests**

| Test | When to use | Rule |
|---|---|---|
| $p$-series | $\sum\frac1{n^p}$ | converges ⇔ $p>1$ |
| Geometric | $\sum q^n$ | converges ⇔ $\lvert q\rvert<1$ |
| Comparison | positive terms, "looks like" $\frac1{n^p}$ | $0\le a_n\le b_n$, $\sum b_n$ conv. ⇒ $\sum a_n$ conv. |
| Limit comparison | fractions of polynomials | $\frac{a_n}{b_n}\to c\in(0,\infty)$ ⇒ same behaviour |
| Ratio | $n!$, $a^n$ | $L=\lim\left\lvert\frac{a_{n+1}}{a_n}\right\rvert$: $L<1$ conv., $L>1$ div., $L=1$ no info |
| Root | $(\dots)^n$ | $L=\lim\sqrt[n]{\lvert a_n\rvert}$: same rule as ratio |
| Leibniz | alternating $\sum(-1)^nb_n$ | $b_n$ decreasing to $0$ ⇒ converges |

**Absolute convergence.** $\sum\lvert a_n\rvert<\infty$ ⇒ $\sum a_n$ converges. **Conditional convergence:** $\sum a_n$ converges but $\sum\lvert a_n\rvert$ does not. Example: $\sum\frac{(-1)^{n+1}}{n}=\ln2$.

**Fast rule for fractions of polynomials.** $\sum\frac{P(n)}{Q(n)}$ converges ⇔ $\deg Q-\deg P\ge2$.

**Worked example 1.** $\sum\frac{2n+1}{n^3+5}$: $\deg Q-\deg P=3-1=2$. Behaves like $\frac2{n^2}$ ⇒ converges.

**Worked example 2.** $\sum\frac{2^n}{n!}$. Ratio test:
$\frac{a_{n+1}}{a_n}=\frac{2^{n+1}}{(n+1)!}\cdot\frac{n!}{2^n}=\frac{2}{n+1}\to0<1$ ⇒ converges (the sum is $e^2-1$ from $n=1$).

**Values you should know**

| Series | Value |
|---|---|
| $\sum_{n=0}^\infty q^n$ | $\frac1{1-q}$, $\lvert q\rvert<1$ |
| $\sum_{n=1}^\infty q^n$ | $\frac{q}{1-q}$ |
| $\sum_{n=0}^\infty\frac{x^n}{n!}$ | $e^x$ |
| $\sum_{n=0}^\infty\frac{(-1)^n}{n!}$ | $e^{-1}$ |
| $\sum_{n=1}^\infty\frac1{n(n+1)}$ | $1$ (telescoping: $\frac1n-\frac1{n+1}$) |
| $\sum_{n=1}^\infty\frac1{n^2}$ | $\frac{\pi^2}{6}$ |
| $\sum_{n=1}^\infty\frac{(-1)^{n+1}}{n}$ | $\ln2$ |

**Official problem 15:** $\left(\sum\frac1{k!}\right)\left(\sum\frac{(-1)^k}{k!}\right)=e\cdot e^{-1}=1$.

> **Trap:** check the **starting index**. $\sum_{n=0}^\infty(\frac12)^n=2$, but $\sum_{n=1}^\infty(\frac12)^n=1$.

---

## 4. Power series and radius of convergence 🟢

**Idea.** A power series $\sum a_n(x-x_0)^n$ converges on an interval around $x_0$. Its half-width is the **radius** $R$.
- $\lvert x-x_0\rvert<R$: converges (absolutely).
- $\lvert x-x_0\rvert>R$: diverges.
- $\lvert x-x_0\rvert=R$: check each endpoint by hand.

**Formula.**
$$R=\lim_{n\to\infty}\left\lvert\frac{a_n}{a_{n+1}}\right\rvert\quad\text{or}\quad R=\frac{1}{\lim\sqrt[n]{\lvert a_n\rvert}}.$$

**Worked example.** $\sum_{n\ge1}\frac{x^n}{n\,3^n}$.
1. $a_n=\frac1{n3^n}$.
2. $\frac{a_n}{a_{n+1}}=\frac{(n+1)3^{n+1}}{n\,3^n}=3\cdot\frac{n+1}{n}\to3$. So $R=3$.
3. $x=3$: $\sum\frac1n$ diverges. $x=-3$: $\sum\frac{(-1)^n}{n}$ converges.
4. Interval of convergence: $[-3,3)$.

**Table**

| Series | $R$ |
|---|---|
| $\sum x^n$, $\sum\frac{x^n}{n}$, $\sum\frac{x^n}{n^2}$ | $1$ |
| $\sum\frac{x^n}{n!}$ | $\infty$ |
| $\sum n!\,x^n$ | $0$ |
| $\sum c^nx^n$ | $\frac1{\lvert c\rvert}$ |
| $\sum\frac{x^n}{c^n}$ | $\lvert c\rvert$ |

Inside $(x_0-R,x_0+R)$ you may differentiate and integrate term by term; $R$ stays the same.
> **Trap:** factors like $n$, $n^2$, $\frac1n$ do **not** change $R$. Only exponential factors $c^n$ and factorials do.

---

## 5. Taylor series 🟢

**Idea.** Near a point $a$, a smooth function looks like a polynomial. The Taylor polynomial is the best such polynomial.

**Formula.**
$$T_n(x)=\sum_{k=0}^n\frac{f^{(k)}(a)}{k!}(x-a)^k=f(a)+f'(a)(x-a)+\frac{f''(a)}{2}(x-a)^2+\dots$$
**Remainder (Lagrange):** $f(x)-T_n(x)=\dfrac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}$ for some $\xi$ between $a$ and $x$.

**Series at $a=0$ (Maclaurin) — learn by heart**

| $f(x)$ | Series | Valid for |
|---|---|---|
| $e^x$ | $1+x+\frac{x^2}{2}+\frac{x^3}{6}+\dots$ | all $x$ |
| $\sin x$ | $x-\frac{x^3}{6}+\frac{x^5}{120}-\dots$ | all $x$ |
| $\cos x$ | $1-\frac{x^2}{2}+\frac{x^4}{24}-\dots$ | all $x$ |
| $\frac1{1-x}$ | $1+x+x^2+x^3+\dots$ | $\lvert x\rvert<1$ |
| $\ln(1+x)$ | $x-\frac{x^2}{2}+\frac{x^3}{3}-\dots$ | $-1<x\le1$ |
| $(1+x)^\alpha$ | $1+\alpha x+\frac{\alpha(\alpha-1)}{2}x^2+\dots$ | $\lvert x\rvert<1$ |

**Worked example 1.** Coefficient of $x^3$ in $e^{2x}$.
1. Put $2x$ into the $e^x$ series: $\frac{(2x)^3}{3!}=\frac{8x^3}{6}$.
2. Coefficient $=\frac43$.

**Worked example 2 (limits).** $\lim_{x\to0}\frac{1-\cos x}{x^2}$.
1. $1-\cos x=\frac{x^2}{2}-\frac{x^4}{24}+\dots$
2. Divide by $x^2$: $\frac12-\frac{x^2}{24}+\dots\to\frac12$.

> **Trap:** do not forget the $k!$. The coefficient is $\frac{f^{(k)}(0)}{k!}$, not $f^{(k)}(0)$.

---

## 6. Derivatives in several variables 🟢

**Partial derivative** $\frac{\partial f}{\partial x}$ (also $f_x$): differentiate in $x$, treat all other variables as constants.

**Gradient** $\nabla f=(f_x,f_y)$: the vector of all partial derivatives. It points in the direction of fastest increase.

**Directional derivative** in direction $v$ with $\lVert v\rVert=1$: $D_vf=\nabla f\cdot v$.

**Worked example.** $f(x,y)=x^2y$, point $(1,2)$, direction $v=\frac15(3,4)$.
1. $f_x=2xy=4$, $f_y=x^2=1$. So $\nabla f(1,2)=(4,1)$.
2. $D_vf=(4,1)\cdot(\frac35,\frac45)=\frac{12+4}{5}=\frac{16}{5}$.

**Other objects**

| Name | What it is |
|---|---|
| Jacobian $J_f$ of $f:\mathbb R^n\to\mathbb R^m$ | $m\times n$ matrix of all $\frac{\partial f_i}{\partial x_j}$ |
| Hessian $H_f$ | matrix of second derivatives $\begin{pmatrix}f_{xx}&f_{xy}\\f_{yx}&f_{yy}\end{pmatrix}$ |
| Chain rule | $\frac{d}{dt}f(x(t),y(t))=f_x\,x'(t)+f_y\,y'(t)$ |
| Schwarz | if $f\in C^2$: $f_{xy}=f_{yx}$ (Hessian symmetric) |

**What implies what** (at a point):
$$\text{continuous partials }(C^1)\ \Rightarrow\ \text{differentiable}\ \Rightarrow\ \text{continuous}.$$
The arrows do **not** go back. Also: partials exist ⇏ continuous. Example: $f=\frac{xy}{x^2+y^2}$, $f(0,0)=0$. Both partials at $0$ are $0$, but on the line $y=x$ the value is $\frac12$.

### Local extrema (2 variables)
1. Solve $\nabla f=0$ → critical points.
2. Compute $D=f_{xx}f_{yy}-f_{xy}^2$ at each point.

| Result | Type |
|---|---|
| $D>0$, $f_{xx}>0$ | local minimum |
| $D>0$, $f_{xx}<0$ | local maximum |
| $D<0$ | saddle point |
| $D=0$ | test gives no answer |

**Worked example.** $f(x,y)=x^3-3x+y^2$.
1. $f_x=3x^2-3=0\Rightarrow x=\pm1$. $f_y=2y=0\Rightarrow y=0$.
2. $f_{xx}=6x$, $f_{yy}=2$, $f_{xy}=0$, so $D=12x$.
3. $(1,0)$: $D=12>0$, $f_{xx}=6>0$ → local min. $(-1,0)$: $D=-12<0$ → saddle.

- **Lagrange multipliers** (extremum of $f$ with $g=0$): solve $\nabla f=\lambda\nabla g$, $g=0$. Example: max of $xy$ on $x+y=1$ is at $x=y=\frac12$, value $\frac14$.
- **One-variable fact (official problem 22).** A polynomial with $d$ distinct real roots has $d-1$ critical points (Rolle); they alternate max/min.

> **Trap:** $D=0$ means "no information", **not** "saddle". Example: $x^4+y^4$ has a minimum at $0$ with $D=0$.

---

## 7. Integration in one variable 🟢

**Fundamental theorem (FTC).** If $F'=f$, then $\int_a^bf(x)\,dx=F(b)-F(a)$. And $\frac{d}{dx}\int_a^xf(t)\,dt=f(x)$.
With a variable limit: $\frac{d}{dx}\int_0^{g(x)}f(t)\,dt=f(g(x))\,g'(x)$.

**Main techniques**

| Technique | Formula | Use when |
|---|---|---|
| Substitution | $\int f(g(x))g'(x)dx=\int f(u)du$ | inner function and its derivative appear |
| Integration by parts | $\int u\,v'=uv-\int u'v$ | product like $x e^x$, $x\sin x$, $\ln x$ |

**Worked example (parts).** $\int_0^1xe^x\,dx$.
1. $u=x$, $v'=e^x$, so $u'=1$, $v=e^x$.
2. $=[xe^x]_0^1-\int_0^1e^x\,dx=e-(e-1)=1$.

**Worked example (substitution).** $\int_0^1 2x\,e^{x^2}dx$. Put $u=x^2$, $du=2x\,dx$: $\int_0^1e^u\,du=e-1$.

**Antiderivatives to know:** $\int x^n=\frac{x^{n+1}}{n+1}$ ($n\neq-1$), $\int\frac1x=\ln\lvert x\rvert$, $\int e^{ax}=\frac{e^{ax}}{a}$, $\int\frac{1}{1+x^2}=\arctan x$, $\int\sin x=-\cos x$, $\int\cos x=\sin x$.

**Improper integrals**

| Integral | Converges ⇔ |
|---|---|
| $\int_1^\infty\frac{dx}{x^p}$ | $p>1$ (value $\frac1{p-1}$) |
| $\int_0^1\frac{dx}{x^p}$ | $p<1$ (value $\frac1{1-p}$) |
| $\int_0^\infty e^{-ax}dx$, $a>0$ | always (value $\frac1a$) |
| $\int_{-\infty}^{\infty}e^{-x^2}dx$ | value $\sqrt\pi$ |

**Riemann integrable** on $[a,b]$: continuous, monotone, or bounded with finitely many jumps. Not integrable: Dirichlet function ($1$ on $\mathbb Q$, $0$ else).
Odd function on $[-a,a]$: $\int_{-a}^af=0$. Example: $\int_{-1}^1x^3\cos x\,dx=0$.

> **Trap:** $\int_{-1}^1\frac{1}{x^2}dx$ is **not** $-2$. The function blows up at $0$; the integral diverges.

---

## 8. Multiple integrals 🟢

**Idea.** Integrate one variable at a time, **from the inside out**. Inner limits may depend on outer variables.

**Fubini.** For continuous $f$ on a rectangle, the order does not matter:
$$\int_a^b\!\int_c^d f(x,y)\,dy\,dx=\int_c^d\!\int_a^b f(x,y)\,dx\,dy.$$
If $f(x,y)=g(x)h(y)$ on a rectangle: $\iint f=\left(\int g\right)\left(\int h\right)$.

**Worked example (official problem 24).** $\int_0^1\int_0^x\int_0^y yz\,dz\,dy\,dx$.
1. Inner: $\int_0^y yz\,dz=y\cdot\frac{y^2}{2}=\frac{y^3}{2}$.
2. Middle: $\int_0^x\frac{y^3}{2}dy=\frac{x^4}{8}$.
3. Outer: $\int_0^1\frac{x^4}{8}dx=\frac1{40}$.

**Worked example (triangle).** $\int_0^1\int_0^x(x+y)\,dy\,dx$.
1. Inner: $\left[xy+\frac{y^2}{2}\right]_0^x=\frac32x^2$.
2. Outer: $\int_0^1\frac32x^2dx=\frac12$.

**Swapping the order.** Draw the region first.
Region $0\le x\le y\le1$: $\int_0^1\int_x^1 f\,dy\,dx=\int_0^1\int_0^y f\,dx\,dy$.

**Change of variables.** $dx\,dy$ becomes $\lvert\det J\rvert\,du\,dv$.

| Coordinates | Map | Extra factor |
|---|---|---|
| Polar | $x=r\cos\theta,\ y=r\sin\theta$ | $r$ |
| Cylindrical | $(r\cos\theta,r\sin\theta,z)$ | $r$ |
| Spherical | $(\rho\sin\varphi\cos\theta,\rho\sin\varphi\sin\theta,\rho\cos\varphi)$ | $\rho^2\sin\varphi$ |
| Linear $x=Au$ | | $\lvert\det A\rvert$ |

**Worked example (polar).** $\iint_{x^2+y^2\le1}(x^2+y^2)\,dA$.
1. $x^2+y^2=r^2$, $dA=r\,dr\,d\theta$.
2. $\int_0^{2\pi}\int_0^1r^2\cdot r\,dr\,d\theta=2\pi\cdot\frac14=\frac\pi2$.

**Areas and volumes:** disc $\pi R^2$, ball $\frac43\pi R^3$, parallelepiped spanned by $a,b,c$: $\lvert\det(a\ b\ c)\rvert$.
> **Trap:** in polar coordinates, never forget the factor $r$. Without it the example above gives $\frac{2\pi}{3}$ (wrong).

---

## 9. Open, closed and compact sets 🟢

**Plain words** (in $\mathbb{R}$ or $\mathbb{R}^n$):
- **Open:** around each point of the set there is a small ball that is still inside the set. ("No boundary points included.")
- **Closed:** the set contains all its boundary points. Equivalent: if a sequence in the set converges, the limit is in the set.
- **Compact:** closed **and** bounded (Heine–Borel; true in $\mathbb R^n$).
- **Bounded:** fits inside some big ball.

**Examples in $\mathbb R$**

| Set | Open? | Closed? | Compact? |
|---|---|---|---|
| $(0,1)$ | yes | no | no |
| $[0,1]$ | no | yes | **yes** |
| $(0,1]$ | no | no | no |
| $[0,\infty)$ | no | yes | no (unbounded) |
| $\mathbb R$ | yes | yes | no |
| $\emptyset$ | yes | yes | yes |
| $\mathbb Z$ | no | yes | no |
| $\mathbb Q$ | no | no | no |
| finite set $\{1,2,5\}$ | no | yes | yes |
| $\{\frac1n:n\ge1\}$ | no | no ($0$ is missing) | no |
| $\{0\}\cup\{\frac1n:n\ge1\}$ | no | yes | yes |

**Fast rule with continuous functions.** If $g$ is continuous:
- $\{g<c\}$ is open, $\{g\le c\}$ and $\{g=c\}$ are closed.

**Worked example.** $A=\{(x,y):x^2+y^2\le4,\ y\ge0\}$ (a half disc).
1. $x^2+y^2\le4$ is closed, $y\ge0$ is closed. The intersection is closed.
2. It is inside the disc of radius 2, so bounded.
3. Closed + bounded ⇒ **compact**.

**Rules**
- Any union of open sets is open; a **finite** intersection of open sets is open. (Infinite fails: $\bigcap_n(-\frac1n,\frac1n)=\{0\}$.)
- Any intersection of closed sets is closed; a **finite** union of closed sets is closed.
- **Extreme value theorem:** a continuous function on a compact set has a max and a min.
- Interior, closure, boundary: for $[0,1)$: interior $(0,1)$, closure $[0,1]$, boundary $\{0,1\}$.

> **Trap:** "not open" does **not** mean "closed". $(0,1]$ and $\mathbb Q$ are neither.

---

## 10. Fourier series 🟡

**Idea.** Write a $2\pi$-periodic function as a sum of sines and cosines.
$$f(x)\sim\frac{a_0}{2}+\sum_{n\ge1}\left(a_n\cos nx+b_n\sin nx\right),\quad a_n=\frac1\pi\int_{-\pi}^{\pi}f(x)\cos nx\,dx,\quad b_n=\frac1\pi\int_{-\pi}^{\pi}f(x)\sin nx\,dx.$$

> **Must-know facts**
> 1. $f$ **even** ⇒ only cosines ($b_n=0$). $f$ **odd** ⇒ only sines ($a_n=0$).
> 2. $\frac{a_0}{2}$ = mean value of $f$ over one period.
> 3. At a jump, the series converges to the **midpoint** $\frac{f(x^-)+f(x^+)}{2}$.
> 4. $f(x)=x$ on $(-\pi,\pi)$: $b_n=\frac{2(-1)^{n+1}}{n}$, so $x\sim2\left(\sin x-\frac{\sin2x}{2}+\frac{\sin3x}{3}-\dots\right)$.
> 5. Coefficients go to $0$ (Riemann–Lebesgue). Parseval: $\frac1\pi\int_{-\pi}^\pi f^2=\frac{a_0^2}{2}+\sum(a_n^2+b_n^2)$.

> **Trap:** for $f(x)=x$ at $x=\pi$ the series gives $0$ (midpoint of the jump from $\pi$ to $-\pi$), not $\pi$.

---

## 11. Fourier and Laplace transforms 🟡

**Laplace transform:** $F(s)=\mathcal L\{f\}(s)=\int_0^\infty f(t)e^{-st}dt$. It turns linear ODEs into algebra.

> **Must-know facts (Laplace)**
>
> | $f(t)$ | $F(s)$ |
> |---|---|
> | $1$ | $\frac1s$ |
> | $t^n$ | $\frac{n!}{s^{n+1}}$ |
> | $e^{at}$ | $\frac1{s-a}$ |
> | $\sin\omega t$ | $\frac{\omega}{s^2+\omega^2}$ |
> | $\cos\omega t$ | $\frac{s}{s^2+\omega^2}$ |
> | $e^{at}f(t)$ | $F(s-a)$ (shift) |
> | $f'(t)$ | $sF(s)-f(0)$ |

- **Tiny example (Laplace).** $y'=-2y$, $y(0)=3$: $sY-3=-2Y\Rightarrow Y=\frac{3}{s+2}\Rightarrow y=3e^{-2t}$.
- **Fourier transform:** $\hat f(\omega)=\int_{-\infty}^\infty f(t)e^{-i\omega t}dt$ (other books use other constants).

> **Must-know facts (Fourier)**
> 1. It is linear. Derivative: $f'\mapsto i\omega\hat f$.
> 2. Convolution becomes product: $\widehat{f*g}=\hat f\,\hat g$.
> 3. $e^{-\lvert t\rvert}\mapsto\frac{2}{1+\omega^2}$. A Gaussian goes to a Gaussian.
> 4. Real even $f$ ⇒ $\hat f$ real and even.

> **Trap:** $\mathcal L\{\sin2t\}=\frac{2}{s^2+4}$, so $\frac{1}{s^2+4}$ comes from $\frac12\sin2t$ (don't lose the $\frac12$).

---

## 12. Banach and Hilbert spaces 🟡

**Plain words.**
- A **norm** $\lVert x\rVert$ measures length. **Complete** = every Cauchy sequence converges.
- **Banach space** = complete normed space.
- **Hilbert space** = complete space with an inner product $\langle x,y\rangle$ (and $\lVert x\rVert=\sqrt{\langle x,x\rangle}$).

> **Must-know facts**
> 1. Every Hilbert space is a Banach space. Not the other way round.
> 2. $\mathbb{R}^n$ with $\lVert\cdot\rVert_2$ is Hilbert. $\ell^2$ and $L^2[a,b]$ are Hilbert. $\ell^p$, $L^p$ for $p\ne2$ are Banach but not Hilbert.
> 3. $C[a,b]$ with the max-norm $\lVert f\rVert_\infty$ is Banach, not Hilbert.
> 4. A norm comes from an inner product ⇔ **parallelogram law** $\lVert x+y\rVert^2+\lVert x-y\rVert^2=2\lVert x\rVert^2+2\lVert y\rVert^2$.
> 5. Cauchy–Schwarz: $\lvert\langle x,y\rangle\rvert\le\lVert x\rVert\lVert y\rVert$.
> 6. In infinite dimensions, closed + bounded does **not** imply compact.

> **Trap:** "Hilbert" needs an inner product **and** completeness. Polynomials with the max-norm are not complete, so not Banach.

---

## Formula sheet

| Topic | Formula / fact |
|---|---|
| Min of $ax+\frac bx$ ($x>0$) | $2\sqrt{ab}$ at $x=\sqrt{b/a}$ |
| Key limits | $(1+\frac xn)^n\to e^x$, $\sqrt[n]n\to1$, $\frac{\sin x}{x}\to1$ |
| limsup / liminf | largest / smallest accumulation point |
| Term test | $a_n\not\to0$ ⇒ $\sum a_n$ diverges |
| $p$-series | $\sum\frac1{n^p}$ converges ⇔ $p>1$ |
| Geometric | $\sum_{n\ge0}q^n=\frac1{1-q}$, $\lvert q\rvert<1$ |
| Ratio test | $\lim\lvert a_{n+1}/a_n\rvert<1$ ⇒ converges |
| Radius | $R=\lim\lvert a_n/a_{n+1}\rvert$ |
| Taylor | $\sum\frac{f^{(k)}(a)}{k!}(x-a)^k$ |
| $e^x,\sin x,\cos x$ | $\sum\frac{x^n}{n!}$, $x-\frac{x^3}{6}+\dots$, $1-\frac{x^2}{2}+\dots$ |
| Directional derivative | $D_vf=\nabla f\cdot v$, $\lVert v\rVert=1$ |
| Extremum test | $D=f_{xx}f_{yy}-f_{xy}^2$: $>0$ & $f_{xx}>0$ min; $>0$ & $f_{xx}<0$ max; $<0$ saddle |
| Parts | $\int uv'=uv-\int u'v$ |
| Improper | $\int_1^\infty x^{-p}$ conv. ⇔ $p>1$; $\int_0^1x^{-p}$ conv. ⇔ $p<1$ |
| Polar / spherical | $r\,dr\,d\theta$ / $\rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta$ |
| Compact in $\mathbb R^n$ | closed + bounded |
| Fourier | odd ⇒ sines only; even ⇒ cosines only |
| Laplace | $\frac1s,\ \frac{n!}{s^{n+1}},\ \frac1{s-a},\ \frac{\omega}{s^2+\omega^2},\ \frac{s}{s^2+\omega^2}$; $f'\mapsto sF-f(0)$ |
| Hilbert | $\ell^2$, $L^2$; Banach not Hilbert: $\ell^1,\ell^\infty,(C,\lVert\cdot\rVert_\infty)$ |

---

## Practice MCQs

**Q1.** $\displaystyle\lim_{n\to\infty}\left(1+\frac2n\right)^n=$
A) $1$  B) $e$  C) $e^2$  D) $2$

<details><summary>Answer</summary>

**C** — Use $(1+\frac xn)^n\to e^x$ with $x=2$.

</details>

**Q2.** $\displaystyle\sum_{n=0}^\infty\left(\frac13\right)^n=$
A) $\frac32$  B) $\frac12$  C) $3$  D) $\frac23$

<details><summary>Answer</summary>

**A** — Geometric series from $n=0$: $\frac1{1-1/3}=\frac{1}{2/3}=\frac32$.

</details>

**Q3.** Which series converges?
A) $\sum\frac1n$  B) $\sum\frac1{\sqrt n}$  C) $\sum\frac{n}{n+1}$  D) $\sum\frac1{n^2}$

<details><summary>Answer</summary>

**D** — $p$-series with $p=2>1$. A: $p=1$, B: $p=\frac12$ diverge. C: terms $\to1\ne0$.

</details>

**Q4.** The minimum of $x+\frac4x$ for $x>0$ is
A) $2$  B) $4$  C) $5$  D) $8$

<details><summary>Answer</summary>

**B** — $\min(ax+\frac bx)=2\sqrt{ab}=2\sqrt4=4$, at $x=2$. Check: $2+2=4$.

</details>

**Q5.** For $f(x,y)=x^2y+y^3$, the value of $\frac{\partial f}{\partial x}(1,2)$ is
A) $13$  B) $12$  C) $4$  D) $2$

<details><summary>Answer</summary>

**C** — $f_x=2xy$ (treat $y$ as constant). At $(1,2)$: $2\cdot1\cdot2=4$.

</details>

**Q6.** $\displaystyle\lim_{x\to0}\frac{\sin 3x}{x}=$
A) $0$  B) $1$  C) $\frac13$  D) $3$

<details><summary>Answer</summary>

**D** — $\frac{\sin3x}{x}=3\cdot\frac{\sin3x}{3x}\to3\cdot1=3$.

</details>

**Q7.** The radius of convergence of $\displaystyle\sum_{n\ge0}\frac{x^n}{2^n}$ is
A) $2$  B) $\frac12$  C) $1$  D) $\infty$

<details><summary>Answer</summary>

**A** — It is geometric with $q=\frac x2$. It converges for $\lvert x/2\rvert<1$, i.e. $\lvert x\rvert<2$.

</details>

**Q8.** Which subset of $\mathbb R$ is compact?
A) $(0,1]$  B) $[0,\infty)$  C) $[0,1]\cup\{2\}$  D) $\mathbb Q\cap[0,1]$

<details><summary>Answer</summary>

**C** — Closed and bounded. A is not closed (0 missing), B is unbounded, D is not closed (limits like $\frac{1}{\sqrt2}$ missing).

</details>

**Q9.** $\displaystyle\int_0^1\!\int_0^2 xy\,dy\,dx=$
A) $\frac12$  B) $1$  C) $2$  D) $4$

<details><summary>Answer</summary>

**B** — Product on a rectangle: $\int_0^1x\,dx\cdot\int_0^2y\,dy=\frac12\cdot2=1$.

</details>

**Q10.** The Laplace transform of $e^{3t}$ is
A) $\frac1{s+3}$  B) $\frac1{s-3}$  C) $\frac3{s}$  D) $\frac{3}{s^2+9}$

<details><summary>Answer</summary>

**B** — $\mathcal L\{e^{at}\}=\frac1{s-a}$ with $a=3$ (for $s>3$).

</details>

**Q11.** The sequence $a_n=(-1)^n+\frac1n$ has $\limsup a_n$ equal to
A) $1$  B) $\frac32$  C) $0$  D) $2$

<details><summary>Answer</summary>

**A** — Even terms $1+\frac1n\to1$, odd terms $\to-1$. The largest accumulation point is $1$. $\frac32=a_2$ is the sup, not the limsup.

</details>

**Q12.** $\displaystyle\sum_{n=1}^\infty\frac{1}{n(n+1)}=$
A) $\frac12$  B) $2$  C) $1$  D) diverges

<details><summary>Answer</summary>

**C** — $\frac1{n(n+1)}=\frac1n-\frac1{n+1}$. Partial sums telescope to $1-\frac1{N+1}\to1$.

</details>

**Q13.** The coefficient of $x^3$ in the Maclaurin series of $e^{2x}$ is
A) $\frac16$  B) $\frac43$  C) $8$  D) $\frac23$

<details><summary>Answer</summary>

**B** — $e^{2x}=\sum\frac{(2x)^n}{n!}$. For $n=3$: $\frac{8}{6}=\frac43$.

</details>

**Q14.** $f(x,y)=x^2+y^2-2x+4y$ has at its critical point
A) a saddle point  B) a local max with value $5$  C) no critical point  D) a local min with value $-5$

<details><summary>Answer</summary>

**D** — $f_x=2x-2=0$, $f_y=2y+4=0$ ⇒ $(1,-2)$. $D=2\cdot2-0=4>0$, $f_{xx}=2>0$ ⇒ min. $f(1,-2)=1+4-2-8=-5$.

</details>

**Q15.** $\displaystyle\int_0^1 x e^x\,dx=$
A) $e$  B) $e-1$  C) $1$  D) $2e-1$

<details><summary>Answer</summary>

**C** — Parts: $[xe^x]_0^1-\int_0^1e^x\,dx=e-(e-1)=1$.

</details>

**Q16.** $\displaystyle\iint_{x^2+y^2\le1}(x^2+y^2)\,dA=$
A) $\pi$  B) $\frac{2\pi}{3}$  C) $\frac\pi4$  D) $\frac\pi2$

<details><summary>Answer</summary>

**D** — Polar: $\int_0^{2\pi}\int_0^1r^2\cdot r\,dr\,d\theta=2\pi\cdot\frac14=\frac\pi2$. Answer B forgets the factor $r$.

</details>

**Q17.** $\displaystyle\int_0^1\!\int_0^x (x+y)\,dy\,dx=$
A) $\frac12$  B) $\frac13$  C) $1$  D) $\frac32$

<details><summary>Answer</summary>

**A** — Inner: $\left[xy+\frac{y^2}{2}\right]_0^x=\frac32x^2$. Outer: $\int_0^1\frac32x^2dx=\frac12$.

</details>

**Q18.** The directional derivative of $f(x,y)=x^2y$ at $(1,2)$ in direction $v=\frac15(3,4)$ is
A) $4$  B) $\frac{16}{5}$  C) $\frac{11}{5}$  D) $5$

<details><summary>Answer</summary>

**B** — $\nabla f=(2xy,x^2)=(4,1)$. $D_vf=4\cdot\frac35+1\cdot\frac45=\frac{16}5$.

</details>

**Q19.** $\displaystyle\frac{d}{dx}\int_0^{x^2}e^t\,dt=$
A) $e^{x^2}$  B) $2x\,e^{x^2}$  C) $e^{x^2}-1$  D) $2x\,e^{x}$

<details><summary>Answer</summary>

**B** — FTC + chain rule: $f(g(x))\,g'(x)=e^{x^2}\cdot2x$. Check: the integral is $e^{x^2}-1$, its derivative is $2xe^{x^2}$.

</details>

**Q20.** Let $f(x)=x$ on $(-\pi,\pi)$, extended $2\pi$-periodically. Which Fourier coefficients are all zero?
A) $a_n$ (cosine coefficients)  B) $b_n$ (sine coefficients)  C) both  D) none

<details><summary>Answer</summary>

**A** — $f$ is odd, and $\cos nx$ is even, so $f(x)\cos nx$ is odd and its integral over $[-\pi,\pi]$ is $0$. Only sines remain.

</details>

**Q21.** Which space is a Hilbert space?
A) $\ell^1$  B) $C[0,1]$ with $\lVert f\rVert_\infty$  C) $\ell^\infty$  D) $\ell^2$

<details><summary>Answer</summary>

**D** — $\ell^2$ has the inner product $\sum x_ny_n$ and is complete. The others are Banach spaces, but their norms fail the parallelogram law.

</details>

**Q22.** $\displaystyle\int_0^1\!\int_x^1 f(x,y)\,dy\,dx$ is equal to
A) $\int_0^1\!\int_0^y f\,dx\,dy$  B) $\int_0^1\!\int_y^1 f\,dx\,dy$  C) $\int_0^1\!\int_0^1 f\,dx\,dy$  D) $\int_0^1\!\int_0^x f\,dx\,dy$

<details><summary>Answer</summary>

**A** — The region is $0\le x\le y\le1$. For fixed $y$, $x$ runs from $0$ to $y$.

</details>
