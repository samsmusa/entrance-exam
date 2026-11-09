# 1. Analysis

> **Official topics (Placement Test guide):** sequences and series, their convergence in metric spaces; open, closed and compact sets; continuity and differentiability, Jacobian matrix, Taylor expansion; Banach and Hilbert spaces; $L^p$ spaces; Fourier series and Laplace transform.
>
> **Exam:** 7 questions on this topic, 5 options each, about 85 seconds per question. Most questions test a **definition** or a **standard fact**; some need a 1–3 line calculation.
>
> **How to study this file:** every section is 🟢 (it is on the official list). Learn the definitions word for word, read the "Must-know facts", then do the MCQs. Time: about 5 hours + 1 hour MCQs.
>
> *Removed (not on the official list, or covered elsewhere):* AM–GM inequalities, one-variable integration techniques, multiple integrals, Fourier transform, 2-variable extremum test and Lagrange multipliers (→ [11-optimization.md](11-optimization.md)), countable sets (→ [03-discrete-mathematics.md](03-discrete-mathematics.md)), Riemann integrability (→ [07-measure-and-probability.md](07-measure-and-probability.md)).

## Contents
🟢 1. Metric spaces and convergence · 2. Sequences in $\mathbb R$: limits, limsup, liminf · 3. Series and convergence tests · 4. Power series · 5. Open, closed and compact sets · 6. Continuity · 7. Differentiability and the Jacobian matrix · 8. Taylor expansion · 9. Normed, Banach and Hilbert spaces · 10. $L^p$ spaces · 11. Fourier series · 12. Laplace transform
📋 Formula sheet · Practice MCQs (28 questions, 5 options)

---

## 1. Metric spaces and convergence 🟢

**Idea.** A metric $d(x,y)$ measures the distance between two points. With a distance you can say what "$x_n$ gets close to $x$" means, in any set, not only in $\mathbb R$.

**Definition.** A **metric** on a set $X$ is a map $d:X\times X\to[0,\infty)$ with
1. $d(x,y)=0\iff x=y$,
2. $d(x,y)=d(y,x)$ (symmetry),
3. $d(x,z)\le d(x,y)+d(y,z)$ (triangle inequality).

**Examples**

| Space | Metric |
|---|---|
| $\mathbb R^d$ | Euclidean $d(x,y)=\lVert x-y\rVert_2=\sqrt{\sum(x_i-y_i)^2}$ |
| $\mathbb R^d$ | $\lVert x-y\rVert_1=\sum\lvert x_i-y_i\rvert$, $\ \lVert x-y\rVert_\infty=\max\lvert x_i-y_i\rvert$ |
| any normed space | $d(x,y)=\lVert x-y\rVert$ |
| $C[a,b]$ | $d(f,g)=\max_{x}\lvert f(x)-g(x)\rvert$ (sup metric) |
| any set | discrete metric: $d(x,y)=1$ if $x\ne y$, $0$ if $x=y$ |

**Not metrics:** $\lvert x-y\rvert^2$ (fails the triangle inequality: $d(0,2)=4>d(0,1)+d(1,2)=2$), $x-y$ (can be negative), $\lvert x^2-y^2\rvert$ ($d(1,-1)=0$ but $1\ne-1$).

**Convergence.** $x_n\to x$ in $(X,d)$ means
$$d(x_n,x)\to0,\quad\text{i.e. for every }\varepsilon>0\text{ there is }N\text{ with }d(x_n,x)<\varepsilon\text{ for all }n\ge N.$$
In $\mathbb R^d$ this is $\lVert x_n-x\rVert\to0$ (**official example 1**), and it holds ⇔ **each component** converges. All norms on $\mathbb R^d$ give the same convergent sequences.

**Worked example.** $x_n=\left(\frac1n,\ \left(1+\frac1n\right)^n\right)\in\mathbb R^2$.
1. First component $\to0$, second component $\to e$.
2. So $x_n\to(0,e)$.

**Cauchy sequences and completeness**
- $(x_n)$ is **Cauchy** if for every $\varepsilon>0$ there is $N$ with $d(x_n,x_m)<\varepsilon$ for all $n,m\ge N$.
- Convergent ⇒ Cauchy. Cauchy ⇒ bounded.
- $(X,d)$ is **complete** if every Cauchy sequence converges **in $X$**.

| Complete | Not complete |
|---|---|
| $\mathbb R$, $\mathbb R^d$, $[0,1]$, $\mathbb Z$, closed subsets of $\mathbb R^d$ | $\mathbb Q$ ($1,\ 1.4,\ 1.41,\dots\to\sqrt2\notin\mathbb Q$), $(0,1)$ ($\frac1n\to0\notin(0,1)$) |
| $C[a,b]$ with the sup metric | $C[a,b]$ with the $L^2$ metric, polynomials with the sup metric |

**Must-know facts**
> 1. A limit is unique. Convergent ⇒ bounded (bounded does **not** imply convergent: $(-1)^n$).
> 2. **Bolzano–Weierstrass:** every bounded sequence in $\mathbb R^d$ has a convergent subsequence.
> 3. Discrete metric: $x_n\to x$ ⇔ $x_n=x$ for all large $n$ (eventually constant).
> 4. **Banach fixed-point theorem:** a contraction $T$ ($d(Tx,Ty)\le q\,d(x,y)$, $q<1$) on a **complete** metric space has exactly one fixed point, and $x_{n+1}=T(x_n)$ converges to it from any start.

> **Trap:** "$x_n=x$ for infinitely many $n$" is **not** convergence: $0,1,0,1,\dots$ hits $0$ infinitely often but does not converge.

---

## 2. Sequences in $\mathbb R$: limits, limsup, liminf 🟢

**Standard limits** ($n\to\infty$):

| Sequence | Limit |
|---|---|
| $\frac1n$, $q^n$ with $\lvert q\rvert<1$ | $0$ |
| $\sqrt[n]{n}$, $\sqrt[n]{a}$ ($a>0$) | $1$ |
| $\left(1+\frac xn\right)^n$ | $e^x$ (so $(1+\frac1n)^n\to e$, $(1-\frac1n)^n\to\frac1e$) |
| $\frac{n^k}{a^n}$ ($a>1$), $\frac{a^n}{n!}$, $\frac{\ln n}{n}$ | $0$ |
| $\frac{\sin x}{x}$ as $x\to0$ | $1$ |

**Growth order** (slow → fast): $\ln n \ll n \ll n^2 \ll 2^n \ll n! \ll n^n$.

**Rational sequences.** Divide by the highest power of $n$: $\dfrac{3n^2+1}{5n^2-n}\to\dfrac35$.

**Monotone convergence:** monotone **and** bounded ⇒ convergent.

**Accumulation point** of a sequence = limit of some subsequence.
- $\limsup a_n$ = the **largest** accumulation point, $\liminf a_n$ = the **smallest**.
- $a_n$ converges ⇔ $\limsup=\liminf$ (finite).

**Worked example.** $x_n=\left(-1-\frac1n\right)^n=(-1)^n\left(1+\frac1n\right)^n$.
1. $\left(1+\frac1n\right)^n\to e$.
2. Even $n$: $x_n\to e$. Odd $n$: $x_n\to-e$.
3. $\limsup=e$, $\liminf=-e$; the sequence diverges.

> **Trap:** $\sup a_n\ne\limsup a_n$ in general. For $a_n=(-1)^n+\frac1n$: $\sup=a_2=1.5$, but $\limsup=1$. Changing finitely many terms never changes $\limsup$. Also: "$1^\infty$" is not $1$ — $(1+\frac1n)^n\to e$.

---

## 3. Series and convergence tests 🟢

**Idea.** $\sum_{n=1}^\infty a_n$ converges if the partial sums $s_N=a_1+\dots+a_N$ converge.

**Step 0 — term test.** If $a_n\not\to0$, the series **diverges**. (If $a_n\to0$ you know nothing yet: $\sum\frac1n$ diverges.)

| Test | When to use | Rule |
|---|---|---|
| $p$-series | $\sum\frac1{n^p}$ | converges ⇔ $p>1$ |
| Geometric | $\sum q^n$ | converges ⇔ $\lvert q\rvert<1$ |
| Comparison | positive terms | $0\le a_n\le b_n$, $\sum b_n$ conv. ⇒ $\sum a_n$ conv. |
| Limit comparison | fractions of polynomials | $\frac{a_n}{b_n}\to c\in(0,\infty)$ ⇒ same behaviour |
| Ratio | $n!$, $a^n$ | $L=\lim\left\lvert\frac{a_{n+1}}{a_n}\right\rvert$: $L<1$ conv., $L>1$ div., $L=1$ no info |
| Root | $(\dots)^n$ | $L=\lim\sqrt[n]{\lvert a_n\rvert}$: same rule |
| Leibniz | alternating $\sum(-1)^nb_n$ | $b_n$ decreasing to $0$ ⇒ converges |

**Absolute convergence** ($\sum\lvert a_n\rvert<\infty$) ⇒ convergence. **Conditional:** $\sum\frac{(-1)^{n+1}}{n}=\ln2$ converges, $\sum\frac1n$ does not.
In a Banach space (e.g. $\mathbb R^d$): $\sum\lVert x_n\rVert<\infty$ ⇒ $\sum x_n$ converges.

**Fast rule.** $\sum\frac{P(n)}{Q(n)}$ (polynomials) converges ⇔ $\deg Q-\deg P\ge2$.

**Worked example.** $\sum\frac{2^n}{n!}$: $\frac{a_{n+1}}{a_n}=\frac{2}{n+1}\to0<1$ ⇒ converges.

| Series | Value |
|---|---|
| $\sum_{n=0}^\infty q^n$ | $\frac1{1-q}$, $\lvert q\rvert<1$ |
| $\sum_{n=0}^\infty\frac{x^n}{n!}$ | $e^x$ |
| $\sum_{n=1}^\infty\frac1{n(n+1)}$ | $1$ (telescoping) |
| $\sum_{n=1}^\infty\frac1{n^2}$ | $\frac{\pi^2}{6}$ |
| $\sum_{n=1}^\infty\frac{(-1)^{n+1}}{n}$ | $\ln2$ |

> **Trap:** check the **starting index**. $\sum_{n=0}^\infty(\frac12)^n=2$, but $\sum_{n=1}^\infty(\frac12)^n=1$.

---

## 4. Power series 🟢

$\sum a_n(x-x_0)^n$ converges absolutely for $\lvert x-x_0\rvert<R$ and diverges for $\lvert x-x_0\rvert>R$. At $\lvert x-x_0\rvert=R$: check each endpoint by hand.
$$R=\lim_{n\to\infty}\left\lvert\frac{a_n}{a_{n+1}}\right\rvert\quad\text{or}\quad R=\frac{1}{\limsup\sqrt[n]{\lvert a_n\rvert}}.$$

**Worked example.** $\sum_{n\ge1}\frac{x^n}{n\,3^n}$: $\frac{a_n}{a_{n+1}}=3\cdot\frac{n+1}{n}\to3$, so $R=3$. At $x=3$: $\sum\frac1n$ diverges; at $x=-3$: alternating, converges. Interval $[-3,3)$.

| Series | $R$ |
|---|---|
| $\sum x^n$, $\sum\frac{x^n}{n}$, $\sum\frac{x^n}{n^2}$ | $1$ |
| $\sum\frac{x^n}{n!}$ | $\infty$ |
| $\sum n!\,x^n$ | $0$ |
| $\sum c^nx^n$ | $\frac1{\lvert c\rvert}$ |

Inside the interval you may differentiate and integrate term by term; $R$ stays the same.
> **Trap:** factors $n$, $n^2$, $\frac1n$ do **not** change $R$. Only $c^n$ and factorials do.

---

## 5. Open, closed and compact sets 🟢

Let $(X,d)$ be a metric space. **Open ball:** $B(x,r)=\{y:d(x,y)<r\}$.
- **Open:** every point of $A$ has a ball $B(x,r)\subseteq A$.
- **Closed:** the complement is open. Equivalent: if $x_n\in A$ and $x_n\to x$, then $x\in A$.
- **Bounded:** $A\subseteq B(x,R)$ for some $x,R$.
- **Compact:** every sequence in $A$ has a subsequence converging **in $A$** (in metric spaces ⇔ every open cover has a finite subcover).
- **Heine–Borel (only in $\mathbb R^d$):** compact ⇔ closed **and** bounded.

**Examples in $\mathbb R$**

| Set | Open? | Closed? | Compact? |
|---|---|---|---|
| $(0,1)$ | yes | no | no |
| $[0,1]$ | no | yes | **yes** |
| $(0,1]$ | no | no | no |
| $[0,\infty)$ | no | yes | no (unbounded) |
| $\mathbb R$, $\emptyset$ | yes | yes | $\mathbb R$ no, $\emptyset$ yes |
| $\mathbb Z$ | no | yes | no |
| $\mathbb Q$ | no | no | no |
| finite set | no | yes | yes |
| $\{\frac1n:n\ge1\}$ | no | no ($0$ missing) | no |
| $\{0\}\cup\{\frac1n:n\ge1\}$ | no | yes | yes |

**Fast rule.** If $g$ is continuous: $\{g<c\}$ is open; $\{g\le c\}$ and $\{g=c\}$ are closed.
Example: half disc $\{x^2+y^2\le4,\ y\ge0\}$ is closed (two "$\le$" conditions) and bounded ⇒ compact.

**Rules**
- Any union of open sets is open; **finite** intersections of open sets are open ($\bigcap_n(-\frac1n,\frac1n)=\{0\}$ is not open).
- Any intersection of closed sets is closed; **finite** unions of closed sets are closed.
- Compact ⇒ closed and bounded, in **every** metric space. A closed subset of a compact set is compact.
- Interior / closure / boundary of $[0,1)$: $(0,1)$ / $[0,1]$ / $\{0,1\}$.

> **Trap 1:** "not open" does **not** mean "closed": $(0,1]$ and $\mathbb Q$ are neither.
> **Trap 2:** in infinite dimensions, closed + bounded ⇏ compact. The closed unit ball in $\ell^2$ is not compact: $e_1,e_2,\dots$ have $\lVert e_n-e_m\rVert=\sqrt2$, so no subsequence converges.

---

## 6. Continuity 🟢

**Definition ($\varepsilon$–$\delta$).** $f:X\to Y$ is continuous at $x_0$ if for every $\varepsilon>0$ there is $\delta>0$ with $d(x,x_0)<\delta\Rightarrow d(f(x),f(x_0))<\varepsilon$.

**Equivalent forms**
- **Sequences:** $x_n\to x_0\Rightarrow f(x_n)\to f(x_0)$.
- **Topology:** preimages of open sets are open (preimages of closed sets are closed).

**Must-know facts**
> 1. Sums, products, compositions of continuous functions are continuous (quotients where the denominator $\ne0$).
> 2. **Compact image:** $f$ continuous, $K$ compact ⇒ $f(K)$ compact. Hence the **extreme value theorem**: on a compact set, $f$ attains its max and min.
> 3. **Intermediate value theorem:** $f:[a,b]\to\mathbb R$ continuous takes every value between $f(a)$ and $f(b)$.
> 4. **Uniformly continuous:** one $\delta$ works for all points. Lipschitz ⇒ uniformly continuous ⇒ continuous. On a **compact** set, continuous ⇒ uniformly continuous.
> 5. Counterexamples: $\frac1x$ on $(0,1]$ is continuous but unbounded and not uniformly continuous; $x^2$ on $\mathbb R$ is not uniformly continuous.

**Several variables.** To show $f$ is **not** continuous at $0$, find two paths with different limits.
Example: $f(x,y)=\frac{xy}{x^2+y^2}$, $f(0,0)=0$. On $y=0$: $f=0$. On $y=x$: $f=\frac12$. Not continuous at $(0,0)$.

> **Trap:** continuous on $(0,1)$ does not mean bounded or attains a max — the domain must be compact.

---

## 7. Differentiability and the Jacobian matrix 🟢

**One variable.** $f'(x_0)=\lim_{h\to0}\frac{f(x_0+h)-f(x_0)}{h}$. Differentiable ⇒ continuous; not conversely ($\lvert x\rvert$ at $0$).

**Several variables.** $f:\mathbb R^n\to\mathbb R^m$ is **(totally) differentiable** at $x$ if there is a linear map $Df(x)$ with
$$f(x+h)=f(x)+Df(x)\,h+o(\lVert h\rVert).$$
The matrix of $Df(x)$ is the **Jacobian matrix** ($m\times n$, row $i$ = gradient of $f_i$):
$$J_f(x)=\begin{pmatrix}\frac{\partial f_1}{\partial x_1}&\cdots&\frac{\partial f_1}{\partial x_n}\\\vdots&&\vdots\\\frac{\partial f_m}{\partial x_1}&\cdots&\frac{\partial f_m}{\partial x_n}\end{pmatrix}.$$
For $m=1$ the Jacobian is the row $\nabla f^T$ (gradient).

**Worked example.** $f(x,y)=(x^2y,\ x+\sin y)$ at $(1,0)$.
1. $J_f=\begin{pmatrix}2xy&x^2\\1&\cos y\end{pmatrix}$.
2. At $(1,0)$: $J_f=\begin{pmatrix}0&1\\1&1\end{pmatrix}$, $\det J_f=-1$.

**Rules**

| Name | Formula |
|---|---|
| Chain rule | $J_{g\circ f}(x)=J_g(f(x))\,J_f(x)$ (matrix product, order matters) |
| Directional derivative | $D_vf=\nabla f\cdot v$, $\lVert v\rVert=1$; $\nabla f$ points to the fastest increase |
| Hessian | $H_f=\left(\frac{\partial^2f}{\partial x_i\partial x_j}\right)$; symmetric if $f\in C^2$ (Schwarz) |
| Inverse function theorem | $f\in C^1$, $n=m$, $\det J_f(x_0)\ne0$ ⇒ $f$ locally invertible, $J_{f^{-1}}=J_f^{-1}$ |
| Change of variables | $dx\,dy=\lvert\det J\rvert\,du\,dv$; polar coordinates: $\det J=r$ |

**What implies what** (at a point):
$$\text{continuous partials }(C^1)\ \Rightarrow\ \text{differentiable}\ \Rightarrow\ \text{continuous and partials exist}.$$
No arrow goes back. Partials can exist without continuity: $\frac{xy}{x^2+y^2}$ from section 6 has $f_x(0,0)=f_y(0,0)=0$.

**Critical point:** $\nabla f(x_0)=0$. Classification with the Hessian → [11-optimization.md](11-optimization.md).

> **Trap:** the Jacobian of $f:\mathbb R^n\to\mathbb R^m$ is $m\times n$ (rows = output components), not $n\times m$.

---

## 8. Taylor expansion 🟢

**One variable**
$$f(x)=\sum_{k=0}^n\frac{f^{(k)}(a)}{k!}(x-a)^k+R_n,\qquad R_n=\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}\ (\xi\text{ between }a,x).$$

| $f(x)$ | Series at $0$ | Valid for |
|---|---|---|
| $e^x$ | $1+x+\frac{x^2}{2}+\frac{x^3}{6}+\dots$ | all $x$ |
| $\sin x$ | $x-\frac{x^3}{6}+\frac{x^5}{120}-\dots$ | all $x$ |
| $\cos x$ | $1-\frac{x^2}{2}+\frac{x^4}{24}-\dots$ | all $x$ |
| $\frac1{1-x}$ | $1+x+x^2+\dots$ | $\lvert x\rvert<1$ |
| $\ln(1+x)$ | $x-\frac{x^2}{2}+\frac{x^3}{3}-\dots$ | $-1<x\le1$ |
| $(1+x)^\alpha$ | $1+\alpha x+\frac{\alpha(\alpha-1)}{2}x^2+\dots$ | $\lvert x\rvert<1$ |

**Worked examples.**
- Coefficient of $x^3$ in $e^{2x}$: $\frac{(2x)^3}{3!}=\frac{8}{6}x^3$, so $\frac43$.
- $\lim_{x\to0}\frac{1-\cos x}{x^2}$: $1-\cos x=\frac{x^2}{2}-\dots$, limit $\frac12$.

**Several variables (second order)**
$$f(x+h)=f(x)+\nabla f(x)\cdot h+\tfrac12\,h^TH_f(x)\,h+o(\lVert h\rVert^2).$$
**Worked example.** $f(x,y)=e^x\cos y$ at $(0,0)$.
1. $f=1$, $f_x=e^x\cos y=1$, $f_y=-e^x\sin y=0$.
2. $f_{xx}=1$, $f_{yy}=-e^x\cos y=-1$, $f_{xy}=-e^x\sin y=0$.
3. $T_2=1+x+\frac12(x^2-y^2)$.

> **Trap:** do not forget the $k!$ (coefficient is $\frac{f^{(k)}(0)}{k!}$) and the $\frac12$ in front of the Hessian term.

---

## 9. Normed, Banach and Hilbert spaces 🟢

**Norm** on a vector space $V$: $\lVert x\rVert\ge0$ with $\lVert x\rVert=0\iff x=0$; $\lVert\alpha x\rVert=\lvert\alpha\rvert\lVert x\rVert$; $\lVert x+y\rVert\le\lVert x\rVert+\lVert y\rVert$. Every norm gives a metric $d(x,y)=\lVert x-y\rVert$.

**Inner product** $\langle x,y\rangle$: linear in each argument (conjugate-linear in one, over $\mathbb C$), symmetric ($\langle x,y\rangle=\overline{\langle y,x\rangle}$), $\langle x,x\rangle>0$ for $x\ne0$. It gives the norm $\lVert x\rVert=\sqrt{\langle x,x\rangle}$.

**Definitions (official example 2)**
- **Banach space** = complete normed space.
- **Hilbert space** = complete inner product space.

> **Must-know facts**
> 1. Every Hilbert space is Banach; not conversely.
> 2. Hilbert: $\mathbb R^n$ with $\lVert\cdot\rVert_2$, $\ell^2$, $L^2[a,b]$. Banach but **not** Hilbert: $\ell^1$, $\ell^\infty$, $L^p$ for $p\ne2$, $C[a,b]$ with $\lVert\cdot\rVert_\infty$.
> 3. A norm comes from an inner product ⇔ **parallelogram law** $\lVert x+y\rVert^2+\lVert x-y\rVert^2=2\lVert x\rVert^2+2\lVert y\rVert^2$.
> 4. **Cauchy–Schwarz:** $\lvert\langle x,y\rangle\rvert\le\lVert x\rVert\lVert y\rVert$.
> 5. **Finite dimension:** every normed space is complete (Banach), all norms are equivalent, closed + bounded ⇔ compact. In infinite dimension the closed unit ball is **never** compact.
> 6. Not complete: polynomials with $\lVert\cdot\rVert_\infty$ (limit $e^x$ is not a polynomial); $C[0,1]$ with the $L^2$ norm (inner product space, but not Hilbert).
> 7. Hilbert space tools: **orthonormal basis** $(e_n)$ with $x=\sum\langle x,e_n\rangle e_n$ and **Parseval** $\lVert x\rVert^2=\sum\lvert\langle x,e_n\rangle\rvert^2$; **projection theorem:** every closed subspace $M$ gives $H=M\oplus M^\perp$; **Riesz:** every continuous linear functional is $x\mapsto\langle x,y\rangle$ for one $y$.
> 8. A linear map between normed spaces is continuous ⇔ bounded ($\lVert Tx\rVert\le C\lVert x\rVert$).

> **Trap:** Hilbert needs an inner product **and** completeness. "Complete normed space" alone is Banach.

---

## 10. $L^p$ spaces 🟢

**Definition.** For $1\le p<\infty$ and a measure space (e.g. $[a,b]$ or $\mathbb R$ with Lebesgue measure):
$$\lVert f\rVert_p=\left(\int\lvert f\rvert^p\,d\mu\right)^{1/p},\qquad L^p=\{f\text{ measurable}:\lVert f\rVert_p<\infty\}.$$
$\lVert f\rVert_\infty$ = essential supremum (sup ignoring null sets). Functions that agree **almost everywhere** are identified (they are the same element of $L^p$).
Sequence version: $\ell^p=\{(x_n):\sum\lvert x_n\rvert^p<\infty\}$.

**Worked example.** $f(x)=x$ on $[0,1]$: $\lVert f\rVert_2=\left(\int_0^1x^2dx\right)^{1/2}=\frac1{\sqrt3}$, $\lVert f\rVert_1=\frac12$, $\lVert f\rVert_\infty=1$.

> **Must-know facts**
> 1. **Riesz–Fischer:** $L^p$ is a Banach space for $1\le p\le\infty$.
> 2. Only $L^2$ is a Hilbert space, with $\langle f,g\rangle=\int f\bar g$.
> 3. **Hölder:** $\lVert fg\rVert_1\le\lVert f\rVert_p\lVert g\rVert_q$ with $\frac1p+\frac1q=1$ (conjugate exponents; $p=2,q=2$ is Cauchy–Schwarz; $p=1,q=\infty$).
> 4. **Minkowski:** $\lVert f+g\rVert_p\le\lVert f\rVert_p+\lVert g\rVert_p$ (the triangle inequality). For $p<1$ this fails, so $\lVert\cdot\rVert_p$ is not a norm.
> 5. **Inclusions on a finite measure space** (e.g. $[0,1]$): $L^\infty\subset L^2\subset L^1$ ($p\le q\Rightarrow L^q\subset L^p$).
> 6. **For sequences it is the other way:** $\ell^1\subset\ell^2\subset\ell^\infty$.
> 7. On $\mathbb R$ (infinite measure) there is **no** inclusion either way.
> 8. Continuous functions (with compact support) are dense in $L^p$ for $p<\infty$. Dual space: $(L^p)^*=L^q$ for $1\le p<\infty$.

**Examples to remember**
- $f(x)=x^{-1/2}$ on $(0,1)$: $\int_0^1x^{-1/2}dx=2<\infty$, so $f\in L^1$; $\int_0^1x^{-1}dx=\infty$, so $f\notin L^2$.
- $x_n=\frac1n$: $\sum\frac1{n^2}<\infty$ so $(x_n)\in\ell^2$; $\sum\frac1n=\infty$ so $(x_n)\notin\ell^1$.

> **Trap:** the inclusion direction flips between $L^p[0,1]$ (big $p$ ⊂ small $p$) and $\ell^p$ (small $p$ ⊂ big $p$).

---

## 11. Fourier series 🟢

**Real form** for a $2\pi$-periodic $f$:
$$f(x)\sim\frac{a_0}{2}+\sum_{n\ge1}\left(a_n\cos nx+b_n\sin nx\right),\quad a_n=\frac1\pi\int_{-\pi}^{\pi}f(x)\cos nx\,dx,\quad b_n=\frac1\pi\int_{-\pi}^{\pi}f(x)\sin nx\,dx.$$
**Complex form:** $f\sim\sum_{n\in\mathbb Z}c_ne^{inx}$, $c_n=\frac1{2\pi}\int_{-\pi}^{\pi}f(x)e^{-inx}dx$.
**Period $2L$:** replace $nx$ by $\frac{n\pi x}{L}$ and $\frac1\pi$ by $\frac1L$.

> **Must-know facts**
> 1. $f$ **even** ⇒ only cosines ($b_n=0$). $f$ **odd** ⇒ only sines ($a_n=0$).
> 2. $\frac{a_0}{2}$ = mean value of $f$ over one period.
> 3. **Dirichlet:** $f$ piecewise $C^1$ ⇒ the series converges at every $x$ to $\frac{f(x^-)+f(x^+)}{2}$ (midpoint at jumps, $f(x)$ where continuous). Near a jump there is a ~9% overshoot (**Gibbs phenomenon**).
> 4. $f$ continuous, periodic, piecewise $C^1$ ⇒ the series converges **uniformly**.
> 5. **$L^2$ theory:** $\{\frac{1}{\sqrt{2\pi}}e^{inx}\}$ is an orthonormal basis of $L^2(-\pi,\pi)$; for every $f\in L^2$ the series converges **in $L^2$**. **Parseval:** $\frac1\pi\int_{-\pi}^\pi f^2=\frac{a_0^2}{2}+\sum(a_n^2+b_n^2)$.
> 6. **Riemann–Lebesgue:** $a_n,b_n\to0$. Smoother $f$ ⇒ faster decay (jump ⇒ $\sim\frac1n$).
> 7. $f(x)=x$ on $(-\pi,\pi)$: $x\sim2\left(\sin x-\frac{\sin2x}{2}+\frac{\sin3x}{3}-\dots\right)$.
> 8. Square wave ($-1$ on $(-\pi,0)$, $1$ on $(0,\pi)$): $\frac4\pi\left(\sin x+\frac{\sin3x}{3}+\frac{\sin5x}{5}+\dots\right)$.

Fourier series are used to solve the heat and wave equations by separation of variables → [05-differential-equations.md](05-differential-equations.md).

> **Trap:** for $f(x)=x$ at $x=\pi$ the series gives $0$ (midpoint of the jump from $\pi$ to $-\pi$), not $\pi$.

---

## 12. Laplace transform 🟢

**Definition.** $F(s)=\mathcal L\{f\}(s)=\int_0^\infty f(t)e^{-st}dt$. It exists for $s$ large enough if $f$ is piecewise continuous and of exponential order ($\lvert f(t)\rvert\le Me^{ct}$). It is **linear** and turns linear ODEs with constant coefficients into algebra.

| $f(t)$ | $F(s)$ |
|---|---|
| $1$ | $\frac1s$ |
| $t^n$ | $\frac{n!}{s^{n+1}}$ |
| $e^{at}$ | $\frac1{s-a}$ |
| $\sin\omega t$ | $\frac{\omega}{s^2+\omega^2}$ |
| $\cos\omega t$ | $\frac{s}{s^2+\omega^2}$ |

| Rule | Formula |
|---|---|
| Shift in $s$ | $e^{at}f(t)\mapsto F(s-a)$ |
| Shift in $t$ | $u(t-a)f(t-a)\mapsto e^{-as}F(s)$ ($u$ = Heaviside step) |
| First derivative | $f'\mapsto sF(s)-f(0)$ |
| Second derivative | $f''\mapsto s^2F(s)-sf(0)-f'(0)$ |
| Multiply by $t$ | $tf(t)\mapsto-F'(s)$ |
| Convolution | $(f*g)(t)=\int_0^tf(\tau)g(t-\tau)d\tau\mapsto F(s)G(s)$ |

**Worked example.** $y''+y=0$, $y(0)=0$, $y'(0)=1$.
1. Transform: $s^2Y-s\cdot0-1+Y=0$.
2. $Y=\frac1{s^2+1}$.
3. Table: $y(t)=\sin t$.

**Tiny example.** $y'=-2y$, $y(0)=3$: $sY-3=-2Y\Rightarrow Y=\frac3{s+2}\Rightarrow y=3e^{-2t}$.

> **Trap:** $\mathcal L\{\sin2t\}=\frac2{s^2+4}$, so $\frac1{s^2+4}$ is the transform of $\frac12\sin2t$.

---

## Formula sheet

| Topic | Formula / fact |
|---|---|
| Metric | $d\ge0$, $d=0\iff x=y$, symmetric, triangle inequality |
| Convergence | $x_n\to x\iff d(x_n,x)\to0$; in $\mathbb R^d$: componentwise |
| Complete | every Cauchy sequence converges; $\mathbb R^d$ yes, $\mathbb Q$, $(0,1)$ no |
| Key limits | $(1+\frac xn)^n\to e^x$, $\sqrt[n]n\to1$, $\frac{\sin x}{x}\to1$ |
| limsup / liminf | largest / smallest accumulation point |
| Series | term test; $\sum\frac1{n^p}$ conv. ⇔ $p>1$; $\sum q^n=\frac1{1-q}$; ratio test |
| Radius | $R=\lim\lvert a_n/a_{n+1}\rvert$ |
| Compact | sequentially compact; in $\mathbb R^d$ ⇔ closed + bounded |
| Continuous | preimage of open is open; compact → compact; max/min on compact sets |
| Jacobian | $m\times n$, $(J_f)_{ij}=\partial f_i/\partial x_j$; $J_{g\circ f}=J_g(f)\,J_f$ |
| Implications | $C^1$ ⇒ differentiable ⇒ continuous |
| Taylor | $f(x+h)\approx f+\nabla f\cdot h+\frac12h^THh$ |
| Banach / Hilbert | complete normed / complete inner product space |
| Inner product norm | parallelogram law |
| $L^p$ | Banach $1\le p\le\infty$; Hilbert only $p=2$; Hölder $\frac1p+\frac1q=1$ |
| Inclusions | $L^2[0,1]\subset L^1[0,1]$; $\ell^1\subset\ell^2$ |
| Fourier | odd ⇒ sines; even ⇒ cosines; jump ⇒ midpoint |
| Laplace | $\frac1s,\ \frac{n!}{s^{n+1}},\ \frac1{s-a},\ \frac{\omega}{s^2+\omega^2},\ \frac{s}{s^2+\omega^2}$; $f'\mapsto sF-f(0)$ |

---

## Practice MCQs

**Q1.** (official example 1) A sequence $(x_n)$ in $\mathbb R^d$ converges to $x$ if
A) $x_n=x$ for infinitely many $n$  B) $\lVert x_n-x\rVert\to0$  C) $x_n$ is bounded  D) $\lVert x_n\rVert$ is monotone  E) $\lVert x_n\rVert\to\infty$

<details><summary>Answer</summary>

**B** — This is the definition. Bounded sequences need not converge, e.g. $(-1)^n$.

</details>

**Q2.** (official example 2) A Hilbert space is defined as
A) a complete normed space  B) a complete inner product space  C) a compact metric space  D) a finite-dimensional vector space  E) a Banach space with $\ell^1$ norm

<details><summary>Answer</summary>

**B** — A complete normed space (A) is a Banach space; Hilbert additionally needs the norm to come from an inner product.

</details>

**Q3.** Which of these is a metric on $\mathbb R$?
A) $\lvert x-y\rvert^2$  B) $x-y$  C) $\lvert x^2-y^2\rvert$  D) $\dfrac{\lvert x-y\rvert}{1+\lvert x-y\rvert}$  E) $\lvert x\rvert+\lvert y\rvert$

<details><summary>Answer</summary>

**D** — It is the standard bounded metric. A fails the triangle inequality ($4>1+1$), B can be negative, C gives $d(1,-1)=0$, E gives $d(1,1)=2\ne0$.

</details>

**Q4.** Which metric space is complete?
A) $\mathbb Q$  B) $(0,1)$  C) $[0,1]$  D) polynomials on $[0,1]$ with the max-norm  E) $C[0,1]$ with the $L^2$ norm

<details><summary>Answer</summary>

**C** — A closed subset of $\mathbb R$ is complete. A: $\sqrt2$ is missing. B: $\frac1n$ is Cauchy, limit $0\notin(0,1)$. D: Taylor polynomials of $e^x$ are Cauchy, limit not a polynomial. E: continuous functions can converge in $L^2$ to a step function.

</details>

**Q5.** $\displaystyle\lim_{n\to\infty}\left(1+\frac2n\right)^n=$
A) $1$  B) $e$  C) $e^2$  D) $2$  E) $\infty$

<details><summary>Answer</summary>

**C** — $(1+\frac xn)^n\to e^x$ with $x=2$.

</details>

**Q6.** $\displaystyle\sum_{n=0}^\infty\left(\frac13\right)^n=$
A) $\frac32$  B) $\frac12$  C) $3$  D) $\frac23$  E) diverges

<details><summary>Answer</summary>

**A** — $\frac1{1-1/3}=\frac32$. ($\frac12$ is the sum from $n=1$.)

</details>

**Q7.** Which series converges?
A) $\sum\frac1n$  B) $\sum\frac1{\sqrt n}$  C) $\sum\frac{n}{n+1}$  D) $\sum\frac1{n^2}$  E) $\sum\frac{n^2}{n^3+1}$

<details><summary>Answer</summary>

**D** — $p=2>1$. A, B: $p\le1$. C: terms $\to1$. E: degree difference $1$, behaves like $\frac1n$.

</details>

**Q8.** For $a_n=(-1)^n+\frac1n$, $\limsup a_n=$
A) $1$  B) $\frac32$  C) $0$  D) $2$  E) $-1$

<details><summary>Answer</summary>

**A** — Even terms $\to1$, odd terms $\to-1$. $\frac32=a_2$ is the sup, not the limsup.

</details>

**Q9.** The radius of convergence of $\displaystyle\sum_{n\ge0}\frac{x^n}{2^n}$ is
A) $2$  B) $\frac12$  C) $1$  D) $\infty$  E) $0$

<details><summary>Answer</summary>

**A** — Geometric in $q=\frac x2$: converges for $\lvert x\rvert<2$.

</details>

**Q10.** Which subset of $\mathbb R$ is compact?
A) $(0,1]$  B) $[0,\infty)$  C) $[0,1]\cup\{2\}$  D) $\mathbb Q\cap[0,1]$  E) $\mathbb Z$

<details><summary>Answer</summary>

**C** — Closed and bounded. A, D not closed; B, E unbounded.

</details>

**Q11.** The closed unit ball $\{x\in\ell^2:\lVert x\rVert_2\le1\}$ is
A) compact  B) closed and bounded, but not compact  C) open  D) unbounded  E) finite-dimensional

<details><summary>Answer</summary>

**B** — The unit vectors $e_n$ satisfy $\lVert e_n-e_m\rVert=\sqrt2$, so no subsequence converges. Heine–Borel only holds in finite dimension.

</details>

**Q12.** $f:(0,1]\to\mathbb R$, $f(x)=\frac1x$ is
A) uniformly continuous  B) continuous but unbounded  C) discontinuous at $x=1$  D) bounded  E) Lipschitz

<details><summary>Answer</summary>

**B** — Continuous on its domain, but $f(x)\to\infty$ as $x\to0$. The domain is not compact, so no contradiction with the extreme value theorem.

</details>

**Q13.** Which statement is true for every continuous $f:K\to\mathbb R$ on a compact metric space $K$?
A) $f$ is differentiable  B) $f$ is constant  C) $f$ attains a maximum and a minimum  D) $f$ is injective  E) $f(K)$ is open

<details><summary>Answer</summary>

**C** — $f(K)$ is compact in $\mathbb R$, i.e. closed and bounded, so it contains its sup and inf.

</details>

**Q14.** The Jacobian matrix of $f(x,y)=(xy,\ x+y)$ at $(1,2)$ is
A) $\begin{pmatrix}2&1\\1&1\end{pmatrix}$  B) $\begin{pmatrix}1&2\\1&1\end{pmatrix}$  C) $\begin{pmatrix}2&1\end{pmatrix}$  D) $\begin{pmatrix}2&1\\1&1\end{pmatrix}^{-1}$  E) $\begin{pmatrix}2&1\\1&0\end{pmatrix}$

<details><summary>Answer</summary>

**A** — Row 1: $\nabla(xy)=(y,x)=(2,1)$. Row 2: $\nabla(x+y)=(1,1)$. (B uses $(x,y)$ in the wrong order.)

</details>

**Q15.** For $f:\mathbb R^2\to\mathbb R$, which implication is always true?
A) partial derivatives exist ⇒ differentiable  B) differentiable ⇒ continuous  C) continuous ⇒ differentiable  D) partial derivatives exist ⇒ continuous  E) differentiable ⇒ $C^1$

<details><summary>Answer</summary>

**B** — The chain is $C^1$ ⇒ differentiable ⇒ continuous. $\frac{xy}{x^2+y^2}$ disproves A and D.

</details>

**Q16.** If $f:\mathbb R^n\to\mathbb R^m$ and $g:\mathbb R^m\to\mathbb R^k$ are differentiable, then $J_{g\circ f}(x)=$
A) $J_f(x)J_g(x)$  B) $J_g(f(x))\,J_f(x)$  C) $J_f(g(x))\,J_g(x)$  D) $J_g(x)+J_f(x)$  E) $J_g(x)J_f(x)^T$

<details><summary>Answer</summary>

**B** — Chain rule. Sizes: $(k\times m)(m\times n)=k\times n$. ✓

</details>

**Q17.** The coefficient of $x^3$ in the Maclaurin series of $e^{2x}$ is
A) $\frac16$  B) $\frac43$  C) $8$  D) $\frac23$  E) $\frac83$

<details><summary>Answer</summary>

**B** — $\frac{2^3}{3!}=\frac86=\frac43$. ($8$ forgets the factorial.)

</details>

**Q18.** The second-order Taylor polynomial of $f(x,y)=e^x\cos y$ at $(0,0)$ is
A) $1+x+\frac{x^2+y^2}{2}$  B) $1+x+\frac{x^2-y^2}{2}$  C) $1+x-y+\frac{x^2}{2}$  D) $x+\frac{x^2-y^2}{2}$  E) $1+x+x^2-y^2$

<details><summary>Answer</summary>

**B** — $f_x=1$, $f_y=0$, $f_{xx}=1$, $f_{yy}=-1$, $f_{xy}=0$ at the origin; don't forget the $\frac12$ (E).

</details>

**Q19.** $\displaystyle\lim_{x\to0}\frac{1-\cos x}{x^2}=$
A) $0$  B) $1$  C) $\frac12$  D) $2$  E) $\infty$

<details><summary>Answer</summary>

**C** — $1-\cos x=\frac{x^2}{2}-\frac{x^4}{24}+\dots$

</details>

**Q20.** Which space is a Hilbert space?
A) $\ell^1$  B) $C[0,1]$ with $\lVert\cdot\rVert_\infty$  C) $\ell^\infty$  D) $\ell^2$  E) $L^1[0,1]$

<details><summary>Answer</summary>

**D** — $\ell^2$ with $\langle x,y\rangle=\sum x_ny_n$ is complete. The others are Banach, but their norms fail the parallelogram law.

</details>

**Q21.** A norm comes from an inner product if and only if
A) it is complete  B) it satisfies the parallelogram law  C) the space is finite-dimensional  D) it satisfies the triangle inequality  E) the unit ball is compact

<details><summary>Answer</summary>

**B** — $\lVert x+y\rVert^2+\lVert x-y\rVert^2=2\lVert x\rVert^2+2\lVert y\rVert^2$ (Jordan–von Neumann).

</details>

**Q22.** $f(x)=x^{-1/2}$ on $(0,1)$ belongs to
A) $L^1$ and $L^2$  B) $L^1$ but not $L^2$  C) $L^2$ but not $L^1$  D) $L^\infty$  E) neither $L^1$ nor $L^2$

<details><summary>Answer</summary>

**B** — $\int_0^1x^{-1/2}=2$, but $\int_0^1\lvert f\rvert^2=\int_0^1\frac1x=\infty$.

</details>

**Q23.** On $[0,1]$ with Lebesgue measure, which inclusion is true?
A) $L^1\subset L^2$  B) $L^2\subset L^1$  C) $L^1\subset L^\infty$  D) $L^1=L^2$  E) no inclusion holds

<details><summary>Answer</summary>

**B** — On a finite measure space larger $p$ gives a smaller space (Hölder: $\lVert f\rVert_1\le\lVert f\rVert_2$). Q22 shows $L^1\not\subset L^2$.

</details>

**Q24.** In Hölder's inequality $\lVert fg\rVert_1\le\lVert f\rVert_p\lVert g\rVert_q$ with $p=3$, the exponent $q$ is
A) $3$  B) $\frac13$  C) $\frac32$  D) $\frac23$  E) $2$

<details><summary>Answer</summary>

**C** — $\frac13+\frac1q=1\Rightarrow q=\frac32$.

</details>

**Q25.** Let $f(x)=x$ on $(-\pi,\pi)$, extended $2\pi$-periodically. Which Fourier coefficients are all zero?
A) $a_n$ (cosine coefficients)  B) $b_n$ (sine coefficients)  C) both  D) none  E) only $a_0$

<details><summary>Answer</summary>

**A** — $f$ is odd, $f(x)\cos nx$ is odd, its integral over $[-\pi,\pi]$ is $0$. Only sines remain.

</details>

**Q26.** $f=-1$ on $(-\pi,0)$, $f=1$ on $(0,\pi)$, $2\pi$-periodic. Its Fourier series at $x=0$ converges to
A) $1$  B) $-1$  C) $0$  D) $\frac12$  E) it diverges

<details><summary>Answer</summary>

**C** — At a jump the series converges to the midpoint $\frac{-1+1}{2}=0$. (Indeed every $\sin(n\cdot0)=0$.)

</details>

**Q27.** The Laplace transform of $e^{3t}$ is
A) $\frac1{s+3}$  B) $\frac1{s-3}$  C) $\frac3{s}$  D) $\frac{3}{s^2+9}$  E) $\frac{s}{s^2+9}$

<details><summary>Answer</summary>

**B** — $\mathcal L\{e^{at}\}=\frac1{s-a}$ (for $s>3$).

</details>

**Q28.** Using the Laplace transform, $y''+y=0$, $y(0)=0$, $y'(0)=1$ gives $Y(s)=$
A) $\frac{s}{s^2+1}$  B) $\frac{1}{s^2+1}$  C) $\frac1{s-1}$  D) $\frac{1}{s^2-1}$  E) $\frac{s+1}{s^2+1}$

<details><summary>Answer</summary>

**B** — $s^2Y-sy(0)-y'(0)+Y=0\Rightarrow(s^2+1)Y=1$, so $y=\sin t$.

</details>
