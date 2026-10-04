# 07. Measure Theory and Probability

> **Syllabus:**
> - Zero-measures (null sets)
> - Expectations
> - Distributions / densities
> - Independence and conditional probabilities
> - Laws of large numbers and central limit theorem
>
> **How to study this file:** Sections 1–9 are 🟢 core. Learn them well and do the worked examples yourself.
> Sections 10–12 are 🟡: only read the "Must-know facts" boxes. Time: about 4–5 hours, plus 1 hour for the MCQs.

## Contents
1. [Counting probabilities](#1-counting-probabilities-) 🟢
2. [Rules for events (complement, union, union bound)](#2-rules-for-events-) 🟢
3. [Conditional probability, total probability, Bayes](#3-conditional-probability-total-probability-bayes-) 🟢
4. [Independence](#4-independence-) 🟢
5. [Discrete random variables](#5-discrete-random-variables-) 🟢
6. [Continuous random variables: PDF and CDF](#6-continuous-random-variables-pdf-and-cdf-) 🟢
7. [Expectation and variance](#7-expectation-and-variance-) 🟢
8. [Standard distributions](#8-standard-distributions-) 🟢
9. [Geometric probability (areas)](#9-geometric-probability-areas-) 🟢
10. [Central limit theorem and law of large numbers](#10-central-limit-theorem-and-law-of-large-numbers-) 🟢 / 🟡
11. [Markov and Chebyshev inequalities](#11-markov-and-chebyshev-inequalities-) 🟡
12. [Null sets and measure theory](#12-null-sets-and-measure-theory-) 🟡
13. [Formula sheet](#formula-sheet)
14. [Practice MCQs](#practice-mcqs)

**Symbols used in this file**

| Symbol | Meaning |
|---|---|
| $\Omega$ | sample space = set of all possible outcomes |
| $A, B$ | events = subsets of $\Omega$ |
| $A^c$ | complement: "$A$ does not happen" |
| $A\cap B$ | "$A$ and $B$ both happen" |
| $A\cup B$ | "$A$ or $B$ (or both) happens" |
| $P(A)$ | probability of $A$, a number in $[0,1]$ |
| $X, Y$ | random variables (numbers that depend on chance) |
| $E[X]$ | expectation (mean) of $X$ |
| $\operatorname{Var}(X)$ | variance of $X$ |

---

## 1. Counting probabilities 🟢

**Meaning.** If all outcomes are equally likely, probability = "good cases divided by all cases".

**Formula (Laplace).**
$$P(A)=\frac{\lvert A\rvert}{\lvert \Omega\rvert}=\frac{\text{number of good outcomes}}{\text{number of all outcomes}}$$

**Counting tools** ($n! = 1\cdot2\cdots n$, and $\binom nk=\frac{n!}{k!(n-k)!}$ = "$n$ choose $k$"):

| Situation | Number of ways |
|---|---|
| Order matters, with repetition ($k$ draws from $n$) | $n^k$ |
| Order matters, no repetition | $n(n-1)\cdots(n-k+1)$ |
| Order does not matter, no repetition | $\binom nk$ |
| Arrange $n$ different objects in a row | $n!$ |

**Worked example.** Roll two fair dice. What is $P(\text{sum}=7)$?
1. All outcomes: $6\cdot 6=36$ pairs $(a,b)$.
2. Good outcomes: $(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)$, so 6 pairs.
3. $P=\frac{6}{36}=\frac16$.

**Worked example 2.** An urn has 3 red and 2 blue balls. Draw 2 without putting back. $P(\text{both red})$?
1. All ways: $\binom52=10$. Good ways: $\binom32=3$.
2. $P=\frac{3}{10}$. (Check step by step: $\frac35\cdot\frac24=\frac{6}{20}=\frac3{10}$ ✓.)

> **Trap:** with two dice, $(1,6)$ and $(6,1)$ are **different** outcomes. If you count "sums" (2, 3, …, 12) as equally likely, you get wrong answers.

---

## 2. Rules for events 🟢

**Meaning.** Some simple rules let you compute new probabilities from known ones.

| Rule | Formula |
|---|---|
| Complement | $P(A^c)=1-P(A)$ |
| Empty set | $P(\emptyset)=0$ |
| Subset | $A\subseteq B\Rightarrow P(A)\le P(B)$ |
| Union of two (inclusion–exclusion) | $P(A\cup B)=P(A)+P(B)-P(A\cap B)$ |
| Disjoint events ($A\cap B=\emptyset$) | $P(A\cup B)=P(A)+P(B)$ |
| **Union bound** (Boole) | $P(A_1\cup\dots\cup A_n)\le P(A_1)+\dots+P(A_n)$ |
| "At least one" | $P(\text{at least one})=1-P(\text{none})$ |

**Why the union bound is true** (official problem 11). For two events:
$P(A\cup B)=P(A)+P(B)-P(A\cap B)\le P(A)+P(B)$, because $P(A\cap B)\ge0$.
For $n$ events, use induction: add one event at a time.

**Worked example.** $P(A)=0.5$, $P(B)=0.4$, $P(A\cap B)=0.2$.
1. $P(A\cup B)=0.5+0.4-0.2=0.7$.
2. $P(\text{neither }A\text{ nor }B)=1-0.7=0.3$.

**Worked example 2.** Roll a die 4 times. $P(\text{at least one six})$?
1. $P(\text{no six in one roll})=\frac56$. Rolls are independent, so $P(\text{no six at all})=\left(\frac56\right)^4=\frac{625}{1296}$.
2. $P(\text{at least one six})=1-\frac{625}{1296}\approx0.518$.

> **Trap:** the union bound gives only an **upper bound**. With $P(A_i)=0.1,0.2,0.3$ the bound is $0.6$, but the true value can be smaller.

---

## 3. Conditional probability, total probability, Bayes 🟢

**Meaning.** $P(A\mid B)$ = "probability of $A$ **if we already know** that $B$ happened". We look only inside $B$.

**Formulas.**
$$P(A\mid B)=\frac{P(A\cap B)}{P(B)}\qquad (P(B)>0)$$
$$\text{Multiplication rule: } P(A\cap B)=P(B)\,P(A\mid B)$$
If $B_1,\dots,B_n$ split $\Omega$ into disjoint parts (a **partition**):
$$\text{Total probability: } P(A)=\sum_i P(A\mid B_i)\,P(B_i)$$
$$\text{Bayes: } P(B_j\mid A)=\frac{P(A\mid B_j)\,P(B_j)}{P(A)}$$

**Worked example (factory).** Machine M1 makes 60% of items, 3% of them are defective. Machine M2 makes 40%, 5% defective. An item is defective ($D$). Probability it came from M2?
1. Total probability: $P(D)=0.6\cdot0.03+0.4\cdot0.05=0.018+0.020=0.038$.
2. Bayes: $P(M2\mid D)=\frac{0.020}{0.038}=\frac{10}{19}\approx0.526$.

**Worked example (medical test).** 1% of people are ill. The test is positive for 99% of ill people and for 5% of healthy people.
1. $P(+)=0.99\cdot0.01+0.05\cdot0.99=0.0099+0.0495=0.0594$.
2. $P(\text{ill}\mid +)=\frac{0.0099}{0.0594}=\frac16\approx16.7\%$.
3. Lesson: if the illness is rare, most positive tests are false positives.

> **Trap:** $P(A\mid B)\neq P(B\mid A)$ in general. "99% of ill people test positive" is **not** "99% of positive people are ill".

---

## 4. Independence 🟢

**Meaning.** $A$ and $B$ are independent if knowing $B$ does not change the chance of $A$.

**Formula.**
$$A,B\text{ independent}\iff P(A\cap B)=P(A)\,P(B)$$
(Equivalent: $P(A\mid B)=P(A)$ when $P(B)>0$.)

**Facts.**
- If $A,B$ are independent, then also $A$ and $B^c$, $A^c$ and $B$, $A^c$ and $B^c$ are independent.
- For independent events: $P(A\cup B)=1-(1-P(A))(1-P(B))$.
- Three events $A,B,C$ are (mutually) independent if all pairs **and** the triple satisfy the product rule. Pairwise independence alone is not enough.

**Worked example.** $P(A)=0.5$, $P(B)=0.4$, independent.
1. $P(A\cap B)=0.5\cdot0.4=0.2$.
2. $P(A\cup B)=0.5+0.4-0.2=0.7$.

**Disjoint vs independent.** $A$, $B$ disjoint with $P(A)=0.3$, $P(B)=0.4$:
$P(A\cap B)=0$, but $P(A)P(B)=0.12$. So they are **not** independent. (If $A$ happens, we know $B$ did not happen.)

> **Trap:** "disjoint" and "independent" are different. Disjoint events with positive probabilities are always **dependent**.

---

## 5. Discrete random variables 🟢

**Meaning.** A random variable $X$ is a number that depends on chance. "Discrete" means $X$ takes only a list of values (like $0,1,2,\dots$).

**Formulas.**
- **PMF** (probability mass function): $p(k)=P(X=k)$, with $p(k)\ge0$ and $\sum_k p(k)=1$.
- **CDF** (cumulative distribution function): $F(x)=P(X\le x)$.
- $P(a<X\le b)=F(b)-F(a)$.

**Worked example (official problem 14 idea).** Roll two dice. Let $M=\max$ of the two numbers. Find the PMF.
1. $M\le k$ means **both** dice are $\le k$: $P(M\le k)=\frac{k}{6}\cdot\frac{k}{6}=\frac{k^2}{36}$.
2. $P(M=k)=P(M\le k)-P(M\le k-1)=\frac{k^2-(k-1)^2}{36}=\frac{2k-1}{36}$.
3. So $P(M=1)=\frac1{36}$, $P(M=2)=\frac3{36}$, …, $P(M=6)=\frac{11}{36}$. Sum $=\frac{36}{36}=1$ ✓.

**CDF properties:** $F$ is non-decreasing, right-continuous, goes from $0$ (at $-\infty$) to $1$ (at $+\infty$). For discrete $X$ it is a step function; the jump at $k$ is $P(X=k)$.

> **Trap:** for discrete $X$, $P(X<k)$ and $P(X\le k)$ are **different** (they differ by $P(X=k)$).

---

## 6. Continuous random variables: PDF and CDF 🟢

**Meaning.** A continuous $X$ can take any value in an interval. Its probabilities come from a **density** $f$ (PDF): probability = area under $f$.

**Formulas.**
$$P(a\le X\le b)=\int_a^b f(x)\,dx,\qquad f(x)\ge0,\qquad \int_{-\infty}^{\infty}f(x)\,dx=1$$
$$F(x)=P(X\le x)=\int_{-\infty}^x f(t)\,dt,\qquad f(x)=F'(x)$$

**Worked example (find the constant).** $f(x)=cx^2$ for $0\le x\le1$, else $0$. Find $c$ and $P(X\le\frac12)$.
1. Total area must be 1: $\int_0^1 cx^2\,dx=\frac c3=1$, so $c=3$.
2. $P(X\le\tfrac12)=\int_0^{1/2}3x^2\,dx=\left[x^3\right]_0^{1/2}=\frac18$.

**Facts.**
- $P(X=a)=0$ for every single point $a$. So $P(X\le a)=P(X<a)$.
- $f(x)$ is **not** a probability. It can be bigger than 1. Example: $U[0,\frac12]$ has $f(x)=2$.

> **Trap:** "$P(X=a)=0$" does **not** mean "$X=a$ is impossible". It only means the event is a null event.

---

## 7. Expectation and variance 🟢

**Meaning.** $E[X]$ = the long-run average value of $X$. $\operatorname{Var}(X)$ = how much $X$ spreads around its mean. $\sigma=\sqrt{\operatorname{Var}X}$ is the standard deviation (SD).

**Formulas.**

| | Discrete | Continuous |
|---|---|---|
| $E[X]$ | $\sum_k k\,P(X=k)$ | $\int x\,f(x)\,dx$ |
| $E[g(X)]$ | $\sum_k g(k)\,P(X=k)$ | $\int g(x)\,f(x)\,dx$ |

$$\operatorname{Var}(X)=E[(X-E X)^2]=E[X^2]-(E[X])^2$$

**Rules** ($a,b$ are constants):

| Rule | Needs independence? |
|---|---|
| $E[aX+b]=aE[X]+b$ | no |
| $E[X+Y]=E[X]+E[Y]$ | **no** (always true) |
| $E[XY]=E[X]\,E[Y]$ | yes |
| $\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$ | no |
| $\operatorname{Var}(X+Y)=\operatorname{Var}X+\operatorname{Var}Y$ | yes (or uncorrelated) |
| $\operatorname{Var}(X-Y)=\operatorname{Var}X+\operatorname{Var}Y$ | yes — note the **plus** |
| $\operatorname{Var}(X+Y)=\operatorname{Var}X+\operatorname{Var}Y+2\operatorname{Cov}(X,Y)$ | general formula |

Covariance: $\operatorname{Cov}(X,Y)=E[XY]-E[X]E[Y]$. Independent $\Rightarrow\operatorname{Cov}=0$. The converse is false.

**Worked example (one die).**
1. $E[X]=\frac{1+2+\dots+6}{6}=\frac{21}{6}=3.5$.
2. $E[X^2]=\frac{1+4+9+16+25+36}{6}=\frac{91}{6}$.
3. $\operatorname{Var}X=\frac{91}{6}-3.5^2=\frac{91}{6}-\frac{49}{4}=\frac{35}{12}\approx2.92$.

**Worked example (official problem 14: max of two dice).** Use the PMF from Section 5: $P(M=k)=\frac{2k-1}{36}$.
$$E[M]=\frac{1\cdot1+2\cdot3+3\cdot5+4\cdot7+5\cdot9+6\cdot11}{36}=\frac{1+6+15+28+45+66}{36}=\frac{161}{36}\approx4.47$$
Bonus: $\max+\min=$ sum of the dice, and $E[\text{sum}]=7$. So $E[\min]=7-\frac{161}{36}=\frac{91}{36}\approx2.53$.

**Worked example (continuous).** $f(x)=3x^2$ on $[0,1]$.
1. $E[X]=\int_0^1x\cdot3x^2\,dx=\frac34$.
2. $E[X^2]=\int_0^13x^4\,dx=\frac35$.
3. $\operatorname{Var}X=\frac35-\frac9{16}=\frac{3}{80}$.

**Worked example (variance rule).** $X,Y$ independent, $\operatorname{Var}X=1$, $\operatorname{Var}Y=2$.
$\operatorname{Var}(2X-3Y)=2^2\cdot1+(-3)^2\cdot2=4+18=22$.

> **Trap:** $E[X^2]\neq(E[X])^2$ (the difference is the variance), and $E[1/X]\neq 1/E[X]$.

---

## 8. Standard distributions 🟢

Here $q=1-p$. Learn the **mean** and **variance** columns by heart.

| Name | Values | $P(X=k)$ or $f(x)$ | Mean | Variance | Typical use |
|---|---|---|---|---|---|
| Bernoulli$(p)$ | $0,1$ | $P(1)=p,\ P(0)=q$ | $p$ | $pq$ | one yes/no trial |
| Binomial$(n,p)$ | $0,\dots,n$ | $\binom nk p^kq^{n-k}$ | $np$ | $npq$ | successes in $n$ independent trials |
| Geometric$(p)$ | $1,2,\dots$ | $q^{k-1}p$ | $\frac1p$ | $\frac{q}{p^2}$ | number of trials until first success |
| Poisson$(\lambda)$ | $0,1,2,\dots$ | $e^{-\lambda}\frac{\lambda^k}{k!}$ | $\lambda$ | $\lambda$ | number of rare events in a time period |
| Uniform$[a,b]$ | $[a,b]$ | $\frac1{b-a}$ | $\frac{a+b}2$ | $\frac{(b-a)^2}{12}$ | "any point equally likely" |
| Exponential$(\lambda)$ | $[0,\infty)$ | $\lambda e^{-\lambda x}$ | $\frac1\lambda$ | $\frac1{\lambda^2}$ | waiting time |
| Normal $N(\mu,\sigma^2)$ | $\mathbb R$ | $\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ | $\mu$ | $\sigma^2$ | sums and averages, measurement errors |

**Useful extra facts.**
- Exponential: $P(X>t)=e^{-\lambda t}$. It is **memoryless**: $P(X>s+t\mid X>s)=P(X>t)$.
- Poisson: mean = variance $=\lambda$. Sum of independent Poisson$(\lambda)$ and Poisson$(\mu)$ is Poisson$(\lambda+\mu)$.
- Normal: if $X\sim N(\mu,\sigma^2)$, then $Z=\frac{X-\mu}{\sigma}\sim N(0,1)$ (standard normal).

**Worked example (Poisson).** On average 2 calls per hour. $P(\text{at most 1 call})=e^{-2}(1+2)=3e^{-2}\approx0.406$.

**Worked example (Exponential).** Lifetime with mean 2 years, so $\lambda=\frac12$. $P(\text{lives more than 2 years})=e^{-2/2}=e^{-1}\approx0.368$.

> **Trap:** Exponential$(\lambda)$ has mean $\frac1\lambda$, **not** $\lambda$. Uniform variance has **12** in the denominator.

---

## 9. Geometric probability (areas) 🟢

**Meaning.** If $X,Y\sim U[0,1]$ are independent, the point $(X,Y)$ is uniform in the unit square. Then
$$P\big((X,Y)\in R\big)=\text{area of }R\quad(\text{because the square has area }1).$$

**Method.**
1. Draw the unit square.
2. Draw the region $R$ described by the condition.
3. Compute its area (often with triangles: area $=\frac12\cdot$ base $\cdot$ height).

**Worked example (official problem 13).** $P(\lvert X-Y\rvert<\frac12)$.
1. The "bad" region $\lvert x-y\rvert\ge\frac12$ is two corner triangles: one with $y\ge x+\frac12$, one with $y\le x-\frac12$.
2. Each triangle has legs $\frac12$ and $\frac12$, so area $\frac12\cdot\frac12\cdot\frac12=\frac18$.
3. $P=1-2\cdot\frac18=\frac34$.

General rule: $P(\lvert X-Y\rvert<a)=1-(1-a)^2$ for $0\le a\le1$.

**Worked example 2.** $P(X+Y\le\frac12)$.
1. The region is the triangle with corners $(0,0),(\frac12,0),(0,\frac12)$.
2. Area $=\frac12\cdot\frac12\cdot\frac12=\frac18$.

**More results to remember** ($X,Y\sim U[0,1]$ independent):

| Event | Probability |
|---|---|
| $X<Y$ | $\frac12$ (symmetry) |
| $X+Y\le1$ | $\frac12$ |
| $X+Y\le t$, $0\le t\le1$ | $\frac{t^2}2$ |
| $\max(X,Y)\le t$ | $t^2$ |
| $\min(X,Y)>t$ | $(1-t)^2$ |

> **Trap:** the answer is an **area**, so it must be between 0 and 1. If you get more than 1, you counted a region twice.

---

## 10. Central limit theorem and law of large numbers 🟢 / 🟡

Let $X_1,\dots,X_n$ be **iid** (independent, identically distributed) with mean $\mu$ and variance $\sigma^2$.
Let $S_n=X_1+\dots+X_n$ (sum) and $\bar X_n=\frac{S_n}{n}$ (sample mean).

| | Mean | Variance | SD |
|---|---|---|---|
| Sum $S_n$ | $n\mu$ | $n\sigma^2$ | $\sigma\sqrt n$ |
| Mean $\bar X_n$ | $\mu$ | $\frac{\sigma^2}{n}$ | $\frac{\sigma}{\sqrt n}$ |

### Central limit theorem (CLT) 🟢
**Meaning.** For large $n$, the sum (or the mean) is approximately **normal**, whatever the distribution of the $X_i$ is.
$$S_n\approx N(n\mu,\,n\sigma^2),\qquad \bar X_n\approx N\!\left(\mu,\,\frac{\sigma^2}{n}\right)$$

**Recipe.** 1) Find mean and SD of the sum or mean. 2) Compute $z=\frac{\text{value}-\text{mean}}{\text{SD}}$. 3) Read $\Phi(z)$ from the table.

**Small z-table** ($\Phi(z)=P(Z\le z)$, $Z\sim N(0,1)$; $\Phi(-z)=1-\Phi(z)$):

| $z$ | 0 | 1 | 1.1 | 1.5 | 1.645 | 1.96 | 2 | 2.576 | 3 |
|---|---|---|---|---|---|---|---|---|---|
| $\Phi(z)$ | 0.5 | 0.8413 | 0.8643 | 0.9332 | 0.95 | 0.975 | 0.9772 | 0.995 | 0.9987 |

**Worked example (sample mean).** Light bulbs: mean life 1000 h, SD 100 h. Sample of $n=25$. $P(\bar X<960)$?
1. SD of $\bar X$: $\frac{100}{\sqrt{25}}=20$.
2. $z=\frac{960-1000}{20}=-2$.
3. $P=\Phi(-2)=1-0.9772=0.0228$.

**Worked example (coins).** 100 fair coins. $X$ = number of heads. $\mu=np=50$, $\sigma=\sqrt{npq}=\sqrt{25}=5$.
$P(X\le 60)\approx\Phi\left(\frac{60-50}{5}\right)=\Phi(2)=0.977$.

> **Trap:** for the mean use $\frac{\sigma}{\sqrt n}$, not $\sigma$. Forgetting $\sqrt n$ is the most common mistake.

### Law of large numbers (LLN) 🟡

> **Must-know facts**
> - LLN: $\bar X_n\to\mu$ as $n\to\infty$ (the sample mean approaches the true mean).
> - Weak LLN = convergence in probability; strong LLN = almost sure convergence. Both need a **finite mean**.
> - CLT needs a **finite variance**. The $X_i$ do **not** need to be normal.
> - Modes of convergence: almost sure $\Rightarrow$ in probability $\Rightarrow$ in distribution. The arrows do **not** go back.
> - LLN does **not** mean "after many tails, heads is more likely" (gambler's fallacy).

---

## 11. Markov and Chebyshev inequalities 🟡

> **Must-know facts**
> - **Markov:** if $X\ge0$, then $P(X\ge a)\le\frac{E[X]}{a}$. Example: $E[X]=2$ gives $P(X\ge10)\le0.2$.
> - **Chebyshev:** $P(\lvert X-\mu\rvert\ge k\sigma)\le\frac1{k^2}$. Equivalent: $P(\lvert X-\mu\rvert<k\sigma)\ge1-\frac1{k^2}$.
> - $k=2$: at least $\frac34$ of the probability is within $2\sigma$. $k=3$: at least $\frac89$.
> - Chebyshev works for **every** distribution, so it is weaker than the normal 95% / 99.7% rule.
> - Markov needs $X\ge0$.

---

## 12. Null sets and measure theory 🟡

**Short idea.** The **Lebesgue measure** $\lambda$ gives the "length" of a set of real numbers: $\lambda([a,b])=b-a$. A **null set** (zero-measure set) is a set with length 0. "Almost everywhere (a.e.)" or "almost surely (a.s.)" means "except on a null set".

> **Must-know facts**
> - Every single point has measure 0. Every **countable** set has measure 0: $\mathbb N$, $\mathbb Z$, $\mathbb Q$. So $\lambda(\mathbb Q\cap[0,1])=0$ and $\lambda([0,1]\setminus\mathbb Q)=1$.
> - The **Cantor set** has measure 0 but is **uncountable**. So "measure 0" does not imply "countable".
> - A countable union of null sets is a null set. A line in $\mathbb R^2$ has area 0.
> - The Dirichlet function $1_{\mathbb Q}$ on $[0,1]$ is **not** Riemann integrable, but its Lebesgue integral is $0$.
> - Changing a function on a null set does not change its integral.
> - A σ-algebra contains $\Omega$ and is closed under complements and **countable** unions. A probability measure is a measure with $P(\Omega)=1$.

---

## Formula sheet

| Topic | Formula |
|---|---|
| Laplace | $P(A)=\frac{\lvert A\rvert}{\lvert\Omega\rvert}$ |
| Complement | $P(A^c)=1-P(A)$ |
| Union | $P(A\cup B)=P(A)+P(B)-P(A\cap B)$ |
| Union bound | $P(\bigcup A_i)\le\sum P(A_i)$ |
| At least one | $1-P(\text{none})$ |
| Conditional | $P(A\mid B)=\frac{P(A\cap B)}{P(B)}$ |
| Total probability | $P(A)=\sum_i P(A\mid B_i)P(B_i)$ |
| Bayes | $P(B\mid A)=\frac{P(A\mid B)P(B)}{P(A)}$ |
| Independence | $P(A\cap B)=P(A)P(B)$ |
| Density | $f\ge0$, $\int f=1$, $P(a\le X\le b)=\int_a^bf$ |
| CDF | $F(x)=P(X\le x)$, $f=F'$ |
| Expectation | $E[X]=\sum k\,p(k)$ or $\int x f(x)\,dx$ |
| Variance | $\operatorname{Var}X=E[X^2]-(EX)^2$ |
| Linear rules | $E[aX+b]=aEX+b$, $\operatorname{Var}(aX+b)=a^2\operatorname{Var}X$ |
| Sum (independent) | $\operatorname{Var}(aX+bY)=a^2\operatorname{Var}X+b^2\operatorname{Var}Y$ |
| Max of 2 dice | $P(M=k)=\frac{2k-1}{36}$, $E[M]=\frac{161}{36}$ |
| Uniform square | probability = area; $P(\lvert X-Y\rvert<a)=1-(1-a)^2$ |
| Sum of $n$ iid | mean $n\mu$, SD $\sigma\sqrt n$ |
| Mean of $n$ iid | mean $\mu$, SD $\sigma/\sqrt n$ |
| Standardize | $z=\frac{x-\mu}{\sigma}$ |
| Chebyshev | $P(\lvert X-\mu\rvert\ge k\sigma)\le\frac1{k^2}$ |

---

## Practice MCQs

**Q1.** A fair die is rolled once. What is $P(\text{even number})$?
- A) $\frac13$
- B) $\frac12$
- C) $\frac23$
- D) $\frac16$

<details><summary>Answer</summary>

**B** — Good outcomes: 2, 4, 6. So $P=\frac36=\frac12$.

</details>

**Q2.** Two fair dice are rolled. What is $P(\text{sum}=7)$?
- A) $\frac16$
- B) $\frac1{12}$
- C) $\frac7{36}$
- D) $\frac1{11}$

<details><summary>Answer</summary>

**A** — 6 good pairs out of 36: $\frac6{36}=\frac16$. ($\frac1{11}$ wrongly treats the 11 possible sums as equally likely.)

</details>

**Q3.** $P(A)=0.5$, $P(B)=0.4$, $P(A\cap B)=0.2$. What is $P(A\cup B)$?
- A) $0.9$
- B) $0.2$
- C) $0.3$
- D) $0.7$

<details><summary>Answer</summary>

**D** — $0.5+0.4-0.2=0.7$.

</details>

**Q4.** A coin is tossed 3 times. What is $P(\text{at least one head})$?
- A) $\frac12$
- B) $\frac78$
- C) $\frac38$
- D) $\frac34$

<details><summary>Answer</summary>

**B** — $P(\text{no head})=\left(\frac12\right)^3=\frac18$. So $1-\frac18=\frac78$.

</details>

**Q5.** $X$ is a fair die roll. $E[X]=$
- A) $3$
- B) $4$
- C) $3.5$
- D) $\frac{35}{12}$

<details><summary>Answer</summary>

**C** — $\frac{1+2+\dots+6}{6}=\frac{21}6=3.5$. ($\frac{35}{12}$ is the variance.)

</details>

**Q6.** $X\sim U[0,4]$. What is $P(X\le1)$?
- A) $\frac12$
- B) $1$
- C) $\frac13$
- D) $\frac14$

<details><summary>Answer</summary>

**D** — Density $\frac14$ on $[0,4]$. Area from 0 to 1: $1\cdot\frac14=\frac14$.

</details>

**Q7.** $\operatorname{Var}(X)=4$. What is $\operatorname{Var}(2X+3)$?
- A) $16$
- B) $8$
- C) $11$
- D) $19$

<details><summary>Answer</summary>

**A** — $\operatorname{Var}(aX+b)=a^2\operatorname{Var}X=4\cdot4=16$. The $+3$ does not change the spread.

</details>

**Q8.** $X\sim\text{Binomial}(10,\,0.3)$. What is $E[X]$?
- A) $0.3$
- B) $2.1$
- C) $7$
- D) $3$

<details><summary>Answer</summary>

**D** — $E[X]=np=10\cdot0.3=3$. ($2.1=npq$ is the variance.)

</details>

**Q9.** Which statement is the union bound?
- A) $P(A\cup B)=P(A)+P(B)$ always
- B) $P(A_1\cup\dots\cup A_n)\le P(A_1)+\dots+P(A_n)$
- C) $P(A\cap B)\le P(A)P(B)$
- D) $P(A\cup B)\ge P(A)+P(B)$

<details><summary>Answer</summary>

**B** — From $P(A\cup B)=P(A)+P(B)-P(A\cap B)$ and $P(A\cap B)\ge0$, then induction. A is only true for disjoint events.

</details>

**Q10.** $A$ and $B$ are disjoint, $P(A)=0.3$, $P(B)=0.4$. Which is true?
- A) $A$ and $B$ are independent
- B) $P(A\cup B)=0.58$
- C) $A$ and $B$ are not independent
- D) $P(A\mid B)=0.3$

<details><summary>Answer</summary>

**C** — $P(A\cap B)=0$, but $P(A)P(B)=0.12\neq0$. Also $P(A\cup B)=0.7$ and $P(A\mid B)=0$.

</details>

**Q11.** $f(x)=cx^2$ for $0\le x\le1$ (else 0) is a density. What are $c$ and $E[X]$?
- A) $c=3$, $E[X]=\frac34$
- B) $c=2$, $E[X]=\frac23$
- C) $c=1$, $E[X]=\frac13$
- D) $c=3$, $E[X]=\frac12$

<details><summary>Answer</summary>

**A** — $\int_0^1cx^2dx=\frac c3=1\Rightarrow c=3$. $E[X]=\int_0^13x^3dx=\frac34$.

</details>

**Q12.** Machine M1 makes 60% of the items (3% defective), M2 makes 40% (5% defective). An item is defective. $P(\text{from M2})\approx$
- A) $0.40$
- B) $0.05$
- C) $0.038$
- D) $0.526$

<details><summary>Answer</summary>

**D** — $P(D)=0.6\cdot0.03+0.4\cdot0.05=0.038$. Bayes: $\frac{0.020}{0.038}=\frac{10}{19}\approx0.526$.

</details>

**Q13.** $X,Y\sim U[0,1]$ independent. $P(\lvert X-Y\rvert<\frac12)=$
- A) $\frac12$
- B) $\frac14$
- C) $\frac34$
- D) $\frac78$

<details><summary>Answer</summary>

**C** — The complement is two corner triangles, each of area $\frac12\cdot\frac12\cdot\frac12=\frac18$. So $1-\frac14=\frac34$.

</details>

**Q14.** Two fair dice are rolled. $E[\max]=$
- A) $\frac{91}{36}$
- B) $\frac{161}{36}$
- C) $\frac72$
- D) $5$

<details><summary>Answer</summary>

**B** — $P(\max=k)=\frac{2k-1}{36}$. $\sum k(2k-1)=1+6+15+28+45+66=161$. ($\frac{91}{36}$ is $E[\min]$.)

</details>

**Q15.** $X,Y$ independent, $\operatorname{Var}X=1$, $\operatorname{Var}Y=2$. $\operatorname{Var}(2X-3Y)=$
- A) $22$
- B) $-14$
- C) $14$
- D) $8$

<details><summary>Answer</summary>

**A** — $2^2\cdot1+(-3)^2\cdot2=4+18=22$. Variances add, even for a difference.

</details>

**Q16.** $X\sim\text{Exponential}(\lambda=2)$. $P(X>1)=$
- A) $e^{-1/2}$
- B) $1-e^{-2}$
- C) $2e^{-2}$
- D) $e^{-2}$

<details><summary>Answer</summary>

**D** — $P(X>t)=e^{-\lambda t}=e^{-2\cdot1}=e^{-2}\approx0.135$.

</details>

**Q17.** A population has mean 1000 and SD 100. For a sample of size $n=25$, $P(\bar X<960)\approx$
- A) $0.3446$
- B) $0.0228$
- C) $0.1587$
- D) $0.0013$

<details><summary>Answer</summary>

**B** — SD of $\bar X$ is $\frac{100}{\sqrt{25}}=20$. $z=\frac{960-1000}{20}=-2$. $\Phi(-2)=0.0228$.

</details>

**Q18.** $X\sim\text{Poisson}(2)$. $P(X\le1)=$
- A) $e^{-2}$
- B) $2e^{-2}$
- C) $3e^{-2}$
- D) $1-e^{-2}$

<details><summary>Answer</summary>

**C** — $P(0)+P(1)=e^{-2}+2e^{-2}=3e^{-2}\approx0.406$.

</details>

**Q19.** By Chebyshev, $P(\lvert X-\mu\rvert<2\sigma)$ is at least
- A) $\frac12$
- B) $0.95$
- C) $\frac14$
- D) $\frac34$

<details><summary>Answer</summary>

**D** — $1-\frac1{2^2}=\frac34$. (0.95 is only true for the normal distribution.)

</details>

**Q20.** What is the Lebesgue measure of $\mathbb Q\cap[0,1]$?
- A) $0$
- B) $1$
- C) $\frac12$
- D) not defined, because $\mathbb Q$ is dense

<details><summary>Answer</summary>

**A** — The set is countable. Every countable set has Lebesgue measure 0.

</details>

**Q21.** 1% of people have a disease. The test is positive for 99% of ill people and for 5% of healthy people. A person tests positive. $P(\text{ill})\approx$
- A) $0.99$
- B) $0.95$
- C) $\frac16$
- D) $0.01$

<details><summary>Answer</summary>

**C** — $P(+)=0.99\cdot0.01+0.05\cdot0.99=0.0594$. $P(\text{ill}\mid+)=\frac{0.0099}{0.0594}=\frac16\approx0.167$.

</details>
