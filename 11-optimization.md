# 11. Optimization

> Syllabus:
> - Unconstrained and constrained optimization
> - Linear programming / linear optimization
> - Convex optimization
> - Gradient-based methods

> How to study this file:
> - Start with the 🟢 sections. They are the **core**. The test asks short calculations about them (find a minimum, classify a point, evaluate a linear program at its corners, do one gradient step).
> - The 🟡 boxes are **basic facts only**. Read them 2–3 times. You do not need to do long calculations with them.
> - Every section has the same form: **meaning in plain words → recipe → easy example → trap**.
> - At the end: a one-page **Formula sheet** and **25 practice MCQs**. Do the MCQs on paper first, then open the answers.
> - Official problem 22 (number of local maxima of a polynomial) is about this file. See `12-official-problems-solved.md`.

## Contents
1. [🟢 Extrema in one variable](#1--extrema-in-one-variable)
2. [🟢 Counting local maxima and minima of a polynomial](#2--counting-local-maxima-and-minima-of-a-polynomial)
3. [🟢 Extrema in two variables (gradient and Hessian)](#3--extrema-in-two-variables-gradient-and-hessian)
4. [🟢 Lagrange multipliers (one constraint)](#4--lagrange-multipliers-one-constraint)
5. [🟢 Linear programming: the graphical method](#5--linear-programming-the-graphical-method)
6. [🟢 Convex sets and convex functions](#6--convex-sets-and-convex-functions)
7. [🟢 Gradient descent](#7--gradient-descent)
8. [🟡 Advanced topics: must-know facts](#8--advanced-topics-must-know-facts)
9. [Formula sheet](#formula-sheet)
10. [Practice MCQs](#practice-mcqs)

---

## 1. 🟢 Extrema in one variable

**Words you need.**
- A **local minimum** at $x^*$: near $x^*$, no value of $f$ is smaller than $f(x^*)$. (The bottom of a valley.)
- A **local maximum** at $x^*$: near $x^*$, no value of $f$ is bigger than $f(x^*)$. (The top of a hill.)
- **Global** minimum / maximum: the smallest / biggest value on the **whole** domain.
- "Extremum" (plural: extrema) = a maximum or a minimum.
- A **critical point** (also: stationary point) is a point where $f'(x)=0$.

**Plain-words meaning.** At the top of a hill or the bottom of a valley, the graph is flat. So the slope $f'(x)$ is $0$ there.

**Recipe (second derivative test).**
1. Compute $f'(x)$ and solve $f'(x)=0$. The solutions are the critical points.
2. Compute $f''(x)$ at each critical point:
   - $f''(x^*)>0$ (curve opens up, like $\cup$) → **local minimum**.
   - $f''(x^*)<0$ (curve opens down, like $\cap$) → **local maximum**.
   - $f''(x^*)=0$ → the test **says nothing**. Look at the function directly.

**Example.** $f(x)=x^3-3x$.
1. $f'(x)=3x^2-3=0 \Rightarrow x^2=1 \Rightarrow x=1$ or $x=-1$.
2. $f''(x)=6x$.
   - $x=1$: $f''(1)=6>0$ → local minimum, value $f(1)=1-3=-2$.
   - $x=-1$: $f''(-1)=-6<0$ → local maximum, value $f(-1)=-1+3=2$.
3. These are **not** global: $f(x)\to+\infty$ for $x\to+\infty$ and $f(x)\to-\infty$ for $x\to-\infty$.

**On a closed interval $[a,b]$.** A continuous function on a closed and bounded interval always has a global max and a global min (theorem of **Weierstrass**). To find them:
1. Find the critical points inside $(a,b)$.
2. Also take the two **end points** $a$ and $b$.
3. Compute $f$ at all these points. The biggest value is the global max, the smallest is the global min.

**Example.** $f(x)=x^3-3x$ on $[0,3]$. Critical point inside: $x=1$. Values: $f(0)=0$, $f(1)=-2$, $f(3)=27-9=18$. Global min $=-2$ (at $x=1$), global max $=18$ (at $x=3$, an end point).

**Example where the test says nothing.** $f(x)=x^4$: $f'(0)=0$ and $f''(0)=0$. But $x^4\ge 0=f(0)$, so $x=0$ is a (global) minimum. For $f(x)=x^3$: also $f'(0)=f''(0)=0$, but $x=0$ is **not** an extremum (the graph goes up through $0$).

> **Trap:** $f'(x^*)=0$ does **not** prove an extremum ($x^3$ at $0$). And on a closed interval, do not forget the end points: the max is often at an end point.

---

## 2. 🟢 Counting local maxima and minima of a polynomial

**Plain-words meaning.** Between two zeros (roots) of a smooth function, the graph must turn around. So there is a hill or a valley between them.

**The rule (from Rolle's theorem).** Rolle: if $f(a)=f(b)$, then $f'(c)=0$ for some $c$ between $a$ and $b$.

Let $p$ be a polynomial of degree $d$ with $d$ **different real roots** $r_1<r_2<\dots<r_d$. Then:
- There is exactly one critical point in each gap $(r_i,r_{i+1})$. That gives $d-1$ critical points. ($p'$ has degree $d-1$, so there are no others.)
- These $d-1$ points are local extrema, and they **alternate**: max, min, max, … or min, max, min, …

**How to decide where to start.** Look at the sign of $p$ in the first gap $(r_1,r_2)$:
- $p<0$ there → the graph goes down and comes back → the first extremum is a **minimum**.
- $p>0$ there → the first extremum is a **maximum**.

**Example (official problem 22, with $n=1$).** $f(x)=x(x-1)(x-2)(x-3)$.
- Degree $4$, roots $0,1,2,3$, leading coefficient positive.
- 3 gaps → 3 extrema.
- In $(0,1)$, e.g. $x=0.5$: $0.5\cdot(-0.5)\cdot(-1.5)\cdot(-2.5)<0$. So: min, max, min. The graph looks like a "W".
- Answer: **1 local maximum, 2 local minima**.

**General result.** $f(x)=\prod_{k=0}^{2n+1}(x-k)=x(x-1)\cdots(x-2n-1)$ has $2n+2$ roots, so $2n+1$ extrema: min, max, …, min. That is **$n$ local maxima** and $n+1$ local minima.

**Quick table** (positive leading coefficient, all roots real and different):

| Degree $d$ | Extrema | Pattern | Maxima | Minima |
|---|---|---|---|---|
| 2 | 1 | min | 0 | 1 |
| 3 | 2 | max, min | 1 | 1 |
| 4 | 3 | min, max, min | 1 | 2 |
| 5 | 4 | max, min, max, min | 2 | 2 |
| 6 | 5 | min, max, min, max, min | 2 | 3 |

> **Trap:** the rule needs **different real** roots. A polynomial of degree $d$ in general has **at most** $d-1$ local extrema ($x^3$ has degree 3 and **no** extremum).

---

## 3. 🟢 Extrema in two variables (gradient and Hessian)

**Symbols.**
- $f_x=\dfrac{\partial f}{\partial x}$ = derivative in $x$, treating $y$ as a constant. $f_y$ in the same way.
- $f_{xx}$, $f_{yy}$, $f_{xy}$ = second partial derivatives. (For nice functions $f_{xy}=f_{yx}$.)
- **Gradient** $\nabla f=(f_x,\ f_y)$. It is a vector. It points in the direction where $f$ **grows fastest**.
- **Hessian matrix** $H=\begin{pmatrix} f_{xx} & f_{xy}\\ f_{xy} & f_{yy}\end{pmatrix}$. It plays the role of $f''$.
- A **saddle point** is a critical point that is neither max nor min (like the middle of a horse saddle: up in one direction, down in another).

**Recipe.**
1. Solve $\nabla f=0$, that is $f_x=0$ **and** $f_y=0$. These are the critical points.
2. At each critical point compute
$$D=\det H=f_{xx}f_{yy}-f_{xy}^2 .$$
3. Decide:

| $D$ | $f_{xx}$ | Result |
|---|---|---|
| $D>0$ | $f_{xx}>0$ | local **minimum** |
| $D>0$ | $f_{xx}<0$ | local **maximum** |
| $D<0$ | (any) | **saddle point** |
| $D=0$ | — | test says nothing |

**Example 1.** $f(x,y)=x^2+y^2-2x+4y$.
1. $f_x=2x-2=0\Rightarrow x=1$. $f_y=2y+4=0\Rightarrow y=-2$. Critical point $(1,-2)$.
2. $f_{xx}=2$, $f_{yy}=2$, $f_{xy}=0$. $D=2\cdot2-0=4>0$ and $f_{xx}=2>0$.
3. Local minimum. Value: $f(1,-2)=1+4-2-8=-5$.

**Example 2.** $f(x,y)=x^3-3x+y^2$.
1. $f_x=3x^2-3=0\Rightarrow x=\pm1$. $f_y=2y=0\Rightarrow y=0$. Points $(1,0)$ and $(-1,0)$.
2. $f_{xx}=6x$, $f_{yy}=2$, $f_{xy}=0$, so $D=12x$.
   - $(1,0)$: $D=12>0$, $f_{xx}=6>0$ → **local minimum**.
   - $(-1,0)$: $D=-12<0$ → **saddle point**.

**Example 3 (classic saddles).**
- $f=x^2-y^2$ at $(0,0)$: $D=2\cdot(-2)-0=-4<0$ → saddle.
- $f=xy$ at $(0,0)$: $f_{xx}=f_{yy}=0$, $f_{xy}=1$, $D=0-1=-1<0$ → saddle.

**Gradient example.** $f(x,y)=x^2y+3y$ at $(1,2)$: $f_x=2xy=4$, $f_y=x^2+3=4$, so $\nabla f(1,2)=(4,4)$.

**More words (for MCQs).** "Hessian positive definite" = both eigenvalues $>0$ = ($D>0$ and $f_{xx}>0$) → minimum. "Negative definite" → maximum. "Indefinite" (one positive, one negative eigenvalue) = $D<0$ → saddle.

> **Trap:** for $D<0$ you do **not** look at $f_{xx}$: it is always a saddle. And $D=0$ means "unknown", not "saddle".

---

## 4. 🟢 Lagrange multipliers (one constraint)

**Plain-words meaning.** We want the max or min of $f(x,y)$, but we may only use points on a curve $g(x,y)=c$ (the **constraint**). At the best point, the level line of $f$ just **touches** the curve. Then the two gradients are parallel:
$$\nabla f=\lambda\,\nabla g .$$
The number $\lambda$ (Greek "lambda") is called the **Lagrange multiplier**.

**Recipe.**
1. Write the three equations: $f_x=\lambda g_x$, $f_y=\lambda g_y$, $g(x,y)=c$.
2. Solve them for $x$, $y$, $\lambda$.
3. Put every solution into $f$. The biggest value is the max, the smallest is the min.

**Example 1.** Maximize $f=xy$ with $x+y=10$.
1. $\nabla f=(y,x)$, $\nabla g=(1,1)$. Equations: $y=\lambda$, $x=\lambda$, $x+y=10$.
2. So $x=y$, and $2x=10$, so $x=y=5$, $\lambda=5$.
3. Max value $f=25$.

**Faster way for a linear constraint: substitute.** $y=10-x$, so $f=x(10-x)=10x-x^2$. Then $f'=10-2x=0$ gives $x=5$. Same answer. In an MCQ this is often quicker.

**Example 2.** Minimize $f=x^2+y^2$ with $x+2y=5$.
1. $(2x,2y)=\lambda(1,2)$, so $x=\lambda/2$, $y=\lambda$.
2. $\lambda/2+2\lambda=5\Rightarrow \tfrac52\lambda=5\Rightarrow\lambda=2$. So $(x,y)=(1,2)$.
3. Min value $f=1+4=5$. (This is the squared distance from the origin to the line.)

**Example 3 (on a circle).** Max of $f=x+y$ with $x^2+y^2=2$.
1. $(1,1)=\lambda(2x,2y)$, so $x=y=\frac1{2\lambda}$.
2. $2x^2=2\Rightarrow x=\pm1$. Points $(1,1)$ and $(-1,-1)$.
3. $f(1,1)=2$ (max), $f(-1,-1)=-2$ (min).

**Useful facts.**
- Max of $xy$ with $x+y=S$: $x=y=S/2$, value $S^2/4$.
- Min of $x^2+y^2$ with $x+y=c$: value $c^2/2$.

> **Trap:** Lagrange gives only **candidates**. You must compare the values of $f$ to know which is max and which is min. And do not forget the constraint equation $g=c$ in step 1.

---

## 5. 🟢 Linear programming: the graphical method

**Words.**
- A **linear program (LP)**: maximize or minimize a **linear** function (the **objective**), e.g. $z=3x+2y$, subject to **linear inequalities** (the constraints), e.g. $x+y\le4$, $x\ge0$.
- **Feasible region**: all points that satisfy all constraints. For an LP it is a **polygon** (a convex shape with straight sides).
- **Vertex** (corner): a point where two boundary lines meet.

**Main fact.** If an LP has an optimal solution, then the optimum is reached at a **vertex** of the feasible region.

**Recipe (2 variables).**
1. Draw each constraint as a line ($\le$ becomes $=$). Shade the allowed side.
2. Find all vertices: intersections of lines, points on the axes, and the origin if allowed.
3. Compute the objective $z$ at each vertex.
4. Max problem: take the biggest $z$. Min problem: take the smallest.

**Example.** Maximize $z=3x+2y$ with $x+y\le4$, $x+3y\le6$, $x\ge0$, $y\ge0$.
1. Lines: $x+y=4$ meets the axes at $(4,0)$, $(0,4)$. $x+3y=6$ meets them at $(6,0)$, $(0,2)$.
2. Intersection of the two lines: subtract → $2y=2$, so $y=1$, $x=3$. Vertex $(3,1)$.
3. Vertices and values:

| Vertex | $z=3x+2y$ |
|---|---|
| $(0,0)$ | $0$ |
| $(4,0)$ | $\mathbf{12}$ |
| $(3,1)$ | $11$ |
| $(0,2)$ | $4$ |

4. Maximum $z=12$ at $(4,0)$.

With the **same** region, the objective $2x+3y$ gives $0,\ 8,\ 9,\ 6$, so its maximum is $9$ at $(3,1)$. The best corner depends on the objective.

**Three possible outcomes of an LP.**
- **Optimal**: a finite best value exists (as above).
- **Unbounded**: the objective can grow without limit. Example: max $x+y$ with only $x-y\le1$, $x,y\ge0$ (take $y\to\infty$).
- **Infeasible**: no point satisfies all constraints. Example: $x+y\le1$ and $x+y\ge2$.

**Many optima.** If the objective line is parallel to an edge of the polygon, every point of that edge is optimal (infinitely many solutions, never exactly two).

> **Trap:** check **every** vertex, also the ones on the axes. The intersection point of the two main lines is **not** always the optimum (above: $(3,1)$ gives $11<12$). And "the region is unbounded" does not always mean "the LP is unbounded".

---

## 6. 🟢 Convex sets and convex functions

**Convex set — plain words.** A set $C$ is **convex** if for any two points in $C$, the **straight segment** between them is also inside $C$. No holes, no dents.
- Formula: $x,y\in C$ and $0\le t\le1$ $\Rightarrow$ $tx+(1-t)y\in C$.
- Convex: a line, a half-plane $\{ax+by\le c\}$, a disk $\{x^2+y^2\le1\}$, a polygon, a triangle, the whole plane, the feasible region of an LP.
- **Not** convex: a circle line $\{x^2+y^2=1\}$ (the segment between two points goes through the inside), a ring, two separate intervals $[0,1]\cup[2,3]$, the set $\{|x|\ge1\}$.
- The **intersection** of convex sets is convex. The **union** is usually **not**.

**Convex function — plain words.** $f$ is **convex** if the segment (chord) between two points on its graph lies **above** the graph. The graph is shaped like a bowl $\cup$.
- Formula: $f(tx+(1-t)y)\le t\,f(x)+(1-t)\,f(y)$ for $0\le t\le1$.
- **Concave** = $-f$ is convex (shape $\cap$).

**Test with derivatives.**
- One variable: $f''(x)\ge0$ for all $x$ ⇔ $f$ convex.
- Two variables: Hessian positive semidefinite everywhere. For a $2\times2$ Hessian: $f_{xx}\ge0$, $f_{yy}\ge0$ and $D=f_{xx}f_{yy}-f_{xy}^2\ge0$.

**Examples.**

| Convex | Not convex |
|---|---|
| $x^2$, $e^x$, $\lvert x\rvert$, $x^4$ | $x^3$ on $\mathbb R$ ($f''=6x<0$ for $x<0$) |
| $-\ln x$ on $x>0$ | $\ln x$, $\sqrt x$ (these are concave) |
| linear $ax+b$ (convex **and** concave) | $\sin x$, $-x^2$ |
| $x^2+xy+y^2$ ($D=4-1=3\ge0$) | $x^2+4xy+y^2$ ($D=4-16<0$) |

**Why convexity is great for optimization.**
- For a convex function, **every local minimum is a global minimum**.
- If $f$ is convex and differentiable, then $\nabla f(x^*)=0$ ⇔ $x^*$ is a global minimum.
- A **strictly** convex function has **at most one** minimum point (maybe none: $e^x$ has no minimum).

**Example.** $f(x,y)=x^2+xy+y^2-3x$. Hessian $\begin{pmatrix}2&1\\1&2\end{pmatrix}$, $D=3>0$, $f_{xx}=2>0$ → convex. Gradient: $2x+y-3=0$ and $x+2y=0$. From the second, $x=-2y$; then $-4y+y=3$, so $y=-1$, $x=2$. Global minimum $f(2,-1)=4-2+1-6=-3$.

> **Trap:** "convex set" and "convex function" are different ideas. And a sum of convex functions is convex, but a **product** need not be ($x\cdot x^2=x^3$).

---

## 7. 🟢 Gradient descent

**Plain-words meaning.** You stand on a hill in the fog and want to go down. The gradient $\nabla f$ points **uphill**. So you take a small step in the opposite direction, $-\nabla f$. Repeat.

**Formula.**
$$x_{k+1}=x_k-\alpha\,\nabla f(x_k)$$
- $x_k$ = the point after $k$ steps. $x_0$ = start point.
- $\alpha>0$ = **step size** (also called "learning rate").

**Example 1 (one variable).** $f(x)=x^2$, so $f'(x)=2x$. Start $x_0=4$, $\alpha=0.25$.
- $x_1=4-0.25\cdot8=2$.
- $x_2=2-0.25\cdot4=1$.
- Each step halves $x$: $x_{k+1}=(1-2\alpha)x_k=0.5\,x_k$. It goes to the minimum $0$.

**Example 2 (two variables).** $f(x,y)=x^2+3y^2$, start $(1,1)$, $\alpha=0.1$.
1. $\nabla f=(2x,\ 6y)=(2,\ 6)$ at $(1,1)$.
2. $x_1=(1,1)-0.1\cdot(2,6)=(1-0.2,\ 1-0.6)=(0.8,\ 0.4)$.
3. Check: $f$ goes from $1+3=4$ to $0.64+0.48=1.12$. It went down. ✓

**Choosing the step size.** Too small → very slow. Too big → the points jump around or fly away.
- For $f(x)=a x^2$ ($a>0$): $x_{k+1}=(1-2a\alpha)x_k$. This goes to $0$ for every start **iff** $\lvert1-2a\alpha\rvert<1$, i.e. $0<\alpha<\dfrac1a$.
- Example $f=5x^2$: need $0<\alpha<0.2$. At $\alpha=0.2$ the points jump $x_0,-x_0,x_0,\dots$ forever.
- Example $f=x^2$ with $\alpha=1$: $x_{k+1}=-x_k$, no convergence.
- General rule: if $L$ is the largest eigenvalue of the Hessian (largest "curvature"), a fixed step works for $0<\alpha<2/L$. A safe standard choice is $\alpha=1/L$.

> **Trap:** the sign. Descent uses **minus** the gradient. $x_k+\alpha\nabla f$ is a step **uphill** (gradient ascent). MCQs often offer this wrong answer.

---

## 8. 🟡 Advanced topics: must-know facts

You only need these facts. No long calculations.

> **🟡 Must-know facts — KKT conditions (constraints with $\le$)**
> Problem: minimize $f(x)$ with $g_i(x)\le0$.
> 1. **Stationarity:** $\nabla f+\sum\lambda_i\nabla g_i=0$.
> 2. **Feasibility:** $g_i(x^*)\le0$.
> 3. **Sign:** $\lambda_i\ge0$.
> 4. **Complementary slackness:** $\lambda_i\,g_i(x^*)=0$. So if a constraint is not active ($g_i<0$), then $\lambda_i=0$.
> 5. For a **convex** problem, a point satisfying KKT is a **global** minimum. **Slater's condition** = there is a point with all $g_i<0$ strictly; it guarantees strong duality.

> **🟡 Must-know facts — Simplex method**
> 1. It walks from **vertex to neighbouring vertex** of the feasible region. The objective never gets worse.
> 2. Constraints $\le$ are turned into equations with **slack variables** $s\ge0$: $x+y\le4$ becomes $x+y+s=4$.
> 3. Entering variable: most negative entry in the objective row (max problem). Leaving variable: smallest ratio $b_i/a_{ij}$ with $a_{ij}>0$.
> 4. If the entering column has **no positive entry** → the LP is **unbounded**.
> 5. **Bland's rule** (smallest index) prevents **cycling**. Worst case the simplex is exponential, but it is fast in practice.

> **🟡 Must-know facts — LP duality**
> 1. Primal: $\max c^Tx$, $Ax\le b$, $x\ge0$. **Dual:** $\min b^Ty$, $A^Ty\ge c$, $y\ge0$.
> 2. Number of dual variables = number of primal constraints.
> 3. **Weak duality:** every primal value $\le$ every dual value.
> 4. **Strong duality:** if one has an optimum, both do, and the optimal values are **equal**.
> 5. Primal unbounded ⇒ dual **infeasible** (and the other way round).
> 6. The optimal dual variable = **shadow price** of the constraint. A constraint that is not tight at the optimum has shadow price $0$.

> **🟡 Must-know facts — Newton's method for optimization**
> 1. One variable: $x_{k+1}=x_k-\dfrac{f'(x_k)}{f''(x_k)}$. Many variables: $x_{k+1}=x_k-H^{-1}\nabla f(x_k)$.
> 2. Near a good minimum it converges **quadratically** (the number of correct digits roughly doubles each step).
> 3. For a quadratic function with positive definite Hessian it finds the minimum in **exactly one step**.
> 4. It is expensive: it needs the Hessian and a linear solve in each step.

> **🟡 Must-know facts — Speed of gradient methods, BFGS, CG**
> 1. Gradient descent: **linear** convergence for strongly convex functions; $O(1/k)$ for convex functions. Slow and "zig-zag" when the problem is badly conditioned (large condition number $\kappa=\lambda_{\max}/\lambda_{\min}$).
> 2. Nesterov's accelerated gradient: $O(1/k^2)$ for convex functions.
> 3. **BFGS** (quasi-Newton): builds an approximate Hessian from gradients only; **superlinear** convergence.
> 4. **Conjugate gradient (CG)**: for a quadratic with symmetric positive definite $n\times n$ matrix it finishes in **at most $n$ steps** (exact arithmetic).
> 5. Stochastic gradient descent (SGD) uses the gradient of a random sample; it needs **decreasing** step sizes to converge.

> **🟡 Must-know facts — Integer programming**
> 1. Same as an LP but the variables must be integers. In general NP-hard.
> 2. The LP **relaxation** (drop "integer") gives a **bound**: an upper bound for a max problem, a lower bound for a min problem.
> 3. Rounding the LP solution can give a non-feasible or bad point. Methods: branch and bound, cutting planes.

---

## Formula sheet

| Topic | Formula / rule |
|---|---|
| Critical point (1D) | $f'(x)=0$ |
| 2nd derivative test (1D) | $f''>0$ min, $f''<0$ max, $f''=0$ unknown |
| Closed interval $[a,b]$ | compare $f$ at critical points **and** at $a$, $b$ |
| Polynomial, $d$ different real roots | exactly $d-1$ extrema, alternating max/min |
| $\prod_{k=0}^{2n+1}(x-k)$ | $n$ maxima, $n+1$ minima |
| Gradient | $\nabla f=(f_x,f_y)$, points uphill |
| Hessian | $H=\begin{pmatrix}f_{xx}&f_{xy}\\f_{xy}&f_{yy}\end{pmatrix}$ |
| 2D test | $D=f_{xx}f_{yy}-f_{xy}^2$: $D>0,f_{xx}>0$ min; $D>0,f_{xx}<0$ max; $D<0$ saddle; $D=0$ unknown |
| Lagrange | $\nabla f=\lambda\nabla g$ and $g=c$ |
| $\max xy$, $x+y=S$ | $S^2/4$ at $x=y=S/2$ |
| $\min x^2+y^2$, $x+y=c$ | $c^2/2$ |
| LP | optimum at a **vertex**; outcomes: optimal / unbounded / infeasible |
| Convex set | segment between two points stays inside |
| Convex function | $f''\ge0$ (1D); Hessian PSD (2D); local min = global min |
| Gradient descent | $x_{k+1}=x_k-\alpha\nabla f(x_k)$ |
| Step size for $f=ax^2$ | converges iff $0<\alpha<1/a$; general $0<\alpha<2/L$ |
| KKT | $\lambda_i\ge0$, $\lambda_ig_i=0$ |
| LP duality | $\max c^Tx,\ Ax\le b,\ x\ge0$ ↔ $\min b^Ty,\ A^Ty\ge c,\ y\ge0$ |
| Newton (opt.) | $x_{k+1}=x_k-f'/f''$; one step for quadratics |
| CG | $\le n$ steps on an $n\times n$ SPD quadratic |

---

## Practice MCQs

**Q1.** The function $f(x)=x^2-6x+5$ has its minimum at
A) $x=-3$  B) $x=3$  C) $x=5$  D) $x=-4$

<details><summary>Answer</summary>

**B** — $f'(x)=2x-6=0\Rightarrow x=3$, and $f''=2>0$. ($-4$ is the minimum **value** $f(3)=9-18+5$, not the point.)

</details>

**Q2.** For $f(x)=x^3-12x$, the point $x=2$ is
A) a local maximum  B) not a critical point  C) a local minimum  D) an inflection point

<details><summary>Answer</summary>

**C** — $f'(x)=3x^2-12$, $f'(2)=0$. $f''(x)=6x$, $f''(2)=12>0$ → local minimum.

</details>

**Q3.** The gradient of $f(x,y)=x^2y+3y$ at $(1,2)$ is
A) $(4,4)$  B) $(2,4)$  C) $(4,3)$  D) $(4,7)$

<details><summary>Answer</summary>

**A** — $f_x=2xy=4$, $f_y=x^2+3=4$.

</details>

**Q4.** Which function is convex on all of $\mathbb R$?
A) $x^3$  B) $-x^2$  C) $\sin x$  D) $e^x$

<details><summary>Answer</summary>

**D** — $(e^x)''=e^x>0$. $x^3$ has $f''=6x<0$ for $x<0$; $-x^2$ is concave; $\sin x$ changes curvature.

</details>

**Q5.** The point $(0,0)$ for $f(x,y)=x^2-y^2$ is
A) a local minimum  B) a local maximum  C) a saddle point  D) not a critical point

<details><summary>Answer</summary>

**C** — $\nabla f=(2x,-2y)=0$ at $(0,0)$. $D=2\cdot(-2)-0=-4<0$ → saddle.

</details>

**Q6.** Which set is convex?
A) the disk $\{x^2+y^2\le1\}$  B) the circle $\{x^2+y^2=1\}$  C) $[0,1]\cup[2,3]$  D) $\{x\in\mathbb R:\lvert x\rvert\ge1\}$

<details><summary>Answer</summary>

**A** — a segment between two points of a disk stays in the disk. For B, C, D you can find a segment that leaves the set.

</details>

**Q7.** Maximize $x+y$ subject to $x\le3$, $y\le2$, $x\ge0$, $y\ge0$. The optimal value is
A) $3$  B) $5$  C) $6$  D) $2$

<details><summary>Answer</summary>

**B** — vertices $(0,0),(3,0),(3,2),(0,2)$ give $0,3,5,2$. Max $5$ at $(3,2)$.

</details>

**Q8.** One step of gradient descent on $f(x)=x^2$ from $x_0=4$ with $\alpha=0.25$ gives
A) $6$  B) $0$  C) $3$  D) $2$

<details><summary>Answer</summary>

**D** — $f'(4)=8$, $x_1=4-0.25\cdot8=2$. (A $=6$ is the wrong "plus" step.)

</details>

**Q9.** The maximum of $xy$ subject to $x+y=6$ is
A) $6$  B) $9$  C) $12$  D) $36$

<details><summary>Answer</summary>

**B** — $x=y=3$, $xy=9$. (Rule: $S^2/4=36/4$.)

</details>

**Q10.** How many local maxima does $f(x)=x(x-1)(x-2)(x-3)(x-4)(x-5)$ have?
A) $1$  B) $3$  C) $5$  D) $2$

<details><summary>Answer</summary>

**D** — 6 different roots → 5 extrema. Degree even, positive leading coefficient → pattern min, max, min, max, min → 2 maxima. (Formula with $2n+1=5$, $n=2$.)

</details>

**Q11.** The critical point $(0,0)$ of $f(x,y)=x^2+xy+y^2$ is
A) a local minimum  B) a local maximum  C) a saddle point  D) impossible to classify with $D$

<details><summary>Answer</summary>

**A** — $f_{xx}=2$, $f_{yy}=2$, $f_{xy}=1$; $D=4-1=3>0$ and $f_{xx}>0$ → minimum.

</details>

**Q12.** The function $f(x,y)=x^3-3x+y^2$ has
A) two local minima  B) one local maximum and one local minimum  C) one local minimum and one saddle point  D) two saddle points

<details><summary>Answer</summary>

**C** — critical points $(\pm1,0)$; $D=12x$: at $(1,0)$ $D>0$, $f_{xx}>0$ → min; at $(-1,0)$ $D<0$ → saddle.

</details>

**Q13.** For $f(x)=x^4$ at $x=0$:
A) $f''(0)>0$, so it is a minimum  B) $0$ is not a critical point  C) $f''(0)=0$, but $0$ is a global minimum  D) $0$ is a local maximum

<details><summary>Answer</summary>

**C** — $f'(0)=f''(0)=0$, so the test says nothing. But $x^4\ge0=f(0)$, so it is a global minimum.

</details>

**Q14.** The global minimum value of $f(x)=x^3-3x$ on $[0,3]$ is
A) $0$  B) $-2$  C) $2$  D) $18$

<details><summary>Answer</summary>

**B** — critical point inside: $x=1$. Values: $f(0)=0$, $f(1)=-2$, $f(3)=18$. Smallest is $-2$. ($18$ is the maximum.)

</details>

**Q15.** Maximize $2x+3y$ subject to $x+y\le4$, $x+3y\le6$, $x,y\ge0$. The optimal value is
A) $8$  B) $6$  C) $12$  D) $9$

<details><summary>Answer</summary>

**D** — vertices $(0,0),(4,0),(3,1),(0,2)$ give $0,8,9,6$. Max $9$ at $(3,1)$.

</details>

**Q16.** One gradient descent step on $f(x,y)=x^2+2y^2$ from $(1,1)$ with $\alpha=0.1$ gives
A) $(0.8,\ 0.6)$  B) $(0.9,\ 0.8)$  C) $(0.8,\ 0.8)$  D) $(1.2,\ 1.4)$

<details><summary>Answer</summary>

**A** — $\nabla f=(2x,4y)=(2,4)$. New point $(1-0.2,\ 1-0.4)=(0.8,0.6)$. D is the uphill step.

</details>

**Q17.** The minimum of $x^2+y^2$ subject to $x+2y=5$ is
A) $\tfrac52$  B) $25$  C) $5$  D) $\sqrt5$

<details><summary>Answer</summary>

**C** — Lagrange: $(2x,2y)=\lambda(1,2)$ → $y=2x$; $x+4x=5$ → $(1,2)$, value $1+4=5$. ($\sqrt5$ is the distance, not the squared distance.)

</details>

**Q18.** Let $f$ be convex and differentiable on $\mathbb R^n$. Which statement is true?
A) $f$ always has a minimum point  B) $f$ can have two different local minima with different values  C) $f$ is always strictly convex  D) if $\nabla f(x^*)=0$, then $x^*$ is a global minimum

<details><summary>Answer</summary>

**D** — for convex functions, a critical point is a global minimum. A is false ($e^x$), B is false (local = global), C is false (linear functions).

</details>

**Q19.** Gradient descent with fixed step $\alpha$ on $f(x)=5x^2$ converges for every start point if and only if
A) $0<\alpha<1$  B) $0<\alpha<0.2$  C) $0<\alpha<0.1$  D) $0<\alpha\le0.2$

<details><summary>Answer</summary>

**B** — $x_{k+1}=x_k-\alpha\cdot10x_k=(1-10\alpha)x_k$. Need $\lvert1-10\alpha\rvert<1$ ⇔ $0<\alpha<0.2$. At $\alpha=0.2$ it jumps between $\pm x_0$.

</details>

**Q20.** The maximum of $x+y$ on the circle $x^2+y^2=2$ is
A) $\sqrt2$  B) $1$  C) $4$  D) $2$

<details><summary>Answer</summary>

**D** — Lagrange gives $x=y$, so $x=y=\pm1$. $f(1,1)=2$ is the max.

</details>

**Q21.** 🟡 In the KKT conditions for $\min f(x)$ with $g_i(x)\le0$, complementary slackness says
A) $\lambda_i\,g_i(x^*)=0$ for every $i$  B) $\lambda_i\le0$  C) $\nabla f(x^*)=0$  D) $g_i(x^*)=0$ for every $i$

<details><summary>Answer</summary>

**A** — either the constraint is active ($g_i=0$) or its multiplier is $0$. ($\lambda_i\ge0$ is a different KKT condition.)

</details>

**Q22.** 🟡 A maximization LP is unbounded. Then its dual LP is
A) unbounded  B) optimal  C) infeasible  D) degenerate

<details><summary>Answer</summary>

**C** — by weak duality, any feasible dual point would give an upper bound for the primal. So no dual point can exist.

</details>

**Q23.** 🟡 Newton's method applied to minimize $f(x)=\tfrac12x^TQx-b^Tx$ with $Q$ symmetric positive definite
A) needs about $n$ steps  B) reaches the minimum in exactly one step  C) converges only linearly  D) never converges

<details><summary>Answer</summary>

**B** — $x_1=x_0-Q^{-1}(Qx_0-b)=Q^{-1}b$, which is the minimum. (A describes the conjugate gradient method.)

</details>

**Q24.** 🟡 The simplex method moves
A) through the inside of the feasible region  B) along the gradient direction  C) randomly between feasible points  D) from a vertex to a neighbouring vertex

<details><summary>Answer</summary>

**D** — it goes along edges of the feasible polygon/polyhedron, from corner to corner.

</details>

**Q25.** The critical point $(0,0)$ of $f(x,y)=x^2+4xy+y^2$ is
A) a saddle point  B) a local minimum  C) a local maximum  D) a global minimum

<details><summary>Answer</summary>

**A** — $f_{xx}=2$, $f_{yy}=2$, $f_{xy}=4$; $D=4-16=-12<0$ → saddle. (Trap: $f_{xx}>0$ does not matter when $D<0$.)

</details>
