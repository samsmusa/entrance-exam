# 12. Official Practice Problems — Full Solutions

> Source: *Problems for Applicants of the Master Program in Mathematics* (Hochschule Mittweida, PT 2018).
> These 25 problems show the **level and style** the university expects.
> The real test is **multiple choice**, so each solution also has:
> - **Fast MCQ route**: the quickest way to the answer when you only have to pick an option
> - **MCQ version**: how the problem would probably look in the test
> - **Study file**: which file in this folder covers the topic
>
> **How to use:** try all 25 first *without* looking (the official instructions say so too). Then check your work here.

## Overview

| # | Topic | Answer / key fact | Study file |
|---|---|---|---|
| 1 | Inequalities | $x+\frac1x\ge 2$, equality iff $x=1$ | 01 |
| 2 | Induction, binomial theorem | Pascal's rule | 03 |
| 3 | Primes | Euclid's proof | 04 |
| 4 | Double sums | $m(m+1)$ with $m=\lfloor n/2\rfloor$ | 03 |
| 5 | Groups | Right cancellation | 02 |
| 6 | Sets, preimages | $f^{-1}$ preserves $\cup$ | 03 |
| 7 | Determinants | $\det(\alpha A)=\alpha^n\delta$ | 02 |
| 8 | Linear algebra / geometry | $V=\lvert\det(a,b,c)\rvert$ | 02 |
| 9 | Relations | Congruence is an equivalence relation | 03 / 04 |
| 10 | Irrationality | $\sqrt3\notin\mathbb Q$ | 04 |
| 11 | Probability | Union bound (Boole) | 07 |
| 12 | Linear systems | 3-dimensional affine solution space | 06 / 02 |
| 13 | Geometric probability | $3/4$ | 07 |
| 14 | Expectation | $161/36\approx 4.47$ | 07 |
| 15 | Series | $e\cdot e^{-1}=1$ | 01 |
| 16 | Counting | $\binom{n+2}{2}$ | 03 |
| 17 | Functions | Injection $A\to B$ ⇒ surjection $B\to A$ | 03 |
| 18 | Countability | $\mathbb N\times\mathbb N$ countable | 03 / 01 |
| 19 | Sequences | Accumulation points $\pm e$ | 01 |
| 20 | Rings/fields | $\mathbb Z/m\mathbb Z$ has zero divisors | 02 / 04 |
| 21 | Modular arithmetic | $4$ | 04 |
| 22 | Extrema of polynomials | $n$ local maxima | 11 / 01 |
| 23 | Graphs | $m\ge n$ ⇒ cycle | 09 |
| 24 | Iterated integrals | $1/40$ | 01 |
| 25 | ODE | $y=2e^t-t-1$ | 05 |

---

## Exercise 1 — $x + \frac1x \ge 2$ for $x>0$

**Proof.** For $x>0$:
$$x+\frac1x-2=\frac{x^2-2x+1}{x}=\frac{(x-1)^2}{x}\ge 0.$$
Equality holds iff $x=1$.

Another route is the AM–GM inequality: $\frac{x+1/x}{2}\ge\sqrt{x\cdot\frac1x}=1$.

**Fast MCQ route:** "minimum of $x+1/x$ on $(0,\infty)$" is $2$, reached at $x=1$. For $x<0$ the expression is $\le -2$.
**MCQ version:** *What is $\min_{x>0}(x+4/x)$?* By AM–GM it is $2\sqrt4=4$, at $x=2$. In general $\min(ax+b/x)=2\sqrt{ab}$.

---

## Exercise 2 — Binomial theorem by induction

**Claim:** $(x+y)^n=\sum_{k=0}^n\binom nk x^k y^{n-k}$.

- **Base case** $n=0$: both sides equal $1$.
- **Inductive step.** Assume the claim for $n$. Then
$$(x+y)^{n+1}=(x+y)\sum_{k=0}^n\binom nk x^ky^{n-k}=\sum_{k=0}^n\binom nk x^{k+1}y^{n-k}+\sum_{k=0}^n\binom nk x^ky^{n+1-k}.$$
In the first sum, shift the index ($k\to k-1$). Then combine the two sums with **Pascal's rule** $\binom n{k-1}+\binom nk=\binom{n+1}k$:
$$=\sum_{k=0}^{n+1}\binom{n+1}{k}x^ky^{n+1-k}.\ \blacksquare$$

**Fast MCQ facts:** $\sum_k\binom nk=2^n$ (set $x=y=1$). $\sum_k(-1)^k\binom nk=0$ for $n\ge1$. The coefficient of $x^k$ in $(1+x)^n$ is $\binom nk$.

---

## Exercise 3 — There are infinitely many primes

**Proof (Euclid).** Suppose $p_1,\dots,p_r$ were all the primes, and let $N=p_1p_2\cdots p_r+1$. Since $N>1$, it has a prime factor $p$, so $p=p_i$ for some $i$. Then $p_i\mid N$ and $p_i\mid p_1\cdots p_r$, so $p_i\mid 1$. That is a contradiction. $\blacksquare$

**Trap:** $N$ itself does **not** have to be prime. For example, $2\cdot3\cdot5\cdot7\cdot11\cdot13+1=30031=59\cdot509$.

---

## Exercise 4 — $\displaystyle\sum_{k=0}^n\sum_{j=0}^k(-1)^jk$

The factor $k$ does not depend on $j$, so pull it out of the inner sum:
$$\sum_{k=0}^n k\sum_{j=0}^k(-1)^j,\qquad \sum_{j=0}^k(-1)^j=\begin{cases}1 & k\text{ even}\\ 0 & k\text{ odd}\end{cases}$$
So only even $k$ contribute. Write $k=2i$ and $m=\lfloor n/2\rfloor$:
$$\sum_{i=0}^{m}2i=m(m+1)=\Big\lfloor\frac n2\Big\rfloor\Big(\Big\lfloor\frac n2\Big\rfloor+1\Big).$$
**Check:** $n=4$ gives $0+2+4=6=2\cdot3$ ✓.

**Fast MCQ route:** put $n=1,2,3,4$ into the options. The values must be $0,2,2,6$.

---

## Exercise 5 — In a group, $xz=yz\Rightarrow x=y$

Multiply both sides on the right by $z^{-1}$ and use associativity:
$$x=x(zz^{-1})=(xz)z^{-1}=(yz)z^{-1}=y(zz^{-1})=y.\ \blacksquare$$
**Trap:** $xz=zy$ does **not** imply $x=y$ in a non-abelian group. Cancellation only works on the same side.

---

## Exercise 6 — $f^{-1}(Y\cup Z)=f^{-1}(Y)\cup f^{-1}(Z)$

$$x\in f^{-1}(Y\cup Z)\iff f(x)\in Y\cup Z\iff f(x)\in Y\ \lor\ f(x)\in Z\iff x\in f^{-1}(Y)\cup f^{-1}(Z).\ \blacksquare$$

**MCQ trap table (very commonly asked):**

| Identity | Always true? |
|---|---|
| $f^{-1}(Y\cup Z)=f^{-1}(Y)\cup f^{-1}(Z)$ | ✅ |
| $f^{-1}(Y\cap Z)=f^{-1}(Y)\cap f^{-1}(Z)$ | ✅ |
| $f^{-1}(B\setminus Y)=A\setminus f^{-1}(Y)$ | ✅ |
| $f(U\cup V)=f(U)\cup f(V)$ | ✅ |
| $f(U\cap V)=f(U)\cap f(V)$ | ❌ only $\subseteq$ (equality if $f$ is injective) |
| $f(f^{-1}(Y))=Y$ | ❌ only $\subseteq$ (equality if $f$ is surjective) |
| $f^{-1}(f(U))=U$ | ❌ only $\supseteq$ (equality if $f$ is injective) |

---

## Exercise 7 — $\det(\alpha A)$ for an $n\times n$ matrix with $\det A=\delta$

The determinant is linear in **each of the $n$ rows**. Multiplying every row by $\alpha$ therefore gives
$$\det(\alpha A)=\alpha^n\delta.$$
**Trap answers:** $\alpha\delta$ and $n\alpha\delta$ are wrong.
**Related facts:** $\det(AB)=\det A\det B$, $\det A^{T}=\det A$, $\det A^{-1}=1/\det A$, $\det(-A)=(-1)^n\det A$.

---

## Exercise 8 — Volume of the parallelepiped spanned by $a,b,c\in\mathbb R^3$

$$V=\lvert\det(a\ b\ c)\rvert=\lvert a\cdot(b\times c)\rvert\quad\text{(scalar triple product)}.$$
Linear independence means $V>0$. The volume of the tetrahedron with the same edges is $V/6$. In $\mathbb R^2$ the area of the parallelogram is $\lvert\det(a\ b)\rvert$.

---

## Exercise 9 — $x\equiv y\iff k\mid x-y$ is an equivalence relation on $\mathbb Z$

- **Reflexive:** $x-x=0=k\cdot0$.
- **Symmetric:** if $x-y=kq$, then $y-x=k(-q)$.
- **Transitive:** if $x-y=kq$ and $y-z=kr$, then $x-z=k(q+r)$. $\blacksquare$

There are exactly $k$ equivalence classes: $[0],[1],\dots,[k-1]$, which form $\mathbb Z/k\mathbb Z$.

---

## Exercise 10 — $\sqrt3$ is irrational

Suppose $\sqrt3=p/q$ with $\gcd(p,q)=1$. Then $p^2=3q^2$, so $3\mid p^2$. Since $3$ is prime, $3\mid p$. Write $p=3r$. Then $9r^2=3q^2$, so $q^2=3r^2$ and $3\mid q$. Now $3$ divides both $p$ and $q$, which contradicts $\gcd(p,q)=1$. $\blacksquare$

**General fact:** $\sqrt n$ is irrational unless $n$ is a perfect square. Also, $\sqrt[k]{n}$ is rational only if it is an integer.

---

## Exercise 11 — Union bound $\Pr\left(\bigcup A_i\right)\le\sum\Pr(A_i)$

Use induction on $n$. The case $n=1$ is trivial. For the step:
$$\Pr\Big(\bigcup_{i=1}^{n+1}A_i\Big)=\Pr(U_n)+\Pr(A_{n+1})-\Pr(U_n\cap A_{n+1})\le\Pr(U_n)+\Pr(A_{n+1})\le\sum_{i=1}^{n+1}\Pr(A_i).$$
Here $U_n=\bigcup_{i\le n}A_i$. Equality holds iff the events are pairwise disjoint up to null sets.

---

## Exercise 12 — Solution space of $Ax=b$ where $A$ is $m\times(m+2)$ with $\operatorname{rank}A=m-1=\operatorname{rank}(A\mid b)$

- $\operatorname{rank}A=\operatorname{rank}(A\mid b)$, so by the Kronecker–Capelli (Rouché–Capelli) theorem the system is **solvable**.
- The solution set is $x_p+\ker A$, an **affine subspace**.
- $\dim\ker A=n-\operatorname{rank}A=(m+2)-(m-1)=3$.

**Answer:** the solutions form a **3-dimensional affine subspace** of $\mathbb R^{m+2}$, so there are infinitely many. It is a linear subspace only if $b=0$.

**General rule (very likely in the MCQ):** number of free parameters = number of unknowns − rank. If $\operatorname{rank}A<\operatorname{rank}(A\mid b)$, there is no solution.

---

## Exercise 13 — $X,Y\sim U[0,1]$ independent, $\Pr(|X-Y|<\tfrac12)$

$(X,Y)$ is uniform on the unit square, so probability = area. The region $|x-y|\ge\frac12$ consists of two corner triangles with legs $\frac12$, each with area $\frac18$:
$$\Pr=1-2\cdot\tfrac18=\tfrac34.$$
**General fact:** $\Pr(|X-Y|<a)=1-(1-a)^2$ for $0\le a\le1$.

---

## Exercise 14 — $E[\max]$ of two dice

$\Pr(X\le k)=\left(\frac k6\right)^2$, so $\Pr(X=k)=\frac{k^2-(k-1)^2}{36}=\frac{2k-1}{36}$.
$$EX=\sum_{k=1}^6k\cdot\frac{2k-1}{36}=\frac{2\cdot91-21}{36}=\frac{161}{36}\approx4.47.$$
(Using $\sum k^2=91$ and $\sum k=21$.)
**Related facts:** $E[\min]=7-\frac{161}{36}=\frac{91}{36}$, since $\max+\min=$ sum, whose expectation is $7$.

---

## Exercise 15 — $\left(\sum\frac1{k!}\right)\left(\sum\frac{(-1)^k}{k!}\right)=1$

The two series are $e^1$ and $e^{-1}$, so the product is $e^{0}=1$.

**Rigorous version:** both series converge absolutely, so their Cauchy product converges to the product of the sums. The $n$-th term of the Cauchy product is
$$\sum_{k=0}^n\frac{1}{k!}\cdot\frac{(-1)^{n-k}}{(n-k)!}=\frac1{n!}\sum_{k}\binom nk(-1)^{n-k}=\frac{(1-1)^n}{n!}=\begin{cases}1&n=0\\0&n\ge1.\end{cases}$$

---

## Exercise 16 — Nonnegative integer solutions of $x+y+z=n$

Use **stars and bars**: place $n$ stars and $2$ bars in a row.
$$\binom{n+2}{2}=\frac{(n+1)(n+2)}2.$$
**General rule:** $x_1+\dots+x_k=n$ has $\binom{n+k-1}{k-1}$ solutions with $x_i\ge0$ and $\binom{n-1}{k-1}$ solutions with $x_i\ge1$.

---

## Exercise 17 — An injection $f:A\to B$ with $A\neq\emptyset$ gives a surjection $B\to A$

Fix $a_0\in A$ and define
$$g(b)=\begin{cases}\text{the unique }a\text{ with }f(a)=b & b\in f(A)\\ a_0 & \text{otherwise.}\end{cases}$$
The element $a$ is unique because $f$ is injective, so $g$ is well-defined. Since $g(f(a))=a$ for every $a$, $g$ is surjective. $\blacksquare$
(This is why $A\ne\emptyset$ is needed: otherwise $a_0$ would not exist.)

---

## Exercise 18 — The product of two countable sets is countable

Let $\alpha:A\to\mathbb N$ and $\beta:B\to\mathbb N$ be injective. The map $(a,b)\mapsto 2^{\alpha(a)}3^{\beta(b)}$ is injective by unique prime factorization. So $A\times B$ injects into $\mathbb N$ and is countable.
Alternative: the Cantor pairing $\pi(i,j)=\frac{(i+j)(i+j+1)}2+j$ is a bijection $\mathbb N^2\to\mathbb N$.

**MCQ facts:** countable sets include $\mathbb Z$, $\mathbb Q$, $\mathbb N^k$, finite strings over a finite alphabet, algebraic numbers, and countable unions of countable sets. Uncountable sets include $\mathbb R$, $[0,1]$, $\mathcal P(\mathbb N)$, $\{0,1\}^{\mathbb N}$, and the irrationals.

---

## Exercise 19 — Accumulation points of $x_n=\left(-1-\frac1n\right)^n$

$$x_n=(-1)^n\left(1+\tfrac1n\right)^n,\qquad\left(1+\tfrac1n\right)^n\to e.$$
The even terms tend to $e$ and the odd terms tend to $-e$.
**Accumulation points: $\{e,-e\}$.** So $\limsup x_n=e$ and $\liminf x_n=-e$.

**Trap:** do not answer $\pm1$, and do not answer $e^{-1}$, which is the limit of $(1-\frac1n)^n$.

---

## Exercise 20 — For composite $m>1$, $\mathbb Z/m\mathbb Z$ is not a field

Write $m=ab$ with $1<a,b<m$. Then $[a]\neq[0]$ and $[b]\ne[0]$, but $[a][b]=[m]=[0]$. A field has no zero divisors. (If $[a]^{-1}$ existed, then $[b]=[a]^{-1}[a][b]=0$, a contradiction.) $\blacksquare$

**Full statement:** $\mathbb Z/m\mathbb Z$ is a field $\iff$ $m$ is prime. $[a]$ is invertible $\iff\gcd(a,m)=1$.

---

## Exercise 21 — $12345678^{78}\bmod 5$

- $12345678\equiv 8\equiv3\pmod5$, because only the last digit matters mod $5$.
- $3^4\equiv1\pmod 5$ by Fermat, so exponents can be reduced mod $4$.
- $78=4\cdot19+2$, so $3^{78}\equiv3^2=9\equiv\mathbf{4}$.

**Fast MCQ route:** the powers of $3$ mod $5$ cycle as $3,4,2,1$. Since $78\bmod4=2$, take the 2nd entry, which is $4$.

---

## Exercise 22 — Number of local maxima of $f(x)=\prod_{k=0}^{2n+1}(x-k)$

- $f$ has degree $2n+2$ (even), a positive leading coefficient, and $2n+2$ simple roots $0,1,\dots,2n+1$.
- By Rolle's theorem, $f'$ has a root in each of the $2n+1$ gaps. Since $\deg f'=2n+1$, these are **all** the critical points, and they are all simple. So the critical points alternate between maxima and minima.
- $f\to+\infty$ on both sides, so the first and last critical points are minima. The pattern is min, max, min, …, min, which gives $n+1$ minima and **$n$ maxima**.

Check with $n=1$: $x(x-1)(x-2)(x-3)$ has a W shape with 1 local max ✓.

**Fast MCQ route:** a polynomial with $d$ distinct real roots has $d-1$ critical points that alternate. For even degree with positive leading coefficient there are $\frac{d}{2}-1$ maxima.

---

## Exercise 23 — Simple graph with $m\ge n$ has a cycle

Suppose $G$ has no cycle. Then $G$ is a forest. If it has $c\ge1$ components (trees), and a tree with $n_i$ vertices has $n_i-1$ edges, then
$$m=\sum(n_i-1)=n-c\le n-1<n.$$
That contradicts $m\ge n$. $\blacksquare$

**MCQ facts:** a tree has $n-1$ edges, is connected and acyclic, and adding any edge creates exactly one cycle.

---

## Exercise 24 — $\displaystyle\int_0^1\int_0^x\int_0^y yz\,dz\,dy\,dx$

Integrate from the inside out:
$$\int_0^y yz\,dz=y\cdot\frac{y^2}2=\frac{y^3}2,\qquad\int_0^x\frac{y^3}2dy=\frac{x^4}8,\qquad\int_0^1\frac{x^4}8dx=\frac1{40}.$$
**Answer: $\frac1{40}$.**
**Trap:** always integrate the **innermost** variable first. Its limits may depend on the outer variables.

---

## Exercise 25 — $y'=y+t$, $y(0)=1$

The equation is linear first-order: $y'-y=t$. Use the integrating factor $e^{-t}$:
$$(ye^{-t})'=te^{-t}\ \Rightarrow\ ye^{-t}=-te^{-t}-e^{-t}+C\ \Rightarrow\ y=Ce^t-t-1.$$
From $y(0)=C-1=1$ we get $C=2$:
$$\boxed{y(t)=2e^t-t-1}$$
**Check:** $y'=2e^t-1$ and $y+t=2e^t-1$ ✓.
**Fast MCQ route:** plug each option into the ODE **and** check the initial condition. This often takes less than 30 seconds.
